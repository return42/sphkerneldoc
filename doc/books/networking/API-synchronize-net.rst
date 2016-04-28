.. -*- coding: utf-8; mode: rst -*-

.. _API-synchronize-net:

===============
synchronize_net
===============

*man synchronize_net(9)*

*4.6.0-rc5*

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

Wait for packets currently being received to be done. Does not block
later packets from starting.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
