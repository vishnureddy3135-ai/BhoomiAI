import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-this-before-deployment")

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify({"status": "ok", "app": "BhoomiAI"})

@app.post("/api/assistant")
def assistant():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "Please enter a question."}), 400

    # Safe starter response. Connect a verified AI provider in this endpoint later.
    q = question.lower()
    if any(word in q for word in ["yellow", "leaf", "disease", "pest"]):
        answer = ("Yellowing or damaged leaves can have several causes, including pests, "
                  "disease, nutrient deficiency, or water stress. Photograph the whole plant "
                  "and affected leaves, check nearby plants, and confirm the cause with a local "
                  "agricultural extension officer before applying chemicals.")
    elif any(word in q for word in ["water", "irrigation", "soil"]):
        answer = ("Irrigation depends on crop type, growth stage, soil, recent rainfall, and "
                  "local weather. Check moisture near the root zone and avoid relying on a "
                  "fixed schedule alone.")
    elif any(word in q for word in ["price", "sell", "market"]):
        answer = ("Compare prices at nearby regulated markets, account for grading and transport "
                  "costs, and obtain more than one buyer quote before deciding. Live mandi prices "
                  "are not connected in this starter version.")
    else:
        answer = ("I can help you think through crop care, irrigation, weather, markets, and "
                  "storage. Please share your crop, growth stage, location, and what you observed. "
                  "For important decisions, verify advice with a qualified local agricultural expert.")
    return jsonify({"answer": answer, "mode": "starter-demo"})

@app.post("/api/crop-check")
def crop_check():
    data = request.get_json(silent=True) or {}
    crop = (data.get("crop") or "your crop").strip()
    symptoms = (data.get("symptoms") or "the symptoms observed").strip()
    return jsonify({
        "result": f"For {crop}: you reported {symptoms}. Several conditions can look similar. "
                  "Take clear photos of the whole plant and affected leaves, inspect nearby plants, "
                  "and consult an agricultural extension officer for confirmation before treatment.",
        "mode": "starter-demo"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=os.getenv("FLASK_DEBUG") == "1")
