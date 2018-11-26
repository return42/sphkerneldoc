.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/wdt.c

.. _`wdt_start`:

wdt_start
=========

.. c:function:: int wdt_start( void)

    :param void:
        no arguments
    :type void: 

.. _`wdt_start.description`:

Description
-----------

Start the watchdog driver.

.. _`wdt_stop`:

wdt_stop
========

.. c:function:: int wdt_stop( void)

    :param void:
        no arguments
    :type void: 

.. _`wdt_stop.description`:

Description
-----------

Stop the watchdog driver.

.. _`wdt_ping`:

wdt_ping
========

.. c:function:: void wdt_ping( void)

    :param void:
        no arguments
    :type void: 

.. _`wdt_ping.description`:

Description
-----------

Reload counter one with the watchdog heartbeat. We don't bother
reloading the cascade counter.

.. _`wdt_set_heartbeat`:

wdt_set_heartbeat
=================

.. c:function:: int wdt_set_heartbeat(int t)

    :param t:
        the new heartbeat value that needs to be set.
    :type t: int

.. _`wdt_set_heartbeat.description`:

Description
-----------

Set a new heartbeat value for the watchdog device. If the heartbeat
value is incorrect we keep the old value and return -EINVAL. If
successful we return 0.

.. _`wdt_get_status`:

wdt_get_status
==============

.. c:function:: int wdt_get_status( void)

    :param void:
        no arguments
    :type void: 

.. _`wdt_get_status.description`:

Description
-----------

Extract the status information from a WDT watchdog device. There are
several board variants so we have to know which bits are valid. Some
bits default to one and some to zero in order to be maximally painful.

we then map the bits onto the status ioctl flags.

.. _`wdt_get_temperature`:

wdt_get_temperature
===================

.. c:function:: int wdt_get_temperature( void)

    :param void:
        no arguments
    :type void: 

.. _`wdt_get_temperature.description`:

Description
-----------

Reports the temperature in degrees Fahrenheit. The API is in
farenheit. It was designed by an imperial measurement luddite.

.. _`wdt_interrupt`:

wdt_interrupt
=============

.. c:function:: irqreturn_t wdt_interrupt(int irq, void *dev_id)

    :param irq:
        Interrupt number
    :type irq: int

    :param dev_id:
        Unused as we don't allow multiple devices.
    :type dev_id: void \*

.. _`wdt_interrupt.description`:

Description
-----------

Handle an interrupt from the board. These are raised when the status
map changes in what the board considers an interesting way. That means
a failure condition occurring.

.. _`wdt_write`:

wdt_write
=========

.. c:function:: ssize_t wdt_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

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

.. _`wdt_write.description`:

Description
-----------

A write to a watchdog device is defined as a keepalive signal. Any
write of data will do, as we we don't define content meaning.

.. _`wdt_ioctl`:

wdt_ioctl
=========

.. c:function:: long wdt_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    :param file:
        file handle to the device
    :type file: struct file \*

    :param cmd:
        watchdog command
    :type cmd: unsigned int

    :param arg:
        argument pointer
    :type arg: unsigned long

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

    :param inode:
        inode of device
    :type inode: struct inode \*

    :param file:
        file handle to device
    :type file: struct file \*

.. _`wdt_open.description`:

Description
-----------

The watchdog device has been opened. The watchdog device is single
open and on opening we load the counters. Counter zero is a 100Hz
cascade, into counter 1 which downcounts to reboot. When the counter
triggers counter 2 downcounts the length of the reset pulse which
set set to be as long as possible.

.. _`wdt_release`:

wdt_release
===========

.. c:function:: int wdt_release(struct inode *inode, struct file *file)

    :param inode:
        inode to board
    :type inode: struct inode \*

    :param file:
        file handle to board
    :type file: struct file \*

.. _`wdt_release.description`:

Description
-----------

The watchdog has a configurable API. There is a religious dispute
between people who want their watchdog to be able to shut down and
those who want to be sure if the watchdog manager dies the machine
reboots. In the former case we disable the counters, in the latter
case you have to open it again very soon.

.. _`wdt_temp_read`:

wdt_temp_read
=============

.. c:function:: ssize_t wdt_temp_read(struct file *file, char __user *buf, size_t count, loff_t *ptr)

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

.. _`wdt_temp_read.description`:

Description
-----------

Temp_read reports the temperature in degrees Fahrenheit. The API is in
farenheit. It was designed by an imperial measurement luddite.

.. _`wdt_temp_open`:

wdt_temp_open
=============

.. c:function:: int wdt_temp_open(struct inode *inode, struct file *file)

    :param inode:
        inode of device
    :type inode: struct inode \*

    :param file:
        file handle to device
    :type file: struct file \*

.. _`wdt_temp_open.description`:

Description
-----------

The temperature device has been opened.

.. _`wdt_temp_release`:

wdt_temp_release
================

.. c:function:: int wdt_temp_release(struct inode *inode, struct file *file)

    :param inode:
        inode to board
    :type inode: struct inode \*

    :param file:
        file handle to board
    :type file: struct file \*

.. _`wdt_temp_release.description`:

Description
-----------

The temperature device has been closed.

.. _`wdt_notify_sys`:

wdt_notify_sys
==============

.. c:function:: int wdt_notify_sys(struct notifier_block *this, unsigned long code, void *unused)

    :param this:
        our notifier block
    :type this: struct notifier_block \*

    :param code:
        the event being reported
    :type code: unsigned long

    :param unused:
        unused
    :type unused: void \*

.. _`wdt_notify_sys.description`:

Description
-----------

Our notifier is called on system shutdowns. We want to turn the card
off at reboot otherwise the machine will reboot again during memory
test or worse yet during the following fsck. This would suck, in fact
trust me - if it happens it does suck.

.. _`wdt_exit`:

wdt_exit
========

.. c:function:: void __exit wdt_exit( void)

    :param void:
        no arguments
    :type void: 

.. _`wdt_exit.description`:

Description
-----------

Unload the watchdog. You cannot do this with any file handles open.
If your watchdog is set to continue ticking on close and you unload
it, well it keeps ticking. We won't get the interrupt but the board
will not touch PC memory so all is fine. You just have to load a new
module in 60 seconds or reboot.

.. _`wdt_init`:

wdt_init
========

.. c:function:: int wdt_init( void)

    :param void:
        no arguments
    :type void: 

.. _`wdt_init.description`:

Description
-----------

Set up the WDT watchdog board. All we have to do is grab the
resources we require and bitch if anyone beat us to them.
The \ :c:func:`open`\  function will actually kick the board off.

.. This file was automatic generated / don't edit.

