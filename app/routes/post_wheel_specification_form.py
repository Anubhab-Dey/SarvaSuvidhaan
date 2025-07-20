# This file contains the code to take the input from the user of wheel specifications and validates it and then calls the corresponding method to process further


from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.post_wheel_specification_form import WheelSpecificationFormSchema
from methods.post_wheel_specification_form import create_wheel_spec_form
from app.database import get_db

router = APIRouter()


@router.post(
    "/api/forms/wheel-specifications",
    response_description="Wheel specification submitted successfully",
    status_code=status.HTTP_201_CREATED,
    summary="Submit ICF wheel specification form",
    tags=["Wheel Specification Forms"],
    responses={
        201: {
            "description": "Form submitted successfully",
            "content": {
                "application/json": {
                    "example": {
                        "success": True,
                        "message": "Wheel specification submitted successfully.",
                        "data": {
                            "formNumber": "WHEEL-2025-001",
                            "submittedBy": "user_id_123",
                            "submittedDate": "2025-07-03",
                            "status": "Saved"
                        }
                    }
                }
            }
        },
        400: {
            "description": "Missing required fields",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Missing required fields"
                    }
                }
            }
        },
        409: {
            "description": "Form with this number already exists",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Form with this number already exists"
                    }
                }
            }
        },
        500: {
            "description": "Internal server/database error",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Database error during form creation"
                    }
                }
            }
        },
    }
)
async def post_wheel_specification_form(
    form: WheelSpecificationFormSchema,
    db: AsyncSession = Depends(get_db)
):
    """
    Submits a new ICF wheel specification form to the system.

    - Requires a unique `formNumber`
    - `submittedBy` is typically the user ID
    - `submittedDate` must follow `YYYY-MM-DD`
    - `fields` must be a dictionary of wheel parameters (all values as strings)
    - Duplicate form numbers will return 409 Conflict
    """
    return await create_wheel_spec_form(db, form.model_dump())
