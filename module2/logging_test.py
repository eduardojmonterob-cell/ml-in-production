from loguru import logger


# DEBUG
# INFO
# WARNINIG
# ERROR
# CRITICAL

logger.add('app.log', rotation='1 MB') # many options for rotation

def divide(a,b):
    return a / b

res = divide(10, 2)
logger.info(f"Division a / b")
print(res)