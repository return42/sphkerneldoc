
.. _API-rcu-barrier:

===========
rcu_barrier
===========

*man rcu_barrier(9)*

*4.6.0-rc1*

Wait until all in-flight ``call_rcu`` callbacks complete.


Synopsis
========

.. c:function:: void rcu_barrier( void )

Arguments
=========

``void``
    no arguments


Description
===========

Note that this primitive does not necessarily wait for an RCU grace period to complete. For example, if there are no RCU callbacks queued anywhere in the system, then
``rcu_barrier`` is within its rights to return immediately, without waiting for anything, much less an RCU grace period.
