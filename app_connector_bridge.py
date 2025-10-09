#!/usr/bin/env python3
"""
Perplexity App Connector Bridge
Enables full connector support for Perplexity mobile/desktop app
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
import os
from typing import Dict, Any
import uvicorn
from datetime import datetime

app = FastAPI(title="Perplexity App Connector Bridge", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
PERPLEXITY_API_KEY = "pplx-PXs49HgS3RmNFGpiI48FzrDOsuKokMX83dEHzqOAjBoMrXgl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#"
MCP_SERVER_URL = "https://perplexity-mcp-server-production.railway.app"

# Unified connectors for mobile app
CONNECTORS = {
    "fileops": {
        "name": "FileOps Suite",
        "tools": ["file_process", "gdrive_access"],
        "endpoint": f"{MCP_SERVER_URL}/mcp"
    },
    "legal_ai": {
        "name": "Legal AI Suite", 
        "tools": ["legal_research", "evidence_fusion"],
        "endpoint": f"{MCP_SERVER_URL}/mcp"
    },
    "advanced_labs": {
        "name": "Advanced Labs",
        "tools": ["quantum_process", "vr_simulation"],
        "endpoint": f"{MCP_SERVER_URL}/mcp"
    },
    "case_management": {
        "name": "Case Management",
        "tools": ["memory_search", "case_orchestration"],
        "endpoint": f"{MCP_SERVER_URL}/mcp"
    }
}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "perplexity-app-connector-bridge",
        "connectors_available": len(CONNECTORS)
    }

@app.get("/connectors")
async def list_connectors():
    return {"connectors": CONNECTORS}

@app.post("/connectors/{connector_id}/execute")
async def execute_connector(connector_id: str, request: Request):
    if connector_id not in CONNECTORS:
        raise HTTPException(status_code=404, detail="Connector not found")
    
    body = await request.json()
    tool_name = body.get("tool")
    context = body.get("context", {})
    
    connector = CONNECTORS[connector_id]
    
    if tool_name not in connector["tools"]:
        raise HTTPException(status_code=400, detail=f"Tool {tool_name} not available")
    
    # Execute MCP tool
    payload = {
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": context
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}"
    }
    
    try:
        response = requests.post(connector["endpoint"], json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        return {
            "status": "success",
            "tool": tool_name,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"MCP server error: {str(e)}")

@app.get("/mobile/dashboard")
async def mobile_dashboard():
    return {
        "case_overview": {
            "case_id": "1FDV-23-0001009",
            "status": "Active",
            "next_hearing": "2025-11-08",
            "exhibits_ready": 8
        },
        "connector_status": {
            "online": len(CONNECTORS),
            "total": len(CONNECTORS)
        },
        "quick_actions": [
            {"name": "Legal Research", "connector": "legal_ai", "tool": "legal_research"},
            {"name": "Process Files", "connector": "fileops", "tool": "file_process"},
            {"name": "Search Memory", "connector": "case_management", "tool": "memory_search"}
        ]
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)