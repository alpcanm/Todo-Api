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

    def get_method(self,parameter:str):
        dbData = TableNotes.query.filter_by(rel_notebook_id=parameter).all()
        resultList = []
        for x in dbData:
            result = NoteModel.fromJson(x.__dict__)
            resultList.append(result.toDict())
        return jsonify(resultList)

    def put_method(self):
        return "PUT Method"
