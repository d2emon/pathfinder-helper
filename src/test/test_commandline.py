"""
Testing Commandline
"""

import pytest
import gui
import gui.commandline


LOGPATH = "../log/{}"


def test_log_setup():
    logger = gui.commandline.setupLog({'filename': LOGPATH.format("logfile.log")})
    assert logger == gui.logger
    

def test_help_message():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-h", ])
        gui.commandline.parseArgs(["--help", ])


def test_loglevel():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-d", ])
        gui.commandline.parseArgs(["--debug", ])


def test_logfile():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-l", LOGPATH.format("logtest.log"), ])
        gui.commandline.parseArgs(["--logfile", LOGPATH.format("logtest.log"), ])


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
        gui.commandline.parseArgs(["-f", LOGPATH.format("filename.test"), ])
        gui.commandline.parseArgs(["--file", LOGPATH.format("filename.test"), ])


def test_actions():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-l", LOGPATH.format("filename.test"), ], True)
