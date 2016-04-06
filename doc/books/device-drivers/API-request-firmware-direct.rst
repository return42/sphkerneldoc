
.. _API-request-firmware-direct:

=======================
request_firmware_direct
=======================

*man request_firmware_direct(9)*

*4.6.0-rc1*

load firmware directly without usermode helper


Synopsis
========

.. c:function:: int request_firmware_direct( const struct firmware ** firmware_p, const char * name, struct device * device )

Arguments
=========

``firmware_p``
    pointer to firmware image

``name``
    name of firmware file

``device``
    device for which firmware is being loaded


Description
===========

This function works pretty much like ``request_firmware``, but this doesn't fall back to usermode helper even if the firmware couldn't be loaded directly from fs. Hence it's useful
for loading optional firmwares, which aren't always present, without extra long timeouts of udev.
