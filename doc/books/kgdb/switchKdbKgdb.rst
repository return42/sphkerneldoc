.. -*- coding: utf-8; mode: rst -*-

.. _switchKdbKgdb:

=============================
kgdb and kdb interoperability
=============================

It is possible to transition between kdb and kgdb dynamically. The debug
core will remember which you used the last time and automatically start
in the same mode.


Switching between kdb and kgdb
==============================


Switching from kgdb to kdb
--------------------------

There are two ways to switch from kgdb to kdb: you can use gdb to issue
a maintenance packet, or you can blindly type the command $3#33.
Whenever the kernel debugger stops in kgdb mode it will print the
message ``KGDB or $3#33 for KDB``. It is important to note that you have
to type the sequence correctly in one pass. You cannot type a backspace
or delete because kgdb will interpret that as part of the debug stream.

1. Change from kgdb to kdb by blindly typing:

   ``$3#33``

2. Change from kgdb to kdb with gdb

   ``maintenance packet 3``

   NOTE: Now you must kill gdb. Typically you press control-z and issue
   the command: kill -9 %


Change from kdb to kgdb
-----------------------

There are two ways you can change from kdb to kgdb. You can manually
enter kgdb mode by issuing the kgdb command from the kdb shell prompt,
or you can connect gdb while the kdb shell prompt is active. The kdb
shell looks for the typical first commands that gdb would issue with the
gdb remote protocol and if it sees one of those commands it
automatically changes into kgdb mode.

1. From kdb issue the command:

   ``kgdb``

   Now disconnect your terminal program and connect gdb in its place

2. At the kdb prompt, disconnect the terminal program and connect gdb in
   its place.


Running kdb commands from gdb
=============================

It is possible to run a limited set of kdb commands from gdb, using the
gdb monitor command. You don't want to execute any of the run control or
breakpoint operations, because it can disrupt the state of the kernel
debugger. You should be using gdb for breakpoints and run control
operations if you have gdb connected. The more useful commands to run
are things like lsmod, dmesg, ps or possibly some of the memory
information commands. To see all the kdb commands you can run
``monitor help``.

Example:


.. code-block:: c

    (gdb) monitor ps
    1 idle process (state I) and
    27 sleeping system daemon (state M) processes suppressed,
    use 'ps A' to see all.
    Task Addr       Pid   Parent [*] cpu State Thread     Command

    0xc78291d0        1        0  0    0   S  0xc7829404  init
    0xc7954150      942        1  0    0   S  0xc7954384  dropbear
    0xc78789c0      944        1  0    0   S  0xc7878bf4  sh
    (gdb)




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
