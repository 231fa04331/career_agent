from typing import List
from pydantic import BaseModel, Field


class Profile(BaseModel):
    """
    Structured profile extracted from the resume.
    """

    name: str = Field(description="Candidate's full name")

    summary: str = Field(description="Professional summary")

    skills: List[str] = Field(description="Technical skills")

    experience: str = Field(description="Years or level of experience")

    roles: List[str] = Field(description="Suitable job roles")

    education: str = Field(description="Highest education")

    projects: List[str] = Field(description="Major projects")