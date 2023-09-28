from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/Summarize", methods=["POST"])
def Summarize():
    if request.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}

        data = request.form["data"]

        minL = 20
        maxL = int(request.form["MaxL"])  # Convert MaxL to an integer

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        response = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL},
        })[0]

        # Extract the summary_text from the JSON response
        summary_text = response["summary_text"]

        return render_template("index.html", result=summary_text)

    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
