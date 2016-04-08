
.. _API-rio-unregister-driver:

=====================
rio_unregister_driver
=====================

*man rio_unregister_driver(9)*

*4.6.0-rc1*

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

Deletes the ``struct rio_driver`` from the list of registered RIO drivers, gives it a chance to clean up by calling its ``remove`` function for each device it was responsible for,
and marks those devices as driverless.
