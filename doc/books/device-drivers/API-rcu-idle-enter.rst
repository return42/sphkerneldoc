.. -*- coding: utf-8; mode: rst -*-

.. _API-rcu-idle-enter:

==============
rcu_idle_enter
==============

*man rcu_idle_enter(9)*

*4.6.0-rc5*

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

Enter idle mode, in other words, -leave- the mode in which RCU read-side
critical sections can occur. (Though RCU read-side critical sections can
occur in irq handlers in idle, a possibility handled by ``irq_enter``
and ``irq_exit``.)

We crowbar the ->dynticks_nesting field to zero to allow for the
possibility of usermode upcalls having messed up our count of interrupt
nesting level during the prior busy period.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
