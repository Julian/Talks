---
title: Python's Standard Library
location: Columbia University PDL
date: 2025/4/4
author: Julian Berman
---

Hi.
===

<!-- column_layout: [3, 2] -->

<!-- column: 0 -->

<!-- new_lines: 3 -->

![image:width:33%](github.png)

<!-- new_lines: 3 -->

![image:width:25%](githublogo.png)

`/in/julian-berman`

<!-- column: 1 -->

<!-- new_lines: 5 -->

![image](jsonschemalogo.png)
![image](leannvimlogo.png)

<!-- new_lines: 2 -->

---

<!-- new_lines: 2 -->

![image:width:40%](deloittedigitallogo.png)
![image:width:40%](postmanlogo.png)

<!-- end_slide -->

Three Types of Python Code
==========================

<!-- column_layout: [2, 2, 2] -->

<!-- column: 0 -->
<!-- jump_to_middle -->
# Built-ins

```python +exec
print(len([2, 4, 6]))
```

<!-- pause -->
<!-- column: 1 -->
<!-- jump_to_middle -->
# Standard Library

```python +exec
import math
/// print(
math.sqrt(2)
/// )
```

<!-- pause -->
<!-- column: 2 -->
<!-- jump_to_middle -->
# Third Party Libraries

```python
import numpy
import pandas
import pygame
...
```

<!-- end_slide -->

*Three Types of Python Code
===========================

<!-- column_layout: [2, 2, 2] -->

<!-- column: 0 -->
<!-- jump_to_middle -->

```python +exec
import json
print(json)
```

<!-- column: 1 -->
<!-- jump_to_middle -->

```python +exec
import math
print(math)
```

<!-- column: 2 -->
<!-- jump_to_middle -->

```python +exec
import sys
print(sys)
```

<!-- end_slide -->

# What's in the Standard Library?

```python +exec
import sys
/// modules = \
sorted(sys.stdlib_module_names)
/// cols = 6
/// padding = 0
/// width = max(len(m) for m in modules) + padding
/// for i in range(0, len(modules), cols):
///     print("".join(f"{m:<{width}}" for m in modules[i:i+cols]))
/// print(f"\n{len(modules)} modules")
```

<!-- end_slide -->

<!-- jump_to_middle -->

Thanks!
===

<!-- column_layout: [1, 3, 1] -->
<!-- column: 1 -->

Questions?

<!-- end_slide -->

<!-- jump_to_middle -->

Let's cross some off.
===

<!-- end_slide -->

<!-- jump_to_middle -->

```python +exec
import _random
print(_random)
```
<!-- pause -->

```python +exec
import random
print(random)
```

<!-- new_lines: 3 -->

<!-- pause -->

These are "private" and/or "implementation details".
They won't appear in the online documentation.

<!-- pause -->

There are also a bunch of "misnamed" private modules which don't follow the convention, like `sre_compile`, `sre_constants`, `genericpath`...

<!-- end_slide -->

# What's in the Standard Library? Take 2

```python +exec
import sys
MISNAMED_PRIVATE = {"pydoc_data", "sre_compile", "sre_constants", "sre_parse", "genericpath"}
/// modules = \
sorted(
  name
  for name in sys.stdlib_module_names
  if not name.startswith("_")
     and name not in MISNAMED_PRIVATE
)
/// cols = 6
/// padding = 2
/// width = max(len(m) for m in modules) + padding
/// for i in range(0, len(modules), cols):
///     print("".join(f"{m:<{width}}" for m in modules[i:i+cols]))
/// print(f"\n{len(modules)} modules")
```

<!-- end_slide -->

# What's in the Standard Library? Take 3

```python +exec
import sys
MISNAMED_PRIVATE = {"pydoc_data", "sre_compile", "sre_constants", "sre_parse", "genericpath"}
/// modules = \
sorted(
  name
  for name in sys.stdlib_module_names
  if (not name.startswith("_") or name.startswith("__"))
      and name not in MISNAMED_PRIVATE
)
/// cols = 6
/// padding = 2
/// width = max(len(m) for m in modules) + padding
/// for i in range(0, len(modules), cols):
///     print("".join(f"{m:<{width}}" for m in modules[i:i+cols]))
/// print(f"\n{len(modules)} modules")
```

<!-- end_slide -->

# What's in the Standard Library? Take 4

<!-- column_layout: [2, 1, 6] -->

<!-- column: 0 -->

<!-- jump_to_middle -->

## Not Really for Programmers

* `ensurepip`
* `site`
* `py_compile`
* `compileall`
* `zipimport`

These have to do with:

  - setting up a Python installation

  or

  - managing it in a way generally unrelated to programming in the language

<!-- column: 2 -->

<!-- pause -->

```python +exec
import sys
FOR_SYSADMIN = {"ensurepip", "site", "py_compile", "compileall", "zipimport"}
MISNAMED_PRIVATE = {"pydoc_data", "sre_compile", "sre_constants", "sre_parse", "genericpath"}
IGNORED = FOR_SYSADMIN | MISNAMED_PRIVATE
/// modules = \
sorted(
  name
  for name in sys.stdlib_module_names - IGNORED
  if not name.startswith("_")
  or name.startswith("__")
)
/// cols = 6
/// padding = 2
/// width = max(len(m) for m in modules) + padding
/// for i in range(0, len(modules), cols):
///     print("".join(f"{m:<{width}}" for m in modules[i:i+cols]))
/// print(f"\n{len(modules)} modules")
```

<!-- end_slide -->

# What's in the Standard Library? Take 5

<!-- column_layout: [2, 1, 6] -->

<!-- column: 0 -->

## Is This a Joke?

```python +exec
import this
```

<!-- pause -->

---

### (No, it's mostly for kids.)

```python
from turtle import *
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)
```

![image:width:33%](turtle-star.png)

---

<!-- pause -->
<!-- column: 2 -->

### (Yes.)

```python +exec
import antigravity
```

<!-- pause -->

```python +exec
import sys
JOKES = {"antigravity", "this", "turtle", "turtledemo"}
FOR_SYSADMIN = {"ensurepip", "site", "py_compile", "compileall", "zipimport"}
MISNAMED_PRIVATE = {"pydoc_data", "sre_compile", "sre_constants", "sre_parse", "genericpath"}
IGNORED = JOKES | FOR_SYSADMIN | MISNAMED_PRIVATE
/// modules = \
sorted(
  name
  for name in sys.stdlib_module_names - IGNORED
  if not name.startswith("_")
  or name.startswith("__")
)
/// cols = 6
/// padding = 2
/// width = max(len(m) for m in modules) + padding
/// for i in range(0, len(modules), cols):
///     print("".join(f"{m:<{width}}" for m in modules[i:i+cols]))
/// print(f"\n{len(modules)} modules")
```

<!-- end_slide -->

<!-- jump_to_middle -->

# Ask an LLM?

```sh +exec +acquire_terminal
nvim -c "CopilotChat
Help us learn about the Python standard library.

There are around 200 modules which are not private or implementation details.
Divide them up into 4 groups, containing modules which:

* target a common use case, are well written and widely used
* target a common use case, but are considered poor implementations
* target a rare or hyper-specific use case
* are considered bad or outdated ideas entirely
/// " -c "wincmd o"
```

<!-- end_slide -->

<!-- jump_to_middle -->

# Starting With the Worst

[PEP 594](https://peps.python.org/pep-0594/)
===

<!-- pause -->

But these have still taken an incredibly long time to remove.
Python doesn't like breaking existing code without very good reason!

<!-- end_slide -->

# What's in the Standard Library? Take 6

```python +exec
import sys
DEAD = {"aifc", "asynchat", "asyncore", "audioop", "cgi", "cgitb", "chunk",
        "crypt", "imghdr", "mailcap", "msilib", "nntplib", "nis",
        "ossaudiodev", "pipes", "smtpd", "sndhdr", "spwd", "sunau",
        "telnetlib", "uu", "xdrlib"}
JOKES = {"antigravity", "this", "turtle", "turtledemo"}
FOR_SYSADMIN = {"ensurepip", "site", "py_compile", "compileall", "zipimport"}
MISNAMED_PRIVATE = {"pydoc_data", "sre_compile", "sre_constants", "sre_parse", "genericpath"}
IGNORED = DEAD | JOKES | FOR_SYSADMIN | MISNAMED_PRIVATE
/// modules = \
sorted(
  name
  for name in sys.stdlib_module_names - IGNORED
  if not name.startswith("_")
  or name.startswith("__")
)
/// cols = 6
/// padding = 2
/// width = max(len(m) for m in modules) + padding
/// for i in range(0, len(modules), cols):
///     print("".join(f"{m:<{width}}" for m in modules[i:i+cols]))
/// print(f"\n{len(modules)} modules")
```

<!-- end_slide -->

<!-- jump_to_middle -->
OK, Let's see some things that aren't terrible.
==

<!-- end_slide -->
<!-- jump_to_middle -->

# The Good

* `pathlib`
* `subprocess`
* `os` + `sys` + `platform`
* `sqlite3`
* `json` + `csv` + `tomllib`
* `datetime` + `time` + `zoneinfo`
* `collections`
* `random`
* `math` + `cmath` + `statistics`
* `fractions` + `decimal`
* `pprint` + `textwrap` + `string` + `unicodedata`
* `re`
* `pdb` + `profile` + `pstats`
* `typing`
* `itertools`
* `functools` + `contextlib`

<!-- end_slide -->
<!-- jump_to_middle -->

# `pathlib`

```python +exec
from pathlib import Path

directory = Path.home() / "Desktop/example_dir"
directory.mkdir(exist_ok=True)

path = directory / "output.txt"
path.write_text("Hello, pathlib world!")
print(path.parent)
print(path.suffix)
```

<!-- pause -->

```python +exec
/// from pathlib import Path
/// directory = Path.home() / "Desktop/example_dir"
/// path = directory / "output.txt"
print(path.read_text())
path.unlink()
directory.rmdir()
```

<!-- pause -->

(There's also the `ntpath` and `posixpath` modules, and `genericpath` which is seemingly private and misnamed.)

<!-- end_slide -->
<!-- jump_to_middle -->

# `subprocess`

```python +exec
import subprocess
my_computer_name = subprocess.run(
  ["hostname"],
  capture_output=True,
  check=True,
  text=True,
).stdout.rstrip()
print(f"My computer is named {my_computer_name}.")
```

<!-- pause -->

```python +exec
/// import subprocess
subprocess.run(["ping", "-c", "3", "google.com"])
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `os`, `sys` and `platform`

```python +exec
import os
print(f"I use: {os.environ.get("SHELL")}")
print(os.cpu_count())
```

<!-- pause -->

```python +exec
import platform
print(platform.mac_ver())
```

<!-- pause -->

```python +exec
import sys
print(sys.executable)
sys.stdout.write("Hello!")
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `sqlite3`

```python +exec
import sqlite3
connection = sqlite3.connect("database.db")
with connection:
  connection.execute(
      """
      CREATE TABLE IF NOT EXISTS contacts
      (
          id INTEGER PRIMARY KEY,
          name TEXT,
          email TEXT
      ) STRICT
      """
  )
connection.close()
/// from pathlib import Path
/// Path("database.db").unlink()
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `json` + `csv` + `tomllib`

```python +exec
import json
contact = json.loads('{"name": "Julian", "email": "jb4661@columbia.edu"}')
print(json.dumps({contact["name"]: contact["email"]}))
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `datetime` + `time` + `zoneinfo` (+ `calendar`)

```python +exec
from time import time
print("Timestamp:", time())

from datetime import datetime
from zoneinfo import ZoneInfo

tokyo = ZoneInfo("Asia/Tokyo")
now_in_tokyo = datetime.now(tz=tokyo)
print(now_in_tokyo)

print(now_in_tokyo - datetime(2025, 1, 1, tzinfo=tokyo))
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `collections`

```python +exec
counts = {"Julian": 37, "Alice": 3}
print(counts["Bob"])
```

<!-- pause -->

```python +exec
from collections import defaultdict
counts = defaultdict(int, {"Julian": 37, "Alice": 3})
print(counts["Bob"])
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `random`

```python +exec
import random
print(random.randint(1, 10))
print(random.choice(["Julian", "Alice", "Bob"]))
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `math` + `cmath` + `statistics`

```python +exec
import cmath
import math
print(math.sqrt(2))
print(cmath.sqrt(-1 + 1j))
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `fractions` + `decimal`

```python +exec
from fractions import Fraction
from decimal import Decimal

print(Fraction(2, 3) * 3)
print(Decimal("0.2") + Decimal("0.3"))
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `pprint`

```python +exec
print({"some": "long", "dictionary": list(range(10)), "or": "other", "container": "!"})
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `pprint`

```python +exec
from pprint import pp
pp({"some": "long", "dictionary": list(range(10)), "or": "other", "container": "!"})
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `textwrap`

```python +exec
def print_squares():
    for i in range(1, 4):
        for j in range(1, 4):
          print(
            f"""
            {i} * {j} = {i * j}
            """.rstrip("\n"),
            end="",
          )
  
print_squares()
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `textwrap`

```python +exec
def print_squares():
    for i in range(1, 4):
        for j in range(1, 4):
          print(
f"""
{i} * {j} = {i * j}
""".rstrip("\n"),
            end="",
          )
  
print_squares()
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `textwrap`

```python +exec
from textwrap import dedent

def print_squares():
    for i in range(1, 4):
        for j in range(1, 4):
          print(
            dedent(
              f"""
              {i} * {j} = {i * j}
              """
            ).rstrip("\n"),
            end="",
          )
  
print_squares()
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `string` (+ `unicodedata`)

```python +exec
import string
print(string.digits, "\n", string.punctuation)
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `re`

```python +exec
import re
text = "Python was created in 1991 by Guido van Rossum."
match = re.search(r"\d{4}", text)
print(match.group(0))
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `typing`

```python +exec
import typing

users: dict[str, dict[str, typing.Any]] = {
  "Julian": {"name": "Julian Berman", "email": "jb4661@columbia.edu"},
}

def find_email(name: str) -> str | None:
  user = users.get(name)
  if user is not None:
    return user["email"]

print(find_email("Julian"))
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `itertools`

```python +exec
import itertools

count = itertools.count()
print(next(count))
print(next(count))
print(next(count))

names = itertools.cycle(["Julian", "Alice", "Bob"])
print(next(names))
print(next(names))
print(next(names))
print(next(names))
print(next(names))
print(next(names))
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `functools`

```python +exec
from functools import cache

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(37))
```

<!-- end_slide -->
<!-- jump_to_middle -->

# `contextlib`

```python +exec
import contextlib
import sqlite3

with contextlib.closing(sqlite3.connect(":memory:")) as connection:
  connection.execute(
      """
      CREATE TABLE IF NOT EXISTS contacts
      (
          id INTEGER PRIMARY KEY,
          name TEXT,
          email TEXT
      ) STRICT
      """
  )
```

<!-- end_slide -->
<!-- jump_to_middle -->

# Where Are We?

\_\_future\_\_
abc
argparse
array
ast
asyncio
atexit
base64
bdb
binascii
bisect
builtins
bz2
cProfile
`calendar`
`cmath`
cmd
code
codecs
codeop
`collections`
colorsys
concurrent
configparser
`contextlib`
contextvars
copy
copyreg
`csv`
ctypes
curses
dataclasses
`datetime`
dbm
`decimal`
difflib
dis
doctest
email
encodings
enum
errno
faulthandler
fcntl
filecmp
fileinput
fnmatch
`fractions`
ftplib
`functools`
gc
`genericpath`
getopt
getpass
gettext
glob
graphlib
grp
gzip
hashlib
heapq
hmac
html
http
idlelib
imaplib
importlib
inspect
io
ipaddress
`itertools`
`json`
keyword
linecache
locale
logging
lzma
mailbox
marshal
`math`
mimetypes
mmap
modulefinder
msvcrt
multiprocessing
netrc
nt
`ntpath`
nturl2path
numbers
opcode
operator
optparse
`os`
`pathlib`
pdb
pickle
pickletools
pkgutil
`platform`
plistlib
poplib
posix
`posixpath`
`pprint`
profile
pstats
pty
pwd
pyclbr
pydoc
`pydoc_data`
pyexpat
queue
quopri
`random`
`re`
readline
reprlib
resource
rlcompleter
runpy
sched
secrets
select
selectors
shelve
shlex
shutil
signal
smtplib
socket
socketserver
`sqlite3`
`sre_compile`
`sre_constants`
`sre_parse`
ssl
stat
`statistics`
`string`
stringprep
struct
`subprocess`
symtable
`sys`
sysconfig
syslog
tabnanny
tarfile
tempfile
termios
`textwrap`
threading
`time`
timeit
tkinter
token
tokenize
`tomllib`
trace
traceback
tracemalloc
tty
`turtle`
`turtledemo`
types
`typing`
`unicodedata`
unittest
urllib
uuid
venv
warnings
wave
weakref
webbrowser
winreg
winsound
wsgiref
xml
xmlrpc
zipapp
zipfile
`zipimport`
zlib
`zoneinfo`

<!-- end_slide -->
<!-- jump_to_middle -->

# Obsolete or Worse Than an Alternative 🌶️

<!-- incremental_lists: true -->
<!-- column_layout: [1, 2] -->

<!-- column: 0 -->

* `os.path` -> `pathlib`
* `glob` -> `pathlib` (but `fnmatch` still sometimes useful)

<!-- column: 1 -->
```python +exec
/// from pathlib import Path
print(list(Path.home().glob("D*")))
```

<!-- column: 0 -->

* `getopt` -> `optparse` -> `argparse` -> `click`

<!-- column: 1 -->

```sh
script.py --output file.txt
```
<!-- column: 0 -->

* `array` -> `numpy`
* `configparser` -> `tomllib`
* `ctypes`
* `urllib` -> (`requests`) -> `httpx`
* `unittest` -> `pytest`
* `html`, `xml`, (`xmlrpc`, `pyexpat`) -> `lxml`
* `ftplib`
* `doctest` -> `sphinx.ext.doctest`
* `tkinter`
* `idlelib` -> anything, but often VSCode

<!-- end_slide -->
<!-- jump_to_middle -->

# Too Low Level or Insecure 🌶️🌶️

<!-- incremental_lists: true -->

* `curses`, `termios` -> `rich`, `prompt-toolkit`, `urwid`
* `hashlib`, `hmac`, `ssl` -> `cryptography`
* `pickle`, `marshal`, `shelve`,(`copyreg`, `pickletools`)
* `socket`, `socketserver`, `select`, `selectors`
* `email`, `http`, `quopri`, `imaplib`, `poplib`, `smtplib`, `wsgiref`
* `atexit`, `signal`
* `threading`, `multiprocessing`, `concurrent`, `contextvars`

<!-- end_slide -->
<!-- jump_to_middle -->

# Worse Than an Alternative 🌶️🌶️🌶️

<!-- incremental_lists: true -->
<!-- column_layout: [1, 2] -->

<!-- column: 0 -->

* `dataclasses` -> `attrs`

<!-- column: 1 -->

```python +exec
from dataclasses import dataclass

@dataclass
class Point:
  x : int
  y : int

print(Point(x=12, y=37))
```

<!-- column: 0 -->

* `asyncio`, `concurrent.futures` -> `trio`
* `copy`
* `logging` -> `structlog`

<!-- end_slide -->
<!-- jump_to_middle -->

# Where Are We?

\_\_future\_\_
abc
`argparse`
`array`
ast
`asyncio`
`atexit`
base64
bdb
binascii
bisect
builtins
bz2
cProfile
`calendar`
`cmath`
cmd
code
codecs
codeop
`collections`
colorsys
`concurrent`
`configparser`
`contextlib`
`contextvars`
`copy`
`copyreg`
`csv`
`ctypes`
`curses`
`dataclasses`
`datetime`
dbm
`decimal`
difflib
dis
`doctest`
`email`
encodings
enum
errno
faulthandler
fcntl
filecmp
fileinput
`fnmatch`
`fractions`
`ftplib`
`functools`
gc
`genericpath`
`getopt`
getpass
gettext
`glob`
graphlib
grp
gzip
`hashlib`
heapq
`hmac`
`html`
`http`
`idlelib`
`imaplib`
importlib
inspect
io
ipaddress
`itertools`
`json`
keyword
linecache
locale
`logging`
lzma
mailbox
`marshal`
`math`
mimetypes
mmap
modulefinder
msvcrt
`multiprocessing`
netrc
nt
`ntpath`
nturl2path
numbers
opcode
operator
`optparse`
`os`
`pathlib`
pdb
`pickle`
`pickletools`
pkgutil
`platform`
plistlib
`poplib`
posix
`posixpath`
`pprint`
profile
pstats
pty
pwd
pyclbr
pydoc
`pydoc_data`
`pyexpat`
queue
`quopri`
`random`
`re`
readline
reprlib
resource
rlcompleter
runpy
sched
secrets
`select`
`selectors`
`shelve`
shlex
shutil
`signal`
`smtplib`
`socket`
`socketserver`
`sqlite3`
`sre_compile`
`sre_constants`
`sre_parse`
`ssl`
stat
`statistics`
`string`
stringprep
struct
`subprocess`
symtable
`sys`
sysconfig
syslog
tabnanny
tarfile
tempfile
`termios`
`textwrap`
`threading`
`time`
timeit
`tkinter`
token
tokenize
`tomllib`
trace
traceback
tracemalloc
tty
`turtle`
`turtledemo`
types
`typing`
`unicodedata`
`unittest`
`urllib`
uuid
venv
warnings
wave
weakref
webbrowser
winreg
winsound
`wsgiref`
`xml`
`xmlrpc`
zipapp
zipfile
`zipimport`
zlib
`zoneinfo`

<!-- end_slide -->
<!-- jump_to_middle -->

# Let's try out a few

https://classroom.github.com/a/PC7zhbVW
===

<!-- end_slide -->

Further Reading
===

<!-- jump_to_middle -->

* [The Standard Library documentation](https://docs.python.org/3/library/index.html)
* Doug Hellmann's [PyMOTW](https://pymotw.com/3/)


<!-- new_line -->

* [Anthony Sottile](https://www.youtube.com/@anthonywritescode/search?query=python)

<!-- end_slide -->

<!-- jump_to_middle -->

Thanks!
===

<!-- column_layout: [1, 3, 1] -->
<!-- column: 1 -->

Questions?
