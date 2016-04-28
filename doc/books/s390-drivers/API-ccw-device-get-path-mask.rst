.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-get-path-mask:

========================
ccw_device_get_path_mask
========================

*man ccw_device_get_path_mask(9)*

*4.6.0-rc5*

get currently available paths


Synopsis
========

.. c:function:: __u8 ccw_device_get_path_mask( struct ccw_device * cdev )

Arguments
=========

``cdev``
    ccw device to be queried


Returns
=======

``0`` if no subchannel for the device is available, else the mask of
currently available paths for the ccw device's subchannel.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
