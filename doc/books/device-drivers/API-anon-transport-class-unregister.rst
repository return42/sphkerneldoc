
.. _API-anon-transport-class-unregister:

===============================
anon_transport_class_unregister
===============================

*man anon_transport_class_unregister(9)*

*4.6.0-rc1*

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

Must be called prior to deallocating the memory for the anon transport class.
