# 🚀 Getting Started

## المتطلبات:
- Docker & Docker Compose
- Python 3.10+
- Node.js 18+
- PostgreSQL 15+
- Redis 7+

## التثبيت:

### 1. استنساخ المستودع
```bash
git clone https://github.com/Ffaa3dd/phoenix-ai-os.git
cd phoenix-ai-os
```

### 2. إعداد متغيرات البيئة
```bash
cp .env.example .env
# عدّل .env حسب احتياجات البيئة الخاصة بك
```

### 3. تشغيل Docker
```bash
docker-compose up -d
```

### 4. التحقق من الخدمات
```bash
# PostgreSQL
psql -U phoenix_user -d phoenix_ai_os

# Redis
redis-cli ping

# AI Core (بعد التثبيت)
curl http://localhost:8000/docs

# Trading Server (بعد التثبيت)
curl http://localhost:3000/health
```

## البنية الأساسية:

```
phoenix-ai-os/
├── docs/                # التوثيق
├── specs/               # المواصفات
├── src/
│   ├── ai_core/        # Python AI System
│   ├── trading_server/ # Node.js API
│   ├── broker_layer/   # Broker Logic
│   ├── memory/         # Memory Systems
│   ├── risk_engine/    # Risk Management
│   └── mobile/         # Flutter App
├── prompts/            # AI Prompts
├── research/           # Research Files
├── decisions/          # Architecture Decisions
├── tasks/              # Task Tracking
├── tests/              # Test Suite
├── docker-compose.yml  # Docker Setup
└── README.md          # This file
```

## الخطوات التالية:

1. **اقرأ التوثيق:**
   - `docs/vision.md` - الرؤية الكاملة
   - `docs/architecture.md` - المعمارية
   - `docs/roadmap.md` - خريطة الطريق

2. **ابدأ بالتطوير:**
   - `src/ai_core/` - ابدأ بـ AI Core
   - `src/trading_server/` - ثم Trading Server
   - `src/broker_layer/` - ثم Broker Layer

3. **تتبع المهام:**
   - انظر `tasks/README.md`
   - حدث `PROJECT_STATUS.md`

## المساهمة:

انظر `CONTRIBUTING.md` لتفاصيل المساهمة
