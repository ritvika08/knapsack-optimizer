from flask import Flask, render_template, request
from greedy import greedy_knapsack
from dp import knapsack_dp

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        values = list(map(int, request.form["values"].split(",")))
        weights = list(map(int, request.form["weights"].split(",")))
        capacity = int(request.form["capacity"])

        greedy_result = greedy_knapsack(values, weights, capacity)
        dp_result = knapsack_dp(values, weights, capacity)

        result = {
            "greedy": greedy_result[0],
            "dp": dp_result
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)