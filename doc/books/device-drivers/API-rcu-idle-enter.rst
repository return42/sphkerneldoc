
.. _API-rcu-idle-enter:

==============
rcu_idle_enter
==============

*man rcu_idle_enter(9)*

*4.6.0-rc1*

inform RCU that current CPU is entering idle


Synopsis
========

.. c:function:: void rcu_idle_enter( void )

Arguments
=========

``void``
    no arguments


Description
===========

Enter idle mode, in other words, -leave- the mode in which RCU read-side critical sections can occur. (Though RCU read-side critical sections can occur in irq handlers in idle, a
possibility handled by ``irq_enter`` and ``irq_exit``.)

We crowbar the ->dynticks_nesting field to zero to allow for the possibility of usermode upcalls having messed up our count of interrupt nesting level during the prior busy
period.
