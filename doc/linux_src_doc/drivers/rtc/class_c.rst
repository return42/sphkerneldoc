.. -*- coding: utf-8; mode: rst -*-

=======
class.c
=======


.. _`rtc_device_register`:

rtc_device_register
===================

.. c:function:: struct rtc_device *rtc_device_register (const char *name, struct device *dev, const struct rtc_class_ops *ops, struct module *owner)

    register w/ RTC class

    :param const char \*name:

        *undescribed*

    :param struct device \*dev:
        the device to register

    :param const struct rtc_class_ops \*ops:

        *undescribed*

    :param struct module \*owner:

        *undescribed*



.. _`rtc_device_register.description`:

Description
-----------

:c:func:`rtc_device_unregister` must be called when the class device is no
longer needed.

Returns the pointer to the new struct class device.



.. _`rtc_device_unregister`:

rtc_device_unregister
=====================

.. c:function:: void rtc_device_unregister (struct rtc_device *rtc)

    removes the previously registered RTC class device

    :param struct rtc_device \*rtc:
        the RTC class device to destroy



.. _`devm_rtc_device_register`:

devm_rtc_device_register
========================

.. c:function:: struct rtc_device *devm_rtc_device_register (struct device *dev, const char *name, const struct rtc_class_ops *ops, struct module *owner)

    resource managed rtc_device_register()

    :param struct device \*dev:
        the device to register

    :param const char \*name:
        the name of the device

    :param const struct rtc_class_ops \*ops:
        the rtc operations structure

    :param struct module \*owner:
        the module owner



.. _`devm_rtc_device_register.description`:

Description
-----------

``return`` a struct rtc on success, or an ERR_PTR on error

Managed :c:func:`rtc_device_register`. The rtc_device returned from this function
are automatically freed on driver detach. See :c:func:`rtc_device_register`
for more information.



.. _`devm_rtc_device_unregister`:

devm_rtc_device_unregister
==========================

.. c:function:: void devm_rtc_device_unregister (struct device *dev, struct rtc_device *rtc)

    resource managed devm_rtc_device_unregister()

    :param struct device \*dev:
        the device to unregister

    :param struct rtc_device \*rtc:
        the RTC class device to unregister



.. _`devm_rtc_device_unregister.description`:

Description
-----------

Deallocated a rtc allocated with :c:func:`devm_rtc_device_register`. Normally this
function will not need to be called and the resource management code will
ensure that the resource is freed.

