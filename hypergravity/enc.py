from cryptography.fernet import Fernet

ENC_KEY = b'lMg05d-R_TSTiYzscI0WZpQaIXrCaBM0FnxEELkBp_k='
fernet = Fernet(ENC_KEY)

MY_ADSABS_TOKEN = fernet.decrypt(
    b'gAAAAABj1NgTsGr-QlZowWPjGDTdjZAFqIUYO8fKFaNZDP6uGFZ3Lxz1XsYfE2BIjIGtYS1MwBfrZfppVkHzuMh1OXrX'
    b'Q8h-aVE3AiOzZQtYQ1GlJya-N9TF7wjq2vJFUoaOoH8AsuI0'
).decode("utf-8")
