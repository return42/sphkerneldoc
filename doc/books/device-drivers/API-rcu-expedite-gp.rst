.. -*- coding: utf-8; mode: rst -*-

.. _API-rcu-expedite-gp:

===============
rcu_expedite_gp
===============

*man rcu_expedite_gp(9)*

*4.6.0-rc5*

Expedite future RCU grace periods


Synopsis
========

.. c:function:: void rcu_expedite_gp( void )

Arguments
=========

``void``
    no arguments


Description
===========

After a call to this function, future calls to ``synchronize_rcu`` and
friends act as the corresponding ``synchronize_rcu_expedited`` function
had instead been called.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
