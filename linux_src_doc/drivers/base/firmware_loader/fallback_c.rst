.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/firmware_loader/fallback.c

.. _`timeout_store`:

timeout_store
=============

.. c:function:: ssize_t timeout_store(struct class *class, struct class_attribute *attr, const char *buf, size_t count)

    set number of seconds to wait for firmware

    :param struct class \*class:
        device class pointer

    :param struct class_attribute \*attr:
        device attribute pointer

    :param const char \*buf:
        buffer to scan for timeout value

    :param size_t count:
        number of bytes in \ ``buf``\ 

.. _`timeout_store.description`:

Description
-----------

Sets the number of seconds to wait for the firmware.  Once
this expires an error will be returned to the driver and no
firmware will be provided.

.. _`timeout_store.note`:

Note
----

zero means 'wait forever'.

.. _`firmware_loading_store`:

firmware_loading_store
======================

.. c:function:: ssize_t firmware_loading_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    set value in the 'loading' control file

    :param struct device \*dev:
        device pointer

    :param struct device_attribute \*attr:
        device attribute pointer

    :param const char \*buf:
        buffer to scan for loading control value

    :param size_t count:
        number of bytes in \ ``buf``\ 

.. _`firmware_loading_store.the-relevant-values-are`:

The relevant values are
-----------------------


1: Start a load, discarding any previous partial load.
0: Conclude the load and hand the data to the driver code.
-1: Conclude the load with an error and discard any written data.

.. _`firmware_data_write`:

firmware_data_write
===================

.. c:function:: ssize_t firmware_data_write(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buffer, loff_t offset, size_t count)

    write method for firmware

    :param struct file \*filp:
        open sysfs file

    :param struct kobject \*kobj:
        kobject for the device

    :param struct bin_attribute \*bin_attr:
        bin_attr structure

    :param char \*buffer:
        buffer being written

    :param loff_t offset:
        buffer offset for write in total data store area

    :param size_t count:
        buffer size

.. _`firmware_data_write.description`:

Description
-----------

Data written to the 'data' attribute will be later handed to
the driver as a firmware image.

.. _`fw_load_sysfs_fallback`:

fw_load_sysfs_fallback
======================

.. c:function:: int fw_load_sysfs_fallback(struct fw_sysfs *fw_sysfs, enum fw_opt opt_flags, long timeout)

    load a firmware via the sysfs fallback mechanism

    :param struct fw_sysfs \*fw_sysfs:
        firmware sysfs information for the firmware to load

    :param enum fw_opt opt_flags:
        flags of options, FW_OPT\_\*

    :param long timeout:
        timeout to wait for the load

.. _`fw_load_sysfs_fallback.description`:

Description
-----------

In charge of constructing a sysfs fallback interface for firmware loading.

.. _`firmware_fallback_sysfs`:

firmware_fallback_sysfs
=======================

.. c:function:: int firmware_fallback_sysfs(struct firmware *fw, const char *name, struct device *device, enum fw_opt opt_flags, int ret)

    use the fallback mechanism to find firmware

    :param struct firmware \*fw:
        pointer to firmware image

    :param const char \*name:
        name of firmware file to look for

    :param struct device \*device:
        device for which firmware is being loaded

    :param enum fw_opt opt_flags:
        options to control firmware loading behaviour

    :param int ret:
        return value from direct lookup which triggered the fallback mechanism

.. _`firmware_fallback_sysfs.description`:

Description
-----------

This function is called if direct lookup for the firmware failed, it enables
a fallback mechanism through userspace by exposing a sysfs loading
interface. Userspace is in charge of loading the firmware through the syfs
loading interface. This syfs fallback mechanism may be disabled completely
on a system by setting the proc sysctl value ignore_sysfs_fallback to true.
If this false we check if the internal API caller set the \ ``FW_OPT_NOFALLBACK``\ 
flag, if so it would also disable the fallback mechanism. A system may want
to enfoce the sysfs fallback mechanism at all times, it can do this by
setting ignore_sysfs_fallback to false and force_sysfs_fallback to true.
Enabling force_sysfs_fallback is functionally equivalent to build a kernel
with CONFIG_FW_LOADER_USER_HELPER_FALLBACK.

.. This file was automatic generated / don't edit.

