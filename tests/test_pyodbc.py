import logging
import sys
import pytest

logger = logging.getLogger(__name__)
@pytest.mark.skipif(sys.platform != 'win32', reason="PYDOBC only on windows")
def test_find_pyodbc_driver():
    try:
        import pyodbc
    except ImportError:
        logger.error("Must install pyodbc for ImpactWorld. See install instructions for optional package"
                       " installation or install it indepedently and retry.")
    driver_check = ([x for x in pyodbc.drivers()])
    driver_found = any('Microsoft Access Driver' in word for word in driver_check)
    logger.debug("Found pyodbc drivers: %s", driver_check)
    assert driver_found == True
