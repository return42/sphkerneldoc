
.. _API-synchronize-sched-expedited:

===========================
synchronize_sched_expedited
===========================

*man synchronize_sched_expedited(9)*

*4.6.0-rc1*

Brute-force RCU-sched grace period


Synopsis
========

.. c:function:: void synchronize_sched_expedited( void )

Arguments
=========

``void``
    no arguments


Description
===========

Wait for an RCU-sched grace period to elapse, but use a “big hammer” approach to force the grace period to end quickly. This consumes significant time on all CPUs and is unfriendly
to real-time workloads, so is thus not recommended for any sort of common-case code. In fact, if you are using ``synchronize_sched_expedited`` in a loop, please restructure your
code to batch your updates, and then use a single ``synchronize_sched`` instead.

This implementation can be thought of as an application of sequence locking to expedited grace periods, but using the sequence counter to determine when someone else has already
done the work instead of for retrying readers.
