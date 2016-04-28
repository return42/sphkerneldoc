.. -*- coding: utf-8; mode: rst -*-

.. _API-ida-simple-remove:

=================
ida_simple_remove
=================

*man ida_simple_remove(9)*

*4.6.0-rc5*

remove an allocated id.


Synopsis
========

.. c:function:: void ida_simple_remove( struct ida * ida, unsigned int id )

Arguments
=========

``ida``
    the (initialized) ida.

``id``
    the id returned by ida_simple_get.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
