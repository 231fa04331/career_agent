import json

from langchain_core.prompts import ChatPromptTemplate

from config import llm
from state import CareerState
from models.cover_letter_schema import CoverLetter


cover_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert career coach.

Write a professional cover letter.

Requirements:

- Address the hiring manager professionally.
- Highlight relevant technical skills.
- Mention relevant academic projects.
- Explain why the candidate is a strong fit.
- Keep it around 250 words.
- Maintain a professional tone.

Return only the cover letter.
"""
    ),
    (
        "human",
        """
Candidate Profile:

{profile}

Selected Job:

{job}
"""
    )
])


structured_llm = llm.with_structured_output(CoverLetter)


def cover_letter_agent(state: CareerState) -> CareerState:

    chain = cover_prompt | structured_llm

    best_job = state["matched_jobs"][0]

    cover_letter = chain.invoke({
        "profile": json.dumps(
            state["profile"].model_dump(),
            indent=2
        ),
        "job": json.dumps(
            best_job.model_dump(),
            indent=2
        )
    })

    state["cover_letter"] = cover_letter.cover_letter

    return state