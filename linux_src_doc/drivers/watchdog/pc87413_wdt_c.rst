.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/pc87413_wdt.c

.. _`pc87413_open`:

pc87413_open
============

.. c:function:: int pc87413_open(struct inode *inode, struct file *file)

    :param inode:
        inode of device
    :type inode: struct inode \*

    :param file:
        file handle to device
    :type file: struct file \*

.. _`pc87413_release`:

pc87413_release
===============

.. c:function:: int pc87413_release(struct inode *inode, struct file *file)

    :param inode:
        inode to board
    :type inode: struct inode \*

    :param file:
        file handle to board
    :type file: struct file \*

.. _`pc87413_release.description`:

Description
-----------

The watchdog has a configurable API. There is a religious dispute
between people who want their watchdog to be able to shut down and
those who want to be sure if the watchdog manager dies the machine
reboots. In the former case we disable the counters, in the latter
case you have to open it again very soon.

.. _`pc87413_status`:

pc87413_status
==============

.. c:function:: int pc87413_status( void)

    :param void:
        no arguments
    :type void: 

.. _`pc87413_status.description`:

Description
-----------

return, if the watchdog is enabled (timeout is set...)

.. _`pc87413_write`:

pc87413_write
=============

.. c:function:: ssize_t pc87413_write(struct file *file, const char __user *data, size_t len, loff_t *ppos)

    :param file:
        file handle to the watchdog
    :type file: struct file \*

    :param data:
        data buffer to write
    :type data: const char __user \*

    :param len:
        length in bytes
    :type len: size_t

    :param ppos:
        pointer to the position to write. No seeks allowed
    :type ppos: loff_t \*

.. _`pc87413_write.description`:

Description
-----------

A write to a watchdog device is defined as a keepalive signal. Any
write of data will do, as we we don't define content meaning.

.. _`pc87413_ioctl`:

pc87413_ioctl
=============

.. c:function:: long pc87413_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    :param file:
        file handle to the device
    :type file: struct file \*

    :param cmd:
        watchdog command
    :type cmd: unsigned int

    :param arg:
        argument pointer
    :type arg: unsigned long

.. _`pc87413_ioctl.description`:

Description
-----------

The watchdog API defines a common set of functions for all watchdogs
according to their available features. We only actually usefully support
querying capabilities and current status.

.. _`pc87413_notify_sys`:

pc87413_notify_sys
==================

.. c:function:: int pc87413_notify_sys(struct notifier_block *this, unsigned long code, void *unused)

    :param this:
        our notifier block
    :type this: struct notifier_block \*

    :param code:
        the event being reported
    :type code: unsigned long

    :param unused:
        unused
    :type unused: void \*

.. _`pc87413_notify_sys.description`:

Description
-----------

Our notifier is called on system shutdowns. We want to turn the card
off at reboot otherwise the machine will reboot again during memory
test or worse yet during the following fsck. This would suck, in fact
trust me - if it happens it does suck.

.. _`pc87413_init`:

pc87413_init
============

.. c:function:: int pc87413_init( void)

    module's "constructor"

    :param void:
        no arguments
    :type void: 

.. _`pc87413_init.description`:

Description
-----------

Set up the WDT watchdog board. All we have to do is grab the
resources we require and bitch if anyone beat us to them.
The \ :c:func:`open`\  function will actually kick the board off.

.. _`pc87413_exit`:

pc87413_exit
============

.. c:function:: void __exit pc87413_exit( void)

    module's "destructor"

    :param void:
        no arguments
    :type void: 

.. _`pc87413_exit.description`:

Description
-----------

Unload the watchdog. You cannot do this with any file handles open.
If your watchdog is set to continue ticking on close and you unload
it, well it keeps ticking. We won't get the interrupt but the board
will not touch PC memory so all is fine. You just have to load a new
module in 60 seconds or reboot.

.. This file was automatic generated / don't edit.

