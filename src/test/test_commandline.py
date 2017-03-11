"""
Testing Commandline
"""

import pytest
from gui import logger
import gui.commandline


LOGPATH = "../log/{}"
LOGFILE = LOGPATH.format("testlog.log")


def test_log_setup():
    assert gui.commandline.setupLog({'--logfile': LOGFILE}) == logger
    

def test_help_message():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-h", ])
        gui.commandline.parseArgs(["--help", ])
    assert excinfo is not None


def test_loglevel():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-d", ])
        gui.commandline.parseArgs(["--debug", ])


def test_logfile():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-l", LOGFILE, ])
        gui.commandline.parseArgs(["--logfile", LOGFILE, ])


def test_logformat():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["--logformat", "format", ])


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
