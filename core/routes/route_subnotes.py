
from __init__ import db
from flask.json import jsonify
from flask.wrappers import Request
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
        dbData = TableSubNotes.query.filter_by(
            rel_note_id=parameter, is_visible=True).all()
        resultList = []
        for x in dbData:
            result = SubnoteModel.fromJson(x.__dict__)
            resultList.append(result.toDict())
        return jsonify(resultList)

    def patch_method(self, parameter: int, request: Request):
        vari = request.get_json()
        column_name = None
        new_value = None
        for key, value in vari.items():
            column_name = key
            new_value = value
        db.session.query(TableSubNotes).filter_by(sub_note_id=parameter).update(
            {column_name: new_value})
        db.session.commit()
        return "this is an update method"
