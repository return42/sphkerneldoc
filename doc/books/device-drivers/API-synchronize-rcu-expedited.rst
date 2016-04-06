
.. _API-synchronize-rcu-expedited:

=========================
synchronize_rcu_expedited
=========================

*man synchronize_rcu_expedited(9)*

*4.6.0-rc1*

Brute-force RCU grace period


Synopsis
========

.. c:function:: void synchronize_rcu_expedited( void )

Arguments
=========

``void``
    no arguments


Description
===========

Wait for an RCU-preempt grace period, but expedite it. The basic idea is to invoke ``synchronize_sched_expedited`` to push all the tasks to the ->blkd_tasks lists and wait for
this list to drain. This consumes significant time on all CPUs and is unfriendly to real-time workloads, so is thus not recommended for any sort of common-case code. In fact, if
you are using ``synchronize_rcu_expedited`` in a loop, please restructure your code to batch your updates, and then Use a single ``synchronize_rcu`` instead.
