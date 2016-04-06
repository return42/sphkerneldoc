
.. _API-anon-transport-class-register:

=============================
anon_transport_class_register
=============================

*man anon_transport_class_register(9)*

*4.6.0-rc1*

register an anonymous class


Synopsis
========

.. c:function:: int anon_transport_class_register( struct anon_transport_class * atc )

Arguments
=========

``atc``
    The anon transport class to register


Description
===========

The anonymous transport class contains both a transport class and a container. The idea of an anonymous class is that it never actually has any device attributes associated with it
(and thus saves on container storage). So it can only be used for triggering events. Use prezero and then use ``DECLARE_ANON_TRANSPORT_CLASS`` to initialise the anon transport
class storage.
