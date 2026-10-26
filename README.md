# ?? AI-Driven Cloud SRE & DevSecOps MCP Agent Toolkit

[![MCP](https://img.shields.io/badge/Protocol-Model_Context_Protocol-8A2BE2?style=for-the-badge&logo=anthropic&logoColor=white)](https://modelcontextprotocol.io)
[![Azure](https://img.shields.io/badge/Cloud-Microsoft_Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com)
[![Multi-Agent](https://img.shields.io/badge/Architecture-Autonomous_Swarm-00A2FF?style=for-the-badge)](https://github.com/gunjankumargaurav7350)
[![Author](https://img.shields.io/badge/Architect-Gunjan_Kumar_Gaurav-0A0E27?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gunjan-gaurav)

Production-ready **Model Context Protocol (MCP)** server and **Autonomous Multi-Agent Swarm** bridging Large Language Models (LLMs) with Microsoft Azure infrastructure, Terraform state management, and real-time SRE observability.

---

## ? Agentic Architecture Flow

```
[ Model Context Protocol (MCP) ]         [ Enterprise RAG Knowledge Base ]
• Azure Resource Graph MCP               • CIS & ISO Compliance Vectors
• Terraform State Query MCP              • Enterprise ADR Knowledge Base
• K8s Cluster Telemetry MCP              • Cloud Architecture SOPs
                 \                      /
                  \                    /
                   v                  v
             [ Autonomous Multi-Agent Swarm ]
                            |
                            |--> [ 1. IaC Auto-Fixer ]   : Scans Checkov & auto-generates HCL fixes
                            |--> [ 2. Drift Sentinel ]   : Catches portal changes & alerts or self-heals
                            |--> [ 3. SRE Root-Cause ]   : Correlates telemetry & writes RCA in minutes
                            `--> [ 4. FinOps Optimizer ] : Detects orphaned disks & auto-rightsizes
```

---

## ??? Implemented MCP Tools

1. `query_azure_resource_graph`: Executes KQL queries across Azure subscriptions to inspect resources and security posture.
2. `analyze_terraform_drift`: Compares live Azure Activity logs against Terraform state files to identify out-of-band console drift.
3. `triage_sre_incident`: Ingests Azure Monitor exceptions and distributed traces to synthesize 5-minute Root Cause Analyses (RCAs).
4. `rag_compliance_audit`: Vector search indexing CIS Azure Benchmarks to evaluate pull requests before merge.

---

## ?? Setup & Integration

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start MCP server locally
python src/mcp_server.py
```

Add to your **Antigravity IDE / Claude Desktop / Cursor** `mcp_config.json`:
```json
{
  "mcpServers": {
    "azure-devsecops-sre": {
      "command": "python",
      "args": ["src/mcp_server.py"]
    }
  }
}
```

---

## ?? Author & Inquiries

**Gunjan Kumar Gaurav**  
*Senior Cloud & DevSecOps Consultant | Azure Solutions Architect Expert (AZ-305)*  
LinkedIn: [linkedin.com/in/gunjan-gaurav](https://www.linkedin.com/in/gunjan-gaurav) | Email: `gunjankumargaurav7@gmail.com`
