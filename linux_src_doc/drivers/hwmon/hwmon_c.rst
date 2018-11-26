.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwmon/hwmon.c

.. _`hwmon_device_register_with_groups`:

hwmon_device_register_with_groups
=================================

.. c:function:: struct device *hwmon_device_register_with_groups(struct device *dev, const char *name, void *drvdata, const struct attribute_group **groups)

    register w/ hwmon

    :param dev:
        the parent device
    :type dev: struct device \*

    :param name:
        hwmon name attribute
    :type name: const char \*

    :param drvdata:
        driver data to attach to created device
    :type drvdata: void \*

    :param groups:
        List of attribute groups to create
    :type groups: const struct attribute_group \*\*

.. _`hwmon_device_register_with_groups.description`:

Description
-----------

\ :c:func:`hwmon_device_unregister`\  must be called when the device is no
longer needed.

Returns the pointer to the new device.

.. _`hwmon_device_register_with_info`:

hwmon_device_register_with_info
===============================

.. c:function:: struct device *hwmon_device_register_with_info(struct device *dev, const char *name, void *drvdata, const struct hwmon_chip_info *chip, const struct attribute_group **extra_groups)

    register w/ hwmon

    :param dev:
        the parent device
    :type dev: struct device \*

    :param name:
        hwmon name attribute
    :type name: const char \*

    :param drvdata:
        driver data to attach to created device
    :type drvdata: void \*

    :param chip:
        pointer to hwmon chip information
    :type chip: const struct hwmon_chip_info \*

    :param extra_groups:
        pointer to list of additional non-standard attribute groups
    :type extra_groups: const struct attribute_group \*\*

.. _`hwmon_device_register_with_info.description`:

Description
-----------

\ :c:func:`hwmon_device_unregister`\  must be called when the device is no
longer needed.

Returns the pointer to the new device.

.. _`hwmon_device_register`:

hwmon_device_register
=====================

.. c:function:: struct device *hwmon_device_register(struct device *dev)

    register w/ hwmon

    :param dev:
        the device to register
    :type dev: struct device \*

.. _`hwmon_device_register.description`:

Description
-----------

\ :c:func:`hwmon_device_unregister`\  must be called when the device is no
longer needed.

Returns the pointer to the new device.

.. _`hwmon_device_unregister`:

hwmon_device_unregister
=======================

.. c:function:: void hwmon_device_unregister(struct device *dev)

    removes the previously registered class device

    :param dev:
        the class device to destroy
    :type dev: struct device \*

.. _`devm_hwmon_device_register_with_groups`:

devm_hwmon_device_register_with_groups
======================================

.. c:function:: struct device *devm_hwmon_device_register_with_groups(struct device *dev, const char *name, void *drvdata, const struct attribute_group **groups)

    register w/ hwmon

    :param dev:
        the parent device
    :type dev: struct device \*

    :param name:
        hwmon name attribute
    :type name: const char \*

    :param drvdata:
        driver data to attach to created device
    :type drvdata: void \*

    :param groups:
        List of attribute groups to create
    :type groups: const struct attribute_group \*\*

.. _`devm_hwmon_device_register_with_groups.description`:

Description
-----------

Returns the pointer to the new device. The new device is automatically
unregistered with the parent device.

.. _`devm_hwmon_device_register_with_info`:

devm_hwmon_device_register_with_info
====================================

.. c:function:: struct device *devm_hwmon_device_register_with_info(struct device *dev, const char *name, void *drvdata, const struct hwmon_chip_info *chip, const struct attribute_group **groups)

    register w/ hwmon

    :param dev:
        the parent device
    :type dev: struct device \*

    :param name:
        hwmon name attribute
    :type name: const char \*

    :param drvdata:
        driver data to attach to created device
    :type drvdata: void \*

    :param chip:
        pointer to hwmon chip information
    :type chip: const struct hwmon_chip_info \*

    :param groups:
        pointer to list of driver specific attribute groups
    :type groups: const struct attribute_group \*\*

.. _`devm_hwmon_device_register_with_info.description`:

Description
-----------

Returns the pointer to the new device. The new device is automatically
unregistered with the parent device.

.. _`devm_hwmon_device_unregister`:

devm_hwmon_device_unregister
============================

.. c:function:: void devm_hwmon_device_unregister(struct device *dev)

    removes a previously registered hwmon device

    :param dev:
        the parent device of the device to unregister
    :type dev: struct device \*

.. This file was automatic generated / don't edit.

