"""
Testing Commandline
"""

import pytest
import gui.commandline


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
        gui.commandline.parseArgs(["-l", "logtest.log", ])
        gui.commandline.parseArgs(["--logfile", "logtest.log", ])


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
        gui.commandline.parseArgs(["-f", "filename.test", ])
        gui.commandline.parseArgs(["--file", "filename.test", ])


def test_actions():
    import getopt
    with pytest.raises(getopt.GetoptError) as excinfo:
        gui.commandline.parseArgs(["-l", "filename.test", ], True)
