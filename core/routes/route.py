from flask.wrappers import Request
from core.models.model_note_book import NoteBookModel
from core.tables.table import TableNoteBooks
from __init__ import db

class RouteNoteBook:
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
        dict_note_book = NoteBookModel.fromJson(self.request.json)
        table_note_book = TableNoteBooks.defineTable(dict_note_book)
        db.session.add(table_note_book)
        db.session.commit()
        return " table_note_book.notebook_id"

    def get_method(self):
        return "this is a get method"

    def put_method(self):
        return "PUT Method"
