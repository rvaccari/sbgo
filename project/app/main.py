import fastapi

app = fastapi.FastAPI()


@app.get("/health")
def health():
    return fastapi.Response(content="OK")
