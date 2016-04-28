.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-register-driver:

===================
rio_register_driver
===================

*man rio_register_driver(9)*

*4.6.0-rc5*

register a new RIO driver


Synopsis
========

.. c:function:: int rio_register_driver( struct rio_driver * rdrv )

Arguments
=========

``rdrv``
    the RIO driver structure to register


Description
===========

Adds a ``struct rio_driver`` to the list of registered drivers. Returns
a negative value on error, otherwise 0. If no error occurred, the driver
remains registered even if no device was claimed during registration.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
