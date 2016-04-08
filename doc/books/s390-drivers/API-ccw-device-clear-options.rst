
.. _API-ccw-device-clear-options:

========================
ccw_device_clear_options
========================

*man ccw_device_clear_options(9)*

*4.6.0-rc1*

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

All flags specified in ``flags`` are cleared, the remainder is left untouched.
