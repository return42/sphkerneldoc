.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cnt32_to_63.h

.. _`cnt32_to_63`:

cnt32_to_63
===========

.. c:function::  cnt32_to_63( cnt_lo)

    Expand a 32-bit counter to a 63-bit counter

    :param  cnt_lo:
        The low part of the counter

.. _`cnt32_to_63.description`:

Description
-----------

Many hardware clock counters are only 32 bits wide and therefore have
a relatively short period making wrap-arounds rather frequent.  This
is a problem when implementing \ :c:func:`sched_clock`\  for example, where a 64-bit
non-wrapping monotonic value is expected to be returned.

To overcome that limitation, let's extend a 32-bit counter to 63 bits
in a completely lock free fashion. Bits 0 to 31 of the clock are provided
by the hardware while bits 32 to 62 are stored in memory.  The top bit in
memory is used to synchronize with the hardware clock half-period.  When
the top bit of both counters (hardware and in memory) differ then the
memory is updated with a new value, incrementing it when the hardware
counter wraps around.

Because a word store in memory is atomic then the incremented value will
always be in synch with the top bit indicating to any potential concurrent
reader if the value in memory is up to date or not with regards to the
needed increment.  And any race in updating the value in memory is harmless
as the same value would simply be stored more than once.

.. _`cnt32_to_63.the-restrictions-for-the-algorithm-to-work-properly-are`:

The restrictions for the algorithm to work properly are
-------------------------------------------------------


1) this code must be called at least once per each half period of the
32-bit counter;

2) this code must not be preempted for a duration longer than the
32-bit counter half period minus the longest period between two
calls to this code;

Those requirements ensure proper update to the state bit in memory.
This is usually not a problem in practice, but if it is then a kernel
timer should be scheduled to manage for this code to be executed often
enough.

.. _`cnt32_to_63.and-finally`:

And finally
-----------


3) the cnt_lo argument must be seen as a globally incrementing value,
meaning that it should be a direct reference to the counter data which
can be evaluated according to a specific ordering within the macro,
and not the result of a previous evaluation stored in a variable.

For example, this is wrong:

u32 partial = \ :c:func:`get_hw_count`\ ;
u64 full = cnt32_to_63(partial);
return full;

.. _`cnt32_to_63.this-is-fine`:

This is fine
------------


u64 full = cnt32_to_63(\ :c:func:`get_hw_count`\ );
return full;

Note that the top bit (bit 63) in the returned value should be considered
as garbage.  It is not cleared here because callers are likely to use a
multiplier on the returned value which can get rid of the top bit
implicitly by making the multiplier even, therefore saving on a runtime
clear-bit instruction. Otherwise caller must remember to clear the top
bit explicitly.

.. This file was automatic generated / don't edit.

