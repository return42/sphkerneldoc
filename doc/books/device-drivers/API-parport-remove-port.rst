
.. _API-parport-remove-port:

===================
parport_remove_port
===================

*man parport_remove_port(9)*

*4.6.0-rc1*

deregister a parallel port


Synopsis
========

.. c:function:: void parport_remove_port( struct parport * port )

Arguments
=========

``port``
    parallel port to deregister


Description
===========

When a parallel port driver is forcibly unloaded, or a parallel port becomes inaccessible, the port driver must call this function in order to deal with device drivers that still
want to use it.

The parport structure associated with the port has its operations structure replaced with one containing 'null' operations that return errors or just don't do anything.

Any drivers that have registered themselves using ``parport_register_driver`` are notified that the port is no longer accessible by having their ``detach`` routines called with
``port`` as the parameter.
