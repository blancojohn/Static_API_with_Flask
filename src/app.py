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

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

member1= Member(jackson_family._generateId(), "John", "Jackson", 33, [7, 13, 12])
jackson_family.add_member(member1)

member2= Member(jackson_family._generateId(), "Jane", "Jackson", 35, [10, 14, 3])
jackson_family.add_member(member2)

member3= Member(jackson_family._generateId(), "Jimmy", "Jackson", 5, [1])
jackson_family.add_member(member3)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():

    # this is how you can use the Family datastructure by calling its methods
    members= jackson_family.get_all_members() #es utilazado en el map a continuación
    members_serialize= list(map(lambda member: member.serialize(), members))

    return jsonify(members_serialize), 200

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
