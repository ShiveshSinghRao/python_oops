class Validator:
    def __init__(self, strict=False):
        self.strict = strict

    @staticmethod
    def is_valid_email(email: str) -> bool:
        return "@" in email and "." in email.split("@")[-1]

    def validate(self, user_data: dict) -> list[str]:
        errors = []
        if not self.is_valid_email(user_data.get("email", "")):
            errors.append("Invalid email")
        if self.strict and len(user_data.get("name", "")) < 3:
            errors.append("Name too short")
        return errors


v = Validator(strict=True)
print(v.validate({"email": "bob@x.co", "name": "Bo"}))
# ["Name too short"]

# Can also use without an instance:
print(Validator.is_valid_email("bad-email"))
# False


"""
d un of v.validate({"email": "bob@x.co", "name": "Bo"}):

validate is a regular method → called as validate(self=v, user_data={"email": "bob@x.co", "name": "Bo"})
errors = []
Calls self.is_valid_email("bob@x.co")
is_valid_email is a staticmethod → self is not passed
Effectively calls is_valid_email("bob@x.co")
"@" in "bob@x.co" → True
"bob@x.co".split("@")[-1] → "x.co", "." in "x.co" → True
Returns True
not True → False, so "Invalid email" is not appended
self.strict → True, len("Bo") → 2 < 3 → True
Appends "Name too short"
Returns ["Name too short"]   
"""