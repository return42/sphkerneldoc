.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/tty_ioctl.c

.. _`tty_chars_in_buffer`:

tty_chars_in_buffer
===================

.. c:function:: int tty_chars_in_buffer(struct tty_struct *tty)

    characters pending

    :param tty:
        terminal
    :type tty: struct tty_struct \*

.. _`tty_chars_in_buffer.description`:

Description
-----------

Return the number of bytes of data in the device private
output queue. If no private method is supplied there is assumed
to be no queue on the device.

.. _`tty_write_room`:

tty_write_room
==============

.. c:function:: int tty_write_room(struct tty_struct *tty)

    write queue space

    :param tty:
        terminal
    :type tty: struct tty_struct \*

.. _`tty_write_room.description`:

Description
-----------

Return the number of bytes that can be queued to this device
at the present time. The result should be treated as a guarantee
and the driver cannot offer a value it later shrinks by more than
the number of bytes written. If no method is provided 2K is always
returned and data may be lost as there will be no flow control.

.. _`tty_driver_flush_buffer`:

tty_driver_flush_buffer
=======================

.. c:function:: void tty_driver_flush_buffer(struct tty_struct *tty)

    discard internal buffer

    :param tty:
        terminal
    :type tty: struct tty_struct \*

.. _`tty_driver_flush_buffer.description`:

Description
-----------

Discard the internal output buffer for this device. If no method
is provided then either the buffer cannot be hardware flushed or
there is no buffer driver side.

.. _`tty_throttle`:

tty_throttle
============

.. c:function:: void tty_throttle(struct tty_struct *tty)

    flow control

    :param tty:
        terminal
    :type tty: struct tty_struct \*

.. _`tty_throttle.description`:

Description
-----------

Indicate that a tty should stop transmitting data down the stack.
Takes the termios rwsem to protect against parallel throttle/unthrottle
and also to ensure the driver can consistently reference its own
termios data at this point when implementing software flow control.

.. _`tty_unthrottle`:

tty_unthrottle
==============

.. c:function:: void tty_unthrottle(struct tty_struct *tty)

    flow control

    :param tty:
        terminal
    :type tty: struct tty_struct \*

.. _`tty_unthrottle.description`:

Description
-----------

Indicate that a tty may continue transmitting data down the stack.
Takes the termios rwsem to protect against parallel throttle/unthrottle
and also to ensure the driver can consistently reference its own
termios data at this point when implementing software flow control.

Drivers should however remember that the stack can issue a throttle,
then change flow control method, then unthrottle.

.. _`tty_throttle_safe`:

tty_throttle_safe
=================

.. c:function:: int tty_throttle_safe(struct tty_struct *tty)

    flow control

    :param tty:
        terminal
    :type tty: struct tty_struct \*

.. _`tty_throttle_safe.description`:

Description
-----------

Similar to \ :c:func:`tty_throttle`\  but will only attempt throttle
if tty->flow_change is TTY_THROTTLE_SAFE. Prevents an accidental
throttle due to race conditions when throttling is conditional
on factors evaluated prior to throttling.

Returns 0 if tty is throttled (or was already throttled)

.. _`tty_unthrottle_safe`:

tty_unthrottle_safe
===================

.. c:function:: int tty_unthrottle_safe(struct tty_struct *tty)

    flow control

    :param tty:
        terminal
    :type tty: struct tty_struct \*

.. _`tty_unthrottle_safe.description`:

Description
-----------

Similar to \ :c:func:`tty_unthrottle`\  but will only attempt unthrottle
if tty->flow_change is TTY_UNTHROTTLE_SAFE. Prevents an accidental
unthrottle due to race conditions when unthrottling is conditional
on factors evaluated prior to unthrottling.

Returns 0 if tty is unthrottled (or was already unthrottled)

.. _`tty_wait_until_sent`:

tty_wait_until_sent
===================

.. c:function:: void tty_wait_until_sent(struct tty_struct *tty, long timeout)

    wait for I/O to finish

    :param tty:
        tty we are waiting for
    :type tty: struct tty_struct \*

    :param timeout:
        how long we will wait
    :type timeout: long

.. _`tty_wait_until_sent.description`:

Description
-----------

Wait for characters pending in a tty driver to hit the wire, or
for a timeout to occur (eg due to flow control)

.. _`tty_wait_until_sent.locking`:

Locking
-------

none

.. _`tty_termios_copy_hw`:

tty_termios_copy_hw
===================

.. c:function:: void tty_termios_copy_hw(struct ktermios *new, struct ktermios *old)

    copy hardware settings

    :param new:
        New termios
    :type new: struct ktermios \*

    :param old:
        Old termios
    :type old: struct ktermios \*

.. _`tty_termios_copy_hw.description`:

Description
-----------

Propagate the hardware specific terminal setting bits from
the old termios structure to the new one. This is used in cases
where the hardware does not support reconfiguration or as a helper
in some cases where only minimal reconfiguration is supported

.. _`tty_termios_hw_change`:

tty_termios_hw_change
=====================

.. c:function:: int tty_termios_hw_change(const struct ktermios *a, const struct ktermios *b)

    check for setting change

    :param a:
        termios
    :type a: const struct ktermios \*

    :param b:
        termios to compare
    :type b: const struct ktermios \*

.. _`tty_termios_hw_change.description`:

Description
-----------

Check if any of the bits that affect a dumb device have changed
between the two termios structures, or a speed change is needed.

.. _`tty_set_termios`:

tty_set_termios
===============

.. c:function:: int tty_set_termios(struct tty_struct *tty, struct ktermios *new_termios)

    update termios values

    :param tty:
        tty to update
    :type tty: struct tty_struct \*

    :param new_termios:
        desired new value
    :type new_termios: struct ktermios \*

.. _`tty_set_termios.description`:

Description
-----------

Perform updates to the termios values set on this terminal.
A master pty's termios should never be set.

.. _`tty_set_termios.locking`:

Locking
-------

termios_rwsem

.. _`set_termios`:

set_termios
===========

.. c:function:: int set_termios(struct tty_struct *tty, void __user *arg, int opt)

    set termios values for a tty

    :param tty:
        terminal device
    :type tty: struct tty_struct \*

    :param arg:
        user data
    :type arg: void __user \*

    :param opt:
        option information
    :type opt: int

.. _`set_termios.description`:

Description
-----------

Helper function to prepare termios data and run necessary other
functions before using tty_set_termios to do the actual changes.

.. _`set_termios.locking`:

Locking
-------

Called functions take ldisc and termios_rwsem locks

.. _`set_termiox`:

set_termiox
===========

.. c:function:: int set_termiox(struct tty_struct *tty, void __user *arg, int opt)

    set termiox fields if possible

    :param tty:
        terminal
    :type tty: struct tty_struct \*

    :param arg:
        termiox structure from user
    :type arg: void __user \*

    :param opt:
        option flags for ioctl type
    :type opt: int

.. _`set_termiox.description`:

Description
-----------

Implement the device calling points for the SYS5 termiox ioctl
interface in Linux

.. _`set_sgttyb`:

set_sgttyb
==========

.. c:function:: int set_sgttyb(struct tty_struct *tty, struct sgttyb __user *sgttyb)

    set legacy terminal values

    :param tty:
        tty structure
    :type tty: struct tty_struct \*

    :param sgttyb:
        pointer to old style terminal structure
    :type sgttyb: struct sgttyb __user \*

.. _`set_sgttyb.description`:

Description
-----------

Updates a terminal from the legacy BSD style terminal information
structure.

.. _`set_sgttyb.locking`:

Locking
-------

termios_rwsem

.. _`tty_change_softcar`:

tty_change_softcar
==================

.. c:function:: int tty_change_softcar(struct tty_struct *tty, int arg)

    carrier change ioctl helper

    :param tty:
        tty to update
    :type tty: struct tty_struct \*

    :param arg:
        enable/disable CLOCAL
    :type arg: int

.. _`tty_change_softcar.description`:

Description
-----------

Perform a change to the CLOCAL state and call into the driver
layer to make it visible. All done with the termios rwsem

.. _`tty_mode_ioctl`:

tty_mode_ioctl
==============

.. c:function:: int tty_mode_ioctl(struct tty_struct *tty, struct file *file, unsigned int cmd, unsigned long arg)

    mode related ioctls

    :param tty:
        tty for the ioctl
    :type tty: struct tty_struct \*

    :param file:
        file pointer for the tty
    :type file: struct file \*

    :param cmd:
        command
    :type cmd: unsigned int

    :param arg:
        ioctl argument
    :type arg: unsigned long

.. _`tty_mode_ioctl.description`:

Description
-----------

Perform non line discipline specific mode control ioctls. This
is designed to be called by line disciplines to ensure they provide
consistent mode setting.

.. This file was automatic generated / don't edit.

