.. -*- coding: utf-8; mode: rst -*-

================
firmware_class.c
================



.. _xref_timeout_store:

timeout_store
=============

.. c:function:: ssize_t timeout_store (struct class * class, struct class_attribute * attr, const char * buf, size_t count)

    set number of seconds to wait for firmware

    :param struct class * class:
        device class pointer

    :param struct class_attribute * attr:
        device attribute pointer

    :param const char * buf:
        buffer to scan for timeout value

    :param size_t count:
        number of bytes in **buf**



Description
-----------

	Sets the number of seconds to wait for the firmware.  Once
	this expires an error will be returned to the driver and no
	firmware will be provided.



Note
----

zero means 'wait forever'.




.. _xref_firmware_loading_store:

firmware_loading_store
======================

.. c:function:: ssize_t firmware_loading_store (struct device * dev, struct device_attribute * attr, const char * buf, size_t count)

    set value in the 'loading' control file

    :param struct device * dev:
        device pointer

    :param struct device_attribute * attr:
        device attribute pointer

    :param const char * buf:
        buffer to scan for loading control value

    :param size_t count:
        number of bytes in **buf**



1
-

Start a load, discarding any previous partial load.



0
-

Conclude the load and hand the data to the driver code.
	-1: Conclude the load with an error and discard any written data.




.. _xref_firmware_data_write:

firmware_data_write
===================

.. c:function:: ssize_t firmware_data_write (struct file * filp, struct kobject * kobj, struct bin_attribute * bin_attr, char * buffer, loff_t offset, size_t count)

    write method for firmware

    :param struct file * filp:
        open sysfs file

    :param struct kobject * kobj:
        kobject for the device

    :param struct bin_attribute * bin_attr:
        bin_attr structure

    :param char * buffer:
        buffer being written

    :param loff_t offset:
        buffer offset for write in total data store area

    :param size_t count:
        buffer size



Description
-----------

	Data written to the 'data' attribute will be later handed to
	the driver as a firmware image.




.. _xref_request_firmware:

request_firmware
================

.. c:function:: int request_firmware (const struct firmware ** firmware_p, const char * name, struct device * device)

    send firmware request and wait for it

    :param const struct firmware ** firmware_p:
        pointer to firmware image

    :param const char * name:
        name of firmware file

    :param struct device * device:
        device for which firmware is being loaded



Description
-----------

     **firmware_p** will be used to return a firmware image by the name
     of **name** for device **device**.


     Should be called from user context where sleeping is allowed.


     **name** will be used as $FIRMWARE in the uevent environment and
     should be distinctive enough not to be confused with any other
     firmware image for this or any other device.


	Caller must hold the reference count of **device**.


	The function can be called safely inside device's suspend and
	resume callback.




.. _xref_request_firmware_direct:

request_firmware_direct
=======================

.. c:function:: int request_firmware_direct (const struct firmware ** firmware_p, const char * name, struct device * device)

    load firmware directly without usermode helper

    :param const struct firmware ** firmware_p:
        pointer to firmware image

    :param const char * name:
        name of firmware file

    :param struct device * device:
        device for which firmware is being loaded



Description
-----------

This function works pretty much like :c:func:`request_firmware`, but this doesn't
fall back to usermode helper even if the firmware couldn't be loaded
directly from fs.  Hence it's useful for loading optional firmwares, which
aren't always present, without extra long timeouts of udev.




.. _xref_release_firmware:

release_firmware
================

.. c:function:: void release_firmware (const struct firmware * fw)

    release the resource associated with a firmware image

    :param const struct firmware * fw:
        firmware resource to release




.. _xref_request_firmware_nowait:

request_firmware_nowait
=======================

.. c:function:: int request_firmware_nowait (struct module * module, bool uevent, const char * name, struct device * device, gfp_t gfp, void * context, void (*cont) (const struct firmware *fw, void *context)

    asynchronous version of request_firmware

    :param struct module * module:
        module requesting the firmware

    :param bool uevent:
        sends uevent to copy the firmware image if this flag
        	is non-zero else the firmware copy must be done manually.

    :param const char * name:
        name of firmware file

    :param struct device * device:
        device for which firmware is being loaded

    :param gfp_t gfp:
        allocation flags

    :param void * context:
        will be passed over to **cont**, and
        	**fw** may be ``NULL`` if firmware request fails.

    :param void (*)(const struct firmware *fw, void *context) cont:
        function will be called asynchronously when the firmware
        	request is over.



Description
-----------

	Caller must hold the reference count of **device**.


	Asynchronous variant of :c:func:`request_firmware` for user contexts:
		- sleep for as small periods as possible since it may
		increase kernel boot time of built-in device drivers
		requesting firmware in their ->:c:func:`probe` methods, if
		**gfp** is GFP_KERNEL.


		- can't sleep at all if **gfp** is GFP_ATOMIC.




.. _xref_cache_firmware:

cache_firmware
==============

.. c:function:: int cache_firmware (const char * fw_name)

    cache one firmware image in kernel memory space

    :param const char * fw_name:
        the firmware image name



Description
-----------

Cache firmware in kernel memory so that drivers can use it when
system isn't ready for them to request firmware image from userspace.
Once it returns successfully, driver can use request_firmware or its
nowait version to get the cached firmware without any interacting
with userspace


Return 0 if the firmware image has been cached successfully
Return !0 otherwise




.. _xref_uncache_firmware:

uncache_firmware
================

.. c:function:: int uncache_firmware (const char * fw_name)

    remove one cached firmware image

    :param const char * fw_name:
        the firmware image name



Description
-----------

Uncache one firmware image which has been cached successfully
before.


Return 0 if the firmware cache has been removed successfully
Return !0 otherwise




.. _xref_device_cache_fw_images:

device_cache_fw_images
======================

.. c:function:: void device_cache_fw_images ( void)

    cache devices' firmware

    :param void:
        no arguments



Description
-----------



If one device called request_firmware or its nowait version
successfully before, the firmware names are recored into the
device's devres link list, so device_cache_fw_images can call
:c:func:`cache_firmware` to cache these firmwares for the device,
then the device driver can load its firmwares easily at
time when system is not ready to complete loading firmware.




.. _xref_device_uncache_fw_images:

device_uncache_fw_images
========================

.. c:function:: void device_uncache_fw_images ( void)

    uncache devices' firmware

    :param void:
        no arguments



Description
-----------



uncache all firmwares which have been cached successfully
by device_uncache_fw_images earlier




.. _xref_device_uncache_fw_images_delay:

device_uncache_fw_images_delay
==============================

.. c:function:: void device_uncache_fw_images_delay (unsigned long delay)

    uncache devices firmwares

    :param unsigned long delay:
        number of milliseconds to delay uncache device firmwares



Description
-----------

uncache all devices's firmwares which has been cached successfully
by device_cache_fw_images after **delay** milliseconds.


