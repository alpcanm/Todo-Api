class NoteBookModel:
    noteBookId = None
    relUserId = None
    text = None
    createdAt = None
    lastUpdate = None
    isVisible = None
    iconData = None

    def __init__(self, noteBookId,
                 relUserId,
                 text,
                 createdAt,
                 lastUpdate,
                 isVisible,
                 iconData):
        self.noteBookId = noteBookId
        self.relUserId = relUserId
        self.text = text
        self.createdAt = createdAt
        self.lastUpdate = lastUpdate
        self.isVisible = isVisible
        self.iconData = iconData

    @classmethod
    def fromJson(cls, dict: dict):
        return cls(dict["noteBookId"],
                   dict["relUserId"],
                   dict["text"],
                   dict["createdAt"],
                   dict["lastUpdate"],
                   dict["isVisible"],
                   dict["iconData"])

    def toDict(self):
        return {
            "noteBookId": self.noteBookId,
            "relUserId": self.relUserId,
            "text": self.text,
            "lastUpdate": self.lastUpdate,
            "createdAt": self.createdAt,
            "iconData": self.iconData,
            "isVisible": self.isVisible
        }

        
