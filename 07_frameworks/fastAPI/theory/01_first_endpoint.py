"""
Topic: First FastAPI Endpoint

FastAPI is an ASGI web framework focused on building APIs quickly,
with automatic data validation and interactive documentation.

Coming from Spring Boot, think of it this way:
- FastAPI app instance  -> roughly like your @SpringBootApplication class
- @app.get / @app.post  -> roughly like @GetMapping / @PostMapping
- Uvicorn                -> the ASGI server that runs your app (like Tomcat runs Spring)

Unlike Spring, there's no build tool (Maven/Gradle), no XML/annotations-heavy
config, and no mandatory project structure. You just write Python functions
and decorate them with routes.

How to run this file:
    uvicorn theory.01_first_endpoint:app --reload

Then open:
    http://127.0.0.1:8000        -> the actual endpoint response
    http://127.0.0.1:8000/docs   -> auto-generated interactive Swagger UI
    http://127.0.0.1:8000/redoc  -> alternative auto-generated docs
"""

from fastapi import FastAPI

# The FastAPI instance is the core of the application.
# Every route we define gets attached to this object.
app = FastAPI(
    title="Learning FastAPI",
    description="First endpoint example for the python-fundamentals repo",
    version="0.1.0",
)


# A "path operation" (aka route/endpoint) is defined with a decorator
# that matches the HTTP method: @app.get, @app.post, @app.put, @app.delete...
@app.get("/")
def read_root():
    """
    Root endpoint.

    FastAPI automatically converts the returned dict into a JSON response.
    No need for @ResponseBody or explicit serialization like in Spring.
    """
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
def health_check():
    """
    A common pattern: a lightweight endpoint to check if the API is alive.
    Useful later for Docker/Kubernetes liveness probes (ties into your
    DevOps roadmap).
    """
    return {"status": "ok"}


# Key takeaways:
# 1. The function name (read_root, health_check) is NOT part of the URL,
#    it's just a Python identifier. The route path comes from the decorator.
# 2. The return value is automatically serialized to JSON.
# 3. Documentation at /docs is generated for free from your function
#    signatures and type hints (more on that in the next topics).