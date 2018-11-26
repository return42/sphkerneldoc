.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/industrialio-core.c

.. _`iio_find_channel_from_si`:

iio_find_channel_from_si
========================

.. c:function:: const struct iio_chan_spec *iio_find_channel_from_si(struct iio_dev *indio_dev, int si)

    get channel from its scan index

    :param indio_dev:
        device
    :type indio_dev: struct iio_dev \*

    :param si:
        scan index to match
    :type si: int

.. _`iio_get_time_ns`:

iio_get_time_ns
===============

.. c:function:: s64 iio_get_time_ns(const struct iio_dev *indio_dev)

    utility function to get a time stamp for events etc

    :param indio_dev:
        device
    :type indio_dev: const struct iio_dev \*

.. _`iio_get_time_res`:

iio_get_time_res
================

.. c:function:: unsigned int iio_get_time_res(const struct iio_dev *indio_dev)

    utility function to get time stamp clock resolution in nano seconds.

    :param indio_dev:
        device
    :type indio_dev: const struct iio_dev \*

.. _`of_iio_read_mount_matrix`:

of_iio_read_mount_matrix
========================

.. c:function:: int of_iio_read_mount_matrix(const struct device *dev, const char *propname, struct iio_mount_matrix *matrix)

    retrieve iio device mounting matrix from device-tree "mount-matrix" property

    :param dev:
        device the mounting matrix property is assigned to
    :type dev: const struct device \*

    :param propname:
        device specific mounting matrix property name
    :type propname: const char \*

    :param matrix:
        where to store retrieved matrix
    :type matrix: struct iio_mount_matrix \*

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

    :param buf:
        The buffer to which the formatted value gets written
        which is assumed to be big enough (i.e. PAGE_SIZE).
    :type buf: char \*

    :param type:
        One of the IIO_VAL_* constants. This decides how the val
        and val2 parameters are formatted.
    :type type: unsigned int

    :param size:
        Number of IIO value entries contained in vals
    :type size: int

    :param vals:
        Pointer to the values, exact meaning depends on the
        type parameter.
    :type vals: int \*

.. _`iio_format_value.return`:

Return
------

0 by default, a negative number on failure or the
        total number of characters written for a type that belongs
        to the IIO_VAL_* constant.

.. _`iio_str_to_fixpoint`:

iio_str_to_fixpoint
===================

.. c:function:: int iio_str_to_fixpoint(const char *str, int fract_mult, int *integer, int *fract)

    Parse a fixed-point number from a string

    :param str:
        The string to parse
    :type str: const char \*

    :param fract_mult:
        Multiplier for the first decimal place, should be a power of 10
    :type fract_mult: int

    :param integer:
        The integer part of the number
    :type integer: int \*

    :param fract:
        The fractional part of the number
    :type fract: int \*

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

    :param attr_list:
        List of IIO device attributes
    :type attr_list: struct list_head \*

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

    :param sizeof_priv:
        Space to allocate for private structure.
    :type sizeof_priv: int

.. _`iio_device_free`:

iio_device_free
===============

.. c:function:: void iio_device_free(struct iio_dev *dev)

    free an iio_dev from a driver

    :param dev:
        the iio_dev associated with the device
    :type dev: struct iio_dev \*

.. _`devm_iio_device_alloc`:

devm_iio_device_alloc
=====================

.. c:function:: struct iio_dev *devm_iio_device_alloc(struct device *dev, int sizeof_priv)

    Resource-managed \ :c:func:`iio_device_alloc`\ 

    :param dev:
        Device to allocate iio_dev for
    :type dev: struct device \*

    :param sizeof_priv:
        Space to allocate for private structure.
    :type sizeof_priv: int

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

    :param dev:
        Device this iio_dev belongs to
    :type dev: struct device \*

    :param iio_dev:
        the iio_dev associated with the device
    :type iio_dev: struct iio_dev \*

.. _`devm_iio_device_free.description`:

Description
-----------

Free iio_dev allocated with \ :c:func:`devm_iio_device_alloc`\ .

.. _`iio_chrdev_open`:

iio_chrdev_open
===============

.. c:function:: int iio_chrdev_open(struct inode *inode, struct file *filp)

    chrdev file open for buffer access and ioctls

    :param inode:
        Inode structure for identifying the device in the file system
    :type inode: struct inode \*

    :param filp:
        File structure for iio device used to keep and later access
        private data
    :type filp: struct file \*

.. _`iio_chrdev_open.return`:

Return
------

0 on success or -EBUSY if the device is already opened

.. _`iio_chrdev_release`:

iio_chrdev_release
==================

.. c:function:: int iio_chrdev_release(struct inode *inode, struct file *filp)

    chrdev file close buffer access and ioctls

    :param inode:
        Inode structure pointer for the char device
    :type inode: struct inode \*

    :param filp:
        File structure pointer for the char device
    :type filp: struct file \*

.. _`iio_chrdev_release.return`:

Return
------

0 for successful release

.. _`iio_device_unregister`:

iio_device_unregister
=====================

.. c:function:: void iio_device_unregister(struct iio_dev *indio_dev)

    unregister a device from the IIO subsystem

    :param indio_dev:
        Device structure representing the device.
    :type indio_dev: struct iio_dev \*

.. _`devm_iio_device_unregister`:

devm_iio_device_unregister
==========================

.. c:function:: void devm_iio_device_unregister(struct device *dev, struct iio_dev *indio_dev)

    Resource-managed \ :c:func:`iio_device_unregister`\ 

    :param dev:
        Device this iio_dev belongs to
    :type dev: struct device \*

    :param indio_dev:
        the iio_dev associated with the device
    :type indio_dev: struct iio_dev \*

.. _`devm_iio_device_unregister.description`:

Description
-----------

Unregister iio_dev registered with \ :c:func:`devm_iio_device_register`\ .

.. _`iio_device_claim_direct_mode`:

iio_device_claim_direct_mode
============================

.. c:function:: int iio_device_claim_direct_mode(struct iio_dev *indio_dev)

    Keep device in direct mode

    :param indio_dev:
        the iio_dev associated with the device
    :type indio_dev: struct iio_dev \*

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

    :param indio_dev:
        the iio_dev associated with the device
    :type indio_dev: struct iio_dev \*

.. _`iio_device_release_direct_mode.description`:

Description
-----------

Release the claim. Device is no longer guaranteed to stay
in direct mode.

Use with \ :c:func:`iio_device_claim_direct_mode`\ 

.. This file was automatic generated / don't edit.

