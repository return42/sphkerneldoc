.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/lirc_dev.h

.. _`lirc_dev`:

struct lirc_dev
===============

.. c:type:: struct lirc_dev

    represents a LIRC device

.. _`lirc_dev.definition`:

Definition
----------

.. code-block:: c

    struct lirc_dev {
        char name[40];
        unsigned int minor;
        __u32 code_length;
        __u32 features;
        unsigned int buffer_size;
        unsigned int chunk_size;
        struct lirc_buffer *buf;
        bool buf_internal;
        void *data;
        struct rc_dev *rdev;
        const struct file_operations *fops;
        struct module *owner;
        bool attached;
        int open;
        struct mutex mutex;
        struct device dev;
        struct cdev cdev;
    }

.. _`lirc_dev.members`:

Members
-------

name
    used for logging

minor
    the minor device (/dev/lircX) number for the device

code_length
    length of a remote control key code expressed in bits

features
    lirc compatible hardware features, like LIRC_MODE_RAW,
    LIRC_CAN\_\*, as defined at include/media/lirc.h.

buffer_size
    Number of FIFO buffers with \ ``chunk_size``\  size.
    Only used if \ ``rbuf``\  is NULL.

chunk_size
    Size of each FIFO buffer.
    Only used if \ ``rbuf``\  is NULL.

buf
    if \ ``NULL``\ , lirc_dev will allocate and manage the buffer,
    otherwise allocated by the caller which will
    have to write to the buffer by other means, like irq's
    (see also lirc_serial.c).

buf_internal
    whether lirc_dev has allocated the read buffer or not

data
    private per-driver data

rdev
    &struct rc_dev associated with the device

fops
    &struct file_operations for the device

owner
    the module owning this struct

attached
    if the device is still live

open
    open count for the device's chardev

mutex
    serialises file_operations calls

dev
    &struct device assigned to the device

cdev
    &struct cdev assigned to the device

.. This file was automatic generated / don't edit.

