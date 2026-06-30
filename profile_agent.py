from langchain_core.prompts import ChatPromptTemplate

from config import llm
from state import CareerState
from models.profile_schema import Profile


# Prompt used by the Profile Agent
profile_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert Resume Analyzer.

Extract the candidate information from the resume.

Focus on:

- Name
- Professional Summary
- Technical Skills
- Experience
- Suitable Job Roles
- Education
- Projects

Return the information in the required structured format.
"""
    ),
    ("human", "{resume}")
])


# Create a structured LLM
structured_llm = llm.with_structured_output(Profile)


def profile_agent(state: CareerState) -> CareerState:
    """
    Extract candidate profile from resume text.
    """

    chain = profile_prompt | structured_llm

    profile = chain.invoke({
        "resume": state["resume_text"]
    })

    state["profile"] = profile

    return state