.. -*- coding: utf-8; mode: rst -*-

.. _CompilingAKernel:

******************
Compiling a kernel
******************

-  In order to enable compilation of kdb, you must first enable kgdb.

-  The kgdb test compile options are described in the kgdb test suite
   chapter.


.. _CompileKGDB:

Kernel config options for kgdb
==============================

To enable ``CONFIG_KGDB`` you should look under "Kernel hacking" /
"Kernel debugging" and select "KGDB: kernel debugger".

While it is not a hard requirement that you have symbols in your vmlinux
file, gdb tends not to be very useful without the symbolic data, so you
will want to turn on ``CONFIG_DEBUG_INFO`` which is called "Compile the
kernel with debug info" in the config menu.

It is advised, but not required, that you turn on the
``CONFIG_FRAME_POINTER`` kernel option which is called "Compile the
kernel with frame pointers" in the config menu. This option inserts code
to into the compiled executable which saves the frame information in
registers or on the stack at different points which allows a debugger
such as gdb to more accurately construct stack back traces while
debugging the kernel.

If the architecture that you are using supports the kernel option
CONFIG_STRICT_KERNEL_RWX, you should consider turning it off. This
option will prevent the use of software breakpoints because it marks
certain regions of the kernel's memory space as read-only. If kgdb
supports it for the architecture you are using, you can use hardware
breakpoints if you desire to run with the CONFIG_STRICT_KERNEL_RWX
option turned on, else you need to turn off this option.

Next you should choose one of more I/O drivers to interconnect debugging
host and debugged target. Early boot debugging requires a KGDB I/O
driver that supports early debugging and the driver must be built into
the kernel directly. Kgdb I/O driver configuration takes place via
kernel or module parameters which you can learn more about in the in the
section that describes the parameter "kgdboc".

Here is an example set of .config symbols to enable or disable for kgdb:

-  # CONFIG_STRICT_KERNEL_RWX is not set

-  CONFIG_FRAME_POINTER=y

-  CONFIG_KGDB=y

-  CONFIG_KGDB_SERIAL_CONSOLE=y


.. _CompileKDB:

Kernel config options for kdb
=============================

Kdb is quite a bit more complex than the simple gdbstub sitting on top
of the kernel's debug core. Kdb must implement a shell, and also adds
some helper functions in other parts of the kernel, responsible for
printing out interesting data such as what you would see if you ran
"lsmod", or "ps". In order to build kdb into the kernel you follow the
same steps as you would for kgdb.

The main config option for kdb is ``CONFIG_KGDB_KDB`` which is called
"KGDB_KDB: include kdb frontend for kgdb" in the config menu. In theory
you would have already also selected an I/O driver such as the
CONFIG_KGDB_SERIAL_CONSOLE interface if you plan on using kdb on a
serial port, when you were configuring kgdb.

If you want to use a PS/2-style keyboard with kdb, you would select
CONFIG_KDB_KEYBOARD which is called "KGDB_KDB: keyboard as input
device" in the config menu. The CONFIG_KDB_KEYBOARD option is not used
for anything in the gdb interface to kgdb. The CONFIG_KDB_KEYBOARD
option only works with kdb.

Here is an example set of .config symbols to enable/disable kdb:

-  # CONFIG_STRICT_KERNEL_RWX is not set

-  CONFIG_FRAME_POINTER=y

-  CONFIG_KGDB=y

-  CONFIG_KGDB_SERIAL_CONSOLE=y

-  CONFIG_KGDB_KDB=y

-  CONFIG_KDB_KEYBOARD=y


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
