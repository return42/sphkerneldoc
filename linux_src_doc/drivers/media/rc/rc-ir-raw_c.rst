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

.. c:function:: int ir_raw_event_store_edge(struct rc_dev *dev, bool pulse)

    notify raw ir decoders of the start of a pulse/space

    :param struct rc_dev \*dev:
        the struct rc_dev device descriptor

    :param bool pulse:
        true for pulse, false for space

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

.. _`ir_raw_gen_manchester`:

ir_raw_gen_manchester
=====================

.. c:function:: int ir_raw_gen_manchester(struct ir_raw_event **ev, unsigned int max, const struct ir_raw_timings_manchester *timings, unsigned int n, u64 data)

    Encode data with Manchester (bi-phase) modulation.

    :param struct ir_raw_event \*\*ev:
        Pointer to pointer to next free event. \*@ev is incremented for
        each raw event filled.

    :param unsigned int max:
        Maximum number of raw events to fill.

    :param const struct ir_raw_timings_manchester \*timings:
        Manchester modulation timings.

    :param unsigned int n:
        Number of bits of data.

    :param u64 data:
        Data bits to encode.

.. _`ir_raw_gen_manchester.description`:

Description
-----------

Encodes the \ ``n``\  least significant bits of \ ``data``\  using Manchester (bi-phase)
modulation with the timing characteristics described by \ ``timings``\ , writing up
to \ ``max``\  raw IR events using the \*@ev pointer.

.. _`ir_raw_gen_manchester.return`:

Return
------

0 on success.
-ENOBUFS if there isn't enough space in the array to fit the
full encoded data. In this case all \ ``max``\  events will have been
written.

.. _`ir_raw_gen_pd`:

ir_raw_gen_pd
=============

.. c:function:: int ir_raw_gen_pd(struct ir_raw_event **ev, unsigned int max, const struct ir_raw_timings_pd *timings, unsigned int n, u64 data)

    Encode data to raw events with pulse-distance modulation.

    :param struct ir_raw_event \*\*ev:
        Pointer to pointer to next free event. \*@ev is incremented for
        each raw event filled.

    :param unsigned int max:
        Maximum number of raw events to fill.

    :param const struct ir_raw_timings_pd \*timings:
        Pulse distance modulation timings.

    :param unsigned int n:
        Number of bits of data.

    :param u64 data:
        Data bits to encode.

.. _`ir_raw_gen_pd.description`:

Description
-----------

Encodes the \ ``n``\  least significant bits of \ ``data``\  using pulse-distance
modulation with the timing characteristics described by \ ``timings``\ , writing up
to \ ``max``\  raw IR events using the \*@ev pointer.

.. _`ir_raw_gen_pd.return`:

Return
------

0 on success.
-ENOBUFS if there isn't enough space in the array to fit the
full encoded data. In this case all \ ``max``\  events will have been
written.

.. _`ir_raw_gen_pl`:

ir_raw_gen_pl
=============

.. c:function:: int ir_raw_gen_pl(struct ir_raw_event **ev, unsigned int max, const struct ir_raw_timings_pl *timings, unsigned int n, u64 data)

    Encode data to raw events with pulse-length modulation.

    :param struct ir_raw_event \*\*ev:
        Pointer to pointer to next free event. \*@ev is incremented for
        each raw event filled.

    :param unsigned int max:
        Maximum number of raw events to fill.

    :param const struct ir_raw_timings_pl \*timings:
        Pulse distance modulation timings.

    :param unsigned int n:
        Number of bits of data.

    :param u64 data:
        Data bits to encode.

.. _`ir_raw_gen_pl.description`:

Description
-----------

Encodes the \ ``n``\  least significant bits of \ ``data``\  using space-distance
modulation with the timing characteristics described by \ ``timings``\ , writing up
to \ ``max``\  raw IR events using the \*@ev pointer.

.. _`ir_raw_gen_pl.return`:

Return
------

0 on success.
-ENOBUFS if there isn't enough space in the array to fit the
full encoded data. In this case all \ ``max``\  events will have been
written.

.. _`ir_raw_encode_scancode`:

ir_raw_encode_scancode
======================

.. c:function:: int ir_raw_encode_scancode(enum rc_proto protocol, u32 scancode, struct ir_raw_event *events, unsigned int max)

    Encode a scancode as raw events

    :param enum rc_proto protocol:
        protocol

    :param u32 scancode:
        scancode filter describing a single scancode

    :param struct ir_raw_event \*events:
        array of raw events to write into

    :param unsigned int max:
        max number of raw events

.. _`ir_raw_encode_scancode.description`:

Description
-----------

Attempts to encode the scancode as raw events.

.. _`ir_raw_encode_scancode.return`:

Return
------

The number of events written.
-ENOBUFS if there isn't enough space in the array to fit the
encoding. In this case all \ ``max``\  events will have been written.
-EINVAL if the scancode is ambiguous or invalid, or if no
compatible encoder was found.

.. This file was automatic generated / don't edit.

