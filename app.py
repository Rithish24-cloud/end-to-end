from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask DevOps Project! it is safe?  i have this "

@app.route("/about")
def about():
    return "This is an end-to-end CI/CD pipeline project on AWS /  hi how are you?."

@app.route("/health")
def health():
    return jsonify({"status": "success", "message": "Application is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)