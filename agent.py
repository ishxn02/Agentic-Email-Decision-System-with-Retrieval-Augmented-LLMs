from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from schemas import ActionDecision
from config import get_llm
from prompts import SYSTEM_PROMPT, HUMAN_PROMPT

class EmailDecisionAgent:
    def __init__(self):
        self.llm = get_llm()
        self.parser = PydanticOutputParser(pydantic_object=ActionDecision)

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("human", HUMAN_PROMPT)
        ])

    def decide(self, summary: str, intent: str, urgency: str, similar_cases: list) -> ActionDecision:
        formatted_prompt = self.prompt.format_messages(
            summary=summary,
            intent=intent,
            urgency=urgency,
            similar_cases="\n".join(similar_cases)
        )

        response = self.llm.invoke(formatted_prompt)
        decision = self.parser.parse(response.content)

        if decision.confidence < 0.6:
            decision.action = "notify_admin"
            decision.reasoning += " | Confidence too low, escalating to human."

        return decision