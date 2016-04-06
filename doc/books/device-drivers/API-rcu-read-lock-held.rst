
.. _API-rcu-read-lock-held:

==================
rcu_read_lock_held
==================

*man rcu_read_lock_held(9)*

*4.6.0-rc1*

might we be in RCU read-side critical section?


Synopsis
========

.. c:function:: int rcu_read_lock_held( void )

Arguments
=========

``void``
    no arguments


Description
===========

If CONFIG_DEBUG_LOCK_ALLOC is selected, returns nonzero iff in an RCU read-side critical section. In absence of CONFIG_DEBUG_LOCK_ALLOC, this assumes we are in an RCU
read-side critical section unless it can prove otherwise. This is useful for debug checks in functions that require that they be called within an RCU read-side critical section.

Checks ``debug_lockdep_rcu_enabled`` to prevent false positives during boot and while lockdep is disabled.

Note that ``rcu_read_lock`` and the matching ``rcu_read_unlock`` must occur in the same context, for example, it is illegal to invoke ``rcu_read_unlock`` in process context if the
matching ``rcu_read_lock`` was invoked from within an irq handler.

Note that ``rcu_read_lock`` is disallowed if the CPU is either idle or offline from an RCU perspective, so check for those as well.
