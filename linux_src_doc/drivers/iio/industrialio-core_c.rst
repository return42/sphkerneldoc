.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/industrialio-core.c

.. _`iio_find_channel_from_si`:

iio_find_channel_from_si
========================

.. c:function:: const struct iio_chan_spec *iio_find_channel_from_si(struct iio_dev *indio_dev, int si)

    get channel from its scan index

    :param struct iio_dev \*indio_dev:
        device

    :param int si:
        scan index to match

.. _`iio_get_time_ns`:

iio_get_time_ns
===============

.. c:function:: s64 iio_get_time_ns(const struct iio_dev *indio_dev)

    utility function to get a time stamp for events etc

    :param const struct iio_dev \*indio_dev:
        device

.. _`iio_get_time_res`:

iio_get_time_res
================

.. c:function:: unsigned int iio_get_time_res(const struct iio_dev *indio_dev)

    utility function to get time stamp clock resolution in nano seconds.

    :param const struct iio_dev \*indio_dev:
        device

.. _`of_iio_read_mount_matrix`:

of_iio_read_mount_matrix
========================

.. c:function:: int of_iio_read_mount_matrix(const struct device *dev, const char *propname, struct iio_mount_matrix *matrix)

    retrieve iio device mounting matrix from device-tree "mount-matrix" property

    :param const struct device \*dev:
        device the mounting matrix property is assigned to

    :param const char \*propname:
        device specific mounting matrix property name

    :param struct iio_mount_matrix \*matrix:
        where to store retrieved matrix

.. _`of_iio_read_mount_matrix.description`:

Description
-----------

If device is assigned no mounting matrix property, a default 3x3 identity
matrix will be filled in.

.. _`of_iio_read_mount_matrix.return`:

Return
------

0 if success, or a negative error code on failure.

.. _`iio_format_value`:

iio_format_value
================

.. c:function:: ssize_t iio_format_value(char *buf, unsigned int type, int size, int *vals)

    Formats a IIO value into its string representation

    :param char \*buf:
        The buffer to which the formatted value gets written
        which is assumed to be big enough (i.e. PAGE_SIZE).

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

.. c:function:: int iio_str_to_fixpoint(const char *str, int fract_mult, int *integer, int *fract)

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

.. c:function:: void iio_free_chan_devattr_list(struct list_head *attr_list)

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

.. c:function:: struct iio_dev *iio_device_alloc(int sizeof_priv)

    allocate an iio_dev from a driver

    :param int sizeof_priv:
        Space to allocate for private structure.

.. _`iio_device_free`:

iio_device_free
===============

.. c:function:: void iio_device_free(struct iio_dev *dev)

    free an iio_dev from a driver

    :param struct iio_dev \*dev:
        the iio_dev associated with the device

.. _`devm_iio_device_alloc`:

devm_iio_device_alloc
=====================

.. c:function:: struct iio_dev *devm_iio_device_alloc(struct device *dev, int sizeof_priv)

    Resource-managed \ :c:func:`iio_device_alloc`\ 

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
\ :c:func:`devm_iio_device_free`\  must be used.

.. _`devm_iio_device_alloc.return`:

Return
------

Pointer to allocated iio_dev on success, NULL on failure.

.. _`devm_iio_device_free`:

devm_iio_device_free
====================

.. c:function:: void devm_iio_device_free(struct device *dev, struct iio_dev *iio_dev)

    Resource-managed \ :c:func:`iio_device_free`\ 

    :param struct device \*dev:
        Device this iio_dev belongs to

    :param struct iio_dev \*iio_dev:
        the iio_dev associated with the device

.. _`devm_iio_device_free.description`:

Description
-----------

Free iio_dev allocated with \ :c:func:`devm_iio_device_alloc`\ .

.. _`iio_chrdev_open`:

iio_chrdev_open
===============

.. c:function:: int iio_chrdev_open(struct inode *inode, struct file *filp)

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

.. c:function:: int iio_chrdev_release(struct inode *inode, struct file *filp)

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

.. c:function:: int iio_device_register(struct iio_dev *indio_dev)

    register a device with the IIO subsystem

    :param struct iio_dev \*indio_dev:
        Device structure filled by the device driver

.. _`iio_device_unregister`:

iio_device_unregister
=====================

.. c:function:: void iio_device_unregister(struct iio_dev *indio_dev)

    unregister a device from the IIO subsystem

    :param struct iio_dev \*indio_dev:
        Device structure representing the device.

.. _`devm_iio_device_register`:

devm_iio_device_register
========================

.. c:function:: int devm_iio_device_register(struct device *dev, struct iio_dev *indio_dev)

    Resource-managed \ :c:func:`iio_device_register`\ 

    :param struct device \*dev:
        Device to allocate iio_dev for

    :param struct iio_dev \*indio_dev:
        Device structure filled by the device driver

.. _`devm_iio_device_register.description`:

Description
-----------

Managed iio_device_register.  The IIO device registered with this
function is automatically unregistered on driver detach. This function
calls \ :c:func:`iio_device_register`\  internally. Refer to that function for more
information.

If an iio_dev registered with this function needs to be unregistered
separately, \ :c:func:`devm_iio_device_unregister`\  must be used.

.. _`devm_iio_device_register.return`:

Return
------

0 on success, negative error number on failure.

.. _`devm_iio_device_unregister`:

devm_iio_device_unregister
==========================

.. c:function:: void devm_iio_device_unregister(struct device *dev, struct iio_dev *indio_dev)

    Resource-managed \ :c:func:`iio_device_unregister`\ 

    :param struct device \*dev:
        Device this iio_dev belongs to

    :param struct iio_dev \*indio_dev:
        the iio_dev associated with the device

.. _`devm_iio_device_unregister.description`:

Description
-----------

Unregister iio_dev registered with \ :c:func:`devm_iio_device_register`\ .

.. _`iio_device_claim_direct_mode`:

iio_device_claim_direct_mode
============================

.. c:function:: int iio_device_claim_direct_mode(struct iio_dev *indio_dev)

    Keep device in direct mode

    :param struct iio_dev \*indio_dev:
        the iio_dev associated with the device

.. _`iio_device_claim_direct_mode.description`:

Description
-----------

If the device is in direct mode it is guaranteed to stay
that way until \ :c:func:`iio_device_release_direct_mode`\  is called.

Use with \ :c:func:`iio_device_release_direct_mode`\ 

.. _`iio_device_claim_direct_mode.return`:

Return
------

0 on success, -EBUSY on failure

.. _`iio_device_release_direct_mode`:

iio_device_release_direct_mode
==============================

.. c:function:: void iio_device_release_direct_mode(struct iio_dev *indio_dev)

    releases claim on direct mode

    :param struct iio_dev \*indio_dev:
        the iio_dev associated with the device

.. _`iio_device_release_direct_mode.description`:

Description
-----------

Release the claim. Device is no longer guaranteed to stay
in direct mode.

Use with \ :c:func:`iio_device_claim_direct_mode`\ 

.. This file was automatic generated / don't edit.

