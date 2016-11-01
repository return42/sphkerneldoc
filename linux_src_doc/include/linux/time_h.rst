.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/time.h

.. _`mktime`:

mktime
======

.. c:function:: unsigned long mktime(const unsigned int year, const unsigned int mon, const unsigned int day, const unsigned int hour, const unsigned int min, const unsigned int sec)

    :param const unsigned int year:
        *undescribed*

    :param const unsigned int mon:
        *undescribed*

    :param const unsigned int day:
        *undescribed*

    :param const unsigned int hour:
        *undescribed*

    :param const unsigned int min:
        *undescribed*

    :param const unsigned int sec:
        *undescribed*

.. _`time_to_tm`:

time_to_tm
==========

.. c:function:: void time_to_tm(time_t totalsecs, int offset, struct tm *result)

    converts the calendar time to local broken-down time

    :param time_t totalsecs:
        00:00 on January 1, 1970,
        Coordinated Universal Time (UTC).
        \ ``offset``\       offset seconds adding to totalsecs.
        \ ``result``\       pointer to struct tm variable to receive broken-down time

    :param int offset:
        *undescribed*

    :param struct tm \*result:
        *undescribed*

.. _`timespec_to_ns`:

timespec_to_ns
==============

.. c:function:: s64 timespec_to_ns(const struct timespec *ts)

    Convert timespec to nanoseconds

    :param const struct timespec \*ts:
        pointer to the timespec variable to be converted

.. _`timespec_to_ns.description`:

Description
-----------

Returns the scalar nanosecond representation of the timespec
parameter.

.. _`timeval_to_ns`:

timeval_to_ns
=============

.. c:function:: s64 timeval_to_ns(const struct timeval *tv)

    Convert timeval to nanoseconds

    :param const struct timeval \*tv:
        *undescribed*

.. _`timeval_to_ns.description`:

Description
-----------

Returns the scalar nanosecond representation of the timeval
parameter.

.. _`ns_to_timespec`:

ns_to_timespec
==============

.. c:function:: struct timespec ns_to_timespec(const s64 nsec)

    Convert nanoseconds to timespec

    :param const s64 nsec:
        the nanoseconds value to be converted

.. _`ns_to_timespec.description`:

Description
-----------

Returns the timespec representation of the nsec parameter.

.. _`ns_to_timeval`:

ns_to_timeval
=============

.. c:function:: struct timeval ns_to_timeval(const s64 nsec)

    Convert nanoseconds to timeval

    :param const s64 nsec:
        the nanoseconds value to be converted

.. _`ns_to_timeval.description`:

Description
-----------

Returns the timeval representation of the nsec parameter.

.. _`timespec_add_ns`:

timespec_add_ns
===============

.. c:function:: void timespec_add_ns(struct timespec *a, u64 ns)

    Adds nanoseconds to a timespec

    :param struct timespec \*a:
        pointer to timespec to be incremented

    :param u64 ns:
        unsigned nanoseconds value to be added

.. _`timespec_add_ns.description`:

Description
-----------

This must always be inlined because its used from the x86-64 vdso,
which cannot call other kernel functions.

.. This file was automatic generated / don't edit.

