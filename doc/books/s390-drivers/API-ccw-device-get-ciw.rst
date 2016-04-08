
.. _API-ccw-device-get-ciw:

==================
ccw_device_get_ciw
==================

*man ccw_device_get_ciw(9)*

*4.6.0-rc1*

Search for CIW command in extended sense data.


Synopsis
========

.. c:function:: struct ciw ⋆ ccw_device_get_ciw( struct ccw_device * cdev, __u32 ct )

Arguments
=========

``cdev``
    ccw device to inspect

``ct``
    command type to look for


Description
===========

During SenseID, command information words (CIWs) describing special commands available to the device may have been stored in the extended sense data. This function searches for
CIWs of a specified command type in the extended sense data.


Returns
=======

``NULL`` if no extended sense data has been stored or if no CIW of the specified command type could be found, else a pointer to the CIW of the specified command type.
