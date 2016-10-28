.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/it87_wdt.c

.. _`wdt_set_timeout`:

wdt_set_timeout
===============

.. c:function:: int wdt_set_timeout(int t)

    set a new timeout value with watchdog ioctl

    :param int t:
        timeout value in seconds

.. _`wdt_set_timeout.description`:

Description
-----------

The hardware device has a 8 or 16 bit watchdog timer (depends on
chip version) that can be configured to count seconds or minutes.

Used within WDIOC_SETTIMEOUT watchdog device ioctl.

.. _`wdt_get_status`:

wdt_get_status
==============

.. c:function:: int wdt_get_status(int *status)

    determines the status supported by watchdog ioctl

    :param int \*status:
        status returned to user space

.. _`wdt_get_status.description`:

Description
-----------

The status bit of the device does not allow to distinguish
between a regular system reset and a watchdog forced reset.
But, in test mode it is useful, so it is supported through
WDIOC_GETSTATUS watchdog ioctl. Additionally the driver
reports the keepalive signal and the acception of the magic.

Used within WDIOC_GETSTATUS watchdog device ioctl.

.. _`wdt_open`:

wdt_open
========

.. c:function:: int wdt_open(struct inode *inode, struct file *file)

    watchdog file_operations .open

    :param struct inode \*inode:
        inode of the device

    :param struct file \*file:
        file handle to the device

.. _`wdt_open.description`:

Description
-----------

The watchdog timer starts by opening the device.

Used within the file operation of the watchdog device.

.. _`wdt_release`:

wdt_release
===========

.. c:function:: int wdt_release(struct inode *inode, struct file *file)

    watchdog file_operations .release

    :param struct inode \*inode:
        inode of the device

    :param struct file \*file:
        file handle to the device

.. _`wdt_release.description`:

Description
-----------

Closing the watchdog device either stops the watchdog timer
or in the case, that nowayout is set or the magic character
wasn't written, a critical warning about an running watchdog
timer is given.

Used within the file operation of the watchdog device.

.. _`wdt_write`:

wdt_write
=========

.. c:function:: ssize_t wdt_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    watchdog file_operations .write

    :param struct file \*file:
        file handle to the watchdog

    :param const char __user \*buf:
        buffer to write

    :param size_t count:
        count of bytes

    :param loff_t \*ppos:
        pointer to the position to write. No seeks allowed

.. _`wdt_write.description`:

Description
-----------

A write to a watchdog device is defined as a keepalive signal. Any
write of data will do, as we don't define content meaning.

Used within the file operation of the watchdog device.

.. _`wdt_ioctl`:

wdt_ioctl
=========

.. c:function:: long wdt_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    watchdog file_operations .unlocked_ioctl

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
according to their available features.

Used within the file operation of the watchdog device.

.. This file was automatic generated / don't edit.

