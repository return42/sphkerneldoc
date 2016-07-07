.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ring_buffer.h

.. _`ring_buffer_type`:

enum ring_buffer_type
=====================

.. c:type:: enum ring_buffer_type

    internal ring buffer types

.. _`ring_buffer_type.definition`:

Definition
----------

.. code-block:: c

    enum ring_buffer_type {
        RINGBUF_TYPE_DATA_TYPE_LEN_MAX,
        RINGBUF_TYPE_PADDING,
        RINGBUF_TYPE_TIME_EXTEND,
        RINGBUF_TYPE_TIME_STAMP
    };

.. _`ring_buffer_type.constants`:

Constants
---------

RINGBUF_TYPE_DATA_TYPE_LEN_MAX
    *undescribed*

RINGBUF_TYPE_PADDING
    Left over page padding or discarded event
    If time_delta is 0:
    array is ignored
    size is variable depending on how much
    padding is needed
    If time_delta is non zero:
    array[0] holds the actual length
    size = 4 + length (bytes)

RINGBUF_TYPE_TIME_EXTEND
    Extend the time delta
    array[0] = time delta (28 .. 59)
    size = 8 bytes

RINGBUF_TYPE_TIME_STAMP
    Sync time stamp with external clock
    array[0]    = tv_nsec
    array[1..2] = tv_sec
    size = 16 bytes

.. _`ring_buffer_type.description`:

Description
-----------

<= \ ``RINGBUF_TYPE_DATA_TYPE_LEN_MAX``\ :
Data record
If type_len is zero:
array[0] holds the actual length
array[1..(length+3)/4] holds data
size = 4 + length (bytes)
else
length = type_len << 2
array[0..(length+3)/4-1] holds data
size = 4 + length (bytes)

.. This file was automatic generated / don't edit.

