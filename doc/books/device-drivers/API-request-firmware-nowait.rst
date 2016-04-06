
.. _API-request-firmware-nowait:

=======================
request_firmware_nowait
=======================

*man request_firmware_nowait(9)*

*4.6.0-rc1*

asynchronous version of request_firmware


Synopsis
========

.. c:function:: int request_firmware_nowait( struct module * module, bool uevent, const char * name, struct device * device, gfp_t gfp, void * context, void (*cont) const struct firmware *fw, void *context )

Arguments
=========

``module``
    module requesting the firmware

``uevent``
    sends uevent to copy the firmware image if this flag is non-zero else the firmware copy must be done manually.

``name``
    name of firmware file

``device``
    device for which firmware is being loaded

``gfp``
    allocation flags

``context``
    will be passed over to ``cont``, and ``fw`` may be ``NULL`` if firmware request fails.

``cont``
    function will be called asynchronously when the firmware request is over.


Description
===========

Caller must hold the reference count of ``device``.

Asynchronous variant of ``request_firmware`` for user contexts: - sleep for as small periods as possible since it may increase kernel boot time of built-in device drivers
requesting firmware in their ->``probe`` methods, if ``gfp`` is GFP_KERNEL.

- can't sleep at all if ``gfp`` is GFP_ATOMIC.
