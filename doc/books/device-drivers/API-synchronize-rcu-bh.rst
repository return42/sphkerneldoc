
.. _API-synchronize-rcu-bh:

==================
synchronize_rcu_bh
==================

*man synchronize_rcu_bh(9)*

*4.6.0-rc1*

wait until an rcu_bh grace period has elapsed.


Synopsis
========

.. c:function:: void synchronize_rcu_bh( void )

Arguments
=========

``void``
    no arguments


Description
===========

Control will return to the caller some time after a full rcu_bh grace period has elapsed, in other words after all currently executing rcu_bh read-side critical sections have
completed. RCU read-side critical sections are delimited by ``rcu_read_lock_bh`` and ``rcu_read_unlock_bh``, and may be nested.

See the description of ``synchronize_sched`` for more detailed information on memory ordering guarantees.
