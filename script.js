// Debug logging utility - set to true for verbose console logs
const DEBUG = false;
function debug(...args) {
  if (DEBUG) console.debug('[67]', ...args);
}

// Wait for DOM to be fully loaded before initializing
window.addEventListener('DOMContentLoaded', init);

function init() {
  debug('DOM loaded, initializing app');
  
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
  
  // Diagnostics elements
  const diagModel = document.getElementById('diagModel');
  const diagFps = document.getElementById('diagFps');
  const diagLast = document.getElementById('diagLast');
  const diagErr = document.getElementById('diagErr');

  // MediaPipe
  let stream = null, running = false, hands = null, raf = 0;
  let lastTrigger = 0;
  let modelReady = false;

  // FPS tracking
  let lastFrameTime = 0;
  let frameCount = 0;
  let fps = 0;

  // Trigger smoothing
  const TRIGGER_WINDOW = 10;  // frames
  const TRIGGER_MIN_HITS = 5; // within window
  const buffer = [];

  // WebAudio simple bass hit - only create after user gesture
  let audioCtx = null;
  
  function initAudioContext() {
    // Initialize AudioContext on first user gesture (iOS requirement)
    if (!audioCtx) {
      try {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        debug('AudioContext created');
      } catch (e) {
        console.error('Failed to create AudioContext:', e);
      }
    }
  }
  
  function playBassHit() {
    if (!soundToggle.checked) return;
    try {
      // Ensure AudioContext exists
      if (!audioCtx) {
        console.warn('AudioContext not initialized yet');
        return;
      }
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
      debug('Bass hit played');
    } catch (e) { 
      console.error('Error playing bass:', e);
    }
  }

  function resizeCanvas() {
    const r = canvas.getBoundingClientRect();
    canvas.width = r.width * devicePixelRatio;
    canvas.height = r.height * devicePixelRatio;
    ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
    debug('Canvas resized:', canvas.width, 'x', canvas.height);
  }
  
  addEventListener('resize', resizeCanvas, { passive: true });
  resizeCanvas();

  async function initHands() {
    try {
      debug('Initializing MediaPipe hands...');
      diagModel.textContent = 'loading...';
      
      // Wait for window.Vision to be available
      if (typeof window.Vision === 'undefined') {
        throw new Error('MediaPipe Vision bundle not loaded. Please refresh the page.');
      }
      
      const { FilesetResolver, HandLandmarker } = window.Vision;
      
      // Use exact WASM base path for MediaPipe v0.10.10
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
      
      modelReady = true;
      diagModel.textContent = 'ready';
      diagErr.textContent = '—';
      debug('MediaPipe hands initialized successfully');
    } catch (e) {
      modelReady = false;
      diagModel.textContent = 'failed';
      diagErr.textContent = e.message.substring(0, 50);
      throw e;
    }
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
      // Cleanup: remove element after animation completes
      el.animate([
        { transform: el.style.transform + ' scale(0.9)', opacity: el.style.opacity },
        { transform: el.style.transform + ' scale(1.1)', opacity: 0 }
      ], { duration: ttl, easing: 'ease-out' }).finished.then(() => el.remove());
    }
    debug(`Sprayed ${count} text elements`);
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
    debug('Burst triggered for', n, 'fingers');
  }

  async function start() {
    try {
      // Initialize AudioContext on user gesture (required for iOS)
      initAudioContext();
      
      msg.textContent = 'Requesting camera…';
      diagErr.textContent = '—';
      
      // Request camera access
      stream = await navigator.mediaDevices.getUserMedia({ 
        video: { facingMode: 'user' }, 
        audio: false 
      });
      
      video.srcObject = stream;
      await video.play();
      debug('Camera started');
      
      // Initialize MediaPipe if not already done
      if (!modelReady) {
        msg.textContent = 'Loading hand model…';
        await initHands();
      }
      
      running = true;
      startBtn.disabled = true;
      stopBtn.disabled = false;
      msg.textContent = 'Show 6 or 7 fingers';
      
      // Reset tracking
      buffer.length = 0;
      lastFrameTime = performance.now();
      frameCount = 0;
      
      loop();
    } catch (e) {
      // Detailed error handling for different camera errors
      let errorMsg = 'Camera error. ';
      
      if (e.name === 'NotAllowedError' || e.name === 'PermissionDeniedError') {
        errorMsg = 'Camera permission denied. Please allow camera access and try again.';
      } else if (e.name === 'NotFoundError' || e.name === 'DevicesNotFoundError') {
        errorMsg = 'No camera found. Please connect a camera and try again.';
      } else if (e.name === 'NotReadableError' || e.name === 'TrackStartError') {
        errorMsg = 'Camera is in use by another app. Please close other apps and try again.';
      } else if (e.name === 'OverconstrainedError' || e.name === 'ConstraintNotSatisfiedError') {
        errorMsg = 'Camera constraints not supported. Try a different device.';
      } else if (e.message && e.message.includes('MediaPipe')) {
        errorMsg = 'Failed to load hand detection model. Please refresh and try again.';
      } else {
        errorMsg = `Error: ${e.message || e.name || 'Unknown error'}`;
      }
      
      msg.textContent = errorMsg;
      diagErr.textContent = e.name || 'Error';
      console.error('Start error:', e);
      
      // Re-enable start button on error
      startBtn.disabled = false;
      stopBtn.disabled = true;
    }
  }

  function stop() {
    running = false;
    
    // Cancel animation frame
    if (raf) {
      cancelAnimationFrame(raf);
      raf = 0;
    }
    
    // Stop all camera tracks
    if (stream) {
      stream.getTracks().forEach(t => t.stop());
      stream = null;
    }
    
    // Clear video source
    video.srcObject = null;
    
    startBtn.disabled = false;
    stopBtn.disabled = true;
    msg.textContent = 'Stopped.';
    diagLast.textContent = '—';
    diagFps.textContent = '—';
    buffer.length = 0;
    
    debug('Stopped');
  }

  fsBtn.onclick = () => {
    if (document.documentElement.requestFullscreen) {
      document.documentElement.requestFullscreen();
    }
  };
  
  startBtn.onclick = start;
  stopBtn.onclick = stop;

  function drawFrame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const w = canvas.width, h = canvas.height;
    ctx.drawImage(video, 0, 0, w, h);
  }

  function cooldownPassed() {
    const cd = parseInt(cooldownInput.value, 10);
    return performance.now() - lastTrigger > cd;
  }

  function updateFPS() {
    frameCount++;
    const now = performance.now();
    const elapsed = now - lastFrameTime;
    
    // Update FPS every second
    if (elapsed >= 1000) {
      fps = Math.round((frameCount * 1000) / elapsed);
      diagFps.textContent = fps;
      frameCount = 0;
      lastFrameTime = now;
    }
  }

  function loop() {
    if (!running) return;
    raf = requestAnimationFrame(loop);
    
    drawFrame();
    updateFPS();

    if (!hands) return;
    
    const ts = performance.now();
    const res = hands.detectForVideo(video, ts);
    let total = 0;
    
    if (res.landmarks) {
      for (const lm of res.landmarks) total += countRaisedFingers(lm);
    }
    
    const hit = (total === 6 || total === 7);
    buffer.push(hit ? 1 : 0);
    if (buffer.length > TRIGGER_WINDOW) buffer.shift();
    
    const score = buffer.reduce((a,b)=>a+b,0);

    // Update diagnostics
    if (total > 0) {
      diagLast.textContent = total;
    }

    // Trigger burst if enough frames match and cooldown passed
    if (score >= TRIGGER_MIN_HITS && cooldownPassed()) {
      lastTrigger = performance.now();
      startBurst(total);
    }
  }

  // Keep canvas resolution in sync with CSS size
  const ro = new ResizeObserver(resizeCanvas);
  ro.observe(stage);
  
  // Pre-initialize MediaPipe on page load (but don't block UI)
  if (typeof window.Vision !== 'undefined') {
    initHands().catch(e => {
      console.warn('Pre-initialization of MediaPipe failed:', e);
      // Don't block - we'll try again when user clicks Start
    });
  } else {
    console.warn('MediaPipe Vision bundle not loaded yet. Will initialize on Start.');
    diagModel.textContent = 'waiting...';
  }
  
  debug('Initialization complete');
}
