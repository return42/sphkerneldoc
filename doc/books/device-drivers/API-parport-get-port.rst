.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-get-port:

================
parport_get_port
================

*man parport_get_port(9)*

*4.6.0-rc5*

increment a port's reference count


Synopsis
========

.. c:function:: struct parport * parport_get_port( struct parport * port )

Arguments
=========

``port``
    the port


Description
===========

This ensures that a struct parport pointer remains valid until the
matching ``parport_put_port`` call.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
