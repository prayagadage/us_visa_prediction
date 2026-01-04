from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys


logging.info("Welcoe to US Visa Prediction Project")

try:
    1/0
except Exception as e:
    raise USvisaException(e,sys)
