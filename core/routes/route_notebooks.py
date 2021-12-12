from flask.json import jsonify
from flask.wrappers import Request
from core.models.model_notebook import NoteBookModel
from core.tables.table_notebooks import TableNoteBooks
from __init__ import db
import json


class RouteNoteBooks:
    def __init__(self, request: Request):
        self.request = request

    def switch(self, parameter: str):
        if self.request.method == "PUT":
            return self.put_method()
        elif self.request.method == "POST":
            return self.post_method()
        else:
            return self.get_method(parameter)

    def post_method(self):
        client = NoteBookModel.fromJson(self.request.json)
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
