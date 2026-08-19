from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    with open("index.html", "r") as file:
    	html_code = file.read()
    return html_code

if __name__ == "__main__":
	app.run(port=5185, debug=True)