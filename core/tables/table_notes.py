from datetime import datetime

from __init__ import db
from core.models.model_notebook import NoteBookModel


class TableNotes(db.Model):
    __tablename__ = "notes"
    note_id = db.Column(db.Integer, primary_key=True)
    rel_notebook_id = db.Column(db.String(64))
    text = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    last_update = db.Column(db.DateTime, onupdate=datetime.utcnow)
    is_visible = db.Column(db.Boolean)
    is_major = db.Column(db.Boolean)
    is_complete = db.Column(db.Boolean)
    comment = db.Column(db.String(500))
    sequence = db.Column(db.Integer)

    def __repr__(self):
        return '<Note %r>' % self.text

    @classmethod
    def defineTable(cls, dictNoteBook: NoteBookModel):
        return cls(rel_user_id=dictNoteBook.rel_user_id,
                   text=dictNoteBook.text,
                   created_at=dictNoteBook.created_at,
                   last_update=dictNoteBook.last_update,
                   is_visible=dictNoteBook . is_visible,
                   icon_data=dictNoteBook.icon_data,
                   sequence=dictNoteBook.sequence)
