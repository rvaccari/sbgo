import fastapi
import uvicorn
from decouple import config
from tortoise.contrib.fastapi import register_tortoise

app = fastapi.FastAPI()

register_tortoise(
    app,
    db_url=config("DATABASE_URL", default="sqlite://sqlite.db"),
    modules={"models": ["app.models.customer"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/health")
def health():
    return fastapi.Response(content="OK")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
