.. -*- coding: utf-8; mode: rst -*-

.. _API-synchronize-rcu:

===============
synchronize_rcu
===============

*man synchronize_rcu(9)*

*4.6.0-rc5*

wait until a grace period has elapsed.


Synopsis
========

.. c:function:: void synchronize_rcu( void )

Arguments
=========

``void``
    no arguments


Description
===========

Control will return to the caller some time after a full grace period
has elapsed, in other words after all currently executing RCU read-side
critical sections have completed. Note, however, that upon return from
``synchronize_rcu``, the caller might well be executing concurrently
with new RCU read-side critical sections that began while
``synchronize_rcu`` was waiting. RCU read-side critical sections are
delimited by ``rcu_read_lock`` and ``rcu_read_unlock``, and may be
nested.

See the description of ``synchronize_sched`` for more detailed
information on memory ordering guarantees.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
