class Note:
    note_id = None
    rel_notebook_id = None
    text = None
    created_at = None
    last_update = None
    is_visible = None
    is_major = None
    is_complete = None
    comment = None
    sequence = None

    def __init__(self, note_id,
                 rel_notebook_id,
                 text,
                 created_at,
                 last_update,
                 is_visible,
                 is_major,
                 is_complete,
                 comment,
                 sequence):
        self.note_id = note_id
        self.rel_notebook_id = rel_notebook_id
        self.text = text
        self.created_at = created_at
        self.last_update = last_update
        self.is_visible = is_visible
        self.is_major = is_major
        self.is_complete = is_complete
        self.comment = comment
        self.sequence = sequence

    @classmethod
    def fromJson(cls, dict: dict):
        return cls(note_id=dict["note_id"],
                   rel_notebook_id=dict["rel_notebook_id"],
                   text=dict["text"],
                   created_at=str(dict["created_at"]),
                   last_update=str(dict["last_update"]),
                   is_visible=dict["is_visible"],
                   is_major=dict["is_major"],
                   is_complete=dict["is_complete"],
                   comment=dict["comment"],
                   sequence=dict["sequence"],
                   )

    def toDict(self):
        return {
            "note_id": self.note_id,
            "rel_notebook_id": self.rel_notebook_id,
            "text": self.text,
            "created_at": self.created_at,
            "last_update": self.last_update,
            "is_major": self.is_major,
            "is_visible": self.is_visible,
            "is_complete": self.is_complete,
            "comment": self.comment,
            "sequence": self.sequence,
        }
