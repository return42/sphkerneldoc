.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/time64.h

.. _`timespec64_to_ns`:

timespec64_to_ns
================

.. c:function:: s64 timespec64_to_ns(const struct timespec64 *ts)

    Convert timespec64 to nanoseconds

    :param ts:
        pointer to the timespec64 variable to be converted
    :type ts: const struct timespec64 \*

.. _`timespec64_to_ns.description`:

Description
-----------

Returns the scalar nanosecond representation of the timespec64
parameter.

.. _`ns_to_timespec64`:

ns_to_timespec64
================

.. c:function:: struct timespec64 ns_to_timespec64(const s64 nsec)

    Convert nanoseconds to timespec64

    :param nsec:
        the nanoseconds value to be converted
    :type nsec: const s64

.. _`ns_to_timespec64.description`:

Description
-----------

Returns the timespec64 representation of the nsec parameter.

.. _`timespec64_add_ns`:

timespec64_add_ns
=================

.. c:function:: void timespec64_add_ns(struct timespec64 *a, u64 ns)

    Adds nanoseconds to a timespec64

    :param a:
        pointer to timespec64 to be incremented
    :type a: struct timespec64 \*

    :param ns:
        unsigned nanoseconds value to be added
    :type ns: u64

.. _`timespec64_add_ns.description`:

Description
-----------

This must always be inlined because its used from the x86-64 vdso,
which cannot call other kernel functions.

.. This file was automatic generated / don't edit.

