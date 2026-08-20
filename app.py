from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/order", methods=["POST"])
def order():
    return render_template("success.html",
        name=request.form.get("name",""),
        service=request.form.get("service",""))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
