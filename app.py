from flask import Flask, jsonify
import json


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"




@app.route('/claims', methods=['GET'])
def fetch_all_claims():
    result = get_all_claims()
    return jsonify(result)
    

@app.route('/claims/<int:pet_id>', methods=['GET'])
def fetch_claims_by_pet_id(pet_id):
    result = get_claims_by_pet_id(pet_id)
    return jsonify(result)

def get_all_claims():
    with open('./claim_details.json') as claims:
        claims_data = json.load(claims)
        result = claims_data['claims']
    return result

def get_claims_by_pet_id(pet_id):
    claims_data = get_all_claims()
    filtered_claims_data = [claim for claim in claims_data if claim['pet_id'] == pet_id]
    return filtered_claims_data

    

if __name__ == "__main__":
    app.run()
