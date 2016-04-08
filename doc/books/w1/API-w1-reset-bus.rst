
.. _API-w1-reset-bus:

============
w1_reset_bus
============

*man w1_reset_bus(9)*

*4.6.0-rc1*

Issues a reset bus sequence.


Synopsis
========

.. c:function:: int w1_reset_bus( struct w1_master * dev )

Arguments
=========

``dev``
    the master device


Return
======

0=Device present, 1=No device present or error
