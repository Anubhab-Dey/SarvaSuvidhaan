# This contains schemas which validate and document swagger and the response and the queries to fetch and return the filtered wheel specification data


from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import date


class WheelSpecificationFilterParams(BaseModel):
    formNumber: Optional[str] = Field(
        None,
        example="WHEEL-2025-001",
        description="Unique identifier of the wheel form"
    )
    submittedBy: Optional[str] = Field(
        None,
        example="user_id_123",
        description="User ID who submitted the form"
    )
    submittedDate: Optional[str] = Field(
        None,
        example="2025-07-03",
        description="Date of submission in YYYY-MM-DD format"
    )



class WheelSpecificationFormResponse(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]


class WheelSpecificationGetResponse(BaseModel):
    success: bool = Field(..., example=True)
    message: str = Field(..., example="Filtered wheel specification forms fetched successfully.")
    data: List[WheelSpecificationFormResponse]
