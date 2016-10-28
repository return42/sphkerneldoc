.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/machine.h

.. _`iio_map`:

struct iio_map
==============

.. c:type:: struct iio_map

    description of link between consumer and device channels

.. _`iio_map.definition`:

Definition
----------

.. code-block:: c

    struct iio_map {
        const char *adc_channel_label;
        const char *consumer_dev_name;
        const char *consumer_channel;
        void *consumer_data;
    }

.. _`iio_map.members`:

Members
-------

adc_channel_label
    Label used to identify the channel on the provider.
    This is matched against the datasheet_name element
    of struct iio_chan_spec.

consumer_dev_name
    Name to uniquely identify the consumer device.

consumer_channel
    Unique name used to identify the channel on the
    consumer side.

consumer_data
    Data about the channel for use by the consumer driver.

.. This file was automatic generated / don't edit.

