# This contains the code to route the query params and validate them and the responses when you query wheel specification data


from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.get_wheel_specification_form import (
    WheelSpecificationFilterParams,
    WheelSpecificationGetResponse
)
from app.methods.get_wheel_specification_form import fetch_filtered_wheel_forms

router = APIRouter()


@router.get(
    "/api/forms/wheel-specifications",
    summary="Fetch wheel specification forms by filters",
    response_model=WheelSpecificationGetResponse,
    response_description="Filtered wheel specification form results",
    tags=["Wheel Specification Forms"],
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "List of matching forms",
            "content": {
                "application/json": {
                    "example": {
                        "success": True,
                        "message": "Filtered wheel specification forms fetched successfully.",
                        "data": [
                            {
                                "formNumber": "WHEEL-2025-001",
                                "submittedBy": "user_id_123",
                                "submittedDate": "2025-07-03",
                                "fields": {
                                    "treadDiameterNew": "915 (900-1000)",
                                    "lastShopIssueSize": "837 (800-900)"
                                }
                            }
                        ]
                    }
                }
            }
        },
        400: {
            "description": "Invalid filter values",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid date format. Use YYYY-MM-DD."}
                }
            }
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/json": {
                    "example": {"detail": "Unexpected database failure"}
                }
            }
        },
    }
)
async def get_wheel_specification_form(
    filters: WheelSpecificationFilterParams = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """
    Returns all wheel specification forms that match the optional filters:
    - `formNumber`
    - `submittedBy`
    - `submittedDate` (YYYY-MM-DD)
    """
    return await fetch_filtered_wheel_forms(
        db=db,
        form_number=filters.formNumber,
        submitted_by=filters.submittedBy,
        submitted_date=filters.submittedDate
    )
