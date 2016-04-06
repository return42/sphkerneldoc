
.. _API-transport-class-register:

========================
transport_class_register
========================

*man transport_class_register(9)*

*4.6.0-rc1*

register an initial transport class


Synopsis
========

.. c:function:: int transport_class_register( struct transport_class * tclass )

Arguments
=========

``tclass``
    a pointer to the transport class structure to be initialised


Description
===========

The transport class contains an embedded class which is used to identify it. The caller should initialise this structure with zeros and then generic class must have been
initialised with the actual transport class unique name. There's a macro ``DECLARE_TRANSPORT_CLASS`` to do this (declared classes still must be registered).

Returns 0 on success or error on failure.
