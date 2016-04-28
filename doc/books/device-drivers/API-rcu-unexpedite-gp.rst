.. -*- coding: utf-8; mode: rst -*-

.. _API-rcu-unexpedite-gp:

=================
rcu_unexpedite_gp
=================

*man rcu_unexpedite_gp(9)*

*4.6.0-rc5*

Cancel prior ``rcu_expedite_gp`` invocation


Synopsis
========

.. c:function:: void rcu_unexpedite_gp( void )

Arguments
=========

``void``
    no arguments


Description
===========

Undo a prior call to ``rcu_expedite_gp``. If all prior calls to
``rcu_expedite_gp`` are undone by a subsequent call to
``rcu_unexpedite_gp``, and if the rcu_expedited sysfs/boot parameter is
not set, then all subsequent calls to ``synchronize_rcu`` and friends
will return to their normal non-expedited behavior.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
