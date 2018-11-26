.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/eurotechwdt.c

.. _`eurwdt_ping`:

eurwdt_ping
===========

.. c:function:: void eurwdt_ping( void)

    :param void:
        no arguments
    :type void: 

.. _`eurwdt_ping.description`:

Description
-----------

Reload counter one with the watchdog timeout.

.. _`eurwdt_write`:

eurwdt_write
============

.. c:function:: ssize_t eurwdt_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    :param file:
        file handle to the watchdog
    :type file: struct file \*

    :param buf:
        buffer to write (unused as data does not matter here
    :type buf: const char __user \*

    :param count:
        count of bytes
    :type count: size_t

    :param ppos:
        pointer to the position to write. No seeks allowed
    :type ppos: loff_t \*

.. _`eurwdt_write.description`:

Description
-----------

A write to a watchdog device is defined as a keepalive signal. Any
write of data will do, as we we don't define content meaning.

.. _`eurwdt_ioctl`:

eurwdt_ioctl
============

.. c:function:: long eurwdt_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    :param file:
        file handle to the device
    :type file: struct file \*

    :param cmd:
        watchdog command
    :type cmd: unsigned int

    :param arg:
        argument pointer
    :type arg: unsigned long

.. _`eurwdt_ioctl.description`:

Description
-----------

The watchdog API defines a common set of functions for all watchdogs
according to their available features.

.. _`eurwdt_open`:

eurwdt_open
===========

.. c:function:: int eurwdt_open(struct inode *inode, struct file *file)

    :param inode:
        inode of device
    :type inode: struct inode \*

    :param file:
        file handle to device
    :type file: struct file \*

.. _`eurwdt_open.description`:

Description
-----------

The misc device has been opened. The watchdog device is single
open and on opening we load the counter.

.. _`eurwdt_release`:

eurwdt_release
==============

.. c:function:: int eurwdt_release(struct inode *inode, struct file *file)

    :param inode:
        inode to board
    :type inode: struct inode \*

    :param file:
        file handle to board
    :type file: struct file \*

.. _`eurwdt_release.description`:

Description
-----------

The watchdog has a configurable API. There is a religious dispute
between people who want their watchdog to be able to shut down and
those who want to be sure if the watchdog manager dies the machine
reboots. In the former case we disable the counters, in the latter
case you have to open it again very soon.

.. _`eurwdt_notify_sys`:

eurwdt_notify_sys
=================

.. c:function:: int eurwdt_notify_sys(struct notifier_block *this, unsigned long code, void *unused)

    :param this:
        our notifier block
    :type this: struct notifier_block \*

    :param code:
        the event being reported
    :type code: unsigned long

    :param unused:
        unused
    :type unused: void \*

.. _`eurwdt_notify_sys.description`:

Description
-----------

Our notifier is called on system shutdowns. We want to turn the card
off at reboot otherwise the machine will reboot again during memory
test or worse yet during the following fsck. This would suck, in fact
trust me - if it happens it does suck.

.. _`eurwdt_exit`:

eurwdt_exit
===========

.. c:function:: void __exit eurwdt_exit( void)

    :param void:
        no arguments
    :type void: 

.. _`eurwdt_exit.description`:

Description
-----------

Unload the watchdog. You cannot do this with any file handles open.
If your watchdog is set to continue ticking on close and you unload
it, well it keeps ticking. We won't get the interrupt but the board
will not touch PC memory so all is fine. You just have to load a new
module in 60 seconds or reboot.

.. _`eurwdt_init`:

eurwdt_init
===========

.. c:function:: int eurwdt_init( void)

    :param void:
        no arguments
    :type void: 

.. _`eurwdt_init.description`:

Description
-----------

Set up the WDT watchdog board. After grabbing the resources
we require we need also to unlock the device.
The \ :c:func:`open`\  function will actually kick the board off.

.. This file was automatic generated / don't edit.

