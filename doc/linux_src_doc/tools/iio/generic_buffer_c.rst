.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/iio/generic_buffer.c

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

    :param struct iio_channel_info \*channels:
        the channel info array

    :param int num_channels:
        number of channels

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

    :param char \*data:
        pointer to the start of the scan

    :param struct iio_channel_info \*channels:
        information about the channels.
        Note: size_from_channelarray must have been called first
        to fill the location offsets.

    :param int num_channels:
        number of channels

.. This file was automatic generated / don't edit.

