from typing import List
from pydantic import BaseModel, Field


class MatchedJob(BaseModel):
    title: str = Field(description="Job title")

    company: str = Field(description="Company name")

    url: str = Field(description="Job URL")

    reason: str = Field(description="Reason why this job matches")


class MatchedJobs(BaseModel):
    matched_jobs: List[MatchedJob]