"""
Flask server for the Emotion Detection web application.
"""

from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Render the main HTML page for the application.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Receive text from the web form, call the emotion detector,
    and return a formatted response string or an error message.
    """
    text_to_analyze = request.form.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    # Handle blank or invalid input
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    anger = result.get("anger")
    disgust = result.get("disgust")
    fear = result.get("fear")
    joy = result.get("joy")
    sadness = result.get("sadness")
    dominant = result.get("dominant_emotion")

    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return formatted_output


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
