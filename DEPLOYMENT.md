# GitHub Pages Deployment Guide

This document explains how the 67 Meme Detector was deployed to GitHub Pages.

## Overview

The project now has two versions:
1. **Desktop Version** - Python application using OpenCV (original)
2. **Web Version** - JavaScript application running in the browser (new)

## Web Version Features

The web version (`index.html`) provides:
- Browser-based hand gesture detection using MediaPipe Hands (JavaScript)
- Real-time camera access via getUserMedia API
- No installation required - works directly in any modern browser
- Same core functionality as the desktop version
- Responsive design that works on different screen sizes

## Deployment Setup

### Files Created

1. **`index.html`** - Main web application
   - Complete standalone HTML file
   - Includes CSS styling for the UI
   - JavaScript implementation using MediaPipe Web
   - Finger counting logic translated from Python to JavaScript
   - Meme overlay system with animations

2. **`.github/workflows/pages.yml`** - GitHub Actions workflow
   - Automatically deploys to GitHub Pages on push to main branch
   - Can also be triggered manually via workflow_dispatch
   - Uses official GitHub Pages actions for deployment

### How It Works

1. When changes are pushed to the `main` branch, the GitHub Actions workflow triggers
2. The workflow checks out the code
3. It configures GitHub Pages settings
4. It uploads the entire repository as a Pages artifact
5. It deploys the artifact to GitHub Pages
6. The site becomes available at `https://namitzz.github.io/67/`

## Accessing the Web Version

Once deployed, users can access the detector at:
**https://namitzz.github.io/67/**

The web version will:
1. Request camera permissions when "Start Detector" is clicked
2. Process video in real-time using MediaPipe Hands
3. Detect when 6 or 7 fingers are shown
4. Trigger the meme flood with animated text overlay

## Technical Implementation

### MediaPipe Integration

The web version uses:
- `@mediapipe/hands` - Hand tracking model
- `@mediapipe/camera_utils` - Camera utilities

These are loaded from CDN, so no build step is required.

### Finger Counting Algorithm

The JavaScript implementation mirrors the Python version:
1. Detect hand landmarks (21 points per hand)
2. Count extended fingers by comparing tip vs. joint positions
3. Thumb is special-cased based on handedness (left/right)
4. Other fingers are counted if tip is above PIP joint

### Detection Logic

- Maintains a 10-frame history buffer
- Triggers meme mode when 5+ of last 10 frames detect 6 or 7 fingers
- Meme mode lasts for 5 seconds
- Displays 30 random meme texts with varying sizes, colors, and positions

## Browser Compatibility

The web version works in modern browsers that support:
- getUserMedia API (camera access)
- Canvas API (drawing)
- ES6+ JavaScript features
- WebAssembly (for MediaPipe)

Tested on:
- Chrome/Edge (recommended)
- Firefox
- Safari (iOS/macOS)

## Future Enhancements

Potential improvements for the web version:
- Mobile-optimized UI
- Touch controls
- Configurable settings UI
- Multiple meme image support
- Sound effects
- Recording/sharing capabilities
- PWA support for offline use

## Maintenance

To update the web version:
1. Edit `index.html` as needed
2. Commit and push to the `main` branch
3. GitHub Actions will automatically redeploy
4. Changes appear on the live site within 1-2 minutes

## Troubleshooting

**Site not updating?**
- Check the Actions tab in GitHub to see if the workflow ran
- Verify GitHub Pages is enabled in repository settings
- Check that the workflow has proper permissions

**Camera not working?**
- Browser must be served over HTTPS (GitHub Pages uses HTTPS)
- User must grant camera permissions
- Camera must not be in use by another application

**MediaPipe not loading?**
- Check browser console for errors
- Verify CDN links are accessible
- Try a different browser

## Repository Settings

For this to work, ensure:
1. GitHub Pages is enabled in repository settings
2. Source is set to "GitHub Actions"
3. The repository has Actions enabled
4. Workflow has the required permissions (set in workflow file)
