.. -*- coding: utf-8; mode: rst -*-

.. _KGDBTestSuite:

***************
kgdb Test Suite
***************

When kgdb is enabled in the kernel config you can also elect to enable
the config parameter KGDB_TESTS. Turning this on will enable a special
kgdb I/O module which is designed to test the kgdb internal functions.

The kgdb tests are mainly intended for developers to test the kgdb
internals as well as a tool for developing a new kgdb architecture
specific implementation. These tests are not really for end users of the
Linux kernel. The primary source of documentation would be to look in
the drivers/misc/kgdbts.c file.

The kgdb test suite can also be configured at compile time to run the
core set of tests by setting the kernel config parameter
KGDB_TESTS_ON_BOOT. This particular option is aimed at automated
regression testing and does not require modifying the kernel boot config
arguments. If this is turned on, the kgdb test suite can be disabled by
specifying "kgdbts=" as a kernel boot argument.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
