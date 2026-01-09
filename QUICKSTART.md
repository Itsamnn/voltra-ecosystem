# ⚡ Voltra Ecosystem - Quick Start Guide

Get up and running with the Voltra ecosystem in under 30 minutes!

## 🚀 Prerequisites

Before you begin, ensure you have:
- Git installed
- Docker & Docker Compose installed
- Firebase account (free tier works)
- Google Cloud account with Gemini AI access

## 📦 1. Clone and Setup

```bash
# Clone the umbrella repository
git clone https://github.com/Itsamnn/voltra-ecosystem
cd voltra-ecosystem

# Run setup script
chmod +x scripts/setup.sh
./scripts/setup.sh

# Configure environment
cp .env.example .env
# Edit .env with your credentials
```

## 🔥 2. Firebase Quick Setup

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login and create project
firebase login
firebase projects:create voltra-demo

# Initialize database
firebase init database
```

**Get your credentials:**
1. Go to Firebase Console → Project Settings
2. Generate service account key → Save as `serviceAccount.json`
3. Copy project ID to `.env` file

## 🧠 3. Start Development Environment

```bash
# Start all services
npm run dev

# This starts:
# - NILM Backend (http://localhost:8000)
# - Firebase Emulator (http://localhost:9000)
# - n8n Workflows (http://localhost:5678)
# - Documentation (http://localhost:8080)
```

## 🔌 4. Hardware Simulation (Optional)

If you don't have ESP32 hardware yet, simulate data:

```bash
# Install Python dependencies
pip install firebase-admin requests

# Run data simulator
python scripts/simulate-esp32-data.py
```

## 📱 5. Mobile App (Optional)

```bash
# Clone mobile app
git clone https://github.com/Itsamnn/voltra-nanometer
cd voltra-nanometer

# Add google-services.json to app/ directory
# Open in Android Studio and run
```

## ✅ 6. Verify Everything Works

### Check Backend Health
```bash
curl http://localhost:8000/health
# Should return: {"status": "healthy"}
```

### Test AI Endpoint
```bash
curl -X POST http://localhost:8000/api/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What appliances are currently running?"}'
```

### Check Firebase Data
1. Open http://localhost:9000 (Firebase UI)
2. Navigate to Realtime Database
3. Should see simulated sensor data

### Test n8n Workflows
1. Open http://localhost:5678 (admin/password)
2. Import workflows from `components/voltra-n8n/workflows/`
3. Execute test workflow

## 🎯 What's Next?

### For Hardware Development
1. Get ESP32 development board
2. Follow `components/voltra-esp32/README.md`
3. Flash firmware and connect sensors

### For AI/Backend Development
1. Explore `components/voltra-nilm/`
2. Implement custom NILM algorithms
3. Train your own models

### For Mobile Development
1. Open `components/voltra-nanometer/` in Android Studio
2. Customize UI and add features
3. Test with real Firebase data

### For Automation
1. Create custom n8n workflows
2. Set up Telegram bot integration
3. Configure automated reports

## 🆘 Troubleshooting

### Common Issues

**Docker containers won't start:**
```bash
# Check Docker is running
docker --version
docker-compose --version

# Clean up and retry
docker-compose down
docker system prune -f
npm run dev
```

**Firebase connection errors:**
- Verify `serviceAccount.json` is in root directory
- Check Firebase project ID in `.env`
- Ensure Firebase Realtime Database is enabled

**NILM backend errors:**
- Check Gemini API key in `.env`
- Verify Firebase credentials
- Check Docker logs: `docker-compose logs voltra-nilm`

**n8n workflows not working:**
- Update HTTP endpoints to point to `http://voltra-nilm:8000`
- Check workflow import was successful
- Verify webhook URLs are correct

## 📚 Additional Resources

- [Full Deployment Guide](docs/DEPLOYMENT.md)
- [Architecture Overview](docs/ARCHITECTURE.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Component Documentation](README.md#-ecosystem-repositories)

## 💬 Get Help

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/Itsamnn/voltra-ecosystem/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/Itsamnn/voltra-ecosystem/discussions)
- 📧 **Direct Contact**: [your-email@domain.com]

---

**Happy building! ⚡**