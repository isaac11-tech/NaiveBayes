import uvicorn


if __name__ == "__main__":
     uvicorn.run("model_server.server:app", host="127.0.0.1", port=8000, reload=True)
