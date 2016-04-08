
.. _API-ccw-device-tm-intrg:

===================
ccw_device_tm_intrg
===================

*man ccw_device_tm_intrg(9)*

*4.6.0-rc1*

perform interrogate function


Synopsis
========

.. c:function:: int ccw_device_tm_intrg( struct ccw_device * cdev )

Arguments
=========

``cdev``
    ccw device on which to perform the interrogate function


Description
===========

Perform an interrogate function on the given ccw device. Return zero on success, non-zero otherwise.
