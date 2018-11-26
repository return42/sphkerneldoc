.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/class.c

.. _`rtc_device_register`:

rtc_device_register
===================

.. c:function:: struct rtc_device *rtc_device_register(const char *name, struct device *dev, const struct rtc_class_ops *ops, struct module *owner)

    register w/ RTC class

    :param name:
        *undescribed*
    :type name: const char \*

    :param dev:
        the device to register
    :type dev: struct device \*

    :param ops:
        *undescribed*
    :type ops: const struct rtc_class_ops \*

    :param owner:
        *undescribed*
    :type owner: struct module \*

.. _`rtc_device_register.description`:

Description
-----------

\ :c:func:`rtc_device_unregister`\  must be called when the class device is no
longer needed.

Returns the pointer to the new struct class device.

.. _`rtc_device_unregister`:

rtc_device_unregister
=====================

.. c:function:: void rtc_device_unregister(struct rtc_device *rtc)

    removes the previously registered RTC class device

    :param rtc:
        the RTC class device to destroy
    :type rtc: struct rtc_device \*

.. _`devm_rtc_device_register`:

devm_rtc_device_register
========================

.. c:function:: struct rtc_device *devm_rtc_device_register(struct device *dev, const char *name, const struct rtc_class_ops *ops, struct module *owner)

    resource managed \ :c:func:`rtc_device_register`\ 

    :param dev:
        the device to register
    :type dev: struct device \*

    :param name:
        the name of the device
    :type name: const char \*

    :param ops:
        the rtc operations structure
    :type ops: const struct rtc_class_ops \*

    :param owner:
        the module owner
    :type owner: struct module \*

.. _`devm_rtc_device_register.description`:

Description
-----------

\ ``return``\  a struct rtc on success, or an ERR_PTR on error

Managed \ :c:func:`rtc_device_register`\ . The rtc_device returned from this function
are automatically freed on driver detach. See \ :c:func:`rtc_device_register`\ 
for more information.

.. _`devm_rtc_device_unregister`:

devm_rtc_device_unregister
==========================

.. c:function:: void devm_rtc_device_unregister(struct device *dev, struct rtc_device *rtc)

    resource managed \ :c:func:`devm_rtc_device_unregister`\ 

    :param dev:
        the device to unregister
    :type dev: struct device \*

    :param rtc:
        the RTC class device to unregister
    :type rtc: struct rtc_device \*

.. _`devm_rtc_device_unregister.description`:

Description
-----------

Deallocated a rtc allocated with \ :c:func:`devm_rtc_device_register`\ . Normally this
function will not need to be called and the resource management code will
ensure that the resource is freed.

.. This file was automatic generated / don't edit.

