from datetime import datetime
from __init__ import db
from core.models.model_note_book import NoteBookModel

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

    def __repr__(self):
        return '<Note %r>' % self.text

    @classmethod
    def defineTable(cls, dictNoteBook: NoteBookModel):
        return cls(notebook_id=dictNoteBook.noteBookId,
                   rel_user_id=dictNoteBook.relUserId,
                   text=dictNoteBook.text,
                   created_at=dictNoteBook.createdAt,
                   last_update=dictNoteBook.lastUpdate,
                   is_visible=dictNoteBook . isVisible,
                   icon_data=dictNoteBook.iconData)