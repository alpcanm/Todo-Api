from flask.json import jsonify
from flask.wrappers import Request
from core.models.model_note import NoteModel
from __init__ import db
from core.tables.table_notes import TableNotes


class RouteNotes:
    def __init__(self, request: Request):
        self.request = request

    def switch(self):
        if self.request.method == "PUT":
            return self.put_method()
        elif self.request.method == "POST":
            return self.post_method()
        else:
            return self.get_method()

    def post_method(self):
        client = NoteModel.fromJson(self.request.json)
        table = TableNotes.defineTable(client)
        db.session.add(table)
        db.session.commit()
        return " this is a response "

    def get_method(self):
        dbData = TableNotes.query.filter_by(rel_user_id="1").all()
        resultList = []
        for x in dbData:
            result = NoteModel.fromJson(x.__dict__)
            resultList.append(result.toDict())
        return jsonify(resultList)

    def put_method(self):
        return "PUT Method"
