import json

from langchain_core.prompts import ChatPromptTemplate

from config import llm, tavily_client
from state import CareerState


search_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI Career Search Assistant.

Generate ONE optimized search query based on the candidate profile.

Rules:

- Mention the best matching role.
- Mention important technical skills.
- Mention experience level.
- Mention India.
- Keep it under 20 words.

Return only the search query.
"""
    ),
    ("human", "{profile}")
])


def search_agent(state: CareerState) -> CareerState:

    chain = search_prompt | llm

    response = chain.invoke({
        "profile": json.dumps(
            state["profile"].model_dump(),
            indent=2
        )
    })

    search_query = response.content.strip()

    jobs = tavily_client.search(
        query=search_query,
        max_results=5
    )

    state["search_query"] = search_query

    state["jobs"] = jobs["results"]

    return state