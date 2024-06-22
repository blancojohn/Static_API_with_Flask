"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure, Member
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

text_age= "Years old"
# create the jackson family object
jackson_family = FamilyStructure("Jackson")
member1= Member(jackson_family._generateId(), "John", f"33 {text_age}", [7, 3, 12])
jackson_family.add_member(member1)

member2= Member(jackson_family._generateId(), "Jane", f"35 {text_age}", [10, 14, 3])
jackson_family.add_member(member2)

member3= Member(jackson_family._generateId(), "Jimmy", f"5 {text_age}", [1])
jackson_family.add_member(member3)

print(jackson_family._members)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200

""" @app.route('/member/<int:member_id>', metohds=['GET'])
def handle_member():

    return jsonify({"messagge": "probando ruta"})

@app.route('/member', methods=['POST'])
def add_member():

    return jsonify({""}) """

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
