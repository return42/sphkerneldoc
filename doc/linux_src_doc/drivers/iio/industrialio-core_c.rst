.. -*- coding: utf-8; mode: rst -*-

===================
industrialio-core.c
===================


.. _`iio_find_channel_from_si`:

iio_find_channel_from_si
========================

.. c:function:: const struct iio_chan_spec *iio_find_channel_from_si (struct iio_dev *indio_dev, int si)

    get channel from its scan index

    :param struct iio_dev \*indio_dev:
        device

    :param int si:
        scan index to match



.. _`iio_format_value`:

iio_format_value
================

.. c:function:: ssize_t iio_format_value (char *buf, unsigned int type, int size, int *vals)

    Formats a IIO value into its string representation

    :param char \*buf:
        The buffer to which the formatted value gets written

    :param unsigned int type:
        One of the IIO_VAL_... constants. This decides how the val
        and val2 parameters are formatted.

    :param int size:
        Number of IIO value entries contained in vals

    :param int \*vals:
        Pointer to the values, exact meaning depends on the
        type parameter.



.. _`iio_format_value.return`:

Return
------

0 by default, a negative number on failure or the

           total number of characters written for a type that belongs
           to the IIO_VAL_... constant.



.. _`iio_str_to_fixpoint`:

iio_str_to_fixpoint
===================

.. c:function:: int iio_str_to_fixpoint (const char *str, int fract_mult, int *integer, int *fract)

    Parse a fixed-point number from a string

    :param const char \*str:
        The string to parse

    :param int fract_mult:
        Multiplier for the first decimal place, should be a power of 10

    :param int \*integer:
        The integer part of the number

    :param int \*fract:
        The fractional part of the number



.. _`iio_str_to_fixpoint.description`:

Description
-----------

Returns 0 on success, or a negative error code if the string could not be
parsed.



.. _`iio_free_chan_devattr_list`:

iio_free_chan_devattr_list
==========================

.. c:function:: void iio_free_chan_devattr_list (struct list_head *attr_list)

    Free a list of IIO device attributes

    :param struct list_head \*attr_list:
        List of IIO device attributes



.. _`iio_free_chan_devattr_list.description`:

Description
-----------

This function frees the memory allocated for each of the IIO device
attributes in the list.



.. _`iio_device_alloc`:

iio_device_alloc
================

.. c:function:: struct iio_dev *iio_device_alloc (int sizeof_priv)

    allocate an iio_dev from a driver

    :param int sizeof_priv:
        Space to allocate for private structure.



.. _`iio_device_free`:

iio_device_free
===============

.. c:function:: void iio_device_free (struct iio_dev *dev)

    free an iio_dev from a driver

    :param struct iio_dev \*dev:
        the iio_dev associated with the device



.. _`devm_iio_device_alloc`:

devm_iio_device_alloc
=====================

.. c:function:: struct iio_dev *devm_iio_device_alloc (struct device *dev, int sizeof_priv)

    Resource-managed iio_device_alloc()

    :param struct device \*dev:
        Device to allocate iio_dev for

    :param int sizeof_priv:
        Space to allocate for private structure.



.. _`devm_iio_device_alloc.description`:

Description
-----------

Managed iio_device_alloc. iio_dev allocated with this function is
automatically freed on driver detach.

If an iio_dev allocated with this function needs to be freed separately,
:c:func:`devm_iio_device_free` must be used.



.. _`devm_iio_device_alloc.returns`:

RETURNS
-------

Pointer to allocated iio_dev on success, NULL on failure.



.. _`devm_iio_device_free`:

devm_iio_device_free
====================

.. c:function:: void devm_iio_device_free (struct device *dev, struct iio_dev *iio_dev)

    Resource-managed iio_device_free()

    :param struct device \*dev:
        Device this iio_dev belongs to

    :param struct iio_dev \*iio_dev:
        the iio_dev associated with the device



.. _`devm_iio_device_free.description`:

Description
-----------

Free iio_dev allocated with :c:func:`devm_iio_device_alloc`.



.. _`iio_chrdev_open`:

iio_chrdev_open
===============

.. c:function:: int iio_chrdev_open (struct inode *inode, struct file *filp)

    chrdev file open for buffer access and ioctls

    :param struct inode \*inode:
        Inode structure for identifying the device in the file system

    :param struct file \*filp:
        File structure for iio device used to keep and later access
        private data



.. _`iio_chrdev_open.return`:

Return
------

0 on success or -EBUSY if the device is already opened



.. _`iio_chrdev_release`:

iio_chrdev_release
==================

.. c:function:: int iio_chrdev_release (struct inode *inode, struct file *filp)

    chrdev file close buffer access and ioctls

    :param struct inode \*inode:
        Inode structure pointer for the char device

    :param struct file \*filp:
        File structure pointer for the char device



.. _`iio_chrdev_release.return`:

Return
------

0 for successful release



.. _`iio_device_register`:

iio_device_register
===================

.. c:function:: int iio_device_register (struct iio_dev *indio_dev)

    register a device with the IIO subsystem

    :param struct iio_dev \*indio_dev:
        Device structure filled by the device driver



.. _`iio_device_unregister`:

iio_device_unregister
=====================

.. c:function:: void iio_device_unregister (struct iio_dev *indio_dev)

    unregister a device from the IIO subsystem

    :param struct iio_dev \*indio_dev:
        Device structure representing the device.



.. _`devm_iio_device_register`:

devm_iio_device_register
========================

.. c:function:: int devm_iio_device_register (struct device *dev, struct iio_dev *indio_dev)

    Resource-managed iio_device_register()

    :param struct device \*dev:
        Device to allocate iio_dev for

    :param struct iio_dev \*indio_dev:
        Device structure filled by the device driver



.. _`devm_iio_device_register.description`:

Description
-----------

Managed iio_device_register.  The IIO device registered with this
function is automatically unregistered on driver detach. This function
calls :c:func:`iio_device_register` internally. Refer to that function for more
information.

If an iio_dev registered with this function needs to be unregistered
separately, :c:func:`devm_iio_device_unregister` must be used.



.. _`devm_iio_device_register.returns`:

RETURNS
-------

0 on success, negative error number on failure.



.. _`devm_iio_device_unregister`:

devm_iio_device_unregister
==========================

.. c:function:: void devm_iio_device_unregister (struct device *dev, struct iio_dev *indio_dev)

    Resource-managed iio_device_unregister()

    :param struct device \*dev:
        Device this iio_dev belongs to

    :param struct iio_dev \*indio_dev:
        the iio_dev associated with the device



.. _`devm_iio_device_unregister.description`:

Description
-----------

Unregister iio_dev registered with :c:func:`devm_iio_device_register`.

