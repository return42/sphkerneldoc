.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/time.c

.. _`set_normalized_timespec`:

set_normalized_timespec
=======================

.. c:function:: void set_normalized_timespec(struct timespec *ts, time_t sec, s64 nsec)

    set timespec sec and nsec parts and normalize

    :param ts:
        pointer to timespec variable to be set
    :type ts: struct timespec \*

    :param sec:
        seconds to set
    :type sec: time_t

    :param nsec:
        nanoseconds to set
    :type nsec: s64

.. _`set_normalized_timespec.description`:

Description
-----------

Set seconds and nanoseconds field of a timespec variable and
normalize to the timespec storage format

.. _`set_normalized_timespec.note`:

Note
----

The tv_nsec part is always in the range of
0 <= tv_nsec < NSEC_PER_SEC
For negative values only the tv_sec field is negative !

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

.. _`set_normalized_timespec64`:

set_normalized_timespec64
=========================

.. c:function:: void set_normalized_timespec64(struct timespec64 *ts, time64_t sec, s64 nsec)

    set timespec sec and nsec parts and normalize

    :param ts:
        pointer to timespec variable to be set
    :type ts: struct timespec64 \*

    :param sec:
        seconds to set
    :type sec: time64_t

    :param nsec:
        nanoseconds to set
    :type nsec: s64

.. _`set_normalized_timespec64.description`:

Description
-----------

Set seconds and nanoseconds field of a timespec variable and
normalize to the timespec storage format

.. _`set_normalized_timespec64.note`:

Note
----

The tv_nsec part is always in the range of
0 <= tv_nsec < NSEC_PER_SEC
For negative values only the tv_sec field is negative !

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

.. _`__msecs_to_jiffies`:

\__msecs_to_jiffies
===================

.. c:function:: unsigned long __msecs_to_jiffies(const unsigned int m)

    - convert milliseconds to jiffies

    :param m:
        time in milliseconds
    :type m: const unsigned int

.. _`__msecs_to_jiffies.conversion-is-done-as-follows`:

conversion is done as follows
-----------------------------


- negative values mean 'infinite timeout' (MAX_JIFFY_OFFSET)

- 'too large' values [that would result in larger than
MAX_JIFFY_OFFSET values] mean 'infinite timeout' too.

- all other values are converted to jiffies by either multiplying
the input value by a factor or dividing it with a factor and
handling any 32-bit overflows.
for the details see \__msecs_to_jiffies()

\ :c:func:`msecs_to_jiffies`\  checks for the passed in value being a constant
via \__builtin_constant_p() allowing gcc to eliminate most of the
code, \__msecs_to_jiffies() is called if the value passed does not
allow constant folding and the actual conversion must be done at
runtime.
the \_msecs_to_jiffies helpers are the HZ dependent conversion
routines found in include/linux/jiffies.h

.. _`nsecs_to_jiffies64`:

nsecs_to_jiffies64
==================

.. c:function:: u64 nsecs_to_jiffies64(u64 n)

    Convert nsecs in u64 to jiffies64

    :param n:
        nsecs in u64
    :type n: u64

.. _`nsecs_to_jiffies64.description`:

Description
-----------

Unlike {m,u}secs_to_jiffies, type of input is not unsigned int but u64.
And this doesn't return MAX_JIFFY_OFFSET since this function is designed
for scheduler, not for use in device drivers to calculate timeout value.

.. _`nsecs_to_jiffies64.note`:

note
----

NSEC_PER_SEC = 10^9 = (5^9 \* 2^9) = (1953125 \* 512)
ULLONG_MAX ns = 18446744073.709551615 secs = about 584 years

.. _`nsecs_to_jiffies`:

nsecs_to_jiffies
================

.. c:function:: unsigned long nsecs_to_jiffies(u64 n)

    Convert nsecs in u64 to jiffies

    :param n:
        nsecs in u64
    :type n: u64

.. _`nsecs_to_jiffies.description`:

Description
-----------

Unlike {m,u}secs_to_jiffies, type of input is not unsigned int but u64.
And this doesn't return MAX_JIFFY_OFFSET since this function is designed
for scheduler, not for use in device drivers to calculate timeout value.

.. _`nsecs_to_jiffies.note`:

note
----

NSEC_PER_SEC = 10^9 = (5^9 \* 2^9) = (1953125 \* 512)
ULLONG_MAX ns = 18446744073.709551615 secs = about 584 years

.. This file was automatic generated / don't edit.

