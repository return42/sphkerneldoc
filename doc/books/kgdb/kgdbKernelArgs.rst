
.. _kgdbKernelArgs:

==============================
Kernel Debugger Boot Arguments
==============================

This section describes the various runtime kernel parameters that affect the configuration of the kernel debugger. The following chapter covers using kdb and kgdb as well as
providing some examples of the configuration parameters.


.. _kgdboc:

Kernel parameter: kgdboc
========================

The kgdboc driver was originally an abbreviation meant to stand for "kgdb over console". Today it is the primary mechanism to configure how to communicate from gdb to kgdb as well
as the devices you want to use to interact with the kdb shell.

For kgdb/gdb, kgdboc is designed to work with a single serial port. It is intended to cover the circumstance where you want to use a serial console as your primary console as well
as using it to perform kernel debugging. It is also possible to use kgdb on a serial port which is not designated as a system console. Kgdboc may be configured as a kernel built-in
or a kernel loadable module. You can only make use of ``kgdbwait`` and early debugging if you build kgdboc into the kernel as a built-in.

Optionally you can elect to activate kms (Kernel Mode Setting) integration. When you use kms with kgdboc and you have a video driver that has atomic mode setting hooks, it is
possible to enter the debugger on the graphics console. When the kernel execution is resumed, the previous graphics mode will be restored. This integration can serve as a useful
tool to aid in diagnosing crashes or doing analysis of memory with kdb while allowing the full graphics console applications to run.


.. _kgdbocArgs:

kgdboc arguments
================

Usage: ``kgdboc=[kms][[,]kbd][[,]serial_device][,baud]``

The order listed above must be observed if you use any of the optional configurations together.

Abbreviations:

-  kms = Kernel Mode Setting

-  kbd = Keyboard

You can configure kgdboc to use the keyboard, and/or a serial device depending on if you are using kdb and/or kgdb, in one of the following scenarios. The order listed above must
be observed if you use any of the optional configurations together. Using kms + only gdb is generally not a useful combination.


.. _kgdbocArgs1:

Using loadable module or built-in
=================================

1. As a kernel built-in:

   Use the kernel boot argument: ``kgdboc=<tty-device>,[baud]``

2. As a kernel loadable module:

   Use the command: ``modprobe kgdboc kgdboc=<tty-device>,[baud]``

   Here are two examples of how you might format the kgdboc string. The first is for an x86 target using the first serial port. The second example is for the ARM Versatile AB using
   the second serial port.

   1. ``kgdboc=ttyS0,115200``

   2. ``kgdboc=ttyAMA1,115200``


.. _kgdbocArgs2:

Configure kgdboc at runtime with sysfs
======================================

At run time you can enable or disable kgdboc by echoing a parameters into the sysfs. Here are two examples:

1. Enable kgdboc on ttyS0

   ``echo ttyS0 > /sys/module/kgdboc/parameters/kgdboc``

2. Disable kgdboc

   ``echo "" > /sys/module/kgdboc/parameters/kgdboc``

NOTE: You do not need to specify the baud if you are configuring the console on tty which is already configured or open.


.. _kgdbocArgs3:

More examples
=============

You can configure kgdboc to use the keyboard, and/or a serial device depending on if you are using kdb and/or kgdb, in one of the following scenarios.

1. kdb and kgdb over only a serial port

   ``kgdboc=<serial_device>[,baud]``

   Example: ``kgdboc=ttyS0,115200``

2. kdb and kgdb with keyboard and a serial port

   ``kgdboc=kbd,<serial_device>[,baud]``

   Example: ``kgdboc=kbd,ttyS0,115200``

3. kdb with a keyboard

   ``kgdboc=kbd``

4. kdb with kernel mode setting

   ``kgdboc=kms,kbd``

5. kdb with kernel mode setting and kgdb over a serial port

   ``kgdboc=kms,kbd,ttyS0,115200``

NOTE: Kgdboc does not support interrupting the target via the gdb remote protocol. You must manually send a sysrq-g unless you have a proxy that splits console output to a terminal
program. A console proxy has a separate TCP port for the debugger and a separate TCP port for the "human" console. The proxy can take care of sending the sysrq-g for you.

When using kgdboc with no debugger proxy, you can end up connecting the debugger at one of two entry points. If an exception occurs after you have loaded kgdboc, a message should
print on the console stating it is waiting for the debugger. In this case you disconnect your terminal program and then connect the debugger in its place. If you want to interrupt
the target system and forcibly enter a debug session you have to issue a Sysrq sequence and then type the letter ``g``. Then you disconnect the terminal session and connect gdb.
Your options if you don't like this are to hack gdb to send the sysrq-g for you as well as on the initial connect, or to use a debugger proxy that allows an unmodified gdb to do
the debugging.


.. _kgdbwait:

Kernel parameter: kgdbwait
==========================

The Kernel command line option ``kgdbwait`` makes kgdb wait for a debugger connection during booting of a kernel. You can only use this option if you compiled a kgdb I/O driver
into the kernel and you specified the I/O driver configuration as a kernel command line option. The kgdbwait parameter should always follow the configuration parameter for the kgdb
I/O driver in the kernel command line else the I/O driver will not be configured prior to asking the kernel to use it to wait.

The kernel will stop and wait as early as the I/O driver and architecture allows when you use this option. If you build the kgdb I/O driver as a loadable kernel module kgdbwait
will not do anything.


.. _kgdbcon:

Kernel parameter: kgdbcon
=========================

The kgdbcon feature allows you to see printk() messages inside gdb while gdb is connected to the kernel. Kdb does not make use of the kgdbcon feature.

Kgdb supports using the gdb serial protocol to send console messages to the debugger when the debugger is connected and running. There are two ways to activate this feature.

1. Activate with the kernel command line option:

   ``kgdbcon``

2. Use sysfs before configuring an I/O driver

   ``echo 1 > /sys/module/kgdb/parameters/kgdb_use_con``

   NOTE: If you do this after you configure the kgdb I/O driver, the setting will not take effect until the next point the I/O is reconfigured.

IMPORTANT NOTE: You cannot use kgdboc + kgdbcon on a tty that is an active system console. An example of incorrect usage is ``console=ttyS0,115200 kgdboc=ttyS0 kgdbcon``

It is possible to use this option with kgdboc on a tty that is not a system console.


.. _kgdbreboot:

Run time parameter: kgdbreboot
==============================

The kgdbreboot feature allows you to change how the debugger deals with the reboot notification. You have 3 choices for the behavior. The default behavior is always set to 0.

1. echo -1 > /sys/module/debug_core/parameters/kgdbreboot

   Ignore the reboot notification entirely.

2. echo 0 > /sys/module/debug_core/parameters/kgdbreboot

   Send the detach message to any attached debugger client.

3. echo 1 > /sys/module/debug_core/parameters/kgdbreboot

   Enter the debugger on reboot notify.
