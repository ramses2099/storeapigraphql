from flask import Flask, request, jsonify, render_template
from typing import Optional
from .database import init_db
from .operations import get_all_categories
from ariadne import graphql_sync
from ariadne.constants import CONTENT_TYPE_JSON
from .schema.create import create_schema


# init db
init_db()


app = Flask(__name__)


@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return render_template('index.html')

@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    
    schema = create_schema()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)
    
    status_code = 200 if success else 400
    return jsonify(data=result, errors=result.errors), status_code



