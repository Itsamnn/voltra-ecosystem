# 🚀 Voltra Ecosystem Deployment Guide

This guide provides detailed instructions for deploying the complete Voltra ecosystem across all four components.

## Prerequisites

### Required Accounts & Services
- **Firebase Account** with Realtime Database enabled
- **Google Cloud Platform** account with Gemini AI API access
- **n8n Instance** (cloud or self-hosted)
- **Android Development Environment** (Android Studio)

### Required Tools
- Git
- Docker & Docker Compose
- Node.js (v18+)
- Python (3.9+)
- Android SDK
- Firebase CLI

## Deployment Order

**⚠️ CRITICAL**: Follow this exact order to ensure proper system initialization.

### 1. 🔥 Firebase Setup

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login to Firebase
firebase login

# Initialize new project
firebase init database

# Configure Realtime Database rules
firebase deploy --only database
```

**Generate Service Account:**
1. Go to Firebase Console → Project Settings → Service Accounts
2. Click "Generate new private key"
3. Save as `serviceAccount.json` (keep secure!)

### 2. 🧠 Deploy NILM Backend

```bash
# Clone the repository
git clone https://github.com/[username]/voltra-nilm
cd voltra-nilm

# Set environment variables
cp .env.example .env
# Edit .env with your Firebase credentials and Gemini API key

# Build and run with Docker
docker build -t voltra-nilm .
docker run -d -p 8000:8000 --env-file .env voltra-nilm

# Verify deployment
curl http://localhost:8000/health
```

### 3. 🔌 Flash ESP32 Firmware

```bash
# Clone firmware repository
git clone https://github.com/[username]/voltra-esp32
cd voltra-esp32

# Configure credentials
cp config/config.h.example config/config.h
# Edit config.h with WiFi and Firebase details

# Install ESP-IDF
# Follow: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/

# Build and flash
idf.py build
idf.py -p /dev/ttyUSB0 flash monitor
```

### 4. ⚙️ Setup n8n Workflows

```bash
# Clone n8n workflows
git clone https://github.com/[username]/voltra-n8n
cd voltra-n8n

# Import workflows to your n8n instance
# Method 1: Copy JSON files to n8n import
# Method 2: Use n8n CLI (if available)

# Configure HTTP nodes
# Update all HTTP Request nodes to point to your NILM backend URL
# Example: http://your-server:8000
```

### 5. 📱 Build Android App

```bash
# Clone mobile app
git clone https://github.com/[username]/voltra-nanometer
cd voltra-nanometer

# Configure Firebase
# Add google-services.json to app/ directory

# Build release APK
./gradlew assembleRelease

# Install on device
adb install app/build/outputs/apk/release/app-release.apk
```

## Verification Steps

### 1. Hardware Verification
```bash
# Check Firebase for incoming data
# Should see voltage, current, power readings every 30 seconds
```

### 2. Backend Verification
```bash
# Test NILM endpoints
curl http://your-server:8000/api/disaggregate
curl http://your-server:8000/api/ask -d '{"question": "What appliances are running?"}'
```

### 3. n8n Verification
- Check workflow execution logs
- Test Telegram bot responses
- Verify daily report generation

### 4. Mobile App Verification
- Real-time data sync
- Historical charts loading
- Push notifications working

## Troubleshooting

### Common Issues

**Firebase Connection Failed**
- Verify serviceAccount.json permissions
- Check Firebase project ID in configuration
- Ensure Realtime Database is enabled

**ESP32 Not Sending Data**
- Check WiFi credentials
- Verify Firebase host URL
- Monitor serial output for errors

**NILM Backend Errors**
- Check Gemini AI API key validity
- Verify Firebase credentials
- Review Docker container logs

**n8n Workflow Failures**
- Update HTTP endpoint URLs
- Check authentication tokens
- Verify webhook configurations

**Mobile App Issues**
- Ensure google-services.json is correct
- Check Firebase project configuration
- Verify app signing certificates

## Production Considerations

### Security
- Use environment variables for all secrets
- Enable Firebase security rules
- Implement API rate limiting
- Use HTTPS for all endpoints

### Monitoring
- Set up Firebase monitoring
- Configure Docker health checks
- Implement logging aggregation
- Monitor API response times

### Scaling
- Use Firebase hosting for static assets
- Implement Redis caching for NILM backend
- Consider load balancing for high traffic
- Monitor database performance

## Support

For deployment issues:
1. Check individual repository README files
2. Review troubleshooting sections
3. Open issues in respective repositories
4. Contact: [your-email@domain.com]