
.. _API-rcu-is-watching:

===============
rcu_is_watching
===============

*man rcu_is_watching(9)*

*4.6.0-rc1*

see if RCU thinks that the current CPU is idle


Synopsis
========

.. c:function:: bool notrace rcu_is_watching( void )

Arguments
=========

``void``
    no arguments


Description
===========

If the current CPU is in its idle loop and is neither in an interrupt or NMI handler, return true.
