from flask import Flask, render_template, request

app = Flask(__name__)

# Define add and subtract functions
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            # Get the input values from the form
            x = float(request.form["x"])
            y = float(request.form["y"])
            
            # Determine which operation to perform
            if "add" in request.form:
                result = add(x, y)
            elif "sub" in request.form:
                result = sub(x, y)
        except ValueError:
            result = "Invalid input, please enter valid numbers."

    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
