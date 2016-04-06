
.. _API-driver-init:

===========
driver_init
===========

*man driver_init(9)*

*4.6.0-rc1*

initialize driver model.


Synopsis
========

.. c:function:: void driver_init( void )

Arguments
=========

``void``
    no arguments


Description
===========

Call the driver model init functions to initialize their subsystems. Called early from init/main.c.
