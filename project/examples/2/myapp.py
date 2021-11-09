from app import create_app


app = create_app()


@app.get("/")
def home():
    return "Hello World"
