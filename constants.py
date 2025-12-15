"""
Centralised categorical constants for the email decision agent.

This file is the single source of truth for:
- intents
- urgency levels
- actions
- priority levels
- SLA risk levels
- departments

These constants should be used in prompts, docs and (optionally) validation.
"""

# -----------------------------
# Allowed intent categories
# -----------------------------
INTENT_TYPES = [
    "incident_report",
    "service_request",
    "account_issue",
    "billing_query",
    "sales_inquiry",
    "complaint",
    "feedback",
    "internal_request",
    "security_alert",
    "unknown",
]

# -----------------------------
# Allowed urgency levels
# -----------------------------
URGENCY_LEVELS = [
    "low",
    "medium",
    "high",
    "critical",
]

# -----------------------------
# Allowed agent actions
# (kept aligned with schemas.ActionDecision.action)
# -----------------------------
ACTIONS = [
    "send_auto_reply",
    "create_ticket",
    "notify_admin",
    "archive_email",
    "mark_important",
    "no_action",
]

# -----------------------------
# Priority levels
# -----------------------------
PRIORITY_LEVELS = [
    "low",
    "medium",
    "high",
    "critical",
]

# -----------------------------
# SLA risk levels
# -----------------------------
SLA_RISK_LEVELS = [
    "none",
    "low",
    "medium",
    "high",
]

# -----------------------------
# Departments
# (kept aligned with schemas.ActionDecision.department)
# -----------------------------
DEPARTMENTS = [
    "engineering",
    "support",
    "billing",
    "sales",
    "hr",
    "general",
]


