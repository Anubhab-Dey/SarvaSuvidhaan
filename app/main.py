from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import post_wheel_specification_form

app = FastAPI(
    title="ICF Forms API",
    description="API for submitting and managing ICF Wheel Specification forms.",
    version="1.0.0",
    contact={
        "name": "SarvaSuvidhaa KPA Team",
        "email": "contact@suvidhaen.com"
    },
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(post_wheel_specification_form.router)
