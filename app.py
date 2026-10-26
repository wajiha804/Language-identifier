from flask import Flask, request, render_template_string
from identifier import detect

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Language Identifier</title>
</head>
<body style="font-family: sans-serif; max-width: 600px; margin: 40px auto;">
  <h2>Language Identifier</h2>
  <p>Type or paste a sentence in English, Hindi, Telugu, Spanish or French.</p>
  <form method="post">
    <textarea name="text" rows="4" style="width:100%; font-size:18px;">{{ text }}</textarea><br><br>
    <button type="submit" style="font-size:18px;">Detect</button>
  </form>
  {% if result %}
    <h3>Language: {{ result }}</h3>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    text = request.form.get("text", "")
    result = detect(text) if text.strip() else None
    return render_template_string(PAGE, text=text, result=result)

if __name__ == "__main__":
    app.run(debug=False)