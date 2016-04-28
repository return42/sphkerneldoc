.. -*- coding: utf-8; mode: rst -*-

.. _API-superhyway-register-driver:

==========================
superhyway_register_driver
==========================

*man superhyway_register_driver(9)*

*4.6.0-rc5*

Register a new SuperHyway driver


Synopsis
========

.. c:function:: int superhyway_register_driver( struct superhyway_driver * drv )

Arguments
=========

``drv``
    SuperHyway driver to register.


Description
===========

This registers the passed in ``drv``. Any devices matching the id table
will automatically be populated and handed off to the driver's specified
probe routine.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
