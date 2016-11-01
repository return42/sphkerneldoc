.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/jiffies.h

.. _`msecs_to_jiffies`:

msecs_to_jiffies
================

.. c:function:: unsigned long msecs_to_jiffies(const unsigned int m)

    - convert milliseconds to jiffies

    :param const unsigned int m:
        time in milliseconds

.. _`msecs_to_jiffies.conversion-is-done-as-follows`:

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
the HZ range specific helpers \_msecs_to_jiffies() are called both
directly here and from \__msecs_to_jiffies() in the case where
constant folding is not possible.

.. _`usecs_to_jiffies`:

usecs_to_jiffies
================

.. c:function:: unsigned long usecs_to_jiffies(const unsigned int u)

    - convert microseconds to jiffies

    :param const unsigned int u:
        time in microseconds

.. _`usecs_to_jiffies.conversion-is-done-as-follows`:

conversion is done as follows
-----------------------------


- 'too large' values [that would result in larger than
MAX_JIFFY_OFFSET values] mean 'infinite timeout' too.

- all other values are converted to jiffies by either multiplying
the input value by a factor or dividing it with a factor and
handling any 32-bit overflows as for msecs_to_jiffies.

\ :c:func:`usecs_to_jiffies`\  checks for the passed in value being a constant
via \__builtin_constant_p() allowing gcc to eliminate most of the
code, \__usecs_to_jiffies() is called if the value passed does not
allow constant folding and the actual conversion must be done at
runtime.
the HZ range specific helpers \_usecs_to_jiffies() are called both
directly here and from \__msecs_to_jiffies() in the case where
constant folding is not possible.

.. This file was automatic generated / don't edit.

