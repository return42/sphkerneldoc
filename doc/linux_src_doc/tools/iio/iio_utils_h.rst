.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/iio/iio_utils.h

.. _`iio_channel_info`:

struct iio_channel_info
=======================

.. c:type:: struct iio_channel_info

    information about a given channel

.. _`iio_channel_info.definition`:

Definition
----------

.. code-block:: c

    struct iio_channel_info {
        char *name;
        char *generic_name;
        float scale;
        float offset;
        unsigned index;
        unsigned bytes;
        unsigned bits_used;
        unsigned shift;
        uint64_t mask;
        unsigned be;
        unsigned is_signed;
        unsigned location;
    }

.. _`iio_channel_info.members`:

Members
-------

name
    channel name

generic_name
    general name for channel type

scale
    scale factor to be applied for conversion to si units

offset
    offset to be applied for conversion to si units

index
    the channel index in the buffer output

bytes
    number of bytes occupied in buffer output

bits_used
    number of valid bits of data

shift
    amount of bits to shift right data before applying bit mask

mask
    a bit mask for the raw output

be
    flag if data is big endian

is_signed
    is the raw value stored signed

location
    data offset for this channel inside the buffer (in bytes)

.. This file was automatic generated / don't edit.

