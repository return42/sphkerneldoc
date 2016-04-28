.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-set-options-mask:

===========================
ccw_device_set_options_mask
===========================

*man ccw_device_set_options_mask(9)*

*4.6.0-rc5*

set some options and unset the rest


Synopsis
========

.. c:function:: int ccw_device_set_options_mask( struct ccw_device * cdev, unsigned long flags )

Arguments
=========

``cdev``
    device for which the options are to be set

``flags``
    options to be set


Description
===========

All flags specified in ``flags`` are set, all flags not specified in
``flags`` are cleared.


Returns
=======

``0`` on success, -``EINVAL`` on an invalid flag combination.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
