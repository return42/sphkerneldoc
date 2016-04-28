.. -*- coding: utf-8; mode: rst -*-

.. _API-rcu-is-watching:

===============
rcu_is_watching
===============

*man rcu_is_watching(9)*

*4.6.0-rc5*

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

If the current CPU is in its idle loop and is neither in an interrupt or
NMI handler, return true.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
