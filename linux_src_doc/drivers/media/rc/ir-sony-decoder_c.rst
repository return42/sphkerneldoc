.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/ir-sony-decoder.c

.. _`ir_sony_decode`:

ir_sony_decode
==============

.. c:function:: int ir_sony_decode(struct rc_dev *dev, struct ir_raw_event ev)

    Decode one Sony pulse or space

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

    :param ev:
        the struct ir_raw_event descriptor of the pulse/space
    :type ev: struct ir_raw_event

.. _`ir_sony_decode.description`:

Description
-----------

This function returns -EINVAL if the pulse violates the state machine

.. _`ir_sony_encode`:

ir_sony_encode
==============

.. c:function:: int ir_sony_encode(enum rc_proto protocol, u32 scancode, struct ir_raw_event *events, unsigned int max)

    Encode a scancode as a stream of raw events

    :param protocol:
        protocol to encode
    :type protocol: enum rc_proto

    :param scancode:
        scancode to encode
    :type scancode: u32

    :param events:
        array of raw ir events to write into
    :type events: struct ir_raw_event \*

    :param max:
        maximum size of \ ``events``\ 
    :type max: unsigned int

.. _`ir_sony_encode.return`:

Return
------

The number of events written.
-ENOBUFS if there isn't enough space in the array to fit the
encoding. In this case all \ ``max``\  events will have been written.

.. This file was automatic generated / don't edit.

