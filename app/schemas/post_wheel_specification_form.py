# This file contains schema to validate inputs for creating wheel specifications


from pydantic import BaseModel, Field
from typing import Dict
from datetime import date

class WheelSpecificationFormSchema(BaseModel):
    formNumber: str = Field(
        ...,
        example="WHEEL-2025-001",
        description="Unique identifier for this wheel specification form"
    )
    submittedBy: str = Field(
        ...,
        example="user_id_123",
        description="User ID of the person submitting the form"
    )
    submittedDate: str = Field(
        ...,
        example="2025-07-03",
        description="Date the form is submitted (YYYY-MM-DD)"
    )
    fields: Dict[str, str] = Field(
        ...,
        description="Key-value mapping of wheel measurements and spec values. All values must be strings."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "formNumber": "WHEEL-2025-001",
                "submittedBy": "user_id_123",
                "submittedDate": "2025-07-03",
                "fields": {
                    "treadDiameterNew": "915 (900-1000)",
                    "lastShopIssueSize": "837 (800-900)",
                    "condemningDia": "825 (800-900)",
                    "wheelGauge": "1600 (+2,-1)",
                    "variationSameAxle": "0.5",
                    "variationSameBogie": "5",
                    "variationSameCoach": "13",
                    "wheelProfile": "29.4 Flange Thickness",
                    "intermediateWWP": "20 TO 28",
                    "bearingSeatDiameter": "130.043 TO 130.068",
                    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
                    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
                    "rollerBearingWidth": "93 (+0/-0.250)",
                    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
                    "wheelDiscWidth": "127 (+4/-0)"
                }
            }
        }
