.. -*- coding: utf-8; mode: rst -*-

.. _API-driver-register:

===============
driver_register
===============

*man driver_register(9)*

*4.6.0-rc5*

register driver with bus


Synopsis
========

.. c:function:: int driver_register( struct device_driver * drv )

Arguments
=========

``drv``
    driver to register


Description
===========

We pass off most of the work to the ``bus_add_driver`` call, since most
of the things we have to do deal with the bus structures.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
