from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.utils.dbutils import create_all_tables
from app.routes import post_wheel_specification_form, get_wheel_specification_form

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield

app = FastAPI(
    title="ICF Forms API",
    description="API for managing digital ICF Wheel & Bogie forms.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Register routers
app.include_router(post_wheel_specification_form.router)
app.include_router(get_wheel_specification_form.router)
