
.. _API-ida-get-new-above:

=================
ida_get_new_above
=================

*man ida_get_new_above(9)*

*4.6.0-rc1*

allocate new ID above or equal to a start id


Synopsis
========

.. c:function:: int ida_get_new_above( struct ida * ida, int starting_id, int * p_id )

Arguments
=========

``ida``
    ida handle

``starting_id``
    id to start search at

``p_id``
    pointer to the allocated handle


Description
===========

Allocate new ID above or equal to ``starting_id``. It should be called with any required locks.

If memory is required, it will return ``-EAGAIN``, you should unlock and go back to the ``ida_pre_get`` call. If the ida is full, it will return ``-ENOSPC``.

``p_id`` returns a value in the range ``starting_id`` ... ``0x7fffffff``.
