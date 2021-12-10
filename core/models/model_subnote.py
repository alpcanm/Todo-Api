class Subnote:
    sub_note_id = None
    rel_note_id = None
    text = None
    is_complete = None
    is_visible = None
    created_at = None
    sequence = None

    def __init__(self, sub_note_id, rel_note_id, text, is_complete, is_visible, created_at, sequence):
        self.sub_note_id = sub_note_id
        self.rel_note_id = rel_note_id
        self.text = text
        self.is_complete = is_complete
        self.is_visible = is_visible
        self.created_at = created_at
        self.sequence = sequence

    @classmethod
    def fromJson(cls, dict: dict):
        return cls(sub_note_id=dict["sub_note_id"],
                   rel_note_id=dict["rel_note_id"],
                   text=dict["text"],
                   is_complete=dict["is_complete"],
                   is_visible=dict["is_visible"],
                   created_at=str(dict["created_at"]),
                   sequence=dict["sequence"])

    def toDict(self):
        return {
            "sub_note_id": self.sub_note_id,
            "rel_note_id": self.rel_note_id,
            "text": self.text,
            "is_complete": self.is_complete,
            "is_visible": self.is_visible,
            "created_at": self.created_at,
            "sequence": self.sequence,
        }
