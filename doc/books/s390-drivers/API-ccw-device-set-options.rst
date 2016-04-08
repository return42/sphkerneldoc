
.. _API-ccw-device-set-options:

======================
ccw_device_set_options
======================

*man ccw_device_set_options(9)*

*4.6.0-rc1*

set some options


Synopsis
========

.. c:function:: int ccw_device_set_options( struct ccw_device * cdev, unsigned long flags )

Arguments
=========

``cdev``
    device for which the options are to be set

``flags``
    options to be set


Description
===========

All flags specified in ``flags`` are set, the remainder is left untouched.


Returns
=======

``0`` on success, -``EINVAL`` if an invalid flag combination would ensue.
