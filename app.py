from flask import Flask, request, render_template
from length import convert_length
from weight import convert_weight

app = Flask(__name__)
app.config['SECERT_KEY'] = "JIUKD;H GKH AB,V YHGDVH JHVHvgvddhv"

@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')



@app.route("/length", methods= ['GET', 'POST'])
def length():
    if request.method == 'POST':
        value = request.form.get('value')
        from_unit = request.form.get('from_unit')
        unit = request.form.get('to_unit')
        

        operation = convert_length(value, from_unit, unit)


        
        return render_template("length.html", operation = operation, value=value, from_unit=from_unit,unit=unit)
    return render_template("length.html")



@app.route("/weight", methods=['GET', 'POST'])
def weight():
    if request.method == 'POST':
        value = request.form.get('value')
        from_unit = request.form.get('from_unit')
        unit = request.form.get('unit')
        print(value)
        print(from_unit)
        print(unit)

        operate  = convert_weight(value, from_unit, unit)
        return render_template("weight.html", operate=operate, value=value, from_unit=from_unit, unit=unit)

    return render_template('weight.html')





if __name__ == "__main__":
    app.run(debug=True)
