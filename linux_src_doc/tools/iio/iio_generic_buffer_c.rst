.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/iio/iio_generic_buffer.c

.. _`autochan`:

enum autochan
=============

.. c:type:: enum autochan

    state for the automatic channel enabling mechanism

.. _`autochan.definition`:

Definition
----------

.. code-block:: c

    enum autochan {
        AUTOCHANNELS_DISABLED,
        AUTOCHANNELS_ENABLED,
        AUTOCHANNELS_ACTIVE
    };

.. _`autochan.constants`:

Constants
---------

AUTOCHANNELS_DISABLED
    *undescribed*

AUTOCHANNELS_ENABLED
    *undescribed*

AUTOCHANNELS_ACTIVE
    *undescribed*

.. _`size_from_channelarray`:

size_from_channelarray
======================

.. c:function:: int size_from_channelarray(struct iio_channel_info *channels, int num_channels)

    calculate the storage size of a scan

    :param channels:
        the channel info array
    :type channels: struct iio_channel_info \*

    :param num_channels:
        number of channels
    :type num_channels: int

.. _`size_from_channelarray.description`:

Description
-----------

Has the side effect of filling the channels[i].location values used
in processing the buffer output.

.. _`process_scan`:

process_scan
============

.. c:function:: void process_scan(char *data, struct iio_channel_info *channels, int num_channels)

    print out the values in SI units

    :param data:
        pointer to the start of the scan
    :type data: char \*

    :param channels:
        information about the channels.
        Note: size_from_channelarray must have been called first
        to fill the location offsets.
    :type channels: struct iio_channel_info \*

    :param num_channels:
        number of channels
    :type num_channels: int

.. This file was automatic generated / don't edit.

