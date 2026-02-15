from flask import Flask, url_for

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Suman Portfolio</title>
    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f6f8;
        }}

        /* FULL IMAGE */
        .full-img {{
            width: 100%;
            height: auto;
            display: block;
        }}

        .card {{
            max-width: 600px;
            margin: 50px auto;
            background: white;
            padding: 20px;
            border-radius: 100px;
            box-shadow: 0 15px 20px rgba(0,0,0,0.15);
            text-align: center;
        }}

        h2 {{
            color: #0b78e3;
        }}
    </style>
</head>
<body>

    <!-- FULL WIDTH IMAGE -->
    <img src="{url_for('static', filename='images/101.jpg')}" class="full-img">

    <div class="card">
        <h1>Hello, I am Suman</h1>
        <p>Student | Web & Graphics Enthusiast</p>

        <h2>About Me</h2>
        <p>I am learning Python, Web and Graphics programming.</p>

        <h2>Skills</h2>
        <p>Python, HTML, CSS</p>

        <h2>Contact</h2>
        <p>Email: sumans48750@gmail.com</p>
    </div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    