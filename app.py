import requests
import yaml
from flask import Flask, render_template_string

app = Flask(__name__)


@app.get("/")
def index():
    return render_template_string("<h1>Привет, {{ name }}!</h1>", name="SBOM")


@app.get("/config")
def config():
    return yaml.safe_load("service: sbom-demo\nversion: 0.1.0")


@app.get("/status")
def status():
    response = requests.get("https://example.com", timeout=5)
    return {"upstream": response.status_code}
