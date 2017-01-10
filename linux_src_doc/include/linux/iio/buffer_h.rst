.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/buffer.h

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
        int (*read_first_n)(struct iio_buffer *buffer,size_t n,char __user *buf);
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
    A bitmask combination of INDIO_BUFFER_FLAG_*

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
        struct attribute_group *scan_el_attrs;
        long *scan_mask;
        bool scan_timestamp;
        const struct iio_buffer_access_funcs *access;
        struct list_head scan_el_dev_attr_list;
        struct attribute_group buffer_group;
        struct attribute_group scan_el_group;
        wait_queue_head_t pollq;
        bool stufftoread;
        const struct attribute **attrs;
        struct list_head demux_list;
        void *demux_bounce;
        struct list_head buffer_list;
        struct kref ref;
        unsigned int watermark;
    }

.. _`iio_buffer.members`:

Members
-------

length
    [DEVICE] number of datums in buffer

bytes_per_datum
    [DEVICE] size of individual datum including timestamp

scan_el_attrs
    [DRIVER] control of scan elements if that scan mode
    control method is used

scan_mask
    [INTERN] bitmask used in masking scan mode elements

scan_timestamp
    [INTERN] does the scan mode include a timestamp

access
    [DRIVER] buffer access functions associated with the
    implementation.

scan_el_dev_attr_list
    [INTERN] list of scan element related attributes.

buffer_group
    [INTERN] attributes of the buffer group

scan_el_group
    [DRIVER] attribute group for those attributes not
    created from the iio_chan_info array.

pollq
    [INTERN] wait queue to allow for polling on the buffer.

stufftoread
    [INTERN] flag to indicate new data.

attrs
    [INTERN] standard attributes of the buffer

demux_list
    [INTERN] list of operations required to demux the scan.

demux_bounce
    [INTERN] buffer for doing gather from incoming scan.

buffer_list
    [INTERN] entry in the devices list of current buffers.

ref
    [INTERN] reference count of the buffer.

watermark
    [INTERN] number of datums to wait for poll/read.

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

.. _`iio_push_to_buffers`:

iio_push_to_buffers
===================

.. c:function:: int iio_push_to_buffers(struct iio_dev *indio_dev, const void *data)

    push to a registered buffer.

    :param struct iio_dev \*indio_dev:
        iio_dev structure for device.

    :param const void \*data:
        Full scan.

.. _`iio_device_attach_buffer`:

iio_device_attach_buffer
========================

.. c:function:: void iio_device_attach_buffer(struct iio_dev *indio_dev, struct iio_buffer *buffer)

    Attach a buffer to a IIO device

    :param struct iio_dev \*indio_dev:
        The device the buffer should be attached to

    :param struct iio_buffer \*buffer:
        The buffer to attach to the device

.. _`iio_device_attach_buffer.description`:

Description
-----------

This function attaches a buffer to a IIO device. The buffer stays attached to
the device until the device is freed. The function should only be called at
most once per device.

.. This file was automatic generated / don't edit.

