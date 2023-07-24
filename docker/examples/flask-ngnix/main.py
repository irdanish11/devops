from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("./index.html")

@app.route('/ping', methods=['GET'])
def ping():
    """
    Determine if the container is healthy by running a sample through the algorithm.
    """
    # we will return status ok if the model doesn't barf
    # but you can also insert slightly more sophisticated tests here
    return Response(response='{"status": "healthy"}', status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)