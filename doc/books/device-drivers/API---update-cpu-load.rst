
.. _API---update-cpu-load:

=================
__update_cpu_load
=================

*man __update_cpu_load(9)*

*4.6.0-rc1*

update the rq->cpu_load[] statistics


Synopsis
========

.. c:function:: void __update_cpu_load( struct rq * this_rq, unsigned long this_load, unsigned long pending_updates, int active )

Arguments
=========

``this_rq``
    The rq to update statistics for

``this_load``
    The current load

``pending_updates``
    The number of missed updates

``active``
    !0 for NOHZ_FULL


Description
===========

Update rq->cpu_load[] statistics. This function is usually called every scheduler tick (TICK_NSEC).


This function computes a decaying average
=========================================

load[i]' = (1 - 1/2^i) ⋆ load[i] + (1/2^i) ⋆ load

Because of NOHZ it might not get called on every tick which gives need for the ``pending_updates`` argument.

load[i]_n = (1 - 1/2^i) ⋆ load[i]_n-1 + (1/2^i) ⋆ load_n-1 = A ⋆ load[i]_n-1 + B ; A := (1 - 1/2^i), B := (1/2^i) ⋆ load = A ⋆ (A ⋆ load[i]_n-2 + B) + B = A ⋆ (A ⋆ (A ⋆
load[i]_n-3 + B) + B) + B = A^3 ⋆ load[i]_n-3 + (A^2 + A + 1) ⋆ B = A^n ⋆ load[i]_0 + (A^(n-1) + A^(n-2) + ... + 1) ⋆ B = A^n ⋆ load[i]_0 + ((1 - A^n) / (1 - A)) ⋆ B = (1 -
1/2^i)^n ⋆ (load[i]_0 - load) + load

In the above we've assumed load_n := load, which is true for NOHZ_FULL as any change in load would have resulted in the tick being turned back on.

For regular NOHZ, this reduces to:

load[i]_n = (1 - 1/2^i)^n ⋆ load[i]_0

see ``decay_load_misses``. For NOHZ_FULL we get to subtract and add the extra term. See the ``active`` paramter.
