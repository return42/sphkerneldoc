.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/timecounter.c

.. _`timecounter_read_delta`:

timecounter_read_delta
======================

.. c:function:: u64 timecounter_read_delta(struct timecounter *tc)

    get nanoseconds since last call of this function

    :param tc:
        Pointer to time counter
    :type tc: struct timecounter \*

.. _`timecounter_read_delta.description`:

Description
-----------

When the underlying cycle counter runs over, this will be handled
correctly as long as it does not run over more than once between
calls.

The first call to this function for a new time counter initializes
the time tracking and returns an undefined result.

.. This file was automatic generated / don't edit.

