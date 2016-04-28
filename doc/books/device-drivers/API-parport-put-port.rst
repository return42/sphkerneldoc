.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-put-port:

================
parport_put_port
================

*man parport_put_port(9)*

*4.6.0-rc5*

decrement a port's reference count


Synopsis
========

.. c:function:: void parport_put_port( struct parport * port )

Arguments
=========

``port``
    the port


Description
===========

This should be called once for each call to ``parport_get_port``, once
the port is no longer needed. When the reference count reaches zero
(port is no longer used), free_port is called.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
