.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/buffer_impl.h

.. _`indio_buffer_flag_fixed_watermark`:

INDIO_BUFFER_FLAG_FIXED_WATERMARK
=================================

.. c:function::  INDIO_BUFFER_FLAG_FIXED_WATERMARK()

    Watermark level of the buffer can not be configured. It has a fixed value which will be buffer specific.

.. _`iio_buffer_access_funcs`:

struct iio_buffer_access_funcs
==============================

.. c:type:: struct iio_buffer_access_funcs

    access functions for buffers.

.. _`iio_buffer_access_funcs.definition`:

Definition
----------

.. code-block:: c

    struct iio_buffer_access_funcs {
        int (*store_to)(struct iio_buffer *buffer, const void *data);
        int (*read_first_n)(struct iio_buffer *buffer,size_t n, char __user *buf);
        size_t (*data_available)(struct iio_buffer *buffer);
        int (*request_update)(struct iio_buffer *buffer);
        int (*set_bytes_per_datum)(struct iio_buffer *buffer, size_t bpd);
        int (*set_length)(struct iio_buffer *buffer, int length);
        int (*enable)(struct iio_buffer *buffer, struct iio_dev *indio_dev);
        int (*disable)(struct iio_buffer *buffer, struct iio_dev *indio_dev);
        void (*release)(struct iio_buffer *buffer);
        unsigned int modes;
        unsigned int flags;
    }

.. _`iio_buffer_access_funcs.members`:

Members
-------

store_to
    actually store stuff to the buffer

read_first_n
    try to get a specified number of bytes (must exist)

data_available
    indicates how much data is available for reading from
    the buffer.

request_update
    if a parameter change has been marked, update underlying
    storage.

set_bytes_per_datum
    set number of bytes per datum

set_length
    set number of datums in buffer

enable
    called if the buffer is attached to a device and the
    device starts sampling. Calls are balanced with
    \ ``disable``\ .

disable
    called if the buffer is attached to a device and the
    device stops sampling. Calles are balanced with \ ``enable``\ .

release
    called when the last reference to the buffer is dropped,
    should free all resources allocated by the buffer.

modes
    Supported operating modes by this buffer type

flags
    A bitmask combination of INDIO_BUFFER_FLAG\_\*

.. _`iio_buffer_access_funcs.description`:

Description
-----------

The purpose of this structure is to make the buffer element
modular as event for a given driver, different usecases may require
different buffer designs (space efficiency vs speed for example).

It is worth noting that a given buffer implementation may only support a
small proportion of these functions.  The core code 'should' cope fine with
any of them not existing.

.. _`iio_buffer`:

struct iio_buffer
=================

.. c:type:: struct iio_buffer

    general buffer structure

.. _`iio_buffer.definition`:

Definition
----------

.. code-block:: c

    struct iio_buffer {
        int length;
        int bytes_per_datum;
        const struct iio_buffer_access_funcs *access;
        long *scan_mask;
        struct list_head demux_list;
        wait_queue_head_t pollq;
        unsigned int watermark;
    }

.. _`iio_buffer.members`:

Members
-------

length
    Number of datums in buffer.

bytes_per_datum
    Size of individual datum including timestamp.

access
    Buffer access functions associated with theimplementation.

scan_mask
    Bitmask used in masking scan mode elements.

demux_list
    List of operations required to demux the scan.

pollq
    Wait queue to allow for polling on the buffer.

watermark
    Number of datums to wait for poll/read.

.. _`iio_buffer.description`:

Description
-----------

Note that the internals of this structure should only be of interest to
those writing new buffer implementations.

.. _`iio_update_buffers`:

iio_update_buffers
==================

.. c:function:: int iio_update_buffers(struct iio_dev *indio_dev, struct iio_buffer *insert_buffer, struct iio_buffer *remove_buffer)

    add or remove buffer from active list

    :param struct iio_dev \*indio_dev:
        device to add buffer to

    :param struct iio_buffer \*insert_buffer:
        buffer to insert

    :param struct iio_buffer \*remove_buffer:
        buffer_to_remove

.. _`iio_update_buffers.description`:

Description
-----------

Note this will tear down the all buffering and build it up again

.. _`iio_buffer_init`:

iio_buffer_init
===============

.. c:function:: void iio_buffer_init(struct iio_buffer *buffer)

    Initialize the buffer structure

    :param struct iio_buffer \*buffer:
        buffer to be initialized

.. This file was automatic generated / don't edit.

