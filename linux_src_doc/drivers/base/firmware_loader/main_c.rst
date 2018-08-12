.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/firmware_loader/main.c

.. _`request_firmware`:

request_firmware
================

.. c:function:: int request_firmware(const struct firmware **firmware_p, const char *name, struct device *device)

    send firmware request and wait for it

    :param const struct firmware \*\*firmware_p:
        pointer to firmware image

    :param const char \*name:
        name of firmware file

    :param struct device \*device:
        device for which firmware is being loaded

.. _`request_firmware.description`:

Description
-----------

     \ ``firmware_p``\  will be used to return a firmware image by the name
     of \ ``name``\  for device \ ``device``\ .

     Should be called from user context where sleeping is allowed.

     \ ``name``\  will be used as \ ``$FIRMWARE``\  in the uevent environment and
     should be distinctive enough not to be confused with any other
     firmware image for this or any other device.

     Caller must hold the reference count of \ ``device``\ .

     The function can be called safely inside device's suspend and
     resume callback.

.. _`firmware_request_nowarn`:

firmware_request_nowarn
=======================

.. c:function:: int firmware_request_nowarn(const struct firmware **firmware, const char *name, struct device *device)

    request for an optional fw module

    :param const struct firmware \*\*firmware:
        pointer to firmware image

    :param const char \*name:
        name of firmware file

    :param struct device \*device:
        device for which firmware is being loaded

.. _`firmware_request_nowarn.description`:

Description
-----------

This function is similar in behaviour to \ :c:func:`request_firmware`\ , except
it doesn't produce warning messages when the file is not found.
The sysfs fallback mechanism is enabled if direct filesystem lookup fails,
however, however failures to find the firmware file with it are still
suppressed. It is therefore up to the driver to check for the return value
of this call and to decide when to inform the users of errors.

.. _`request_firmware_direct`:

request_firmware_direct
=======================

.. c:function:: int request_firmware_direct(const struct firmware **firmware_p, const char *name, struct device *device)

    load firmware directly without usermode helper

    :param const struct firmware \*\*firmware_p:
        pointer to firmware image

    :param const char \*name:
        name of firmware file

    :param struct device \*device:
        device for which firmware is being loaded

.. _`request_firmware_direct.description`:

Description
-----------

This function works pretty much like \ :c:func:`request_firmware`\ , but this doesn't
fall back to usermode helper even if the firmware couldn't be loaded
directly from fs.  Hence it's useful for loading optional firmwares, which
aren't always present, without extra long timeouts of udev.

.. _`firmware_request_cache`:

firmware_request_cache
======================

.. c:function:: int firmware_request_cache(struct device *device, const char *name)

    cache firmware for suspend so resume can use it

    :param struct device \*device:
        device for which firmware should be cached for

    :param const char \*name:
        name of firmware file

.. _`firmware_request_cache.description`:

Description
-----------

There are some devices with an optimization that enables the device to not
require loading firmware on system reboot. This optimization may still
require the firmware present on resume from suspend. This routine can be
used to ensure the firmware is present on resume from suspend in these
situations. This helper is not compatible with drivers which use
\ :c:func:`request_firmware_into_buf`\  or \ :c:func:`request_firmware_nowait`\  with no uevent set.

.. _`request_firmware_into_buf`:

request_firmware_into_buf
=========================

.. c:function:: int request_firmware_into_buf(const struct firmware **firmware_p, const char *name, struct device *device, void *buf, size_t size)

    load firmware into a previously allocated buffer

    :param const struct firmware \*\*firmware_p:
        pointer to firmware image

    :param const char \*name:
        name of firmware file

    :param struct device \*device:
        device for which firmware is being loaded and DMA region allocated

    :param void \*buf:
        address of buffer to load firmware into

    :param size_t size:
        size of buffer

.. _`request_firmware_into_buf.description`:

Description
-----------

This function works pretty much like \ :c:func:`request_firmware`\ , but it doesn't
allocate a buffer to hold the firmware data. Instead, the firmware
is loaded directly into the buffer pointed to by \ ``buf``\  and the \ ``firmware_p``\ 
data member is pointed at \ ``buf``\ .

This function doesn't cache firmware either.

.. _`release_firmware`:

release_firmware
================

.. c:function:: void release_firmware(const struct firmware *fw)

    release the resource associated with a firmware image

    :param const struct firmware \*fw:
        firmware resource to release

.. _`request_firmware_nowait`:

request_firmware_nowait
=======================

.. c:function:: int request_firmware_nowait(struct module *module, bool uevent, const char *name, struct device *device, gfp_t gfp, void *context, void (*cont)(const struct firmware *fw, void *context))

    asynchronous version of request_firmware

    :param struct module \*module:
        module requesting the firmware

    :param bool uevent:
        sends uevent to copy the firmware image if this flag
        is non-zero else the firmware copy must be done manually.

    :param const char \*name:
        name of firmware file

    :param struct device \*device:
        device for which firmware is being loaded

    :param gfp_t gfp:
        allocation flags

    :param void \*context:
        will be passed over to \ ``cont``\ , and
        \ ``fw``\  may be \ ``NULL``\  if firmware request fails.

    :param void (\*cont)(const struct firmware \*fw, void \*context):
        function will be called asynchronously when the firmware
        request is over.

.. _`request_firmware_nowait.description`:

Description
-----------

     Caller must hold the reference count of \ ``device``\ .

     Asynchronous variant of \ :c:func:`request_firmware`\  for user contexts:
             - sleep for as small periods as possible since it may
               increase kernel boot time of built-in device drivers
               requesting firmware in their ->probe() methods, if
               \ ``gfp``\  is GFP_KERNEL.

             - can't sleep at all if \ ``gfp``\  is GFP_ATOMIC.

.. _`cache_firmware`:

cache_firmware
==============

.. c:function:: int cache_firmware(const char *fw_name)

    cache one firmware image in kernel memory space

    :param const char \*fw_name:
        the firmware image name

.. _`cache_firmware.description`:

Description
-----------

Cache firmware in kernel memory so that drivers can use it when
system isn't ready for them to request firmware image from userspace.
Once it returns successfully, driver can use request_firmware or its
nowait version to get the cached firmware without any interacting
with userspace

Return 0 if the firmware image has been cached successfully
Return !0 otherwise

.. _`uncache_firmware`:

uncache_firmware
================

.. c:function:: int uncache_firmware(const char *fw_name)

    remove one cached firmware image

    :param const char \*fw_name:
        the firmware image name

.. _`uncache_firmware.description`:

Description
-----------

Uncache one firmware image which has been cached successfully
before.

Return 0 if the firmware cache has been removed successfully
Return !0 otherwise

.. _`device_cache_fw_images`:

device_cache_fw_images
======================

.. c:function:: void device_cache_fw_images( void)

    cache devices' firmware

    :param  void:
        no arguments

.. _`device_cache_fw_images.description`:

Description
-----------

If one device called request_firmware or its nowait version
successfully before, the firmware names are recored into the
device's devres link list, so device_cache_fw_images can call
\ :c:func:`cache_firmware`\  to cache these firmwares for the device,
then the device driver can load its firmwares easily at
time when system is not ready to complete loading firmware.

.. _`device_uncache_fw_images`:

device_uncache_fw_images
========================

.. c:function:: void device_uncache_fw_images( void)

    uncache devices' firmware

    :param  void:
        no arguments

.. _`device_uncache_fw_images.description`:

Description
-----------

uncache all firmwares which have been cached successfully
by device_uncache_fw_images earlier

.. _`device_uncache_fw_images_delay`:

device_uncache_fw_images_delay
==============================

.. c:function:: void device_uncache_fw_images_delay(unsigned long delay)

    uncache devices firmwares

    :param unsigned long delay:
        number of milliseconds to delay uncache device firmwares

.. _`device_uncache_fw_images_delay.description`:

Description
-----------

uncache all devices's firmwares which has been cached successfully
by device_cache_fw_images after \ ``delay``\  milliseconds.

.. This file was automatic generated / don't edit.

