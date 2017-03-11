"""
Testing Commandline
"""

import pytest

import gui
import gui.commandline
import logging


LOGPATH = "../log/{}"
LOGFILE = LOGPATH.format("testlog.log")


def test_log_setup():
    assert gui.commandline.setupLog({'--logfile': LOGFILE}) == gui.logger
    

def test_loglevel():
    import logging
    
    gui.DEBUG = False
    gui.commandline.parseArgs([])
    assert gui.DEBUG == False
    assert gui.logger.getEffectiveLevel() != logging.DEBUG

    gui.DEBUG = False
    gui.commandline.parseArgs(["-d", ])
    assert gui.DEBUG == True
    assert gui.logger.getEffectiveLevel() == logging.DEBUG
    
    gui.DEBUG = False
    gui.commandline.parseArgs(["--debug", ])
    assert gui.DEBUG == True
    assert gui.logger.getEffectiveLevel() == logging.DEBUG


def test_help_message():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-h", ])
        gui.commandline.parseArgs(["--help", ])
    assert excinfo is not None


def test_count():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-c", "5", ])
        gui.commandline.parseArgs(["--count", "5", ])


def test_roll():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-r", "r", ])
        gui.commandline.parseArgs(["--roll", "r", ])


def test_file():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-f", LOGFILE, ])
        gui.commandline.parseArgs(["--file", LOGFILE, ])


def test_actions():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-l", LOGFILE, ], True)
