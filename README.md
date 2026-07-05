# Legal Compliance Agent

[![CI](https://github.com/kogunlowo123/legal-compliance-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/legal-compliance-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Legal | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Legal compliance agent that monitors regulatory changes, maps compliance requirements to business processes, tracks compliance status, generates audit evidence, and manages regulatory filings.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `monitor_regulations` | Monitor regulatory changes relevant to the organization |
| `map_requirements` | Map regulatory requirements to business processes and controls |
| `track_compliance` | Track compliance status across regulatory requirements |
| `collect_evidence` | Collect and organize audit evidence for compliance |
| `generate_filing` | Generate regulatory filing or compliance report |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/legal-compliance/analyze` | Analyze |
| `POST` | `/api/v1/legal-compliance/search` | Search |
| `POST` | `/api/v1/legal-compliance/generate` | Generate document |
| `GET` | `/api/v1/legal-compliance/track` | Track status |
| `POST` | `/api/v1/legal-compliance/report` | Generate report |

## Features

- Legal
- Compliance
- Compliance
- Audit Trail

## Integrations

- Relativity
- Logikcull
- Ironclad
- Docusign Clm
- Westlaw

## Architecture

```
legal-compliance-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── legal_compliance_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Legal Tech Platform + LLM + Document Management**

---

Built as part of the Enterprise AI Agent Platform.
