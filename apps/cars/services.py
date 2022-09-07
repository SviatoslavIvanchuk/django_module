import os
from uuid import uuid1


def upload_to(_, file: str):
    return os.path.join('cars', f'{uuid1()}.{file.split(".")[-1]}')
