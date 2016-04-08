
.. _API-ccw-device-is-pathgroup:

=======================
ccw_device_is_pathgroup
=======================

*man ccw_device_is_pathgroup(9)*

*4.6.0-rc1*

determine if paths to this device are grouped


Synopsis
========

.. c:function:: int ccw_device_is_pathgroup( struct ccw_device * cdev )

Arguments
=========

``cdev``
    ccw device


Description
===========

Return non-zero if there is a path group, zero otherwise.
