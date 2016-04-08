
.. _API-ccw-device-set-online:

=====================
ccw_device_set_online
=====================

*man ccw_device_set_online(9)*

*4.6.0-rc1*

enable a ccw device for I/O


Synopsis
========

.. c:function:: int ccw_device_set_online( struct ccw_device * cdev )

Arguments
=========

``cdev``
    target ccw device


Description
===========

This function first enables ``cdev`` and then calls the driver's ``set_online`` function for ``cdev``, if given. If ``set_online`` returns an error, ``cdev`` is disabled again.


Returns
=======

``0`` on success and a negative error value on failure.


Context
=======

enabled, ccw device lock not held
