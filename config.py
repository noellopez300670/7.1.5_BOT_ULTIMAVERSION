from os import getenv

USERID = int(getenv('USERID'))

if USERID is None:

    raise Exception("Por favor configura el USERID del Bot") 

