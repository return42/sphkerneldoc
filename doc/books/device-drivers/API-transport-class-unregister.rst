.. -*- coding: utf-8; mode: rst -*-

.. _API-transport-class-unregister:

==========================
transport_class_unregister
==========================

*man transport_class_unregister(9)*

*4.6.0-rc5*

unregister a previously registered class


Synopsis
========

.. c:function:: void transport_class_unregister( struct transport_class * tclass )

Arguments
=========

``tclass``
    The transport class to unregister


Description
===========

Must be called prior to deallocating the memory for the transport class.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
