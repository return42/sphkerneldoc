.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/tty_baudrate.c

.. _`tty_termios_baud_rate`:

tty_termios_baud_rate
=====================

.. c:function:: speed_t tty_termios_baud_rate(struct ktermios *termios)

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

.. c:function:: speed_t tty_termios_input_baud_rate(struct ktermios *termios)

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

.. c:function:: void tty_termios_encode_baud_rate(struct ktermios *termios, speed_t ibaud, speed_t obaud)

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

.. c:function:: void tty_encode_baud_rate(struct tty_struct *tty, speed_t ibaud, speed_t obaud)

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

.. This file was automatic generated / don't edit.

