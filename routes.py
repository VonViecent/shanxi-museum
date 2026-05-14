from flask import Blueprint, request, jsonify
from models import db, Artifact, Exhibition, Visitor

api = Blueprint('api', __name__)

# Artifact CRUD
@api.route('/artifacts', methods=['GET'])
def get_artifacts():
    artifacts = Artifact.query.all()
    return jsonify([{'id': a.id, 'name': a.name, 'description': a.description, 'age': a.age, 'origin': a.origin} for a in artifacts])

@api.route('/artifacts', methods=['POST'])
def add_artifact():
    data = request.json
    artifact = Artifact(name=data['name'], description=data.get('description'), age=data.get('age'), origin=data.get('origin'))
    db.session.add(artifact)
    db.session.commit()
    return jsonify({'id': artifact.id}), 201

@api.route('/artifacts/<int:id>', methods=['PUT'])
def update_artifact(id):
    data = request.json
    artifact = Artifact.query.get_or_404(id)
    artifact.name = data['name']
    artifact.description = data.get('description')
    artifact.age = data.get('age')
    artifact.origin = data.get('origin')
    db.session.commit()
    return jsonify({'message': 'Updated'})

@api.route('/artifacts/<int:id>', methods=['DELETE'])
def delete_artifact(id):
    artifact = Artifact.query.get_or_404(id)
    db.session.delete(artifact)
    db.session.commit()
    return jsonify({'message': 'Deleted'})

# Exhibition CRUD
@api.route('/exhibitions', methods=['GET'])
def get_exhibitions():
    exhibitions = Exhibition.query.all()
    return jsonify([{'id': e.id, 'title': e.title, 'description': e.description, 'start_date': str(e.start_date), 'end_date': str(e.end_date)} for e in exhibitions])

@api.route('/exhibitions', methods=['POST'])
def add_exhibition():
    data = request.json
    exhibition = Exhibition(title=data['title'], description=data.get('description'), start_date=data.get('start_date'), end_date=data.get('end_date'))
    db.session.add(exhibition)
    db.session.commit()
    return jsonify({'id': exhibition.id}), 201

@api.route('/exhibitions/<int:id>', methods=['PUT'])
def update_exhibition(id):
    data = request.json
    exhibition = Exhibition.query.get_or_404(id)
    exhibition.title = data['title']
    exhibition.description = data.get('description')
    exhibition.start_date = data.get('start_date')
    exhibition.end_date = data.get('end_date')
    db.session.commit()
    return jsonify({'message': 'Updated'})

@api.route('/exhibitions/<int:id>', methods=['DELETE'])
def delete_exhibition(id):
    exhibition = Exhibition.query.get_or_404(id)
    db.session.delete(exhibition)
    db.session.commit()
    return jsonify({'message': 'Deleted'})

# Visitor CRUD (similarly, but user requested artifacts and exhibitions mainly, but include for completeness)
@api.route('/visitors', methods=['GET'])
def get_visitors():
    visitors = Visitor.query.all()
    return jsonify([{'id': v.id, 'name': v.name, 'email': v.email, 'visit_date': str(v.visit_date)} for v in visitors])

@api.route('/visitors', methods=['POST'])
def add_visitor():
    data = request.json
    visitor = Visitor(name=data['name'], email=data.get('email'), visit_date=data.get('visit_date'))
    db.session.add(visitor)
    db.session.commit()
    return jsonify({'id': visitor.id}), 201

@api.route('/visitors/<int:id>', methods=['PUT'])
def update_visitor(id):
    data = request.json
    visitor = Visitor.query.get_or_404(id)
    visitor.name = data['name']
    visitor.email = data.get('email')
    visitor.visit_date = data.get('visit_date')
    db.session.commit()
    return jsonify({'message': 'Updated'})

@api.route('/visitors/<int:id>', methods=['DELETE'])
def delete_visitor(id):
    visitor = Visitor.query.get_or_404(id)
    db.session.delete(visitor)
    db.session.commit()
    return jsonify({'message': 'Deleted'})