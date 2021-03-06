.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/rc-ir-raw.c

.. _`ir_raw_event_store`:

ir_raw_event_store
==================

.. c:function:: int ir_raw_event_store(struct rc_dev *dev, struct ir_raw_event *ev)

    pass a pulse/space duration to the raw ir decoders

    :param dev:
        the struct rc_dev device descriptor
    :type dev: struct rc_dev \*

    :param ev:
        the struct ir_raw_event descriptor of the pulse/space
    :type ev: struct ir_raw_event \*

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

    :param dev:
        the struct rc_dev device descriptor
    :type dev: struct rc_dev \*

    :param pulse:
        true for pulse, false for space
    :type pulse: bool

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

    :param dev:
        the struct rc_dev device descriptor
    :type dev: struct rc_dev \*

    :param ev:
        the event that has occurred
    :type ev: struct ir_raw_event \*

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

    :param dev:
        the struct rc_dev device descriptor
    :type dev: struct rc_dev \*

    :param idle:
        whether the device is idle or not
    :type idle: bool

.. _`ir_raw_event_handle`:

ir_raw_event_handle
===================

.. c:function:: void ir_raw_event_handle(struct rc_dev *dev)

    schedules the decoding of stored ir data

    :param dev:
        the struct rc_dev device descriptor
    :type dev: struct rc_dev \*

.. _`ir_raw_event_handle.description`:

Description
-----------

This routine will tell rc-core to start decoding stored ir data.

.. _`ir_raw_gen_manchester`:

ir_raw_gen_manchester
=====================

.. c:function:: int ir_raw_gen_manchester(struct ir_raw_event **ev, unsigned int max, const struct ir_raw_timings_manchester *timings, unsigned int n, u64 data)

    Encode data with Manchester (bi-phase) modulation.

    :param ev:
        Pointer to pointer to next free event. \*@ev is incremented for
        each raw event filled.
    :type ev: struct ir_raw_event \*\*

    :param max:
        Maximum number of raw events to fill.
    :type max: unsigned int

    :param timings:
        Manchester modulation timings.
    :type timings: const struct ir_raw_timings_manchester \*

    :param n:
        Number of bits of data.
    :type n: unsigned int

    :param data:
        Data bits to encode.
    :type data: u64

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

    :param ev:
        Pointer to pointer to next free event. \*@ev is incremented for
        each raw event filled.
    :type ev: struct ir_raw_event \*\*

    :param max:
        Maximum number of raw events to fill.
    :type max: unsigned int

    :param timings:
        Pulse distance modulation timings.
    :type timings: const struct ir_raw_timings_pd \*

    :param n:
        Number of bits of data.
    :type n: unsigned int

    :param data:
        Data bits to encode.
    :type data: u64

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

    :param ev:
        Pointer to pointer to next free event. \*@ev is incremented for
        each raw event filled.
    :type ev: struct ir_raw_event \*\*

    :param max:
        Maximum number of raw events to fill.
    :type max: unsigned int

    :param timings:
        Pulse distance modulation timings.
    :type timings: const struct ir_raw_timings_pl \*

    :param n:
        Number of bits of data.
    :type n: unsigned int

    :param data:
        Data bits to encode.
    :type data: u64

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

    :param protocol:
        protocol
    :type protocol: enum rc_proto

    :param scancode:
        scancode filter describing a single scancode
    :type scancode: u32

    :param events:
        array of raw events to write into
    :type events: struct ir_raw_event \*

    :param max:
        max number of raw events
    :type max: unsigned int

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

.. _`ir_raw_edge_handle`:

ir_raw_edge_handle
==================

.. c:function:: void ir_raw_edge_handle(struct timer_list *t)

    Handle \ :c:func:`ir_raw_event_store_edge`\  processing

    :param t:
        timer_list
    :type t: struct timer_list \*

.. _`ir_raw_edge_handle.description`:

Description
-----------

This callback is armed by \ :c:func:`ir_raw_event_store_edge`\ . It does two things:
first of all, rather than calling \ :c:func:`ir_raw_event_handle`\  for each
edge and waking up the rc thread, 15 ms after the first edge
\ :c:func:`ir_raw_event_handle`\  is called. Secondly, generate a timeout event
no more IR is received after the rc_dev timeout.

.. _`ir_raw_encode_carrier`:

ir_raw_encode_carrier
=====================

.. c:function:: int ir_raw_encode_carrier(enum rc_proto protocol)

    Get carrier used for protocol

    :param protocol:
        protocol
    :type protocol: enum rc_proto

.. _`ir_raw_encode_carrier.description`:

Description
-----------

Attempts to find the carrier for the specified protocol

.. _`ir_raw_encode_carrier.return`:

Return
------

The carrier in Hz
-EINVAL if the protocol is invalid, or if no
compatible encoder was found.

.. This file was automatic generated / don't edit.

