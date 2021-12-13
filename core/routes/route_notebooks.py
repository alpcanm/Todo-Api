from flask.json import jsonify
from flask.wrappers import Request
from core.models.model_notebook import NoteBookModel
from core.tables.table_notebooks import TableNoteBooks
from __init__ import db
import json


class RouteNoteBooks:

    def post_method(self, request: Request):
        client = NoteBookModel.fromJson(request.json)
        table = TableNoteBooks.defineTable(client)
        db.session.add(table)
        db.session.commit()

        return " this is a response "

    def get_method(self, parameter: str):
        dbData = TableNoteBooks.query.filter_by(rel_user_id=parameter).all()
        resultList = []
        for x in dbData:
            result = NoteBookModel.fromJson(x.__dict__)
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
        db.session.query(TableNoteBooks).filter_by(notebook_id=parameter).update(
            {column_name: new_value})
        db.session.commit()
        return "this is an update method"
