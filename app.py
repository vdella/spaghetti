from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    """Renders the front page to the user."""
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    """Handles the backend to its frontpage counterpart.
    Gets a result from user input, does operations over it
    according to the desired entry and shows its result."""
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")

    match operation:
        case 'addition':
            var_3 = var_1 + var_2
        case 'subtraction':
            var_3 = var_1 - var_2
        case 'multiplication':
            var_3 = var_1 * var_2
        case 'division':
            var_3 = var_1 / var_2
        case _:
            var_3 = 'Invalid choice.'

    entry = var_3
    return render_template('result.html', entry=entry)


if __name__ == '__main__':
    app.run()
