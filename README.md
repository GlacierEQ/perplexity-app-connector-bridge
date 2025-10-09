# Perplexity App Connector Bridge

**Empowers Perplexity mobile/desktop app with full web connector functionality**

## 🚀 Quick Deploy

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/new?template=https://github.com/GlacierEQ/perplexity-app-connector-bridge)

## 🔧 What This Solves

Perplexity's mobile/desktop app has limited connector support compared to the web version. This bridge service provides:

- **Unified Connectors**: FileOps, Legal AI, Advanced Labs, Case Management
- **MCP Integration**: Full Model Context Protocol support
- **Mobile Dashboard**: Case overview and quick actions
- **Real-time Sync**: Connector status and health monitoring

## 📱 Connector Suites

### FileOps Suite
- `file_process`: File transcription and analysis
- `gdrive_access`: Google Drive integration with forensic logging

### Legal AI Suite  
- `legal_research`: Hawaii family law research
- `evidence_fusion`: Multi-source evidence correlation

### Advanced Labs
- `quantum_process`: Quantum-enhanced file processing
- `vr_simulation`: VR courtroom simulation

### Case Management
- `memory_search`: Context-aware memory retrieval
- `case_orchestration`: Complete workflow automation

## 🔌 API Endpoints

### List Connectors
```http
GET /connectors
```

### Execute Connector Tool
```http
POST /connectors/{connector_id}/execute
{
  "tool": "legal_research",
  "context": {
    "query": "custody modification requirements",
    "case_type": "family_law"
  }
}
```

### Mobile Dashboard
```http
GET /mobile/dashboard
```

## ⚙️ Configuration

Set these environment variables:

```bash
PERPLEXITY_API_KEY=pplx-your-key-here
MCP_SERVER_URL=https://your-mcp-server.railway.app
PORT=8080
```

## 🏃‍♂️ Local Development

```bash
git clone https://github.com/GlacierEQ/perplexity-app-connector-bridge
cd perplexity-app-connector-bridge
pip install -r requirements.txt
python app_connector_bridge.py
```

Bridge runs on http://localhost:8080

## 📊 Mobile App Integration

Once deployed, configure your Perplexity mobile app:

1. **Settings → Connectors**
2. **Add Bridge URL**: `https://your-bridge.railway.app`
3. **Test Connection**: Verify all 4 connector suites are available
4. **Enable Dashboard**: Access case overview and quick actions

## 🔒 Security

- CORS configured for mobile app origins
- API key authentication with Perplexity API
- Secure MCP server communication
- Request/response validation

## 📈 Monitoring

- Health endpoint: `/health`
- Connector status checks
- Real-time sync with mobile app
- Error handling and retry logic

## 🎯 Use Cases

**Legal Research**: Instant access to Hawaii family law research from mobile
**Evidence Processing**: Upload and process files with WhisperX transcription
**Case Management**: Search memory and orchestrate workflows on-the-go
**Advanced Analysis**: Quantum processing and VR simulation for complex cases

---

**Case ID**: 1FDV-23-0001009 | **Status**: Production Ready ⚡