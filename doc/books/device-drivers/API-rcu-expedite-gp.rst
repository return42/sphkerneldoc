
.. _API-rcu-expedite-gp:

===============
rcu_expedite_gp
===============

*man rcu_expedite_gp(9)*

*4.6.0-rc1*

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

After a call to this function, future calls to ``synchronize_rcu`` and friends act as the corresponding ``synchronize_rcu_expedited`` function had instead been called.
