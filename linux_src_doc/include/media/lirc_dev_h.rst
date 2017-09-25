.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/lirc_dev.h

.. _`lirc_driver`:

struct lirc_driver
==================

.. c:type:: struct lirc_driver

    Defines the parameters on a LIRC driver

.. _`lirc_driver.definition`:

Definition
----------

.. code-block:: c

    struct lirc_driver {
        char name[40];
        int minor;
        __u32 code_length;
        unsigned int buffer_size;
        __u32 features;
        unsigned int chunk_size;
        void *data;
        int min_timeout;
        int max_timeout;
        struct lirc_buffer *rbuf;
        struct rc_dev *rdev;
        const struct file_operations *fops;
        struct device *dev;
        struct module *owner;
    }

.. _`lirc_driver.members`:

Members
-------

name
    this string will be used for logs

minor
    indicates minor device (/dev/lirc) number for
    registered driver if caller fills it with negative
    value, then the first free minor number will be used
    (if available).

code_length
    length of the remote control key code expressed in bits.

buffer_size
    Number of FIFO buffers with \ ``chunk_size``\  size. If zero,
    creates a buffer with BUFLEN size (16 bytes).

features
    lirc compatible hardware features, like LIRC_MODE_RAW,
    LIRC_CAN\_\*, as defined at include/media/lirc.h.

chunk_size
    Size of each FIFO buffer.

data
    it may point to any driver data and this pointer will
    be passed to all callback functions.

min_timeout
    Minimum timeout for record. Valid only if
    LIRC_CAN_SET_REC_TIMEOUT is defined.

max_timeout
    Maximum timeout for record. Valid only if
    LIRC_CAN_SET_REC_TIMEOUT is defined.

rbuf
    if not NULL, it will be used as a read buffer, you will
    have to write to the buffer by other means, like irq's
    (see also lirc_serial.c).

rdev
    Pointed to struct rc_dev associated with the LIRC
    device.

fops
    file_operations for drivers which don't fit the current
    driver model.
    Some ioctl's can be directly handled by lirc_dev if the
    driver's ioctl function is NULL or if it returns
    -ENOIOCTLCMD (see also lirc_serial.c).

dev
    pointer to the struct device associated with the LIRC
    device.

owner
    the module owning this struct

.. This file was automatic generated / don't edit.

