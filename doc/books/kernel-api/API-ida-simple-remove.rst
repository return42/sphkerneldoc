
.. _API-ida-simple-remove:

=================
ida_simple_remove
=================

*man ida_simple_remove(9)*

*4.6.0-rc1*

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
