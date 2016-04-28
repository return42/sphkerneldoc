.. -*- coding: utf-8; mode: rst -*-

.. _API-driver-init:

===========
driver_init
===========

*man driver_init(9)*

*4.6.0-rc5*

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

Call the driver model init functions to initialize their subsystems.
Called early from init/main.c.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
