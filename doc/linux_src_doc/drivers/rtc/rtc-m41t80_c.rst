.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/rtc-m41t80.c

.. _`wdt_ping`:

wdt_ping
========

.. c:function:: void wdt_ping( void)

    :param  void:
        no arguments

.. _`wdt_ping.description`:

Description
-----------

Reload counter one with the watchdog timeout. We don't bother reloading
the cascade counter.

.. _`wdt_disable`:

wdt_disable
===========

.. c:function:: void wdt_disable( void)

    :param  void:
        no arguments

.. _`wdt_disable.description`:

Description
-----------

disables watchdog.

.. _`wdt_write`:

wdt_write
=========

.. c:function:: ssize_t wdt_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    :param struct file \*file:
        file handle to the watchdog

    :param const char __user \*buf:
        buffer to write (unused as data does not matter here

    :param size_t count:
        count of bytes

    :param loff_t \*ppos:
        pointer to the position to write. No seeks allowed

.. _`wdt_write.description`:

Description
-----------

A write to a watchdog device is defined as a keepalive signal. Any
write of data will do, as we we don't define content meaning.

.. _`wdt_ioctl`:

wdt_ioctl
=========

.. c:function:: int wdt_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    :param struct file \*file:
        file handle to the device

    :param unsigned int cmd:
        watchdog command

    :param unsigned long arg:
        argument pointer

.. _`wdt_ioctl.description`:

Description
-----------

The watchdog API defines a common set of functions for all watchdogs
according to their available features. We only actually usefully support
querying capabilities and current status.

.. _`wdt_open`:

wdt_open
========

.. c:function:: int wdt_open(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        inode of device

    :param struct file \*file:
        file handle to device

.. _`wdt_release`:

wdt_release
===========

.. c:function:: int wdt_release(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        inode to board

    :param struct file \*file:
        file handle to board

.. _`wdt_notify_sys`:

wdt_notify_sys
==============

.. c:function:: int wdt_notify_sys(struct notifier_block *this, unsigned long code, void *unused)

    :param struct notifier_block \*this:
        our notifier block

    :param unsigned long code:
        the event being reported

    :param void \*unused:
        unused

.. _`wdt_notify_sys.description`:

Description
-----------

Our notifier is called on system shutdowns. We want to turn the card
off at reboot otherwise the machine will reboot again during memory
test or worse yet during the following fsck. This would suck, in fact
trust me - if it happens it does suck.

.. This file was automatic generated / don't edit.

