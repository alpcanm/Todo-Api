from __init__ import db
from datetime import datetime
from core.models.model_note import NoteModel

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
    def defineTable(cls, dictNote: NoteModel):
        return cls(created_at=dictNote.created_at,
                   rel_notebook_id=dictNote.rel_notebook_id,
                   text=dictNote.text,
                   last_update=dictNote.last_update,
                   is_visible=dictNote . is_visible,
                   is_major=dictNote.is_major,
                   is_complete=dictNote.is_complete,
                   comment=dictNote.comment,
                   sequence=dictNote.sequence)
