from flask import Flask, Response
import requests

app = Flask(__name__)

ZIP_URL = "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-13.5.0-amd64-DVD-1.iso"

# https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-13.5.0-amd64-DVD-1.iso
# https://github.com/jquery/jquery/archive/refs/heads/main.zip
@app.route("/")
def home():
    return """
    <a href="/download">Download ZIP</a>
    """

@app.route("/download")
def download():

    file = requests.get(
        ZIP_URL,
        stream=True
    )

    return Response(
        file.iter_content(chunk_size=1024),
        content_type="application/zip"
    )

app.run(debug=True)