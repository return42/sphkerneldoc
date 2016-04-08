
.. _API-synchronize-net:

===============
synchronize_net
===============

*man synchronize_net(9)*

*4.6.0-rc1*

Synchronize with packet receive processing


Synopsis
========

.. c:function:: void synchronize_net( void )

Arguments
=========

``void``
    no arguments


Description
===========

Wait for packets currently being received to be done. Does not block later packets from starting.
