
.. _API-rcu-barrier-tasks:

=================
rcu_barrier_tasks
=================

*man rcu_barrier_tasks(9)*

*4.6.0-rc1*

Wait for in-flight ``call_rcu_tasks`` callbacks.


Synopsis
========

.. c:function:: void rcu_barrier_tasks( void )

Arguments
=========

``void``
    no arguments


Description
===========

Although the current implementation is guaranteed to wait, it is not obligated to, for example, if there are no pending callbacks.
