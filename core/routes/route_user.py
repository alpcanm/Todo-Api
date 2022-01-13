from __init__ import db
from flask.json import jsonify
from flask.wrappers import Request
from core.models.model_user import UserModel
from core.tables.table_user import TableUser


class RouteUsers:
    db_data = None
    identity = None

    def post_method(self, request: Request):
        client = UserModel.fromJson(request.json)
        table = TableUser.defineTable(client)
        db.session.add(table)
        db.session.commit()
        return "this is a response"

    def get_user(self, id: str):
        dbData = TableUser.query.filter_by(
            user_id=id).first()
        result = UserModel.fromJson(dbData.__dict__).toDict()
        return jsonify(result)

    def check_user(self, mail: str, password: str):
        dbData = TableUser.query.filter_by(
            mail=mail, password=password, ).first()
        
        self.identity = str(dbData.__dict__['user_id'])
        self.db_data = dbData

        if dbData != None:
            return True
        else:
            return False

    # def get_method(self, parameter: str):
    #     dbData = TableSubNotes.query.filter_by(
    #         rel_note_id=parameter, is_visible=True).all()
    #     resultList = []
    #     for x in dbData:
    #         result = SubnoteModel.fromJson(x.__dict__)
    #         resultList.append(result.toDict())
    #     return jsonify(resultList)

    # def patch_method(self, parameter: int, request: Request):
    #     vari = request.get_json()
    #     column_name = None
    #     new_value = None
    #     for key, value in vari.items():
    #         column_name = key
    #         new_value = value
    #     db.session.query(TableSubNotes).filter_by(sub_note_id=parameter).update(
    #         {column_name: new_value})
    #     db.session.commit()
    #     return "this is an update method"
