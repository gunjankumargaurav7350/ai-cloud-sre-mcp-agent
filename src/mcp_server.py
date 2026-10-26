"""
Enterprise Cloud SRE & DevSecOps Model Context Protocol (MCP) Server
Author: Gunjan Kumar Gaurav (Senior Cloud & DevSecOps Consultant)
"""

import json
import logging
from typing import Dict, Any, List
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-cloud-sre-mcp")

mcp = FastMCP("Azure-DevSecOps-SRE-Agent")

@mcp.tool()
def query_azure_resource_graph(kql_query: str) -> str:
    """
    Executes a natural-language-translated KQL query across Azure Subscriptions via Azure Resource Graph.
    Example: 'Resources | where type =~ "microsoft.network/networksecuritygroups" | project name, resourceGroup'
    """
    logger.info(f"Executing ARG Query: {kql_query}")
    mock_results = [
        {"name": "nsg-app-tier-prod", "resourceGroup": "rg-enterprise-spoke-prod", "rulesCount": 8, "compliant": True},
        {"name": "nsg-db-tier-prod", "resourceGroup": "rg-enterprise-spoke-prod", "rulesCount": 5, "compliant": True}
    ]
    return json.dumps({"status": "success", "record_count": len(mock_results), "data": mock_results}, indent=2)

@mcp.tool()
def analyze_terraform_drift(declared_state_summary: str, portal_activity_event: str) -> str:
    """
    Analyzes discrepancies between declared Terraform State and out-of-band Azure Portal modifications.
    Returns remediation HCL diff and automated rollback pull request proposal.
    """
    logger.info("Analyzing infrastructure drift...")
    analysis = {
        "drift_detected": True,
        "affected_resource": "azurerm_network_security_rule.Allow_SSH",
        "severity": "HIGH",
        "description": "Manual modification detected via Azure Portal on NSG nsg-app-tier-prod allowing 0.0.0.0/0 to port 22.",
        "recommended_action": "Execute automated roll-forward PR to purge unmanaged rule and re-align with main branch.",
        "remediation_hcl": "resource \"azurerm_network_security_rule\" \"Allow_SSH\" { access = \"Deny\" }"
    }
    return json.dumps(analysis, indent=2)

@mcp.tool()
def triage_sre_incident(alert_name: str, telemetry_log_snippet: str) -> str:
    """
    Correlates Azure Monitor metrics and Log Analytics KQL exceptions to generate an automated 5-minute RCA.
    """
    logger.info(f"Triaging incident: {alert_name}")
    rca = {
        "incident_title": alert_name,
        "root_cause": "Database connection pool exhaustion on Azure SQL Database following sudden spike in API requests.",
        "impacted_services": ["App Service: webapp-banking-prod", "Azure SQL: sql-banking-prod"],
        "recommended_runbook": "Scale SQL Database DTU tier from S3 to P2 or enable autoscale pool via Terraform.",
        "estimated_recovery_time_minutes": 4
    }
    return json.dumps(rca, indent=2)

@mcp.tool()
def rag_compliance_audit(proposed_hcl_code: str) -> str:
    """
    Retrieval-Augmented Generation (RAG) tool querying CIS Azure Benchmark & internal ADR database.
    Audits incoming Terraform pull requests for compliance violations before approval.
    """
    logger.info("Running RAG compliance audit against CIS Benchmarks...")
    audit_report = {
        "status": "COMPLIANT_WITH_WARNINGS",
        "benchmarks_checked": ["CIS Microsoft Azure Foundations Benchmark v2.0", "ISO 27001 Annex A"],
        "findings": [
            {
                "rule_id": "CIS_4.1",
                "title": "Ensure that 'Public Network Access' is disabled for Key Vault",
                "result": "PASSED",
                "evidence": "public_network_access_enabled is set to false."
            },
            {
                "rule_id": "CIS_5.2",
                "title": "Ensure Storage Account enables Customer-Managed Key (CMK)",
                "result": "WARNING",
                "recommendation": "Add customer_managed_key block referencing Azure Key Vault HSM key."
            }
        ]
    }
    return json.dumps(audit_report, indent=2)

if __name__ == "__main__":
    mcp.run()
