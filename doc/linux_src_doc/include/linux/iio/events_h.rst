.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/events.h

.. _`iio_unmod_event_code`:

IIO_UNMOD_EVENT_CODE
====================

.. c:function::  IIO_UNMOD_EVENT_CODE( chan_type,  number,  type,  direction)

    create event identifier for unmodified channels

    :param  chan_type:
        Type of the channel. Should be one of enum iio_chan_type.

    :param  number:
        Channel number.

    :param  type:
        Type of the event. Should be one of enum iio_event_type.

    :param  direction:
        Direction of the event. One of enum iio_event_direction.

.. This file was automatic generated / don't edit.

