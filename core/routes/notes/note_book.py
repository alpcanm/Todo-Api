
from re import S
from flask.wrappers import Request
import json

from core.database.connection import MyDb


class NoteBook:

    def __init__(self, request: Request):
        self.db = MyDb()
        self.request = request
        self.method = request.method

    def switch(self):
        if self.method == "PUT":
            return self.put_method()
        elif self.method == "POST":
            return self.post_method()
        else:
            return self.get_method()

    def post_method(self):
        noteBook = dict(json.loads(self.request.data))
        relUserId = noteBook["relUserId"]
        text = noteBook["text"]
        createdAt = noteBook["createdAt"]
        lastUpdate = noteBook["lastUpdate"]
        isVisible = noteBook["isVisible"]
        iconData = noteBook["iconData"]
        query = f"""
        insert into notebooks (rel_user_id,text,created_at,last_update,is_visible,icon_data)
        values
        ('{relUserId}','{text}','{createdAt}','{lastUpdate}',{isVisible},'{iconData}')
        """

        self.db.post(query)
        return "Post Method"

    def get_method(self):
        query = """
            select * from notebooks
        """
        fetchAll = self.db.get(query)
        resultList = []
        for noteBook in fetchAll:
            resultList.append(self.sorguToPython(noteBook))
        return json.dumps(resultList)

    def sorguToPython(self, noteBook: tuple):
        relUserId = noteBook[0]
        text = noteBook[1]
        createdAt = noteBook[2]
        lastUpdate = noteBook[3]
        isVisible = noteBook[4]
        iconData = noteBook[5]
        noteBookId = str(noteBook[6])
        result = {
            "noteBookId": noteBookId,
            "relUserId": relUserId,
            "text": text,
            "createdAt": createdAt,
            "lastUpdate": lastUpdate,
            "isVisible": isVisible,
            "iconData": iconData
        }
        return result

    def put_method(self):
        return "PUT Method"
