from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head><title>FastAPI on Render</title></head>
        <body>
            <h1>Render + FastAPI からのご挨拶！</h1>
            <p>これは HTML ページです。</p>
        </body>
    </html>
    """
