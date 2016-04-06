
.. _API-transport-class-unregister:

==========================
transport_class_unregister
==========================

*man transport_class_unregister(9)*

*4.6.0-rc1*

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
