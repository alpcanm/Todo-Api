from datetime import datetime
from __init__ import db
from core.models.model_notebook import NoteBookModel


class TableNoteBooks(db.Model):
    __tablename__ = "notebooks"
    notebook_id = db.Column(db.Integer, primary_key=True)
    rel_user_id = db.Column(db.String(64))
    text = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    last_update = db.Column(db.DateTime, onupdate=datetime.utcnow)
    is_visible = db.Column(db.Boolean)
    icon_data = db.Column(db.String(120))
    sequence = db.Column(db.Integer)

    def __repr__(self):
        return '<NoteBook %r>' % self.text

    @classmethod
    def defineTable(cls, dictNoteBook: NoteBookModel):
        return cls(rel_user_id=dictNoteBook.rel_user_id,
                   text=dictNoteBook.text,
                   created_at=dictNoteBook.created_at,
                   last_update=dictNoteBook.last_update,
                   is_visible=dictNoteBook . is_visible,
                   icon_data=dictNoteBook.icon_data,
                   sequence=dictNoteBook.sequence)
