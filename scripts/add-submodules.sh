#!/bin/bash

# Add Voltra Ecosystem Submodules
echo "🔗 Adding Voltra ecosystem submodules..."

# Create components directory
mkdir -p components

# Add each repository as a submodule
echo "📦 Adding voltra-esp32 (Hardware)..."
git submodule add https://github.com/Itsamnn/voltra-esp32.git components/voltra-esp32

echo "🧠 Adding voltra-nilm (Intelligence)..."
git submodule add https://github.com/Itsamnn/voltra-nilm.git components/voltra-nilm

echo "⚙️ Adding voltra-n8n (Orchestration)..."
git submodule add https://github.com/Itsamnn/voltra-n8n.git components/voltra-n8n

echo "📱 Adding voltra-nanometer (Mobile App)..."
git submodule add https://github.com/Itsamnn/voltra-nanometer.git components/voltra-nanometer

# Initialize and update submodules
echo "🔄 Initializing submodules..."
git submodule update --init --recursive

echo "✅ All submodules added successfully!"
echo ""
echo "Repository structure:"
echo "├── components/"
echo "│   ├── voltra-esp32/      # Hardware firmware"
echo "│   ├── voltra-nilm/       # NILM backend"
echo "│   ├── voltra-n8n/        # n8n workflows"
echo "│   └── voltra-nanometer/  # Android app"
echo ""
echo "Next steps:"
echo "1. Configure .env file with your credentials"
echo "2. Run 'npm run dev' to start development environment"