.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-get-id:

=================
ccw_device_get_id
=================

*man ccw_device_get_id(9)*

*4.6.0-rc5*

obtain a ccw device id


Synopsis
========

.. c:function:: void ccw_device_get_id( struct ccw_device * cdev, struct ccw_dev_id * dev_id )

Arguments
=========

``cdev``
    device to obtain the id for

``dev_id``
    where to fill in the values


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
