class AuthenticationService:
    def is_authenticated(self, role_or_id, id=None):
        if id is None:
            return self.authenticate_by_id(role_or_id)
        else:
            return self.authenticate_by_role(role_or_id)

    def authenticate_by_id(self, id):
        return id == 12345

    def authenticate_by_role(self, role):
        return role == 'admin'

class AuthenticationClient:
    def __init__(self, authenticationService):
        self.authenticationService = authenticationService

    def run(self):
        authenticated = self.authenticationService.is_authenticated(33)
        print("is authenticated: ", str(authenticated))


class YetAnotherClient:
    def run(self):
        AuthenticationService().is_authenticated(100)


if __name__ == "__main__":
    client = AuthenticationClient(AuthenticationService())
    client.run()
