function runEmotionDetection() {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let formData = new FormData();
    formData.append("textToAnalyze", textToAnalyze);

    fetch("/emotionDetector", {
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("system_response").innerHTML = data;
    })
    .catch(error => {
        document.getElementById("system_response").innerHTML = "Error: " + error;
    });
}
