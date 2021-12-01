class User:
    def __init__(self, methodType):
        self.method = methodType

    def switch(self):
        if self.method == "PUT":
            return self.put_method()
        elif self.method == "POST":
            return self.post_method()
        else:
            return self.get_method()

    def post_method(self):
        return "Post Method"

    def get_method(self):
        return "Get Method"

    def put_method(self):
        return "PUT Method"
