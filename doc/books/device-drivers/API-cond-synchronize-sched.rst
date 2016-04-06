
.. _API-cond-synchronize-sched:

======================
cond_synchronize_sched
======================

*man cond_synchronize_sched(9)*

*4.6.0-rc1*

Conditionally wait for an RCU-sched grace period


Synopsis
========

.. c:function:: void cond_synchronize_sched( unsigned long oldstate )

Arguments
=========

``oldstate``
    return value from earlier call to ``get_state_synchronize_sched``


Description
===========

If a full RCU-sched grace period has elapsed since the earlier call to ``get_state_synchronize_sched``, just return. Otherwise, invoke ``synchronize_sched`` to wait for a full
grace period.

Yes, this function does not take counter wrap into account. But counter wrap is harmless. If the counter wraps, we have waited for more than 2 billion grace periods (and way more
on a 64-bit system!), so waiting for one additional grace period should be just fine.
