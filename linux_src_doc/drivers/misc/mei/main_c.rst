.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/main.c

.. _`mei_open`:

mei_open
========

.. c:function:: int mei_open(struct inode *inode, struct file *file)

    the open function

    :param inode:
        pointer to inode structure
    :type inode: struct inode \*

    :param file:
        pointer to file structure
    :type file: struct file \*

.. _`mei_open.return`:

Return
------

0 on success, <0 on error

.. _`mei_release`:

mei_release
===========

.. c:function:: int mei_release(struct inode *inode, struct file *file)

    the release function

    :param inode:
        pointer to inode structure
    :type inode: struct inode \*

    :param file:
        pointer to file structure
    :type file: struct file \*

.. _`mei_release.return`:

Return
------

0 on success, <0 on error

.. _`mei_read`:

mei_read
========

.. c:function:: ssize_t mei_read(struct file *file, char __user *ubuf, size_t length, loff_t *offset)

    the read function.

    :param file:
        pointer to file structure
    :type file: struct file \*

    :param ubuf:
        pointer to user buffer
    :type ubuf: char __user \*

    :param length:
        buffer length
    :type length: size_t

    :param offset:
        data offset in buffer
    :type offset: loff_t \*

.. _`mei_read.return`:

Return
------

>=0 data length on success , <0 on error

.. _`mei_write`:

mei_write
=========

.. c:function:: ssize_t mei_write(struct file *file, const char __user *ubuf, size_t length, loff_t *offset)

    the write function.

    :param file:
        pointer to file structure
    :type file: struct file \*

    :param ubuf:
        pointer to user buffer
    :type ubuf: const char __user \*

    :param length:
        buffer length
    :type length: size_t

    :param offset:
        data offset in buffer
    :type offset: loff_t \*

.. _`mei_write.return`:

Return
------

>=0 data length on success , <0 on error

.. _`mei_ioctl_connect_client`:

mei_ioctl_connect_client
========================

.. c:function:: int mei_ioctl_connect_client(struct file *file, struct mei_connect_client_data *data)

    the connect to fw client IOCTL function

    :param file:
        private data of the file object
    :type file: struct file \*

    :param data:
        IOCTL connect data, input and output parameters
    :type data: struct mei_connect_client_data \*

.. _`mei_ioctl_connect_client.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_ioctl_connect_client.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_ioctl_client_notify_request`:

mei_ioctl_client_notify_request
===============================

.. c:function:: int mei_ioctl_client_notify_request(const struct file *file, u32 request)

    propagate event notification request to client

    :param file:
        pointer to file structure
    :type file: const struct file \*

    :param request:
        0 - disable, 1 - enable
    :type request: u32

.. _`mei_ioctl_client_notify_request.return`:

Return
------

0 on success , <0 on error

.. _`mei_ioctl_client_notify_get`:

mei_ioctl_client_notify_get
===========================

.. c:function:: int mei_ioctl_client_notify_get(const struct file *file, u32 *notify_get)

    wait for notification request

    :param file:
        pointer to file structure
    :type file: const struct file \*

    :param notify_get:
        0 - disable, 1 - enable
    :type notify_get: u32 \*

.. _`mei_ioctl_client_notify_get.return`:

Return
------

0 on success , <0 on error

.. _`mei_ioctl`:

mei_ioctl
=========

.. c:function:: long mei_ioctl(struct file *file, unsigned int cmd, unsigned long data)

    the IOCTL function

    :param file:
        pointer to file structure
    :type file: struct file \*

    :param cmd:
        ioctl command
    :type cmd: unsigned int

    :param data:
        pointer to mei message structure
    :type data: unsigned long

.. _`mei_ioctl.return`:

Return
------

0 on success , <0 on error

.. _`mei_compat_ioctl`:

mei_compat_ioctl
================

.. c:function:: long mei_compat_ioctl(struct file *file, unsigned int cmd, unsigned long data)

    the compat IOCTL function

    :param file:
        pointer to file structure
    :type file: struct file \*

    :param cmd:
        ioctl command
    :type cmd: unsigned int

    :param data:
        pointer to mei message structure
    :type data: unsigned long

.. _`mei_compat_ioctl.return`:

Return
------

0 on success , <0 on error

.. _`mei_poll`:

mei_poll
========

.. c:function:: __poll_t mei_poll(struct file *file, poll_table *wait)

    the poll function

    :param file:
        pointer to file structure
    :type file: struct file \*

    :param wait:
        pointer to poll_table structure
    :type wait: poll_table \*

.. _`mei_poll.return`:

Return
------

poll mask

.. _`mei_cl_is_write_queued`:

mei_cl_is_write_queued
======================

.. c:function:: bool mei_cl_is_write_queued(struct mei_cl *cl)

    check if the client has pending writes.

    :param cl:
        writing host client
    :type cl: struct mei_cl \*

.. _`mei_cl_is_write_queued.return`:

Return
------

true if client is writing, false otherwise.

.. _`mei_fsync`:

mei_fsync
=========

.. c:function:: int mei_fsync(struct file *fp, loff_t start, loff_t end, int datasync)

    the fsync handler

    :param fp:
        pointer to file structure
    :type fp: struct file \*

    :param start:
        unused
    :type start: loff_t

    :param end:
        unused
    :type end: loff_t

    :param datasync:
        unused
    :type datasync: int

.. _`mei_fsync.return`:

Return
------

0 on success, -ENODEV if client is not connected

.. _`mei_fasync`:

mei_fasync
==========

.. c:function:: int mei_fasync(int fd, struct file *file, int band)

    asynchronous io support

    :param fd:
        file descriptor
    :type fd: int

    :param file:
        pointer to file structure
    :type file: struct file \*

    :param band:
        band bitmap
    :type band: int

.. _`mei_fasync.return`:

Return
------

negative on error,
0 if it did no changes,
and positive a process was added or deleted

.. _`fw_status_show`:

fw_status_show
==============

.. c:function:: ssize_t fw_status_show(struct device *device, struct device_attribute *attr, char *buf)

    mei device fw_status attribute show method

    :param device:
        device pointer
    :type device: struct device \*

    :param attr:
        attribute pointer
    :type attr: struct device_attribute \*

    :param buf:
        char out buffer
    :type buf: char \*

.. _`fw_status_show.return`:

Return
------

number of the bytes printed into buf or error

.. _`hbm_ver_show`:

hbm_ver_show
============

.. c:function:: ssize_t hbm_ver_show(struct device *device, struct device_attribute *attr, char *buf)

    display HBM protocol version negotiated with FW

    :param device:
        device pointer
    :type device: struct device \*

    :param attr:
        attribute pointer
    :type attr: struct device_attribute \*

    :param buf:
        char out buffer
    :type buf: char \*

.. _`hbm_ver_show.return`:

Return
------

number of the bytes printed into buf or error

.. _`hbm_ver_drv_show`:

hbm_ver_drv_show
================

.. c:function:: ssize_t hbm_ver_drv_show(struct device *device, struct device_attribute *attr, char *buf)

    display HBM protocol version advertised by driver

    :param device:
        device pointer
    :type device: struct device \*

    :param attr:
        attribute pointer
    :type attr: struct device_attribute \*

    :param buf:
        char out buffer
    :type buf: char \*

.. _`hbm_ver_drv_show.return`:

Return
------

number of the bytes printed into buf or error

.. _`fw_ver_show`:

fw_ver_show
===========

.. c:function:: ssize_t fw_ver_show(struct device *device, struct device_attribute *attr, char *buf)

    display ME FW version

    :param device:
        device pointer
    :type device: struct device \*

    :param attr:
        attribute pointer
    :type attr: struct device_attribute \*

    :param buf:
        char out buffer
    :type buf: char \*

.. _`fw_ver_show.return`:

Return
------

number of the bytes printed into buf or error

.. _`mei_minor_get`:

mei_minor_get
=============

.. c:function:: int mei_minor_get(struct mei_device *dev)

    obtain next free device minor number

    :param dev:
        device pointer
    :type dev: struct mei_device \*

.. _`mei_minor_get.return`:

Return
------

allocated minor, or -ENOSPC if no free minor left

.. _`mei_minor_free`:

mei_minor_free
==============

.. c:function:: void mei_minor_free(struct mei_device *dev)

    mark device minor number as free

    :param dev:
        device pointer
    :type dev: struct mei_device \*

.. This file was automatic generated / don't edit.

