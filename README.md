# 🔥 Phoenix AI OS - Intelligent Trading Operating System

> Build an AI trading operating system where the AI analyzes markets, evaluates risk, learns from previous trades, and communicates with a broker layer instead of directly controlling the exchange.

## 📊 Project Overview

Phoenix AI OS is an independent AI Operating System designed for autonomous trading with **safety-first** principles. The system uses multiple AI agents to analyze markets, manage risk, and make intelligent trading decisions while maintaining complete control through a centralized broker layer.

## 🎯 Core Principles

- ✅ **Safety First** - Risk management overrides all decisions
- ✅ **AI Never Executes Directly** - All orders go through broker layer
- ✅ **Everything is Logged** - Full audit trail for every decision
- ✅ **Everything is Testable** - Comprehensive testing framework
- ✅ **Plugin Architecture** - Easy integration and extensibility
- ✅ **Learning System** - AI improves from every trade

## 📂 Project Structure

```
phoenix-ai-os/
├── docs/                    # Complete documentation
├── specs/                   # Technical specifications
├── src/
│   ├── ai_core/            # Python - AI Agents & Decision Engine
│   ├── trading_server/      # Node.js - API Server
│   ├── broker_layer/        # Exchange communication
│   ├── mobile/              # Flutter app
│   ├── memory/              # Memory management system
│   └── risk_engine/         # Risk calculation engine
├── prompts/                 # AI Agent prompt templates
├── research/                # Research & references
├── decisions/               # Architecture decision records
├── tasks/                   # Development tasks & roadmap
├── tests/                   # Test suites
├── docker-compose.yml       # Container orchestration
├── .env.example             # Environment variables
└── README.md                # This file
```

## 🤖 AI Agents (12 Specialized)

1. **Architect Agent** - System design and optimization
2. **Planner Agent** - Trade planning and strategy
3. **Market Analyst** - Market trend analysis
4. **News Analyst** - News sentiment analysis
5. **Technical Analyst** - Technical indicators analysis
6. **Risk Manager Agent** - Risk assessment
7. **Critic Agent** - Decision critique
8. **Reviewer Agent** - Code and logic review
9. **Portfolio Manager** - Portfolio optimization
10. **Strategy Evolution** - Learning and improvement
11. **Market Professor** - Market education
12. **Devil's Advocate** - Counter-arguments

## 💾 Memory Systems

- **Working Memory** - Current session data
- **Short Memory** - Last 24 hours trades
- **Long Memory** - Historical patterns
- **Trading Memory** - All past trades
- **Prompt Memory** - Effective prompts
- **Semantic Memory** - Market knowledge

## 🛡️ Risk Management

- Risk Score Calculation
- ATR-based Position Sizing
- Correlation Analysis
- Drawdown Monitoring
- Daily Loss Limits
- Circuit Breaker System
- Emergency Stop Protocol

## 🚀 Quick Start

```bash
git clone https://github.com/Ffaa3dd/phoenix-ai-os.git
cd phoenix-ai-os
cp .env.example .env
docker-compose up -d
```

## 📚 Documentation

- [`docs/vision.md`](docs/vision.md) - Project vision
- [`docs/project_dna.md`](docs/project_dna.md) - Core principles
- [`docs/architecture.md`](docs/architecture.md) - System architecture
- [`docs/roadmap.md`](docs/roadmap.md) - Development roadmap
- [`docs/coding_rules.md`](docs/coding_rules.md) - Coding standards

## Tech Stack

- **Backend**: Python (AI), Node.js (API)
- **Database**: PostgreSQL
- **Mobile**: Flutter
- **Exchange**: Rise SDK + Phoenix

---

**Made with ❤️ for the future of AI trading**
