from agent import EmailDecisionAgent
from retrieval import retrieve_similar_cases, HISTORICAL_CASES


if __name__ == "__main__":
    agent = EmailDecisionAgent()

    incoming_email = {
        "summary": "Production server is down and affecting users",
        "intent": "urgent_issue",
        "urgency": "high",
    }

    similar_cases = retrieve_similar_cases(
        query_summary=incoming_email["summary"],
        past_cases=HISTORICAL_CASES,
        top_k=2,
    )

    decision = agent.decide(
        summary=incoming_email["summary"],
        intent=incoming_email["intent"],
        urgency=incoming_email["urgency"],
        similar_cases=similar_cases,
    )

    print("Similar cases used for context:")
    for c in similar_cases:
        print(f"- {c}")

    print("\nStructured decision:")
    print(decision.json(indent=2))