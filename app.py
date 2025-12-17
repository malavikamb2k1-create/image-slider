from flask import Flask, render_template

app = Flask(__name__)

print("THIS IS THE IMAGE SLIDER APP")

@app.route("/")
def index():
    images = ["image1.jpeg", "image2.jpeg", "image3.jpeg"]
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)
