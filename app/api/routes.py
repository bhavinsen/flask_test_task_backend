import requests
import datetime
from flask import request, jsonify
from app.api import bp
from app.models.models import About


@bp.route("/getMenu/", methods=["GET"])
def get_menu():
    params = request.args.get('locale')
    
    if params and params == 'en':
        data = [
            {
            "label": "US Population Table",
            "rule": "/api/rules/us_population",
            "type": "table"
            },
            {
            "label": "US Population Chart",
            "rule": "/api/rules/us_population",
            "type": "chart",
            "params": {
                "fill": "red"
                }
            },
            {
            "label": "About",
            "rule": "/api/rules/about",
            "type": "text",
            "params": {
                "font-size": "30px"
                }
            }
        ]
    else:
        data = {"error": "Language not found."}
        
    return jsonify(data), 200


def fetch_us_population_data():
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.RequestException as e:
        print(f"Error occurred while fetching data: {e}")
        return None


@bp.route("/rules/us_population_data/", methods=["GET"])
def get_us_population_data():
    data = fetch_us_population_data()
    if data is None:
        return jsonify({"error": "Failed to fetch data"}), 400

    formatted_data = []
    for obj in data.get('data', []):
        formatted_data.append({
            "year": obj['Year'],
            "population": obj['Population']
        })

    return jsonify(formatted_data), 200


@bp.route("/rules/about/", methods=["GET"])
def get_about():
    about_obj = About.query.first()
    current_dt = datetime.datetime.now()
    formatted_dt = current_dt.strftime("%d/%m/%Y %H:%M:%S")

    res_data = {
        "text": about_obj.text,
        "Last update": formatted_dt
    }
    return jsonify(res_data), 200
