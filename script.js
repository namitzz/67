// Elements
const stage = document.getElementById('stage');
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const overlay = document.getElementById('overlay');
const flash = document.getElementById('flash');
const ctx = canvas.getContext('2d');

const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const fsBtn = document.getElementById('fsBtn');

const soundToggle = document.getElementById('soundToggle');
const intensityInput = document.getElementById('intensity');
const cooldownInput = document.getElementById('cooldown');
const partyToggle = document.getElementById('partyToggle');

const msg = document.getElementById('msg');

// MediaPipe
let stream = null, running = false, hands = null, raf = 0;
let lastTrigger = 0;

// Trigger smoothing
const TRIGGER_WINDOW = 10;  // frames
const TRIGGER_MIN_HITS = 5; // within window
const buffer = [];

// WebAudio simple bass hit
let audioCtx = null;
function playBassHit() {
  if (!soundToggle.checked) return;
  try {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    const now = audioCtx.currentTime;
    osc.frequency.setValueAtTime(90, now);
    osc.frequency.exponentialRampToValueAtTime(40, now + 0.2);
    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.exponentialRampToValueAtTime(0.8, now + 0.01);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.25);
    osc.connect(gain).connect(audioCtx.destination);
    osc.start();
    osc.stop(now + 0.3);
  } catch (e) { /* ignore */ }
}

function resizeCanvas() {
  const r = canvas.getBoundingClientRect();
  canvas.width = r.width * devicePixelRatio;
  canvas.height = r.height * devicePixelRatio;
  ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
}
addEventListener('resize', resizeCanvas, { passive: true });
resizeCanvas();

async function initHands() {
  const { FilesetResolver, HandLandmarker } = window.Vision;
  const resolver = await FilesetResolver.forVisionTasks(
    'https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.10/wasm'
  );
  hands = await HandLandmarker.createFromOptions(resolver, {
    numHands: 2,
    minHandDetectionConfidence: 0.6,
    minHandPresenceConfidence: 0.6,
    minTrackingConfidence: 0.6,
    runningMode: 'VIDEO'
  });
}

function countRaisedFingers(lm) {
  // Basic heuristic: for fingers 1..4 (index..pinky): tip.y < pip.y means up
  const TIP = [4,8,12,16,20], PIP = [2,6,10,14,18];
  let up = 0;
  for (let i = 1; i < 5; i++) if (lm[TIP[i]] && lm[PIP[i]] && lm[TIP[i]].y < lm[PIP[i]].y) up++;
  // Thumb: lateral from wrist
  const wrist = lm[0], thumbTip = lm[4];
  if (wrist && thumbTip && Math.abs(thumbTip.x - wrist.x) > 0.04) up++;
  return up;
}

function sprayTexts(n, amount) {
  const count = amount + Math.floor(Math.random() * amount);
  const w = overlay.clientWidth;
  const h = overlay.clientHeight;
  for (let i = 0; i < count; i++) {
    const el = document.createElement('div');
    el.className = 'spray';
    el.textContent = (n === 6 ? '6 7' : '67');
    const x = Math.random() * w;
    const y = Math.random() * h;
    const size = 14 + Math.random() * 80;
    el.style.left = x + 'px';
    el.style.top = y + 'px';
    el.style.fontSize = size + 'px';
    el.style.color = 'white';
    el.style.opacity = 0.2 + Math.random() * 0.8;
    el.style.transform = `rotate(${(Math.random()*20-10).toFixed(1)}deg)`;
    overlay.appendChild(el);
    const ttl = 600 + Math.random()*800;
    el.animate([
      { transform: el.style.transform + ' scale(0.9)', opacity: el.style.opacity },
      { transform: el.style.transform + ' scale(1.1)', opacity: 0 }
    ], { duration: ttl, easing: 'ease-out' }).finished.then(() => el.remove());
  }
}

function startBurst(n) {
  stage.classList.add('shake');
  stage.classList.add('zoom');
  flash.classList.add('on');
  sprayTexts(n, parseInt(intensityInput.value, 10));
  if (partyToggle.checked) sprayTexts(n, parseInt(intensityInput.value, 10));
  playBassHit();
  setTimeout(() => {
    stage.classList.remove('shake');
    stage.classList.remove('zoom');
    flash.classList.remove('on');
  }, 2200);
}

async function start() {
  try {
    msg.textContent = 'Requesting camera…';
    stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' }, audio: false });
    video.srcObject = stream; await video.play();
    await initHands();
    running = true; startBtn.disabled = true; stopBtn.disabled = false;
    msg.textContent = 'Show 6 or 7 fingers';
    loop();
  } catch (e) {
    msg.textContent = 'Camera blocked or unavailable. Allow access and try again.';
    console.error(e);
  }
}

function stop() {
  running = false; cancelAnimationFrame(raf);
  if (stream) stream.getTracks().forEach(t => t.stop());
  startBtn.disabled = false; stopBtn.disabled = true;
  msg.textContent = 'Stopped.';
  buffer.length = 0;
}

fsBtn.onclick = () => document.documentElement.requestFullscreen?.();
startBtn.onclick = start;
stopBtn.onclick = stop;

function drawFrame() {
  ctx.clearRect(0,0,canvas.width,canvas.height);
  const w = canvas.width, h = canvas.height;
  ctx.drawImage(video, 0, 0, w, h);
}

function cooldownPassed() {
  const cd = parseInt(cooldownInput.value, 10);
  return performance.now() - lastTrigger > cd;
}

function loop() {
  if (!running) return;
  raf = requestAnimationFrame(loop);
  drawFrame();

  if (!hands) return;
  const ts = performance.now();
  const res = hands.detectForVideo(video, ts);
  let total = 0;
  if (res.landmarks) {
    for (const lm of res.landmarks) total += countRaisedFingers(lm);
  }
  const hit = (total === 6 || total === 7);
  buffer.push(hit ? 1 : 0); if (buffer.length > TRIGGER_WINDOW) buffer.shift();
  const score = buffer.reduce((a,b)=>a+b,0);

  if (score >= TRIGGER_MIN_HITS && cooldownPassed()) {
    lastTrigger = performance.now();
    startBurst(total);
  }
}

// Keep canvas resolution in sync with CSS size
const ro = new ResizeObserver(resizeCanvas); ro.observe(stage);
