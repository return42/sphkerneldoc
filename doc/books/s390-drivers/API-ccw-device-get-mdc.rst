
.. _API-ccw-device-get-mdc:

==================
ccw_device_get_mdc
==================

*man ccw_device_get_mdc(9)*

*4.6.0-rc1*

accumulate max data count


Synopsis
========

.. c:function:: int ccw_device_get_mdc( struct ccw_device * cdev, u8 mask )

Arguments
=========

``cdev``
    ccw device for which the max data count is accumulated

``mask``
    mask of paths to use


Description
===========

Return the number of 64K-bytes blocks all paths at least support for a transport command. Return values <= 0 indicate failures.
