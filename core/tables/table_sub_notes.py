from __init__ import db
from datetime import datetime
from core.models.model_subnote import SubnoteModel



class TableSubNotes(db.Model):
    __tablename__ = "subnotes"
    sub_note_id = db.Column(db.Integer, primary_key=True)
    rel_note_id = db.Column(db.String(64))
    text = db.Column(db.String(120))
    is_complete = db.Column(db.Boolean)
    is_visible = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    sequence = db.Column(db.Integer)

    def __repr__(self):
        return '<SubNote %r>' % self.text

    @classmethod
    def defineTable(cls, dictSubNote: SubnoteModel):
        return cls(rel_note_id=dictSubNote.rel_note_id,
                   text=dictSubNote.text,
                   is_complete=dictSubNote.is_complete,
                   is_visible=dictSubNote . is_visible,
                   created_at=dictSubNote.created_at,
                   sequence=dictSubNote.sequence)
