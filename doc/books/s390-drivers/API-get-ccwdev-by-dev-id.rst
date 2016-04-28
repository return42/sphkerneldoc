.. -*- coding: utf-8; mode: rst -*-

.. _API-get-ccwdev-by-dev-id:

====================
get_ccwdev_by_dev_id
====================

*man get_ccwdev_by_dev_id(9)*

*4.6.0-rc5*

obtain device from a ccw device id


Synopsis
========

.. c:function:: struct ccw_device * get_ccwdev_by_dev_id( struct ccw_dev_id * dev_id )

Arguments
=========

``dev_id``
    id of the device to be searched


Description
===========

This function searches all devices attached to the ccw bus for a device
matching ``dev_id``.


Returns
=======

If a device is found its reference count is increased and returned; else
``NULL`` is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
