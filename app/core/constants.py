from decouple import config

TIMEZONE = config("TIMEZONE")
MONGO_URI = config("MONGO_URI")
CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND")

SERVER_ERROR = "Internal Server Error"

OK = 200
INTERNAL_SERVER_ERROR = "A server error occurred"
BAD_REQUEST = "Invalid input data"
ACCEPTED = "Request accepted"
NOT_ACCEPTABLE = "Request not accepted"
