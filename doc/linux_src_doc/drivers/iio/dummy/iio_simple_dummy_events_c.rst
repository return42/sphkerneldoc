.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dummy/iio_simple_dummy_events.c

.. _`iio_simple_dummy_read_event_config`:

iio_simple_dummy_read_event_config
==================================

.. c:function:: int iio_simple_dummy_read_event_config(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, enum iio_event_type type, enum iio_event_direction dir)

    :param struct iio_dev \*indio_dev:
        *undescribed*

    :param const struct iio_chan_spec \*chan:
        *undescribed*

    :param enum iio_event_type type:
        *undescribed*

    :param enum iio_event_direction dir:
        *undescribed*

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

    :param struct iio_dev \*indio_dev:
        the device instance data

    :param const struct iio_chan_spec \*chan:
        channel for the event whose state is being set

    :param enum iio_event_type type:
        type of the event whose state is being set

    :param enum iio_event_direction dir:
        direction of the vent whose state is being set

    :param int state:
        whether to enable or disable the device.

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

    :param struct iio_dev \*indio_dev:
        device instance specific data

    :param const struct iio_chan_spec \*chan:
        channel for the event whose value is being read

    :param enum iio_event_type type:
        type of the event whose value is being read

    :param enum iio_event_direction dir:
        direction of the vent whose value is being read

    :param enum iio_event_info info:
        info type of the event whose value is being read

    :param int \*val:
        value for the event code.

    :param int \*val2:
        *undescribed*

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

    :param struct iio_dev \*indio_dev:
        device instance specific data

    :param const struct iio_chan_spec \*chan:
        channel for the event whose value is being set

    :param enum iio_event_type type:
        type of the event whose value is being set

    :param enum iio_event_direction dir:
        direction of the vent whose value is being set

    :param enum iio_event_info info:
        info type of the event whose value is being set

    :param int val:
        the value to be set.

    :param int val2:
        *undescribed*

.. _`iio_simple_dummy_event_handler`:

iio_simple_dummy_event_handler
==============================

.. c:function:: irqreturn_t iio_simple_dummy_event_handler(int irq, void *private)

    identify and pass on event

    :param int irq:
        irq of event line

    :param void \*private:
        pointer to device instance state.

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

    :param struct iio_dev \*indio_dev:
        device instance data

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

    :param struct iio_dev \*indio_dev:
        device instance data

.. This file was automatic generated / don't edit.

