.. -*- coding: utf-8; mode: rst -*-

.. _API-rcu-read-lock-bh-held:

=====================
rcu_read_lock_bh_held
=====================

*man rcu_read_lock_bh_held(9)*

*4.6.0-rc5*

might we be in RCU-bh read-side critical section?


Synopsis
========

.. c:function:: int rcu_read_lock_bh_held( void )

Arguments
=========

``void``
    no arguments


Description
===========

Check for bottom half being disabled, which covers both the
CONFIG_PROVE_RCU and not cases. Note that if someone uses
``rcu_read_lock_bh``, but then later enables BH, lockdep (if enabled)
will show the situation. This is useful for debug checks in functions
that require that they be called within an RCU read-side critical
section.

Check ``debug_lockdep_rcu_enabled`` to prevent false positives during
boot.

Note that ``rcu_read_lock`` is disallowed if the CPU is either idle or
offline from an RCU perspective, so check for those as well.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
