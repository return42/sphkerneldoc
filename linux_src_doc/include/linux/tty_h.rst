.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/tty.h

.. _`tty_kref_get`:

tty_kref_get
============

.. c:function:: struct tty_struct *tty_kref_get(struct tty_struct *tty)

    get a tty reference

    :param tty:
        tty device
    :type tty: struct tty_struct \*

.. _`tty_kref_get.description`:

Description
-----------

Return a new reference to a tty object. The caller must hold
sufficient locks/counts to ensure that their existing reference cannot
go away

.. _`tty_get_baud_rate`:

tty_get_baud_rate
=================

.. c:function:: speed_t tty_get_baud_rate(struct tty_struct *tty)

    get tty bit rates

    :param tty:
        tty to query
    :type tty: struct tty_struct \*

.. _`tty_get_baud_rate.description`:

Description
-----------

Returns the baud rate as an integer for this terminal. The
termios lock must be held by the caller and the terminal bit
flags may be updated.

.. _`tty_get_baud_rate.locking`:

Locking
-------

none

.. This file was automatic generated / don't edit.

