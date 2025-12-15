from fastapi import FastAPI
from pydantic import BaseModel

from agent import EmailDecisionAgent
from retrieval import retrieve_similar_cases, HISTORICAL_CASES
from schemas import ActionDecision


class EmailRequest(BaseModel):
    subject: str
    body: str
    intent: str
    urgency: str


app = FastAPI(title="Email Decision Agent API")

agent = EmailDecisionAgent()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/decide", response_model=ActionDecision)
def decide_email(req: EmailRequest):
    """
    Decide on the best action for an incoming email.

    - Combines subject + body into a summary.
    - Uses Embedding Gemma to retrieve similar past cases.
    - Calls the Gemma LLM agent to get a structured decision.
    """
    summary = f"{req.subject}\n\n{req.body}".strip()

    similar_cases = retrieve_similar_cases(
        query_summary=summary,
        past_cases=HISTORICAL_CASES,
        top_k=2,
    )

    decision = agent.decide(
        summary=summary,
        intent=req.intent,
        urgency=req.urgency,
        similar_cases=similar_cases,
    )

    return decision


