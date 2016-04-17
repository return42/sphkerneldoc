.. -*- coding: utf-8; mode: rst -*-

========
events.h
========


.. _`iio_event_code`:

IIO_EVENT_CODE
==============

.. c:function:: IIO_EVENT_CODE ( chan_type,  diff,  modifier,  direction,  type,  chan,  chan1,  chan2)

    create event identifier

    :param chan_type:
        Type of the channel. Should be one of enum iio_chan_type.

    :param diff:
        Whether the event is for an differential channel or not.

    :param modifier:
        Modifier for the channel. Should be one of enum iio_modifier.

    :param direction:
        Direction of the event. One of enum iio_event_direction.

    :param type:
        Type of the event. Should be one of enum iio_event_type.

    :param chan:
        Channel number for non-differential channels.

    :param chan1:
        First channel number for differential channels.

    :param chan2:
        Second channel number for differential channels.



.. _`iio_mod_event_code`:

IIO_MOD_EVENT_CODE
==================

.. c:function:: IIO_MOD_EVENT_CODE ( chan_type,  number,  modifier,  type,  direction)

    create event identifier for modified channels

    :param chan_type:
        Type of the channel. Should be one of enum iio_chan_type.

    :param number:
        Channel number.

    :param modifier:
        Modifier for the channel. Should be one of enum iio_modifier.

    :param type:
        Type of the event. Should be one of enum iio_event_type.

    :param direction:
        Direction of the event. One of enum iio_event_direction.



.. _`iio_unmod_event_code`:

IIO_UNMOD_EVENT_CODE
====================

.. c:function:: IIO_UNMOD_EVENT_CODE ( chan_type,  number,  type,  direction)

    create event identifier for unmodified channels

    :param chan_type:
        Type of the channel. Should be one of enum iio_chan_type.

    :param number:
        Channel number.

    :param type:
        Type of the event. Should be one of enum iio_event_type.

    :param direction:
        Direction of the event. One of enum iio_event_direction.

