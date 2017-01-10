.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/industrialio-trigger.c

.. _`iio_trigger_read_name`:

iio_trigger_read_name
=====================

.. c:function:: ssize_t iio_trigger_read_name(struct device *dev, struct device_attribute *attr, char *buf)

    retrieve useful identifying name

    :param struct device \*dev:
        device associated with the iio_trigger

    :param struct device_attribute \*attr:
        pointer to the device_attribute structure that is
        being processed

    :param char \*buf:
        buffer to print the name into

.. _`iio_trigger_read_name.return`:

Return
------

a negative number on failure or the number of written
        characters on success.

.. _`iio_trigger_read_current`:

iio_trigger_read_current
========================

.. c:function:: ssize_t iio_trigger_read_current(struct device *dev, struct device_attribute *attr, char *buf)

    trigger consumer sysfs query current trigger

    :param struct device \*dev:
        device associated with an industrial I/O device

    :param struct device_attribute \*attr:
        pointer to the device_attribute structure that
        is being processed

    :param char \*buf:
        buffer where the current trigger name will be printed into

.. _`iio_trigger_read_current.description`:

Description
-----------

For trigger consumers the current_trigger interface allows the trigger
used by the device to be queried.

.. _`iio_trigger_read_current.return`:

Return
------

a negative number on failure, the number of characters written
        on success or 0 if no trigger is available

.. _`iio_trigger_write_current`:

iio_trigger_write_current
=========================

.. c:function:: ssize_t iio_trigger_write_current(struct device *dev, struct device_attribute *attr, const char *buf, size_t len)

    trigger consumer sysfs set current trigger

    :param struct device \*dev:
        device associated with an industrial I/O device

    :param struct device_attribute \*attr:
        device attribute that is being processed

    :param const char \*buf:
        string buffer that holds the name of the trigger

    :param size_t len:
        length of the trigger name held by buf

.. _`iio_trigger_write_current.description`:

Description
-----------

For trigger consumers the current_trigger interface allows the trigger
used for this device to be specified at run time based on the trigger's
name.

.. _`iio_trigger_write_current.return`:

Return
------

negative error code on failure or length of the buffer
        on success

.. _`devm_iio_trigger_alloc`:

devm_iio_trigger_alloc
======================

.. c:function:: struct iio_trigger *devm_iio_trigger_alloc(struct device *dev, const char *fmt,  ...)

    Resource-managed \ :c:func:`iio_trigger_alloc`\ 

    :param struct device \*dev:
        Device to allocate iio_trigger for

    :param const char \*fmt:
        trigger name format. If it includes format
        specifiers, the additional arguments following
        format are formatted and inserted in the resulting
        string replacing their respective specifiers.

    :param ... :
        variable arguments

.. _`devm_iio_trigger_alloc.description`:

Description
-----------

Managed iio_trigger_alloc.  iio_trigger allocated with this function is
automatically freed on driver detach.

If an iio_trigger allocated with this function needs to be freed separately,
\ :c:func:`devm_iio_trigger_free`\  must be used.

.. _`devm_iio_trigger_alloc.return`:

Return
------

Pointer to allocated iio_trigger on success, NULL on failure.

.. _`devm_iio_trigger_free`:

devm_iio_trigger_free
=====================

.. c:function:: void devm_iio_trigger_free(struct device *dev, struct iio_trigger *iio_trig)

    Resource-managed \ :c:func:`iio_trigger_free`\ 

    :param struct device \*dev:
        Device this iio_dev belongs to

    :param struct iio_trigger \*iio_trig:
        the iio_trigger associated with the device

.. _`devm_iio_trigger_free.description`:

Description
-----------

Free iio_trigger allocated with \ :c:func:`devm_iio_trigger_alloc`\ .

.. _`devm_iio_trigger_register`:

devm_iio_trigger_register
=========================

.. c:function:: int devm_iio_trigger_register(struct device *dev, struct iio_trigger *trig_info)

    Resource-managed \ :c:func:`iio_trigger_register`\ 

    :param struct device \*dev:
        device this trigger was allocated for

    :param struct iio_trigger \*trig_info:
        trigger to register

.. _`devm_iio_trigger_register.description`:

Description
-----------

Managed \ :c:func:`iio_trigger_register`\ .  The IIO trigger registered with this
function is automatically unregistered on driver detach. This function
calls \ :c:func:`iio_trigger_register`\  internally. Refer to that function for more
information.

If an iio_trigger registered with this function needs to be unregistered
separately, \ :c:func:`devm_iio_trigger_unregister`\  must be used.

.. _`devm_iio_trigger_register.return`:

Return
------

0 on success, negative error number on failure.

.. _`devm_iio_trigger_unregister`:

devm_iio_trigger_unregister
===========================

.. c:function:: void devm_iio_trigger_unregister(struct device *dev, struct iio_trigger *trig_info)

    Resource-managed \ :c:func:`iio_trigger_unregister`\ 

    :param struct device \*dev:
        device this iio_trigger belongs to

    :param struct iio_trigger \*trig_info:
        the trigger associated with the device

.. _`devm_iio_trigger_unregister.description`:

Description
-----------

Unregister trigger registered with \ :c:func:`devm_iio_trigger_register`\ .

.. _`iio_trigger_validate_own_device`:

iio_trigger_validate_own_device
===============================

.. c:function:: int iio_trigger_validate_own_device(struct iio_trigger *trig, struct iio_dev *indio_dev)

    Check if a trigger and IIO device belong to the same device

    :param struct iio_trigger \*trig:
        The IIO trigger to check

    :param struct iio_dev \*indio_dev:
        the IIO device to check

.. _`iio_trigger_validate_own_device.description`:

Description
-----------

This function can be used as the validate_device callback for triggers that
can only be attached to their own device.

.. _`iio_trigger_validate_own_device.return`:

Return
------

0 if both the trigger and the IIO device belong to the same
device, -EINVAL otherwise.

.. This file was automatic generated / don't edit.

