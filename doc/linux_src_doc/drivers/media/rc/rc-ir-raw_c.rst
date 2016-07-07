.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/rc-ir-raw.c

.. _`ir_raw_event_store`:

ir_raw_event_store
==================

.. c:function:: int ir_raw_event_store(struct rc_dev *dev, struct ir_raw_event *ev)

    pass a pulse/space duration to the raw ir decoders

    :param struct rc_dev \*dev:
        the struct rc_dev device descriptor

    :param struct ir_raw_event \*ev:
        the struct ir_raw_event descriptor of the pulse/space

.. _`ir_raw_event_store.description`:

Description
-----------

This routine (which may be called from an interrupt context) stores a
pulse/space duration for the raw ir decoding state machines. Pulses are
signalled as positive values and spaces as negative values. A zero value
will reset the decoding state machines.

.. _`ir_raw_event_store_edge`:

ir_raw_event_store_edge
=======================

.. c:function:: int ir_raw_event_store_edge(struct rc_dev *dev, enum raw_event_type type)

    notify raw ir decoders of the start of a pulse/space

    :param struct rc_dev \*dev:
        the struct rc_dev device descriptor

    :param enum raw_event_type type:
        the type of the event that has occurred

.. _`ir_raw_event_store_edge.description`:

Description
-----------

This routine (which may be called from an interrupt context) is used to
store the beginning of an ir pulse or space (or the start/end of ir
reception) for the raw ir decoding state machines. This is used by
hardware which does not provide durations directly but only interrupts
(or similar events) on state change.

.. _`ir_raw_event_store_with_filter`:

ir_raw_event_store_with_filter
==============================

.. c:function:: int ir_raw_event_store_with_filter(struct rc_dev *dev, struct ir_raw_event *ev)

    pass next pulse/space to decoders with some processing

    :param struct rc_dev \*dev:
        the struct rc_dev device descriptor

    :param struct ir_raw_event \*ev:
        *undescribed*

.. _`ir_raw_event_store_with_filter.description`:

Description
-----------

This routine (which may be called from an interrupt context) works
in similar manner to ir_raw_event_store_edge.
This routine is intended for devices with limited internal buffer
It automerges samples of same type, and handles timeouts. Returns non-zero
if the event was added, and zero if the event was ignored due to idle
processing.

.. _`ir_raw_event_set_idle`:

ir_raw_event_set_idle
=====================

.. c:function:: void ir_raw_event_set_idle(struct rc_dev *dev, bool idle)

    provide hint to rc-core when the device is idle or not

    :param struct rc_dev \*dev:
        the struct rc_dev device descriptor

    :param bool idle:
        whether the device is idle or not

.. _`ir_raw_event_handle`:

ir_raw_event_handle
===================

.. c:function:: void ir_raw_event_handle(struct rc_dev *dev)

    schedules the decoding of stored ir data

    :param struct rc_dev \*dev:
        the struct rc_dev device descriptor

.. _`ir_raw_event_handle.description`:

Description
-----------

This routine will tell rc-core to start decoding stored ir data.

.. This file was automatic generated / don't edit.

