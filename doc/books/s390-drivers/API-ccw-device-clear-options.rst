.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-clear-options:

========================
ccw_device_clear_options
========================

*man ccw_device_clear_options(9)*

*4.6.0-rc5*

clear some options


Synopsis
========

.. c:function:: void ccw_device_clear_options( struct ccw_device * cdev, unsigned long flags )

Arguments
=========

``cdev``
    device for which the options are to be cleared

``flags``
    options to be cleared


Description
===========

All flags specified in ``flags`` are cleared, the remainder is left
untouched.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
