# 🤝 Contributing to Voltra Ecosystem

Thank you for your interest in contributing to the Voltra ecosystem! This guide will help you get started with contributing to any of the four repositories.

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Repository Structure](#repository-structure)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow. Please be respectful and constructive in all interactions.

## Getting Started

### Prerequisites
- Git
- Docker & Docker Compose
- Node.js (v18+)
- Python (3.9+)
- Android Studio (for mobile contributions)
- Firebase CLI

### Fork and Clone
```bash
# Fork the umbrella repository
git clone https://github.com/[your-username]/voltra-ecosystem
cd voltra-ecosystem

# Add upstream remote
git remote add upstream https://github.com/Itsamnn/voltra-ecosystem
```

## Development Setup

### 1. Environment Setup
```bash
# Clone all submodules
git submodule update --init --recursive

# Set up development environment
cp .env.example .env
# Edit .env with your development credentials
```

### 2. Component-Specific Setup

#### Hardware (ESP32)
```bash
cd components/voltra-esp32
# Install ESP-IDF
# Follow: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/
```

#### Backend (NILM)
```bash
cd components/voltra-nilm
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Orchestration (n8n)
```bash
cd components/voltra-n8n
npm install -g n8n
# Import workflows for testing
```

#### Mobile App
```bash
cd components/voltra-nanometer
# Open in Android Studio
# Sync Gradle dependencies
```

## Contributing Guidelines

### Branch Naming Convention
- `feature/component-description` - New features
- `bugfix/component-issue-description` - Bug fixes
- `docs/update-description` - Documentation updates
- `refactor/component-improvement` - Code refactoring

Examples:
- `feature/esp32-power-calibration`
- `bugfix/nilm-gemini-timeout`
- `docs/update-deployment-guide`

### Commit Message Format
```
type(component): brief description

Detailed explanation of changes (if needed)

Fixes #issue-number
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
```
feat(esp32): add automatic calibration for CT sensors

Implements self-calibration routine that runs on startup
to improve measurement accuracy across different installations.

Fixes #123
```

### Code Style Guidelines

#### Python (NILM Backend)
- Follow PEP 8
- Use Black for formatting
- Type hints required
- Docstrings for all functions

```python
def disaggregate_power(data: List[float], threshold: float = 0.1) -> Dict[str, float]:
    """
    Disaggregate total power consumption into individual appliances.
    
    Args:
        data: List of power measurements in watts
        threshold: Minimum power threshold for appliance detection
        
    Returns:
        Dictionary mapping appliance names to power consumption
    """
```

#### C++ (ESP32 Firmware)
- Follow Google C++ Style Guide
- Use meaningful variable names
- Comment complex algorithms
- Keep functions under 50 lines

```cpp
/**
 * @brief Calculate RMS voltage from ADC samples
 * @param samples Array of ADC readings
 * @param count Number of samples
 * @return RMS voltage in volts
 */
float calculateRMSVoltage(const uint16_t* samples, size_t count) {
    // Implementation
}
```

#### Kotlin (Android App)
- Follow Android Kotlin Style Guide
- Use data classes for models
- Implement proper error handling
- Use coroutines for async operations

```kotlin
/**
 * Repository for managing energy data from Firebase
 */
class EnergyRepository @Inject constructor(
    private val firebaseDatabase: FirebaseDatabase
) {
    suspend fun getLatestReading(): Result<EnergyReading> {
        // Implementation
    }
}
```

## Repository Structure

### Component Responsibilities

| Component | Responsibility | Technologies |
|-----------|---------------|--------------|
| **voltra-esp32** | Hardware sensing, PZEM metering, GSM | C++ Arduino, PZEM, GSM |
| **voltra-nilm** | NILM inference, appliance analytics | Python FastAPI, ML |
| **voltra-n8n** | Workflow orchestration, Telegram | n8n, JavaScript |
| **voltra-nanometer** | Mobile dashboard, appliance control | Kotlin, Android |

### Cross-Component Changes
If your contribution affects multiple components:
1. Create separate PRs for each component
2. Reference related PRs in descriptions
3. Coordinate merge timing
4. Update integration tests

## Submitting Changes

### Pull Request Process

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Write code following style guidelines
   - Add tests for new functionality
   - Update documentation as needed

3. **Test Locally**
   ```bash
   # Run component-specific tests
   # Verify integration works end-to-end
   ```

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat(component): your change description"
   ```

5. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   # Create PR through GitHub interface
   ```

### PR Requirements

#### Checklist
- [ ] Code follows style guidelines
- [ ] Tests added/updated for changes
- [ ] Documentation updated
- [ ] No breaking changes (or properly documented)
- [ ] All CI checks pass
- [ ] Reviewed by at least one maintainer

#### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Component(s) Affected
- [ ] ESP32 Hardware
- [ ] NILM Backend
- [ ] n8n Orchestration
- [ ] Android App

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)

## Related Issues
Fixes #issue-number
```

## Development Workflow

### Local Testing
```bash
# Start development environment
docker-compose -f docker-compose.dev.yml up

# Run specific component tests
cd components/voltra-nilm
pytest tests/

# Run integration tests
./scripts/test-integration.sh
```

### Debugging
- Use component-specific debugging tools
- Check logs in `logs/` directory
- Use Firebase emulator for testing
- Monitor real-time data flow

## Getting Help

### Resources
- [Architecture Documentation](docs/ARCHITECTURE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- Component-specific README files
- GitHub Discussions for questions

### Contact
- Create GitHub issues for bugs/features
- Use Discussions for general questions
- Email: [maintainer-email@domain.com]

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to Voltra! 🚀