from pydantic import BaseModel, Field
from typing import Literal


class ActionDecision(BaseModel):
    action: Literal[
        "send_auto_reply",
        "create_ticket",
        "notify_admin",
        "archive_email",
        "mark_important",
        "no_action",
    ]
    confidence: float = Field(..., ge=0, le=1)
    reasoning: str

    # New decision dimensions for richer enterprise behavior
    priority: Literal["low", "medium", "high", "critical"]
    sla_risk: Literal["none", "low", "medium", "high"]
    department: Literal[
        "engineering",
        "support",
        "billing",
        "sales",
        "hr",
        "general",
    ]
