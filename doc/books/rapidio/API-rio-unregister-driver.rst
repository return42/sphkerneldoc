.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-unregister-driver:

=====================
rio_unregister_driver
=====================

*man rio_unregister_driver(9)*

*4.6.0-rc5*

unregister a RIO driver


Synopsis
========

.. c:function:: void rio_unregister_driver( struct rio_driver * rdrv )

Arguments
=========

``rdrv``
    the RIO driver structure to unregister


Description
===========

Deletes the ``struct rio_driver`` from the list of registered RIO
drivers, gives it a chance to clean up by calling its ``remove``
function for each device it was responsible for, and marks those devices
as driverless.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
