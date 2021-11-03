from app import create_app

app = create_app()
app.logger.info("MyBlog is running")


@app.get("/")
def home():
    return "Hello World"

