.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/time32.h

.. _`timespec_to_ns`:

timespec_to_ns
==============

.. c:function:: s64 timespec_to_ns(const struct timespec *ts)

    Convert timespec to nanoseconds

    :param ts:
        pointer to the timespec variable to be converted
    :type ts: const struct timespec \*

.. _`timespec_to_ns.description`:

Description
-----------

Returns the scalar nanosecond representation of the timespec
parameter.

.. _`ns_to_timespec`:

ns_to_timespec
==============

.. c:function:: struct timespec ns_to_timespec(const s64 nsec)

    Convert nanoseconds to timespec

    :param nsec:
        the nanoseconds value to be converted
    :type nsec: const s64

.. _`ns_to_timespec.description`:

Description
-----------

Returns the timespec representation of the nsec parameter.

.. _`timespec_add_ns`:

timespec_add_ns
===============

.. c:function:: void timespec_add_ns(struct timespec *a, u64 ns)

    Adds nanoseconds to a timespec

    :param a:
        pointer to timespec to be incremented
    :type a: struct timespec \*

    :param ns:
        unsigned nanoseconds value to be added
    :type ns: u64

.. _`timespec_add_ns.description`:

Description
-----------

This must always be inlined because its used from the x86-64 vdso,
which cannot call other kernel functions.

.. _`timeval_to_ns`:

timeval_to_ns
=============

.. c:function:: s64 timeval_to_ns(const struct timeval *tv)

    Convert timeval to nanoseconds

    :param tv:
        *undescribed*
    :type tv: const struct timeval \*

.. _`timeval_to_ns.description`:

Description
-----------

Returns the scalar nanosecond representation of the timeval
parameter.

.. _`ns_to_timeval`:

ns_to_timeval
=============

.. c:function:: struct timeval ns_to_timeval(const s64 nsec)

    Convert nanoseconds to timeval

    :param nsec:
        the nanoseconds value to be converted
    :type nsec: const s64

.. _`ns_to_timeval.description`:

Description
-----------

Returns the timeval representation of the nsec parameter.

.. This file was automatic generated / don't edit.

