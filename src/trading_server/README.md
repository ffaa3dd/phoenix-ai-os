# src/trading_server - Trading API Server

خادم API للتداول مبني بـ Node.js + TypeScript

## البنية:
```
trading_server/
├── src/
│   ├── routes/         # مسارات API
│   ├── services/       # خدمات الأعمال
│   ├── models/         # نماذج البيانات
│   ├── middleware/     # وسيط Express
│   └── utils/          # أدوات مساعدة
├── tests/              # اختبارات
├── package.json        # المتطلبات
└── tsconfig.json       # إعدادات TypeScript
```

## الميزات:
- REST API
- WebSocket للتحديثات الفورية
- JWT Authentication
- PostgreSQL
- Redis Cache
