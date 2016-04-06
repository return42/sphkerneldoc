
.. _API-parport-get-port:

================
parport_get_port
================

*man parport_get_port(9)*

*4.6.0-rc1*

increment a port's reference count


Synopsis
========

.. c:function:: struct parport ⋆ parport_get_port( struct parport * port )

Arguments
=========

``port``
    the port


Description
===========

This ensures that a struct parport pointer remains valid until the matching ``parport_put_port`` call.
