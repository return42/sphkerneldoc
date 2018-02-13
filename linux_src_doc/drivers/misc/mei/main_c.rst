.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/main.c

.. _`mei_open`:

mei_open
========

.. c:function:: int mei_open(struct inode *inode, struct file *file)

    the open function

    :param struct inode \*inode:
        pointer to inode structure

    :param struct file \*file:
        pointer to file structure

.. _`mei_open.return`:

Return
------

0 on success, <0 on error

.. _`mei_release`:

mei_release
===========

.. c:function:: int mei_release(struct inode *inode, struct file *file)

    the release function

    :param struct inode \*inode:
        pointer to inode structure

    :param struct file \*file:
        pointer to file structure

.. _`mei_release.return`:

Return
------

0 on success, <0 on error

.. _`mei_read`:

mei_read
========

.. c:function:: ssize_t mei_read(struct file *file, char __user *ubuf, size_t length, loff_t *offset)

    the read function.

    :param struct file \*file:
        pointer to file structure

    :param char __user \*ubuf:
        pointer to user buffer

    :param size_t length:
        buffer length

    :param loff_t \*offset:
        data offset in buffer

.. _`mei_read.return`:

Return
------

>=0 data length on success , <0 on error

.. _`mei_write`:

mei_write
=========

.. c:function:: ssize_t mei_write(struct file *file, const char __user *ubuf, size_t length, loff_t *offset)

    the write function.

    :param struct file \*file:
        pointer to file structure

    :param const char __user \*ubuf:
        pointer to user buffer

    :param size_t length:
        buffer length

    :param loff_t \*offset:
        data offset in buffer

.. _`mei_write.return`:

Return
------

>=0 data length on success , <0 on error

.. _`mei_ioctl_connect_client`:

mei_ioctl_connect_client
========================

.. c:function:: int mei_ioctl_connect_client(struct file *file, struct mei_connect_client_data *data)

    the connect to fw client IOCTL function

    :param struct file \*file:
        private data of the file object

    :param struct mei_connect_client_data \*data:
        IOCTL connect data, input and output parameters

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

    :param const struct file \*file:
        pointer to file structure

    :param u32 request:
        0 - disable, 1 - enable

.. _`mei_ioctl_client_notify_request.return`:

Return
------

0 on success , <0 on error

.. _`mei_ioctl_client_notify_get`:

mei_ioctl_client_notify_get
===========================

.. c:function:: int mei_ioctl_client_notify_get(const struct file *file, u32 *notify_get)

    wait for notification request

    :param const struct file \*file:
        pointer to file structure

    :param u32 \*notify_get:
        0 - disable, 1 - enable

.. _`mei_ioctl_client_notify_get.return`:

Return
------

0 on success , <0 on error

.. _`mei_ioctl`:

mei_ioctl
=========

.. c:function:: long mei_ioctl(struct file *file, unsigned int cmd, unsigned long data)

    the IOCTL function

    :param struct file \*file:
        pointer to file structure

    :param unsigned int cmd:
        ioctl command

    :param unsigned long data:
        pointer to mei message structure

.. _`mei_ioctl.return`:

Return
------

0 on success , <0 on error

.. _`mei_compat_ioctl`:

mei_compat_ioctl
================

.. c:function:: long mei_compat_ioctl(struct file *file, unsigned int cmd, unsigned long data)

    the compat IOCTL function

    :param struct file \*file:
        pointer to file structure

    :param unsigned int cmd:
        ioctl command

    :param unsigned long data:
        pointer to mei message structure

.. _`mei_compat_ioctl.return`:

Return
------

0 on success , <0 on error

.. _`mei_poll`:

mei_poll
========

.. c:function:: __poll_t mei_poll(struct file *file, poll_table *wait)

    the poll function

    :param struct file \*file:
        pointer to file structure

    :param poll_table \*wait:
        pointer to poll_table structure

.. _`mei_poll.return`:

Return
------

poll mask

.. _`mei_cl_is_write_queued`:

mei_cl_is_write_queued
======================

.. c:function:: bool mei_cl_is_write_queued(struct mei_cl *cl)

    check if the client has pending writes.

    :param struct mei_cl \*cl:
        writing host client

.. _`mei_cl_is_write_queued.return`:

Return
------

true if client is writing, false otherwise.

.. _`mei_fsync`:

mei_fsync
=========

.. c:function:: int mei_fsync(struct file *fp, loff_t start, loff_t end, int datasync)

    the fsync handler

    :param struct file \*fp:
        pointer to file structure

    :param loff_t start:
        unused

    :param loff_t end:
        unused

    :param int datasync:
        unused

.. _`mei_fsync.return`:

Return
------

0 on success, -ENODEV if client is not connected

.. _`mei_fasync`:

mei_fasync
==========

.. c:function:: int mei_fasync(int fd, struct file *file, int band)

    asynchronous io support

    :param int fd:
        file descriptor

    :param struct file \*file:
        pointer to file structure

    :param int band:
        band bitmap

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

    :param struct device \*device:
        device pointer

    :param struct device_attribute \*attr:
        attribute pointer

    :param char \*buf:
        char out buffer

.. _`fw_status_show.return`:

Return
------

number of the bytes printed into buf or error

.. _`hbm_ver_show`:

hbm_ver_show
============

.. c:function:: ssize_t hbm_ver_show(struct device *device, struct device_attribute *attr, char *buf)

    display HBM protocol version negotiated with FW

    :param struct device \*device:
        device pointer

    :param struct device_attribute \*attr:
        attribute pointer

    :param char \*buf:
        char out buffer

.. _`hbm_ver_show.return`:

Return
------

number of the bytes printed into buf or error

.. _`hbm_ver_drv_show`:

hbm_ver_drv_show
================

.. c:function:: ssize_t hbm_ver_drv_show(struct device *device, struct device_attribute *attr, char *buf)

    display HBM protocol version advertised by driver

    :param struct device \*device:
        device pointer

    :param struct device_attribute \*attr:
        attribute pointer

    :param char \*buf:
        char out buffer

.. _`hbm_ver_drv_show.return`:

Return
------

number of the bytes printed into buf or error

.. _`mei_minor_get`:

mei_minor_get
=============

.. c:function:: int mei_minor_get(struct mei_device *dev)

    obtain next free device minor number

    :param struct mei_device \*dev:
        device pointer

.. _`mei_minor_get.return`:

Return
------

allocated minor, or -ENOSPC if no free minor left

.. _`mei_minor_free`:

mei_minor_free
==============

.. c:function:: void mei_minor_free(struct mei_device *dev)

    mark device minor number as free

    :param struct mei_device \*dev:
        device pointer

.. This file was automatic generated / don't edit.

