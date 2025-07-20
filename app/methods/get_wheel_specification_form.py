# This contains code that returns wheel specification records based of off certain parameters passed to it as arguments.


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
from app.models.wheel_specification_form import WheelSpecificationForm
from fastapi import HTTPException
from datetime import datetime


async def fetch_filtered_wheel_forms(
    db: AsyncSession,
    form_number: str = None,
    submitted_by: str = None,
    submitted_date: str = None
):
    try:
        filters = []

        if form_number:
            filters.append(WheelSpecificationForm.form_number == form_number)
        if submitted_by:
            filters.append(WheelSpecificationForm.submitted_by == submitted_by)
        if submitted_date:
            try:
                parsed_date = datetime.strptime(submitted_date, "%Y-%m-%d").date()
                filters.append(WheelSpecificationForm.submitted_date == parsed_date)
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

        stmt = select(WheelSpecificationForm)
        if filters:
            stmt = stmt.where(and_(*filters))

        result = await db.execute(stmt)
        records = result.scalars().all()

        return {
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": [
                {
                    "formNumber": r.form_number,
                    "submittedBy": r.submitted_by,
                    "submittedDate": str(r.submitted_date),
                    "fields": r.fields
                }
                for r in records
            ]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
