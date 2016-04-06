
.. _API-rcu-idle-exit:

=============
rcu_idle_exit
=============

*man rcu_idle_exit(9)*

*4.6.0-rc1*

inform RCU that current CPU is leaving idle


Synopsis
========

.. c:function:: void rcu_idle_exit( void )

Arguments
=========

``void``
    no arguments


Description
===========

Exit idle mode, in other words, -enter- the mode in which RCU read-side critical sections can occur.

We crowbar the ->dynticks_nesting field to DYNTICK_TASK_NEST to allow for the possibility of usermode upcalls messing up our count of interrupt nesting level during the busy
period that is just now starting.
