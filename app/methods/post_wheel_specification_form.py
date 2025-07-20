from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.models.wheel_specification_form import WheelSpecificationForm
from fastapi import HTTPException
from sqlalchemy.future import select
from datetime import datetime


async def create_wheel_spec_form(db: AsyncSession, payload: dict):
    try:
        form_number = payload.get("formNumber")
        submitted_by = payload.get("submittedBy")
        submitted_date_str = payload.get("submittedDate")
        fields = payload.get("fields")

        if not all([form_number, submitted_by, submitted_date_str, fields]):
            raise HTTPException(status_code=400, detail="Missing required fields")

        submitted_date = datetime.strptime(submitted_date_str, "%Y-%m-%d").date()

        stmt = select(WheelSpecificationForm).where(WheelSpecificationForm.form_number == form_number)
        result = await db.execute(stmt)
        existing = result.scalar_one_or_none()
        if existing:
            raise HTTPException(status_code=409, detail="Form with this number already exists")

        new_form = WheelSpecificationForm(
            form_number=form_number,
            submitted_by=submitted_by,
            submitted_date=submitted_date,
            fields=fields
        )

        db.add(new_form)
        await db.commit()

        return {
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": form_number,
                "submittedBy": submitted_by,
                "submittedDate": submitted_date_str,
                "status": "Saved"
            }
        }

    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Database error during form creation")
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
