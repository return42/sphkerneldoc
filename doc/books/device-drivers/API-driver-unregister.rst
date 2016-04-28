.. -*- coding: utf-8; mode: rst -*-

.. _API-driver-unregister:

=================
driver_unregister
=================

*man driver_unregister(9)*

*4.6.0-rc5*

remove driver from system.


Synopsis
========

.. c:function:: void driver_unregister( struct device_driver * drv )

Arguments
=========

``drv``
    driver.


Description
===========

Again, we pass off most of the work to the bus-level call.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
