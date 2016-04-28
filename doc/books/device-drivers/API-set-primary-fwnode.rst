.. -*- coding: utf-8; mode: rst -*-

.. _API-set-primary-fwnode:

==================
set_primary_fwnode
==================

*man set_primary_fwnode(9)*

*4.6.0-rc5*

Change the primary firmware node of a given device.


Synopsis
========

.. c:function:: void set_primary_fwnode( struct device * dev, struct fwnode_handle * fwnode )

Arguments
=========

``dev``
    Device to handle.

``fwnode``
    New primary firmware node of the device.


Description
===========

Set the device's firmware node pointer to ``fwnode``, but if a secondary
firmware node of the device is present, preserve it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
