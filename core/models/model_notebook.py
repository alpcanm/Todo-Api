from datetime import datetime


class NoteBookModel:
    notebook_id = None
    rel_user_id = None
    text = None
    created_at = None
    last_update = None
    is_visible = None
    icon_data = None
    sequence = None

    def __init__(self, notebook_id,
                 rel_user_id,
                 text,
            created_at,
            last_update,
                 is_visible,
                 icon_data,
                 sequence):
        self.notebook_id = notebook_id
        self.rel_user_id = rel_user_id
        self.text = text
        self.created_at = created_at
        self.last_update = last_update
        self.is_visible = is_visible
        self.icon_data = icon_data
        self.sequence = sequence

    @classmethod
    def fromJson(cls, dict: dict):
        return cls(notebook_id=dict["notebook_id"],
                   rel_user_id=dict["rel_user_id"],
                   text=dict["text"],
                   created_at=datetime.now(),
                   last_update=datetime.now(),
                   is_visible=dict["is_visible"],
                   icon_data=dict["icon_data"], 
                   sequence=dict["sequence"])

    def toDict(self):
        return {
            "notebook_id": self.notebook_id,
            "rel_user_id": self.rel_user_id,
            "text": self.text,
            "last_update": self.last_update,
            "created_at": self.created_at,
            "icon_data": self.icon_data,
            "is_visible": self.is_visible,
            "sequence": self.sequence
        }
