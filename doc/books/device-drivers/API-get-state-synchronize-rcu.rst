.. -*- coding: utf-8; mode: rst -*-

.. _API-get-state-synchronize-rcu:

=========================
get_state_synchronize_rcu
=========================

*man get_state_synchronize_rcu(9)*

*4.6.0-rc5*

Snapshot current RCU state


Synopsis
========

.. c:function:: unsigned long get_state_synchronize_rcu( void )

Arguments
=========

``void``
    no arguments


Description
===========

Returns a cookie that is used by a later call to
``cond_synchronize_rcu`` to determine whether or not a full grace period
has elapsed in the meantime.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
