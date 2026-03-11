from flask import Flask, request, send_from_directory, jsonify
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILES = {
    "A": "parts_A.txt",
    "B": "parts_B.txt",
    "X": "parts_X.txt",
    "Y": "parts_Y.txt",
    "Z": "parts_Z.txt"
}

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "name_generator.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)

@app.route("/save", methods=["POST"])
def save_files():
    data = request.json
    for key, filename in FILES.items():
        content = data.get(key, "")
        with open(os.path.join(BASE_DIR, filename), "w") as f:
            f.write(content.strip() + "\n")
    return jsonify({"status": "success"})

@app.route("/clear", methods=["POST"])
def clear_files():
    for filename in FILES.values():
        with open(os.path.join(BASE_DIR, filename), "w") as f:
            f.write("")
    return jsonify({"status": "success"})

@app.route("/append", methods=["POST"])
def append_files():
    data = request.json
    for key, filename in FILES.items():
        entries = data.get(key, "").strip()
        if entries:
            with open(os.path.join(BASE_DIR, filename), "a") as f:
                for line in entries.splitlines():
                    line = line.strip()
                    if line:
                        f.write(line + "\n")
    return jsonify({"status": "success"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

