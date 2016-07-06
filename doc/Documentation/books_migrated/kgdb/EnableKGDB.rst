.. -*- coding: utf-8; mode: rst -*-

.. _EnableKGDB:

****************
Using kgdb / gdb
****************

In order to use kgdb you must activate it by passing configuration
information to one of the kgdb I/O drivers. If you do not pass any
configuration information kgdb will not do anything at all. Kgdb will
only actively hook up to the kernel trap hooks if a kgdb I/O driver is
loaded and configured. If you unconfigure a kgdb I/O driver, kgdb will
unregister all the kernel hook points.

All kgdb I/O drivers can be reconfigured at run time, if
``CONFIG_SYSFS`` and ``CONFIG_MODULES`` are enabled, by echo'ing a new
config string to ``/sys/module/<driver>/parameter/<option>``. The driver
can be unconfigured by passing an empty string. You cannot change the
configuration while the debugger is attached. Make sure to detach the
debugger with the ``detach`` command prior to trying to unconfigure a
kgdb I/O driver.


.. _ConnectingGDB:

Connecting with gdb to a serial port
====================================

1. Configure kgdboc

   Configure kgdboc at boot using kernel parameters:

   -  ``kgdboc=ttyS0,115200``

   OR

   Configure kgdboc after the kernel has booted:

   -  ``echo ttyS0 > /sys/module/kgdboc/parameters/kgdboc``

2. Stop kernel execution (break into the debugger)

   In order to connect to gdb via kgdboc, the kernel must first be
   stopped. There are several ways to stop the kernel which include
   using kgdbwait as a boot argument, via a sysrq-g, or running the
   kernel until it takes an exception where it waits for the debugger to
   attach.

   -  When logged in as root or with a super user session you can run:

      ``echo g > /proc/sysrq-trigger``

   -  Example using minicom 2.2

      Press: ``Control-a``

      Press: ``f``

      Press: ``g``

   -  When you have telneted to a terminal server that supports sending
      a remote break

      Press: ``Control-]``

      Type in:\ ``send break``

      Press: ``Enter``

      Press: ``g``

3. Connect from gdb

   Example (using a directly connected port):


   .. code-block:: c

           % gdb ./vmlinux
           (gdb) set remotebaud 115200
           (gdb) target remote /dev/ttyS0

   Example (kgdb to a terminal server on TCP port 2012):


   .. code-block:: c

           % gdb ./vmlinux
           (gdb) target remote 192.168.2.2:2012

   Once connected, you can debug a kernel the way you would debug an
   application program.

   If you are having problems connecting or something is going seriously
   wrong while debugging, it will most often be the case that you want
   to enable gdb to be verbose about its target communications. You do
   this prior to issuing the ``target
       remote`` command by typing in: ``set debug remote 1``

Remember if you continue in gdb, and need to "break in" again, you need
to issue an other sysrq-g. It is easy to create a simple entry point by
putting a breakpoint at ``sys_sync`` and then you can run "sync" from a
shell or script to break into the debugger.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
