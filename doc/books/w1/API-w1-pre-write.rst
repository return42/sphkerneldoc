
.. _API-w1-pre-write:

============
w1_pre_write
============

*man w1_pre_write(9)*

*4.6.0-rc1*

pre-write operations


Synopsis
========

.. c:function:: void w1_pre_write( struct w1_master * dev )

Arguments
=========

``dev``
    the master device


Description
===========

Pre-write operation, currently only supporting strong pullups. Program the hardware for a strong pullup, if one has been requested and the hardware supports it.
