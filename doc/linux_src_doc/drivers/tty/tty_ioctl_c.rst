.. -*- coding: utf-8; mode: rst -*-

===========
tty_ioctl.c
===========


.. _`tty_chars_in_buffer`:

tty_chars_in_buffer
===================

.. c:function:: int tty_chars_in_buffer (struct tty_struct *tty)

    characters pending

    :param struct tty_struct \*tty:
        terminal



.. _`tty_chars_in_buffer.description`:

Description
-----------

Return the number of bytes of data in the device private
output queue. If no private method is supplied there is assumed
to be no queue on the device.



.. _`tty_write_room`:

tty_write_room
==============

.. c:function:: int tty_write_room (struct tty_struct *tty)

    write queue space

    :param struct tty_struct \*tty:
        terminal



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

.. c:function:: void tty_driver_flush_buffer (struct tty_struct *tty)

    discard internal buffer

    :param struct tty_struct \*tty:
        terminal



.. _`tty_driver_flush_buffer.description`:

Description
-----------

Discard the internal output buffer for this device. If no method
is provided then either the buffer cannot be hardware flushed or
there is no buffer driver side.



.. _`tty_throttle`:

tty_throttle
============

.. c:function:: void tty_throttle (struct tty_struct *tty)

    flow control

    :param struct tty_struct \*tty:
        terminal



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

.. c:function:: void tty_unthrottle (struct tty_struct *tty)

    flow control

    :param struct tty_struct \*tty:
        terminal



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

.. c:function:: int tty_throttle_safe (struct tty_struct *tty)

    flow control

    :param struct tty_struct \*tty:
        terminal



.. _`tty_throttle_safe.description`:

Description
-----------

Similar to :c:func:`tty_throttle` but will only attempt throttle
if tty->flow_change is TTY_THROTTLE_SAFE. Prevents an accidental
throttle due to race conditions when throttling is conditional
on factors evaluated prior to throttling.

Returns 0 if tty is throttled (or was already throttled)



.. _`tty_unthrottle_safe`:

tty_unthrottle_safe
===================

.. c:function:: int tty_unthrottle_safe (struct tty_struct *tty)

    flow control

    :param struct tty_struct \*tty:
        terminal



.. _`tty_unthrottle_safe.description`:

Description
-----------

Similar to :c:func:`tty_unthrottle` but will only attempt unthrottle
if tty->flow_change is TTY_UNTHROTTLE_SAFE. Prevents an accidental
unthrottle due to race conditions when unthrottling is conditional
on factors evaluated prior to unthrottling.

Returns 0 if tty is unthrottled (or was already unthrottled)



.. _`tty_wait_until_sent`:

tty_wait_until_sent
===================

.. c:function:: void tty_wait_until_sent (struct tty_struct *tty, long timeout)

    wait for I/O to finish

    :param struct tty_struct \*tty:
        tty we are waiting for

    :param long timeout:
        how long we will wait



.. _`tty_wait_until_sent.description`:

Description
-----------

Wait for characters pending in a tty driver to hit the wire, or
for a timeout to occur (eg due to flow control)



.. _`tty_wait_until_sent.locking`:

Locking
-------

none



.. _`tty_termios_baud_rate`:

tty_termios_baud_rate
=====================

.. c:function:: speed_t tty_termios_baud_rate (struct ktermios *termios)

    :param struct ktermios \*termios:
        termios structure



.. _`tty_termios_baud_rate.description`:

Description
-----------

Convert termios baud rate data into a speed. This should be called
with the termios lock held if this termios is a terminal termios
structure. May change the termios data. Device drivers can call this
function but should use ->c_[io]speed directly as they are updated.



.. _`tty_termios_baud_rate.locking`:

Locking
-------

none



.. _`tty_termios_input_baud_rate`:

tty_termios_input_baud_rate
===========================

.. c:function:: speed_t tty_termios_input_baud_rate (struct ktermios *termios)

    :param struct ktermios \*termios:
        termios structure



.. _`tty_termios_input_baud_rate.description`:

Description
-----------

Convert termios baud rate data into a speed. This should be called
with the termios lock held if this termios is a terminal termios
structure. May change the termios data. Device drivers can call this
function but should use ->c_[io]speed directly as they are updated.



.. _`tty_termios_input_baud_rate.locking`:

Locking
-------

none



.. _`tty_termios_encode_baud_rate`:

tty_termios_encode_baud_rate
============================

.. c:function:: void tty_termios_encode_baud_rate (struct ktermios *termios, speed_t ibaud, speed_t obaud)

    :param struct ktermios \*termios:
        ktermios structure holding user requested state

    :param speed_t ibaud:

        *undescribed*

    :param speed_t obaud:

        *undescribed*



.. _`tty_termios_encode_baud_rate.description`:

Description
-----------

Encode the speeds set into the passed termios structure. This is
used as a library helper for drivers so that they can report back
the actual speed selected when it differs from the speed requested

For maximal back compatibility with legacy SYS5/POSIX \*nix behaviour
we need to carefully set the bits when the user does not get the
desired speed. We allow small margins and preserve as much of possible
of the input intent to keep compatibility.



.. _`tty_termios_encode_baud_rate.locking`:

Locking
-------

Caller should hold termios lock. This is already held
when calling this function from the driver termios handler.

The ifdefs deal with platforms whose owners have yet to update them
and will all go away once this is done.



.. _`tty_encode_baud_rate`:

tty_encode_baud_rate
====================

.. c:function:: void tty_encode_baud_rate (struct tty_struct *tty, speed_t ibaud, speed_t obaud)

    set baud rate of the tty

    :param struct tty_struct \*tty:

        *undescribed*

    :param speed_t ibaud:
        input baud rate

    :param speed_t obaud:

        *undescribed*



.. _`tty_encode_baud_rate.description`:

Description
-----------

Update the current termios data for the tty with the new speed
settings. The caller must hold the termios_rwsem for the tty in
question.



.. _`tty_termios_copy_hw`:

tty_termios_copy_hw
===================

.. c:function:: void tty_termios_copy_hw (struct ktermios *new, struct ktermios *old)

    copy hardware settings

    :param struct ktermios \*new:
        New termios

    :param struct ktermios \*old:
        Old termios



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

.. c:function:: int tty_termios_hw_change (struct ktermios *a, struct ktermios *b)

    check for setting change

    :param struct ktermios \*a:
        termios

    :param struct ktermios \*b:
        termios to compare



.. _`tty_termios_hw_change.description`:

Description
-----------

Check if any of the bits that affect a dumb device have changed
between the two termios structures, or a speed change is needed.



.. _`tty_set_termios`:

tty_set_termios
===============

.. c:function:: int tty_set_termios (struct tty_struct *tty, struct ktermios *new_termios)

    update termios values

    :param struct tty_struct \*tty:
        tty to update

    :param struct ktermios \*new_termios:
        desired new value



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

.. c:function:: int set_termios (struct tty_struct *tty, void __user *arg, int opt)

    set termios values for a tty

    :param struct tty_struct \*tty:
        terminal device

    :param void __user \*arg:
        user data

    :param int opt:
        option information



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

.. c:function:: int set_termiox (struct tty_struct *tty, void __user *arg, int opt)

    set termiox fields if possible

    :param struct tty_struct \*tty:
        terminal

    :param void __user \*arg:
        termiox structure from user

    :param int opt:
        option flags for ioctl type



.. _`set_termiox.description`:

Description
-----------

Implement the device calling points for the SYS5 termiox ioctl
interface in Linux



.. _`set_sgttyb`:

set_sgttyb
==========

.. c:function:: int set_sgttyb (struct tty_struct *tty, struct sgttyb __user *sgttyb)

    set legacy terminal values

    :param struct tty_struct \*tty:
        tty structure

    :param struct sgttyb __user \*sgttyb:
        pointer to old style terminal structure



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

.. c:function:: int tty_change_softcar (struct tty_struct *tty, int arg)

    carrier change ioctl helper

    :param struct tty_struct \*tty:
        tty to update

    :param int arg:
        enable/disable CLOCAL



.. _`tty_change_softcar.description`:

Description
-----------

Perform a change to the CLOCAL state and call into the driver
layer to make it visible. All done with the termios rwsem



.. _`tty_mode_ioctl`:

tty_mode_ioctl
==============

.. c:function:: int tty_mode_ioctl (struct tty_struct *tty, struct file *file, unsigned int cmd, unsigned long arg)

    mode related ioctls

    :param struct tty_struct \*tty:
        tty for the ioctl

    :param struct file \*file:
        file pointer for the tty

    :param unsigned int cmd:
        command

    :param unsigned long arg:
        ioctl argument



.. _`tty_mode_ioctl.description`:

Description
-----------

Perform non line discipline specific mode control ioctls. This
is designed to be called by line disciplines to ensure they provide
consistent mode setting.

