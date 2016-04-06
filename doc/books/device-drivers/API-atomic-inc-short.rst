
.. _API-atomic-inc-short:

================
atomic_inc_short
================

*man atomic_inc_short(9)*

*4.6.0-rc1*

increment of a short integer


Synopsis
========

.. c:function:: short int atomic_inc_short( short int * v )

Arguments
=========

``v``
    pointer to type int


Description
===========

Atomically adds 1 to ``v`` Returns the new value of ``u``
