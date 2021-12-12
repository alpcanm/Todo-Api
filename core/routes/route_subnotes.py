from flask.json import jsonify
from flask.wrappers import Request
from __init__ import db
from core.models.model_subnote import SubnoteModel
from core.tables.table_sub_notes import TableSubNotes


class RouteSubNotes:

    def post_method(self, request: Request):
        client = SubnoteModel.fromJson(request.json)
        table = TableSubNotes.defineTable(client)
        db.session.add(table)
        db.session.commit()
        return " this is a response "

    def get_method(self, parameter: str):
        dbData = TableSubNotes.query.filter_by(rel_note_id=parameter).all()
        resultList = []
        for x in dbData:
            result = SubnoteModel.fromJson(x.__dict__)
            resultList.append(result.toDict())
        return jsonify(resultList)

    def put_method(self):
        return "PUT Method"
