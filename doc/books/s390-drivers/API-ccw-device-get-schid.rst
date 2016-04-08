
.. _API-ccw-device-get-schid:

====================
ccw_device_get_schid
====================

*man ccw_device_get_schid(9)*

*4.6.0-rc1*

obtain a subchannel id


Synopsis
========

.. c:function:: void ccw_device_get_schid( struct ccw_device * cdev, struct subchannel_id * schid )

Arguments
=========

``cdev``
    device to obtain the id for

``schid``
    where to fill in the values
