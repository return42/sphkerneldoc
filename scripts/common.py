#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-

# pylint: disable=R0912

u"""
    common
    ~~~~~~

    C&P some of my common usefull python scripting / don't look to close ;-)

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.
"""

# pylint: disable=C0330,W0141

__all__ = [
    'CLI'
    , 'FSPath', 'which'
    , 'progressBar', 'humanizeBytes'
    , 'OS_ENV'
    , 'Container', 'PContainer'
    , 'PANDOC_EXE', 'xml2json', 'jsonFilter', 'json2rst', 'xml_unescape'
    , 'Console', 'Pdb']

# ==============================================================================
# imports
# ==============================================================================

import functools
import os, sys, argparse, codecs, json
import shutil, subprocess, re
import pdb, inspect, linecache
from code   import InteractiveConsole
from codeop import CommandCompiler

import pandocfilters

from os import path
from glob import iglob

PY3 = sys.version_info[0] == 3
PY2 = sys.version_info[0] == 2

if PY3:
    # pylint: disable=C0103
    unicode     = str
    basestring  = str
    raw_input   = input
    from html.parser import HTMLParser # pylint: disable=F0401

if PY2:
    from HTMLParser import HTMLParser  # pylint: disable=F0401

xml_unescape = HTMLParser().unescape   # pylint: disable=C0103

PANDOC_EXE = None

def init():
    global PANDOC_EXE # pylint: disable=W0603
    PANDOC_EXE = which('pandoc')
    setRTE()

# ==============================================================================
def toJSONFilters(input_stream, output_stream, *actions):
# ==============================================================================

    """Modified version of pandoc filter.

    This version of pandoc filter is able to read from any input stream (not only
    from stdin) and writes to any output stream (not only stdout).
    """
    doc = json.loads(input_stream.read())
    fmt = "json"
    altered = functools.reduce(
        lambda x, action: pandocfilters.walk(x, action, fmt, doc[0]['unMeta'])
        , actions, doc )
    json.dump(altered, output_stream)

# ==============================================================================
def xml2json(src, dst, **kwargs):
# ==============================================================================

    u"""convert xml file to json file with pandoc"""

    proc = PANDOC_EXE.Popen(
        "--smart"
        # , "-s" # standalone document
        , "--from", "docbook"
        , "--to", "json"
        , "--output" , dst
        , src
        , **kwargs )
    proc.communicate()

# ==============================================================================
def jsonFilter(src, dst, *filters):
# ==============================================================================

    u"""apply ``*filters`` ton a pandoc json file"""

    with src.openTextFile() as inFile, dst.openTextFile("w") as outFile:
        toJSONFilters(inFile, outFile, *filters)


# ==============================================================================
def json2rst(src, dst, **kwargs):
# ==============================================================================

    u"""convert a json file with pandoc to reST markup"""

    proc = PANDOC_EXE.Popen(
        "--reference-links"
        , "--from", "json"
        , "--to", "rst"
        , "--output" , dst
        # FIXME: this is a hotfix for the large tables of the linux_tv tables
        , "--columns" , "180"
        , src
        , **kwargs )
    proc.communicate()

# ==============================================================================
class CLI(object):
# ==============================================================================

    u"""A comfortable commandline.

    :py:class:`CLI` wraps python functions into subcommands on the
    commandline. It is based on :py:mod:`argparse` and includes a bash
    *completion* (:py:meth:`CLI.autocomplete`).

    A simple usage example:

    .. code-block:: python

       def hello(cliArgs):
           '''A simple *hello* command.

           The *hello* command prints the commandline arguments.
           '''
           from pprint import pformat
           cliArgs.CLI.msg(pformat(cliArgs.__dict__, indent=4))

       def main():
           cli = CLI(description="Wraps python functions to commandline.")
           cli.addCMDParser(hello)

       if __name__ == "__main__":
           main()
    """

    _OUT = sys.__stdout__
    _ERR = sys.__stderr__

    def __init__(self, *args, **kwargs):

        self.cmdFunc       = kwargs.pop("cmdFunc", None)
        self.cliSubParsers = None

        if self.cmdFunc is not None:
            kwargs["epilog"] = kwargs.get("epilog", self.cmdFunc.__doc__)
            kwargs["description"] = kwargs.get(
                "description"
                , kwargs["epilog"].strip().split("\n")[0] if kwargs["epilog"] else None)

        self.parser        = argparse.ArgumentParser(*args, **kwargs)

        if self.cmdFunc is None:
            self.cliSubParsers = self.parser.add_subparsers(title='commands', dest='command')
            self.cliSubParsers.required = True

        self.add_argument  = self.parser.add_argument
        self.add_argument(
            '--debug'
            , action  = 'store_true'
            , help    = 'run in debug mode' )

    def addCMDParser(self, func, cmdName=None):

        if self.cliSubParsers is None:
            raise Exception("this command-line has no sub-commands!")

        subCmd = self.cliSubParsers.add_parser(
            cmdName or func.__name__
            , epilog          = func.__doc__
            , help            = ((func.__doc__ or "").strip().split("\n") + [ "sorry, no help available" ])[0]
        )
        subCmd.set_defaults(func=func)
        return subCmd

    @classmethod
    def msg(cls, message):
        # pylint: disable=W0702,C0321
        try:      message = unicode(message)
        except:   message = repr(message)
        cls.write(message, cls._OUT)

    @classmethod
    def err(cls, message, prefix=u"ERROR: "):
        # pylint: disable=W0702,C0321
        try:      message = unicode(message)
        except:   message = repr(message)
        cls.write(prefix + message, cls._ERR)

    @classmethod
    def write(cls, msg, _file=None, end='\n'):
        _file = _file or cls._OUT
        if not isinstance(msg, basestring):
            msg = unicode(msg)
        _file.write(msg)
        _file.write(end)

    def __call__(self):

        _exitCode  = 0
        _exception = None
        _retVal    = None

        self.autocomplete()

        cmd_args = self.parser.parse_args()
        cmd_args.CLI = self

        if cmd_args.debug:
            sys.stderr.write(u"DEBUG: argparse --> %s\n" % cmd_args)
        try:
            if self.cmdFunc is None:
                _retVal = cmd_args.func(cmd_args)
            else:
                _retVal = self.cmdFunc(cmd_args)
            try:
                _exitCode = int(_retVal)
            except Exception as exc: # pylint: disable=W0703
                pass

        except Exception as exc: # pylint: disable=W0703
            if cmd_args.debug:
                raise
            _exitCode  = 42
            _exception = str(exc)
            sys.stderr.write(u"FATAL ERROR: %s\n" % _exception)
        sys.exit(_exitCode)

    def autocomplete(self):
        u"""bash completion

        To get in use of bash completion, install ``argcomplete``:

        .. code-block:: bash

           pip install argcomplete

        and add the following to your ~/.bashrc:

        .. code-block:: bash

            function _py_argcomplete() {

                local IFS=$(echo -e '\v')
                COMPREPLY=( $(IFS="$IFS" \
                    COMP_LINE="$COMP_LINE" \
                    COMP_POINT="$COMP_POINT" \
                    _ARGCOMPLETE_COMP_WORDBREAKS="$COMP_WORDBREAKS" \
                    _ARGCOMPLETE=1 \
                    "$1" 8>&1 9>&2 1>/dev/null) )
                if [[ $? != 0 ]]; then
                    unset COMPREPLY
                fi
            }

           complete -o nospace -o default -F _py_argcomplete myCommandName
        """

        # only complete when called from _py_argcomplete()
        if '_ARGCOMPLETE' not in os.environ:
            return
        try:
            import argcomplete
        except:   # pylint: disable=W0702
            self.err("ERROR: TAB-completion, python-argcomplete not installed.")
            sys.exit(1)
        argcomplete.autocomplete(self.parser)

# ==============================================================================
class Container(dict):
# ==============================================================================

    u"""
    Containerklasse zum Halten von Werten.
    """
    @property
    def __dict__(self):
        u"""Emulate the ``self.__dict__`` of an ``object`` type.
        """
        return self

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, val):
        self[attr] = val


# ==============================================================================
class PContainer(Container):
# ==============================================================================

    u"""Eine persistente Version der Containerklasse.

    Die Persitenz ist eine json Datei, es können nur Objekte gespeichert werden,
    die von :py:mod:`json.dump` serialisiert werden können.

    """

    def __init__(self, fname, *args, **kwargs):
        dict.__setattr__(self, "pFile", FSPath(fname))
        self.updFromFile()
        super(PContainer, self).__init__(self, *args, **kwargs)

    def updFromFile(self):
        if not self.pFile.EXISTS:
            return
        with self.pFile.openTextFile(mode='r', encoding='utf-8') as jsonFile:
            self.update(json.load(jsonFile, encoding='utf-8'))

    def writeToFile(self):
        tmpFile = FSPath(self.pFile + "tmp")
        with tmpFile.openTextFile(mode='w', encoding='utf-8') as jsonFile:
            jsonFile.write(unicode(json.dumps(self, ensure_ascii=False)))
        tmpFile.move(self.pFile)

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.writeToFile()


# ==============================================================================
class OS_ENV(dict):
# ==============================================================================

    u"""
    Containerklasse für den Zugriff auf das Environment
    """

    @property
    def __dict__(self):
        u"""Emulate the ``self.__dict__`` of an ``object`` type.
        """
        return os.environ

    def __getattr__(self, attr):
        return os.environ[attr]

    def __setattr__(self, attr, val):
        os.environ[attr] = val

    def get(self, attr, default=None):
        return os.environ.get(attr, default)

OS_ENV = OS_ENV()

# ==============================================================================
def which(fname, findall=False):
# ==============================================================================
    u"""
    Sucht die übergebenen Dateinamen im ``PATH``.

    Neben dem Dateinamen wird auf Windows noch nach den Dateinamenserweiterungen
    ".exe", ".cmd", ".bat" gesucht.  Wird nichts gefunden, so wird ``None``
    zurückgegeben.  Es ist nicht zugesichert, dass diese Dateinamen auch
    tatsächlich ausführbare Programme sind.

    Über die Option ``findall`` wird gesteuert, ob der erste Treffer
    zurückgegeben wird oder ob alle Treffer (eine Liste) zurückgegeben werden
    sollen.
    """
    exe = ["", ".exe", ".cmd", ".bat"]
    if sys.platform != 'win32':
        exe = [""]
    envpath = os.environ.get('PATH', None) or os.defpath

    locations = set()
    for folder in envpath.split(os.pathsep):
        for ext in exe:
            fullname = FSPath(folder + os.sep + fname + ext)
            if fullname.ISFILE:
                if not findall:
                    return fullname
                locations.add(fullname)
    return locations or None

# ==============================================================================
class FSPath(unicode):
# ==============================================================================

    u"""
    Ein Pfadname / Datei oder Ordner.

    Mit dem ``FSPath`` (File-System-Path) können Pfadnamen etwas komfortabler
    gehandhabt werden, so können beispielsweise Ordnernamen durch den
    Divisions-Operator (``/``) konkateniert werden und es gibt
    komfort-Funktionen zum Prüfen oder erstellen von Pfaden im Filesystem.

    .. code-block:: python

       >>> folder = FSPath("folder")
       >>> print folder / "subfolder"  # der os.sep ist auf Windows "\\" statt "/"
       folder/subfolder

       >>> print "topfolder" / folder0
       topfolder/folder

       >>> print folder + "addedstr"
       folderaddedstr

       >>> print (folder/"foo"/"bar.txt").splitpath()
       (u'folder/foo', u'bar.txt')

       >>> print (folder/"foo"/"../bar.txt")
       folder/bar.txt
    """

    # pylint: disable=C0103

    def __new__(cls, pathname):
        pathname = path.normpath(path.expanduser(unicode(pathname)))
        return super(FSPath, cls).__new__(cls, pathname)

    @property
    def VALUE(self):
        return unicode(self)

    @property
    def EXISTS(self):
        return path.exists(self)

    @property
    def isReadable(self):
        return os.access(self, os.R_OK)

    @property
    def isWriteable(self):
        return os.access(self, os.W_OK)

    @property
    def isExecutable(self):
        return os.access(self, os.X_OK)

    @property
    def ISDIR(self):
        return path.isdir(self)

    @property
    def ISFILE(self):
        return path.isfile(self)

    @property
    def ISLINK(self):
        return path.islink(self)

    @property
    def DIRNAME(self):
        u"""Der Pfadname des Ordners, in dem die Datei ist.

        Bsp.: ``/path/to/folder/filename.ext`` --> ``/path/to/folder``
        """
        return self.__class__(path.dirname(self))

    @property
    def BASENAME(self):
        u"""Der Name der Datei ohne den Pfadnamen des Ordners aber mit Erweiterung.

        Bsp.: ``/path/to/folder/filename.ext`` --> ``filename.ext``
        """
        return self.__class__(path.basename(self))

    @property
    def FILENAME(self):
        u"""Der Name ohne Erweiterung und ohne Pfad

        Bsp.: ``/path/to/folder/filename.ext`` --> ``filename``

        """
        return self.__class__(path.splitext(path.basename(self))[0])

    @property
    def SUFFIX(self):
        u"""Die Dateiendung.

        Bsp.: ``/path/to/folder/filename.ext`` --> ``.ext``

        """
        return self.__class__(path.splitext(self)[1])

    @property
    def SKIPSUFFIX(self):
        u"""Der komplette Name nur ohne Erweiterung

        Bsp.: ``/path/to/folder/filename.ext`` --> ``/path/to/folder/filename``
        """
        return self.__class__(path.splitext(self)[0])

    @property
    def ABSPATH(self):
        u"""Der absolute Pfadname der Datei

        Bsp.: ``../to/../to/folder/filename.ext`` --> ``/path/to/folder/filename.ext``

        """
        return self.__class__(path.abspath(self))

    @property
    def REALPATH(self):
        u"""Der *reale* Pfadname der Datei (entfernt symbolische Links).
        """
        return self.__class__(path.realpath(self))

    @property
    def POSIXPATH(self):
        u"""Der Pfad in der *POSIX* Notation
        """
        if os.sep == "/":
            return unicode(self)
        else:
            p = unicode(self)
            if p[1] == ":":
                p = "/" + p.replace(":", "", 1)
            return p.replace(os.sep, "/")

    @property
    def NTPATH(self):
        u"""Der Pfad in der Windows üblichen Notation.
        """
        if os.sep == "\\":
            return unicode(self)
        else:
            return unicode(self).replace(os.sep, "\\")

    @property
    def EXPANDVARS(self):
        return self.__class__(path.expandvars(self))

    @property
    def EXPANDUSER(self):
        return self.__class__(path.expanduser(self))

    @classmethod
    def getHOME(cls):
        return cls(path.expanduser("~"))

    def makedirs(self, mode=0o775):
        if not self.ISDIR:
            return os.makedirs(self, mode)

    def __div__(self, pathname):
        return self.__class__(self.VALUE + os.sep + unicode(pathname))
    __truediv__ = __div__

    def __rdiv__(self, pathname):
        return self.__class__(unicode(pathname) + os.sep + self.VALUE)

    def __add__(self, other):
        return self.__class__(self.VALUE + unicode(other))

    def __radd__(self, other):
        return self.__class__(unicode(other) + self.VALUE)

    def relpath(self, start):
        return self.__class__(path.relpath(self, start))

    def splitpath(self):
        head, tail = path.split(self)
        return (self.__class__(head), self.__class__(tail))

    def listdir(self):
        for name in os.listdir(self):
            yield self.__class__(name)

    def glob(self, pattern):
        for name in  iglob(self / pattern ):
            yield self.__class__(name)

    def walk(self, topdown=True, onerror=None, followlinks=False):
        for dirpath, dirnames, filenames in os.walk(self, topdown, onerror, followlinks):
            yield self.__class__(dirpath), dirnames, filenames

    def reMatchFind(self, name, isFile=True, isDir=True, followlinks=False):

        # find first e.g: next(myFolder.reMatchFind(r".*name.*"), None)

        name_re = re.compile(name)
        for folder, dirnames, filenames in self.walk(followlinks=followlinks):
            if isDir:
                for d_name in filter(name_re.match, dirnames):
                    yield folder / d_name
            if isFile:
                for f_name in filter(name_re.match, filenames):
                    yield folder / f_name

    def suffix(self, newSuffix):
        return self.__class__(self.SKIPSUFFIX + newSuffix)

    def copyfile(self, dest, preserve=False):
        if preserve:
            shutil.copy2(self, dest)
        else:
            shutil.copy(self, dest)

    def copytree(self, dest, symlinks=False, ignore=None):
        shutil.copytree(self, dest, symlinks, ignore)

    def move(self, dest):
        shutil.move(self, dest)

    def delete(self):
        return os.remove(self)

    def rmtree(self, ignore_errors=False, onerror=None):
        shutil.rmtree(self, ignore_errors, onerror)

    def filesize(self, precision=None):
        size = os.path.getsize(self)
        if precision is not None:
            size = humanizeBytes(size, precision)
        return size

    def openTextFile(self, mode='r', encoding='utf-8', errors='strict', buffering=1):
        return codecs.open(
            self, mode=mode, encoding=encoding
            , errors=errors, buffering=buffering)

    def readFile(self, encoding='utf-8', errors='strict'):
        with self.openTextFile(encoding=encoding, errors=errors) as f:
            return f.read()

    def Popen(self, *args, **kwargs):
        u"""
        Der ``subprocess.Popen Konstruktor``.

        Das Aufzurufende Kommando ist der Verzeichnispfad des ``self`` Objekts,
        welcher als erstes Argument den übergebenen ``*args`` vorangestellt wird.

        siehe https://docs.python.org/2/library/subprocess.html#popen-constructor

        .. code-block:: python

          from myCourtTools import FSPath
          proc = FSPath("arp").Popen("-a")
          stdout, stderr = proc.communicate()
          retVal = proc.returncode
          print "stdout: %s" % stdout
          print "stder: %s" % stderr
          print "exit code = %d" % retVal

        """
        defaults = {
            'stdout'   : subprocess.PIPE
            , 'stderr' : subprocess.PIPE
            , 'stdin'  : subprocess.PIPE
            }
        defaults.update(kwargs)
        #print " ".join([self,] + list(args))
        return subprocess.Popen(
            [self,] + list(args)
            , **defaults
            )

# ==============================================================================
def humanizeBytes(size, precision=2):
# ==============================================================================

    """
    Emittelt den *menschen lesbaren* Wert der Byteanzahl.
    """
    s = ['B ', 'KB', 'MB', 'GB', 'TB']
    x = len(s)
    p = 0
    while size > 1024 and p < x:
        p += 1
        size = size/1024.0
    return "%.*f %s" % (precision, size, s[p])

# ==============================================================================
def progressBar(step, maxSteps, barSize=None, pipe=sys.stdout, prompt=""):
# ==============================================================================

    """
    Anzeigen einer Progressbar.

    * step: Schrittnummer
    * maxSteps: maximale Anzahl an Schritten
    * barSize: Länge der Balkenanzeige
    """

    percent = float(100)/maxSteps*step

    prompt = "\r" + prompt
    if barSize is None:
        barSize = consoleDimension()[1]
        barSize = barSize - 3 - len(prompt) - len(" %3d%%"  % (100,))

    p_bar = "/" * int(percent / 100 * barSize)
    pipe.write((prompt +  "[%s] %3d%%") % (p_bar.ljust(barSize, "-"), int(percent)))
    pipe.flush()


# ==============================================================================
def consoleDimension():
# ==============================================================================

    rows, columns = 25, 80

    import platform
    if 'Windows' == platform.system():
        try:
            rows, columns = _consoleDimensionsWIN()
        except Exception: # pylint: disable=W0703
            pass
    else:
        try:
            rows, columns = _consoleDimensionsLinux()
        except Exception: # pylint: disable=W0703
            pass
    try:
        rows = int(rows)
    except Exception:     # pylint: disable=W0703
        pass

    try:
        columns = int(columns)
    except Exception:     # pylint: disable=W0703
        pass

    return rows, columns

def _consoleDimensionsLinux():
    rows, columns = os.popen('stty size', 'r').read().split()
    return rows, columns

def _consoleDimensionsWIN():
    # pylint: disable=W0612, R0914

    from ctypes import windll, create_string_buffer

    # stdin handle is -10
    # stdout handle is -11
    # stderr handle is -12

    h = windll.kernel32.GetStdHandle(-12)
    csbi = create_string_buffer(22)
    res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

    columns, rows = 80, 25
    if res:
        import struct
        (bufx, bufy, curx, cury, wattr,
         left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        columns = right - left + 1
        rows    = bottom - top + 1

    return rows, columns


# ==============================================================================
def ERROR(msg): # pylint: disable=C0103
# ==============================================================================

    sys.__stderr__.write(msg + "\n")
    sys.__stderr__.flush()

# ==============================================================================
def descrFrame(frame, arround=3):
# ==============================================================================

    fName  = frame.f_code.co_filename
    lineNo = frame.f_lineno
    lines = []
    for c in range(lineNo - arround, lineNo + arround):
        if c > 0:
            prefix = "%-04s|" % c
            if c == lineNo:
                prefix = "---->"
            line = linecache.getline(fName, c, frame.f_globals)
            if line != '':
                lines.append(prefix + line)
            else:
                if lines:
                    lines[-1] = lines[-1] + "<EOF>\n"
                break
    retVal = (
        "".join(lines)
        + "file: %s:%s\n" % (fName, lineNo)
        )
    return retVal

# ==============================================================================
class Console(InteractiveConsole):
# ==============================================================================

    u"""Eine einfache Konsole.
    """

    EOF = None

    def __init__(self, local_ns=None, global_ns=None
                 , filename="<console>"): # pylint: disable=W0231
        if local_ns is None:
            local_ns = {"__name__": "__console__", "__doc__": None}

        if global_ns is None:
            global_ns = {}

        self.local_ns  = local_ns
        self.global_ns = global_ns
        self.compile   = CommandCompiler()
        self.filename  = filename
        self.resetbuffer()

    def raw_input(self, prompt=""):
        if self.EOF is None:
            return raw_input(prompt)
        else:
            sys.stdout.write(prompt)
            sys.stdout.flush()
            line = sys.stdin.readline()
            ERROR(repr(line))
            if line.strip() == self.EOF:
                raise EOFError
            return line

    def write(self, data):
        sys.stdout.write(data)
        sys.stdout.flush()

    def runcode(self, code):
        try:
            exec(code, self.global_ns, self.local_ns) # pylint: disable=W0122
        except SystemExit:
            raise
        except Exception: # pylint: disable=W0703
            self.showtraceback()

    @classmethod
    def run(cls, local_ns=None, global_ns=None, banner=None
            , filename="<console>", frame=None, EOF=None): # pylint: disable=C0103
        u"""Startet eine Konsole.

        Sofern die Namensräume (``local_ns``, ``global_ns``) nicht expliziet
        anegegeben werden, werden diese aus dem aktuellen Code-Frame
        übernommen.

        .. code-block:: python

          def foo(arg1):
              ...
              Console.run()

        """
        frame = frame or inspect.currentframe().f_back
        if banner is None:
            banner = "console ...\n%s" % descrFrame(frame)
        if local_ns is None:
            local_ns = frame.f_locals
        if global_ns is None:
            global_ns = frame.f_globals
        #inspect.currentframe().f_back
        console = cls(local_ns, global_ns, filename)
        if EOF:
            banner += "\nExit console with %r" % EOF
            console.EOF = EOF # pylint: disable=C0103
        console.interact(banner=banner)

# ==============================================================================
class Pdb(pdb.Pdb):  # pylint: disable=R0904
# ==============================================================================

    def do_src(self, arg):
        if not arg:
            arg = 3
        self.stdout.write(descrFrame(self.curframe, int(arg)) + "\n")

    def help_src(self):
        self.stdout.write("""show
Show source around current command (frame)
""")

    def do_console(self, arg):  # pylint: disable=W0613
        Console.run(frame=self.curframe, EOF='EOF')

    def help_console(self):
        self.stdout.write("""console
run an interactive console in the current frame.
""")

# ==============================================================================
class SDK(object): # pylint: disable=W0622
# ==============================================================================

    u"""Der Namensraum SDK wird in den ``__builtins__`` zur Verfügung gestellt.

    Wird diese Module an einer zentralen Stelle importiert (z.B. beim Start
    der Anwendung im DEBUG Modus). Dann steht der Name SDK zur Verfügung ohne
    das man in seinen Modulen einen Import durchführen muss."""

    @staticmethod
    def BREAKPOINT(frame=None):
        u"""Setzt einen Breakpoint für den debugger """

        frame = frame or inspect.currentframe().f_back
        Pdb().set_trace(frame=frame)

    @staticmethod
    def CONSOLE(frame=None, banner=None):
        u"""Setzt einen Breakpoint für die Console """

        frame = frame or inspect.currentframe().f_back
        Console.run(frame=frame, banner=banner)

def setRTE():
    #import os, sys  # warning this will be imported from outside of the pyenv

    HERE    = os.path.dirname(__file__)           # pylint: disable=C0103
    history = os.path.join(HERE, ".pmbhistory")

    def activate_pyenv():                          # pylint: disable=W0612
        if sys.platform == 'win32':
            af = os.path.join(HERE, "pyenv", "Scripts", "activate_this.py")
        else:
            af = os.path.join(HERE, "pyenv", "bin", "activate_this.py")

        # pylint: disable=W0122
        exec(compile(open('af').read()), dict(__file__=af))

        #if os.environ.get('VIRTUAL_ENV', None) != os.path.join(HERE, "pyenv"):
        #    #sys.stderr.write("activate pyenv.\n")
        #    execfile(af, dict(__file__=af))
        #else:
        #    #sys.stderr.write("pyenv allready activated.\n")
        #    pass

    def import_readline():
        # sys.stderr.write("interactive session / adding tab completion.\n")
        try:
            import readline
            import rlcompleter   # pylint: disable=W0612
        except ImportError:
            try:
                import pyreadline as readline  #pylint: disable=F0401
                import rlcompleter
            except ImportError:
                # sys.stderr.write(
                #     "WARNING: no readline support, no completion."
                #     "\n  Using commandline without completion is'nt funny,"
                #     "\n  install readline or pyreadline at all.\n"
                # )
                readline = None
        return readline

    def bind_tab_complete():
        if readline is None:
            sys.stderr.write("WARNING: no readline support, no completion.\n")

        if readline.__doc__ and 'libedit' in readline.__doc__:
            # Darwin uses 'libedit'::
            #   >>> readline.__doc__
            #   'Importing this module enables command line editing using libedit readline.'
            #
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            # More common is GNU readline::
            #   >>> readline.__doc__
            #   'Importing this module enables command line editing using GNU readline.'
            #
            readline.parse_and_bind("tab: complete")

    def load_history():
        if os.path.exists(history):
            readline.read_history_file(history)

    def save_history():
        readline.write_history_file(history)

    def register_exit_handler():
        import atexit
        atexit.register(save_history)

    #activate_pyenv()
    if sys.__stdin__.isatty():
        readline = import_readline()
        if readline is not None:
            bind_tab_complete()
            load_history()
            register_exit_handler()

# ==============================================================================
# extend builtins
# ==============================================================================

__builtins__["SDK"] = SDK
init()
del setRTE
