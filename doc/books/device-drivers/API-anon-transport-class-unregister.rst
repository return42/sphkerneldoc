.. -*- coding: utf-8; mode: rst -*-

.. _API-anon-transport-class-unregister:

===============================
anon_transport_class_unregister
===============================

*man anon_transport_class_unregister(9)*

*4.6.0-rc5*

unregister an anon class


Synopsis
========

.. c:function:: void anon_transport_class_unregister( struct anon_transport_class * atc )

Arguments
=========

``atc``
    Pointer to the anon transport class to unregister


Description
===========

Must be called prior to deallocating the memory for the anon transport
class.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
