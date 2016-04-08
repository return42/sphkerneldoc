
.. _API-ccw-device-get-id:

=================
ccw_device_get_id
=================

*man ccw_device_get_id(9)*

*4.6.0-rc1*

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
