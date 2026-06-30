import json

from langchain_core.prompts import ChatPromptTemplate

from config import llm
from state import CareerState
from models.matched_job_schema import MatchedJobs


match_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI Job Matching Expert.

You will receive:

1. Candidate Profile
2. Job Listings

Analyze all the jobs carefully.

Select ONLY the BEST 3 jobs.

Rank them from best to worst.

Explain briefly why each job matches the candidate.

Return only the structured output.
"""
    ),
    (
        "human",
        """
Candidate Profile:

{profile}

Job Listings:

{jobs}
"""
    )
])


structured_llm = llm.with_structured_output(MatchedJobs)


def matching_agent(state: CareerState) -> CareerState:

    chain = match_prompt | structured_llm

    matched_jobs = chain.invoke({
        "profile": json.dumps(
            state["profile"].model_dump(),
            indent=2
        ),
        "jobs": json.dumps(
            state["jobs"],
            indent=2
        )
    })

    state["matched_jobs"] = matched_jobs.matched_jobs

    return state