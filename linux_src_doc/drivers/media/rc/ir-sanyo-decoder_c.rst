.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/ir-sanyo-decoder.c

.. _`ir_sanyo_decode`:

ir_sanyo_decode
===============

.. c:function:: int ir_sanyo_decode(struct rc_dev *dev, struct ir_raw_event ev)

    Decode one SANYO pulse or space

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:
        *undescribed*

.. _`ir_sanyo_decode.description`:

Description
-----------

This function returns -EINVAL if the pulse violates the state machine

.. _`ir_sanyo_encode`:

ir_sanyo_encode
===============

.. c:function:: int ir_sanyo_encode(enum rc_proto protocol, u32 scancode, struct ir_raw_event *events, unsigned int max)

    Encode a scancode as a stream of raw events

    :param enum rc_proto protocol:
        protocol to encode

    :param u32 scancode:
        scancode to encode

    :param struct ir_raw_event \*events:
        array of raw ir events to write into

    :param unsigned int max:
        maximum size of \ ``events``\ 

.. _`ir_sanyo_encode.return`:

Return
------

The number of events written.
-ENOBUFS if there isn't enough space in the array to fit the
encoding. In this case all \ ``max``\  events will have been written.

.. This file was automatic generated / don't edit.

