from pydantic import BaseModel, Field


class CoverLetter(BaseModel):
    cover_letter: str = Field(
        description="Professional cover letter"
    )