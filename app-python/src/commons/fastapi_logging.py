import logging

"""
 https://github.com/encode/uvicorn/issues/614
"""

def config_logging(level="INFO"):

   logging.getLogger().handlers.clear()

   logging.basicConfig(
       # match gunicorn format
       format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
       datefmt='[%Y-%m-%d %H:%M:%S %z]',
       level=level)

   logging.getLogger('uvicorn.access').handlers.clear()
   logging.getLogger('uvicorn.error').handlers.clear()
   logging.getLogger('uvicorn.access').propagate = True
   logging.getLogger('uvicorn.error').propagate = False
