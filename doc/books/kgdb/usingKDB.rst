.. -*- coding: utf-8; mode: rst -*-

.. _usingKDB:

*********
Using kdb
*********


.. _quickKDBserial:

Quick start for kdb on a serial port
====================================

This is a quick example of how to use kdb.

1. Configure kgdboc at boot using kernel parameters:

   -  ``console=ttyS0,115200 kgdboc=ttyS0,115200``

   OR

   Configure kgdboc after the kernel has booted; assuming you are using
   a serial port console:

   -  ``echo ttyS0 > /sys/module/kgdboc/parameters/kgdboc``

2. Enter the kernel debugger manually or by waiting for an oops or
   fault. There are several ways you can enter the kernel debugger
   manually; all involve using the sysrq-g, which means you must have
   enabled CONFIG_MAGIC_SYSRQ=y in your kernel config.

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

3. From the kdb prompt you can run the "help" command to see a complete
   list of the commands that are available.

   Some useful commands in kdb include:

   -  lsmod -- Shows where kernel modules are loaded

   -  ps -- Displays only the active processes

   -  ps A -- Shows all the processes

   -  summary -- Shows kernel version info and memory usage

   -  bt -- Get a backtrace of the current process using dump_stack()

   -  dmesg -- View the kernel syslog buffer

   -  go -- Continue the system

4. When you are done using kdb you need to consider rebooting the system
   or using the "go" command to resuming normal kernel execution. If you
   have paused the kernel for a lengthy period of time, applications
   that rely on timely networking or anything to do with real wall clock
   time could be adversely affected, so you should take this into
   consideration when using the kernel debugger.


.. _quickKDBkeyboard:

Quick start for kdb using a keyboard connected console
======================================================

This is a quick example of how to use kdb with a keyboard.

1. Configure kgdboc at boot using kernel parameters:

   -  ``kgdboc=kbd``

   OR

   Configure kgdboc after the kernel has booted:

   -  ``echo kbd > /sys/module/kgdboc/parameters/kgdboc``

2. Enter the kernel debugger manually or by waiting for an oops or
   fault. There are several ways you can enter the kernel debugger
   manually; all involve using the sysrq-g, which means you must have
   enabled CONFIG_MAGIC_SYSRQ=y in your kernel config.

   -  When logged in as root or with a super user session you can run:

      ``echo g > /proc/sysrq-trigger``

   -  Example using a laptop keyboard

      Press and hold down: ``Alt``

      Press and hold down: ``Fn``

      Press and release the key with the label: ``SysRq``

      Release: ``Fn``

      Press and release: ``g``

      Release: ``Alt``

   -  Example using a PS/2 101-key keyboard

      Press and hold down: ``Alt``

      Press and release the key with the label: ``SysRq``

      Press and release: ``g``

      Release: ``Alt``

3. Now type in a kdb command such as "help", "dmesg", "bt" or "go" to
   continue kernel execution.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
