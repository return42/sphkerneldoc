.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/wdt_pci.c

.. _`wdtpci_start`:

wdtpci_start
============

.. c:function:: int wdtpci_start( void)

    :param void:
        no arguments
    :type void: 

.. _`wdtpci_start.description`:

Description
-----------

Start the watchdog driver.

.. _`wdtpci_stop`:

wdtpci_stop
===========

.. c:function:: int wdtpci_stop( void)

    :param void:
        no arguments
    :type void: 

.. _`wdtpci_stop.description`:

Description
-----------

Stop the watchdog driver.

.. _`wdtpci_ping`:

wdtpci_ping
===========

.. c:function:: int wdtpci_ping( void)

    :param void:
        no arguments
    :type void: 

.. _`wdtpci_ping.description`:

Description
-----------

Reload counter one with the watchdog heartbeat. We don't bother
reloading the cascade counter.

.. _`wdtpci_set_heartbeat`:

wdtpci_set_heartbeat
====================

.. c:function:: int wdtpci_set_heartbeat(int t)

    :param t:
        the new heartbeat value that needs to be set.
    :type t: int

.. _`wdtpci_set_heartbeat.description`:

Description
-----------

Set a new heartbeat value for the watchdog device. If the heartbeat
value is incorrect we keep the old value and return -EINVAL.
If successful we return 0.

.. _`wdtpci_get_status`:

wdtpci_get_status
=================

.. c:function:: int wdtpci_get_status(int *status)

    :param status:
        the new status.
    :type status: int \*

.. _`wdtpci_get_status.description`:

Description
-----------

Extract the status information from a WDT watchdog device. There are
several board variants so we have to know which bits are valid. Some
bits default to one and some to zero in order to be maximally painful.

we then map the bits onto the status ioctl flags.

.. _`wdtpci_get_temperature`:

wdtpci_get_temperature
======================

.. c:function:: int wdtpci_get_temperature(int *temperature)

    :param temperature:
        *undescribed*
    :type temperature: int \*

.. _`wdtpci_get_temperature.description`:

Description
-----------

Reports the temperature in degrees Fahrenheit. The API is in
farenheit. It was designed by an imperial measurement luddite.

.. _`wdtpci_interrupt`:

wdtpci_interrupt
================

.. c:function:: irqreturn_t wdtpci_interrupt(int irq, void *dev_id)

    :param irq:
        Interrupt number
    :type irq: int

    :param dev_id:
        Unused as we don't allow multiple devices.
    :type dev_id: void \*

.. _`wdtpci_interrupt.description`:

Description
-----------

Handle an interrupt from the board. These are raised when the status
map changes in what the board considers an interesting way. That means
a failure condition occurring.

.. _`wdtpci_write`:

wdtpci_write
============

.. c:function:: ssize_t wdtpci_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

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

.. _`wdtpci_write.description`:

Description
-----------

A write to a watchdog device is defined as a keepalive signal. Any
write of data will do, as we we don't define content meaning.

.. _`wdtpci_ioctl`:

wdtpci_ioctl
============

.. c:function:: long wdtpci_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    :param file:
        file handle to the device
    :type file: struct file \*

    :param cmd:
        watchdog command
    :type cmd: unsigned int

    :param arg:
        argument pointer
    :type arg: unsigned long

.. _`wdtpci_ioctl.description`:

Description
-----------

The watchdog API defines a common set of functions for all watchdogs
according to their available features. We only actually usefully support
querying capabilities and current status.

.. _`wdtpci_open`:

wdtpci_open
===========

.. c:function:: int wdtpci_open(struct inode *inode, struct file *file)

    :param inode:
        inode of device
    :type inode: struct inode \*

    :param file:
        file handle to device
    :type file: struct file \*

.. _`wdtpci_open.description`:

Description
-----------

The watchdog device has been opened. The watchdog device is single
open and on opening we load the counters. Counter zero is a 100Hz
cascade, into counter 1 which downcounts to reboot. When the counter
triggers counter 2 downcounts the length of the reset pulse which
set set to be as long as possible.

.. _`wdtpci_release`:

wdtpci_release
==============

.. c:function:: int wdtpci_release(struct inode *inode, struct file *file)

    :param inode:
        inode to board
    :type inode: struct inode \*

    :param file:
        file handle to board
    :type file: struct file \*

.. _`wdtpci_release.description`:

Description
-----------

The watchdog has a configurable API. There is a religious dispute
between people who want their watchdog to be able to shut down and
those who want to be sure if the watchdog manager dies the machine
reboots. In the former case we disable the counters, in the latter
case you have to open it again very soon.

.. _`wdtpci_temp_read`:

wdtpci_temp_read
================

.. c:function:: ssize_t wdtpci_temp_read(struct file *file, char __user *buf, size_t count, loff_t *ptr)

    :param file:
        file handle to the watchdog board
    :type file: struct file \*

    :param buf:
        buffer to write 1 byte into
    :type buf: char __user \*

    :param count:
        length of buffer
    :type count: size_t

    :param ptr:
        offset (no seek allowed)
    :type ptr: loff_t \*

.. _`wdtpci_temp_read.description`:

Description
-----------

Read reports the temperature in degrees Fahrenheit. The API is in
fahrenheit. It was designed by an imperial measurement luddite.

.. _`wdtpci_temp_open`:

wdtpci_temp_open
================

.. c:function:: int wdtpci_temp_open(struct inode *inode, struct file *file)

    :param inode:
        inode of device
    :type inode: struct inode \*

    :param file:
        file handle to device
    :type file: struct file \*

.. _`wdtpci_temp_open.description`:

Description
-----------

The temperature device has been opened.

.. _`wdtpci_temp_release`:

wdtpci_temp_release
===================

.. c:function:: int wdtpci_temp_release(struct inode *inode, struct file *file)

    :param inode:
        inode to board
    :type inode: struct inode \*

    :param file:
        file handle to board
    :type file: struct file \*

.. _`wdtpci_temp_release.description`:

Description
-----------

The temperature device has been closed.

.. _`wdtpci_notify_sys`:

wdtpci_notify_sys
=================

.. c:function:: int wdtpci_notify_sys(struct notifier_block *this, unsigned long code, void *unused)

    :param this:
        our notifier block
    :type this: struct notifier_block \*

    :param code:
        the event being reported
    :type code: unsigned long

    :param unused:
        unused
    :type unused: void \*

.. _`wdtpci_notify_sys.description`:

Description
-----------

Our notifier is called on system shutdowns. We want to turn the card
off at reboot otherwise the machine will reboot again during memory
test or worse yet during the following fsck. This would suck, in fact
trust me - if it happens it does suck.

.. This file was automatic generated / don't edit.

