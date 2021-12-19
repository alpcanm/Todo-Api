class UserModel:
    user_id = None
    name = None
    surname = None
    password = None
    mail = None
    created_at = None
    phone_number = None
    photo_url = None
    mail_verified = None

    def __init__(self, user_id,
                 name,
                 surname,
                 mail,
                 created_at,
                 password,
                 phone_number,
                 mail_verified,
                 photo_url,):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.mail = mail
        self.password = password
        self.created_at = created_at
        self.phone_number = phone_number
        self.photo_url = photo_url
        self.mail_verified = mail_verified

    @classmethod
    def fromJson(cls, dict: dict):
        return cls(user_id=dict["user_id"],
                   name=dict["name"],
                   surname=dict["surname"],
                   password=dict["password"],
                   mail=dict["mail"],
                   created_at=str(dict["created_at"]),
                   phone_number=dict["phone_number"],
                   photo_url=dict["photo_url"],
                   mail_verified=dict["mail_verified"],

                   )

    def toDict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'surname': self.surname,
            'mail': self.mail,
            'created_at': self.created_at,
            'password': self.password,
            'phone_number': self.phone_number,
            'photo_url': self.photo_url,
            'mail_verified': self.mail_verified,
        }
