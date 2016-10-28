.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwmon/hwmon.c

.. _`hwmon_device_register_with_groups`:

hwmon_device_register_with_groups
=================================

.. c:function:: struct device *hwmon_device_register_with_groups(struct device *dev, const char *name, void *drvdata, const struct attribute_group **groups)

    register w/ hwmon

    :param struct device \*dev:
        the parent device

    :param const char \*name:
        hwmon name attribute

    :param void \*drvdata:
        driver data to attach to created device

    :param const struct attribute_group \*\*groups:
        List of attribute groups to create

.. _`hwmon_device_register_with_groups.description`:

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

    :param struct device \*dev:
        the device to register

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

    :param struct device \*dev:
        the class device to destroy

.. _`devm_hwmon_device_register_with_groups`:

devm_hwmon_device_register_with_groups
======================================

.. c:function:: struct device *devm_hwmon_device_register_with_groups(struct device *dev, const char *name, void *drvdata, const struct attribute_group **groups)

    register w/ hwmon

    :param struct device \*dev:
        the parent device

    :param const char \*name:
        hwmon name attribute

    :param void \*drvdata:
        driver data to attach to created device

    :param const struct attribute_group \*\*groups:
        List of attribute groups to create

.. _`devm_hwmon_device_register_with_groups.description`:

Description
-----------

Returns the pointer to the new device. The new device is automatically
unregistered with the parent device.

.. _`devm_hwmon_device_unregister`:

devm_hwmon_device_unregister
============================

.. c:function:: void devm_hwmon_device_unregister(struct device *dev)

    removes a previously registered hwmon device

    :param struct device \*dev:
        the parent device of the device to unregister

.. This file was automatic generated / don't edit.

