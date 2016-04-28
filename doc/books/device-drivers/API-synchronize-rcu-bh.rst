.. -*- coding: utf-8; mode: rst -*-

.. _API-synchronize-rcu-bh:

==================
synchronize_rcu_bh
==================

*man synchronize_rcu_bh(9)*

*4.6.0-rc5*

wait until an rcu_bh grace period has elapsed.


Synopsis
========

.. c:function:: void synchronize_rcu_bh( void )

Arguments
=========

``void``
    no arguments


Description
===========

Control will return to the caller some time after a full rcu_bh grace
period has elapsed, in other words after all currently executing rcu_bh
read-side critical sections have completed. RCU read-side critical
sections are delimited by ``rcu_read_lock_bh`` and
``rcu_read_unlock_bh``, and may be nested.

See the description of ``synchronize_sched`` for more detailed
information on memory ordering guarantees.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
