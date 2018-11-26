.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dummy/iio_simple_dummy_events.c

.. _`iio_simple_dummy_read_event_config`:

iio_simple_dummy_read_event_config
==================================

.. c:function:: int iio_simple_dummy_read_event_config(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, enum iio_event_type type, enum iio_event_direction dir)

    :param indio_dev:
        *undescribed*
    :type indio_dev: struct iio_dev \*

    :param chan:
        *undescribed*
    :type chan: const struct iio_chan_spec \*

    :param type:
        *undescribed*
    :type type: enum iio_event_type

    :param dir:
        *undescribed*
    :type dir: enum iio_event_direction

.. _`iio_simple_dummy_read_event_config.description`:

Description
-----------

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License version 2 as published by
the Free Software Foundation.

Event handling elements of industrial I/O reference driver.

.. _`iio_simple_dummy_write_event_config`:

iio_simple_dummy_write_event_config
===================================

.. c:function:: int iio_simple_dummy_write_event_config(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, enum iio_event_type type, enum iio_event_direction dir, int state)

    set whether event is enabled

    :param indio_dev:
        the device instance data
    :type indio_dev: struct iio_dev \*

    :param chan:
        channel for the event whose state is being set
    :type chan: const struct iio_chan_spec \*

    :param type:
        type of the event whose state is being set
    :type type: enum iio_event_type

    :param dir:
        direction of the vent whose state is being set
    :type dir: enum iio_event_direction

    :param state:
        whether to enable or disable the device.
    :type state: int

.. _`iio_simple_dummy_write_event_config.description`:

Description
-----------

This function would normally set the relevant registers on the devices
so that it generates the specified event. Here it just sets up a cached
value.

.. _`iio_simple_dummy_read_event_value`:

iio_simple_dummy_read_event_value
=================================

.. c:function:: int iio_simple_dummy_read_event_value(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, enum iio_event_type type, enum iio_event_direction dir, enum iio_event_info info, int *val, int *val2)

    get value associated with event

    :param indio_dev:
        device instance specific data
    :type indio_dev: struct iio_dev \*

    :param chan:
        channel for the event whose value is being read
    :type chan: const struct iio_chan_spec \*

    :param type:
        type of the event whose value is being read
    :type type: enum iio_event_type

    :param dir:
        direction of the vent whose value is being read
    :type dir: enum iio_event_direction

    :param info:
        info type of the event whose value is being read
    :type info: enum iio_event_info

    :param val:
        value for the event code.
    :type val: int \*

    :param val2:
        *undescribed*
    :type val2: int \*

.. _`iio_simple_dummy_read_event_value.description`:

Description
-----------

Many devices provide a large set of events of which only a subset may
be enabled at a time, with value registers whose meaning changes depending
on the event enabled. This often means that the driver must cache the values
associated with each possible events so that the right value is in place when
the enabled event is changed.

.. _`iio_simple_dummy_write_event_value`:

iio_simple_dummy_write_event_value
==================================

.. c:function:: int iio_simple_dummy_write_event_value(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, enum iio_event_type type, enum iio_event_direction dir, enum iio_event_info info, int val, int val2)

    set value associate with event

    :param indio_dev:
        device instance specific data
    :type indio_dev: struct iio_dev \*

    :param chan:
        channel for the event whose value is being set
    :type chan: const struct iio_chan_spec \*

    :param type:
        type of the event whose value is being set
    :type type: enum iio_event_type

    :param dir:
        direction of the vent whose value is being set
    :type dir: enum iio_event_direction

    :param info:
        info type of the event whose value is being set
    :type info: enum iio_event_info

    :param val:
        the value to be set.
    :type val: int

    :param val2:
        *undescribed*
    :type val2: int

.. _`iio_simple_dummy_event_handler`:

iio_simple_dummy_event_handler
==============================

.. c:function:: irqreturn_t iio_simple_dummy_event_handler(int irq, void *private)

    identify and pass on event

    :param irq:
        irq of event line
    :type irq: int

    :param private:
        pointer to device instance state.
    :type private: void \*

.. _`iio_simple_dummy_event_handler.description`:

Description
-----------

This handler is responsible for querying the device to find out what
event occurred and for then pushing that event towards userspace.
Here only one event occurs so we push that directly on with locally
grabbed timestamp.

.. _`iio_simple_dummy_events_register`:

iio_simple_dummy_events_register
================================

.. c:function:: int iio_simple_dummy_events_register(struct iio_dev *indio_dev)

    setup interrupt handling for events

    :param indio_dev:
        device instance data
    :type indio_dev: struct iio_dev \*

.. _`iio_simple_dummy_events_register.description`:

Description
-----------

This function requests the threaded interrupt to handle the events.
Normally the irq is a hardware interrupt and the number comes
from board configuration files.  Here we get it from a companion
module that fakes the interrupt for us. Note that module in
no way forms part of this example. Just assume that events magically
appear via the provided interrupt.

.. _`iio_simple_dummy_events_unregister`:

iio_simple_dummy_events_unregister
==================================

.. c:function:: void iio_simple_dummy_events_unregister(struct iio_dev *indio_dev)

    tidy up interrupt handling on remove

    :param indio_dev:
        device instance data
    :type indio_dev: struct iio_dev \*

.. This file was automatic generated / don't edit.

