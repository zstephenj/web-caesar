from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/" method="post">
        <label>
        Rotate by: 
        <input type="text" name="rot" value="0">
        <textarea name="text" rows="10" cols="30">{0}</textarea>
        </label>
        <input type="submit" value="Submit">
      </form>
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    org_text = request.form['text']
    enc_text = rotate_string(org_text, rotation)
    final = enc_text
    return form.format(final)

@app.route("/")
def index():
    return form.format('')

app.run ()