from rest_framework.exceptions import APIException

class InternalServerError (APIException):
  def __init__(self, message):
    self.detail = 'Internal Server Error'
    self.status_code = 500