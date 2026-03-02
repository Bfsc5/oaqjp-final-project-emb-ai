from flask import Flask, request
from final_project.emotion_detection import emotion_detection

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("text")

    if not text_to_analyze:
        return "Error: No text provided", 400

    result = emotion_detection(text_to_analyze)

    # Extract values from the dictionary returned by emotion_detection()
    dominant_emotion = result.get("dominant_emotion")
    emotion_score = result.get("emotion_score")

    # Format the output exactly as the customer requires
    formatted_output = (
        f"For the statement '{text_to_analyze}', "
        f"the system detected the emotion '{dominant_emotion}' "
        f"with a confidence score of {emotion_score}."
    )

    return formatted_output, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
