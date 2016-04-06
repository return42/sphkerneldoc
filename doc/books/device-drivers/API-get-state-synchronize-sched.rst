
.. _API-get-state-synchronize-sched:

===========================
get_state_synchronize_sched
===========================

*man get_state_synchronize_sched(9)*

*4.6.0-rc1*

Snapshot current RCU-sched state


Synopsis
========

.. c:function:: unsigned long get_state_synchronize_sched( void )

Arguments
=========

``void``
    no arguments


Description
===========

Returns a cookie that is used by a later call to ``cond_synchronize_sched`` to determine whether or not a full grace period has elapsed in the meantime.
