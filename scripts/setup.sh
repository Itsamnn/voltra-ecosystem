#!/bin/bash

# Voltra Ecosystem Setup Script
echo "🚀 Setting up Voltra Ecosystem..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Initialize git submodules
echo "📦 Initializing git submodules..."
git submodule update --init --recursive

# Copy environment file
if [ ! -f .env ]; then
    echo "📝 Creating environment file..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your configuration before proceeding."
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p data
mkdir -p scripts

# Check if Node.js is installed
if command -v node &> /dev/null; then
    echo "📦 Installing npm dependencies..."
    npm install
else
    echo "⚠️  Node.js not found. Skipping npm install."
fi

# Make scripts executable
chmod +x scripts/*.sh

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your configuration"
echo "2. Run 'npm run dev' to start development environment"
echo "3. Follow the deployment guide in docs/DEPLOYMENT.md"
echo ""
echo "For more information, see README.md"