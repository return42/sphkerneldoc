.. -*- coding: utf-8; mode: rst -*-

.. _API-wakeme-after-rcu:

================
wakeme_after_rcu
================

*man wakeme_after_rcu(9)*

*4.6.0-rc5*

Callback function to awaken a task after grace period


Synopsis
========

.. c:function:: void wakeme_after_rcu( struct rcu_head * head )

Arguments
=========

``head``
    Pointer to rcu_head member within rcu_synchronize structure


Description
===========

Awaken the corresponding task now that a grace period has elapsed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
