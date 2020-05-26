from flask import Flask, request, jsonify

import util



app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add("Access Control",'*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sq = float(request.form['total_sq'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
         'estimated_price': util.get_estimated_price(location,total_sq,bhk,bath)
     })

    response.headers.add("Access")

    return response


if __name__ == '__main__':
    print("Starting Flask Server For Home price prediction ...")
    util.load_saved_artifacts()
    app.run()
