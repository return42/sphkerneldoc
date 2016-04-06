
.. _API-wakeme-after-rcu:

================
wakeme_after_rcu
================

*man wakeme_after_rcu(9)*

*4.6.0-rc1*

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
