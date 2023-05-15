from flask import Flask, render_template

app = Flask(__name__)

jobs = [
  {
    "id": 1,
    "name": "Python Developer",
    "location": "India"
  },
  {
    "id": 2,
    "name": "C++ Developer",
    "location": "India"
  },
  {
    "id": 3,
    "name": "Java Developer",
    "location": "India"
  },
]


@app.route("/")
def home():
  return render_template("home.html", jobs=jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
