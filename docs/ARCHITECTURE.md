# 🏗️ Voltra Ecosystem Architecture

## System Overview

The Voltra ecosystem follows a **microservices architecture** with clear separation of concerns across four distinct components. Each component operates independently while communicating through well-defined interfaces.

## Architecture Principles

### 1. Separation of Concerns
- **Hardware Layer**: Pure sensing and data collection
- **Intelligence Layer**: AI processing and analytics
- **Orchestration Layer**: Workflow automation and routing
- **Presentation Layer**: User interface and visualization

### 2. Event-Driven Communication
- Components communicate via Firebase Realtime Database events
- Asynchronous processing prevents blocking operations
- Real-time data synchronization across all layers

### 3. Scalable Design
- Each component can be scaled independently
- Stateless services enable horizontal scaling
- Cloud-native deployment patterns

## Component Architecture

### 🔌 Hardware Layer (ESP32)

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────┐
│   CT Sensor     │───▶│    ESP32     │───▶│  Firebase   │
│  (Current)      │    │   MCU        │    │    RTDB     │
└─────────────────┘    │              │    └─────────────┘
┌─────────────────┐    │  - ADC       │
│  ZMPT Sensor    │───▶│  - WiFi      │
│  (Voltage)      │    │  - FreeRTOS  │
└─────────────────┘    └──────────────┘
```

**Key Features:**
- Real-time sampling at 1kHz
- Direct Firebase integration
- Deterministic execution
- Low power consumption

### 🧠 Intelligence Layer (NILM Backend)

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Firebase   │───▶│   FastAPI    │───▶│  Gemini AI  │
│    RTDB     │    │   Backend    │    │    API      │
└─────────────┘    │              │    └─────────────┘
                   │ - Data Proc  │
                   │ - NILM Algo  │
                   │ - ML Models  │
                   └──────────────┘
```

**Processing Pipeline:**
1. **Data Ingestion**: Fetch raw telemetry from Firebase
2. **Preprocessing**: Clean and normalize sensor data
3. **Feature Extraction**: Calculate power signatures
4. **Disaggregation**: Apply NILM algorithms
5. **AI Analysis**: Generate insights with Gemini
6. **Storage**: Save results back to Firebase

### ⚙️ Orchestration Layer (n8n)

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Scheduler  │───▶│     n8n      │───▶│ Telegram    │
│  (Cron)     │    │  Workflows   │    │    Bot      │
└─────────────┘    │              │    └─────────────┘
                   │ - HTTP Calls │
                   │ - Routing    │
                   │ - Triggers   │
                   └──────────────┘
```

**Workflow Types:**
- **Daily Reports**: Automated energy analysis
- **Alert System**: Threshold-based notifications
- **Chat Interface**: User query routing

### 📱 Presentation Layer (Android App)

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Firebase   │───▶│   Android    │───▶│    User     │
│    RTDB     │    │     App      │    │ Interface   │
└─────────────┘    │              │    └─────────────┘
                   │ - Real-time  │
                   │ - Charts     │
                   │ - Alerts     │
                   └──────────────┘
```

## Data Flow Architecture

### Real-time Data Flow
```
ESP32 → Firebase → Android App
  ↓
NILM Backend → AI Analysis → Firebase
  ↓
n8n → Telegram Notifications
```

### Batch Processing Flow
```
Scheduler → n8n → NILM Backend → Gemini AI → Report Generation
```

## Technology Stack

### Hardware
- **Microcontroller**: ESP32-WROOM-32
- **Sensors**: PZEM energy meter integration
- **Communication**: WiFi 802.11 b/g/n, GSM module
- **Framework**: Arduino IDE with custom libraries
- **Features**: Relay control, remote monitoring

### Backend
- **Runtime**: Python 3.9+
- **Framework**: FastAPI
- **AI**: Custom NILM algorithms with ML models
- **Database**: Firebase Realtime Database
- **Deployment**: Docker containers
- **Features**: Appliance analytics, energy insights

### Orchestration
- **Platform**: n8n (Node.js)
- **Triggers**: Cron schedules, webhooks
- **Integrations**: HTTP, Telegram, Firebase

### Mobile
- **Language**: Kotlin
- **Framework**: Android Jetpack
- **UI**: Material Design 3
- **Database**: Firebase SDK
- **Features**: Real-time dashboard, appliance control

## Security Architecture

### Authentication & Authorization
- Firebase Authentication for user management
- API key-based service authentication
- Role-based access control (RBAC)

### Data Protection
- TLS/SSL encryption for all communications
- Firebase security rules for data access
- Environment-based configuration management

### Network Security
- VPN support for remote access
- Firewall rules for service isolation
- Rate limiting on public endpoints

## Scalability Considerations

### Horizontal Scaling
- **NILM Backend**: Multiple container instances
- **Firebase**: Auto-scaling database
- **n8n**: Distributed workflow execution

### Performance Optimization
- **Caching**: Redis for frequently accessed data
- **CDN**: Static asset delivery
- **Database**: Indexed queries and partitioning

### Monitoring & Observability
- **Metrics**: Prometheus + Grafana
- **Logging**: Centralized log aggregation
- **Tracing**: Distributed request tracing
- **Alerts**: Real-time system monitoring

## Deployment Architecture

### Development Environment
```
Local Machine → Docker Compose → Local Firebase Emulator
```

### Production Environment
```
Cloud Provider → Kubernetes → Firebase Production → CDN
```

### CI/CD Pipeline
```
Git Push → GitHub Actions → Build → Test → Deploy → Monitor
```

## Future Architecture Enhancements

### Planned Improvements
1. **Edge Computing**: Local NILM processing on ESP32
2. **Machine Learning**: Custom trained models
3. **Multi-tenant**: Support for multiple households
4. **Real-time Analytics**: Stream processing with Apache Kafka
5. **Mobile Expansion**: iOS app development

### Technology Roadmap
- **2025 Q1**: Core system stabilization
- **2025 Q2**: Advanced ML model integration
- **2025 Q3**: Multi-device support
- **2025 Q4**: Commercial deployment readiness