
.. _API-request-firmware:

================
request_firmware
================

*man request_firmware(9)*

*4.6.0-rc1*

send firmware request and wait for it


Synopsis
========

.. c:function:: int request_firmware( const struct firmware ** firmware_p, const char * name, struct device * device )

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

``firmware_p`` will be used to return a firmware image by the name of ``name`` for device ``device``.

Should be called from user context where sleeping is allowed.

``name`` will be used as $FIRMWARE in the uevent environment and should be distinctive enough not to be confused with any other firmware image for this or any other device.

Caller must hold the reference count of ``device``.

The function can be called safely inside device's suspend and resume callback.
