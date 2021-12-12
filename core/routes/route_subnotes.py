from flask.json import jsonify
from flask.wrappers import Request
from __init__ import db
from core.models.model_subnote import SubnoteModel
from core.tables.table_sub_notes import TableSubNotes
class RouteSubNotes:
    def __init__(self, request: Request):
        self.request = request

    def switch(self,parameter:str):
        if self.request.method == "PUT":
            return self.put_method()
        elif self.request.method == "POST":
            return self.post_method()
        else:
            return self.get_method(parameter)

    def post_method(self):
        client = SubnoteModel.fromJson(self.request.json)
        table = TableSubNotes.defineTable(client)
        db.session.add(table)
        db.session.commit()
        return " this is a response "

    def get_method(self,parameter:str):
        dbData = TableSubNotes.query.filter_by(rel_note_id=parameter).all()
        resultList = []
        for x in dbData:
            result = SubnoteModel.fromJson(x.__dict__)
            resultList.append(result.toDict())
        return jsonify(resultList)

    def put_method(self):
        return "PUT Method"
