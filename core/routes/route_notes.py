from flask.json import jsonify
from flask.wrappers import Request
from core.models.model_note import NoteModel
from __init__ import db
from core.tables.table_notes import TableNotes


class RouteNotes:

    def post_method(self, request: Request):
        client = NoteModel.fromJson(request.json)
        table = TableNotes.defineTable(client)
        db.session.add(table)
        db.session.commit()
        return " this is a response "

    def get_method(self, parameter: str):
        dbData = TableNotes.query.filter_by(rel_notebook_id=parameter,is_visible=True).all()
        resultList = []
        for x in dbData:
            result = NoteModel.fromJson(x.__dict__)
            resultList.append(result.toDict())
        return jsonify(resultList)

    def put_method(self):
        return "PUT Method"

    def patch_method(self, parameter: int, request: Request):
        vari = request.get_json()
        column_name = None
        new_value = None
        for key, value in vari.items():
            column_name = key
            new_value = value
        db.session.query(TableNotes).filter_by(note_id=parameter).update(
            {column_name: new_value})
        db.session.commit()
        return "this is an update method"
