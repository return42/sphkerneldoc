.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/ir-rc5-decoder.c

.. _`ir_rc5_decode`:

ir_rc5_decode
=============

.. c:function:: int ir_rc5_decode(struct rc_dev *dev, struct ir_raw_event ev)

    Decode one RC-5 pulse or space

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:
        the struct ir_raw_event descriptor of the pulse/space

.. _`ir_rc5_decode.description`:

Description
-----------

This function returns -EINVAL if the pulse violates the state machine

.. _`ir_rc5_encode`:

ir_rc5_encode
=============

.. c:function:: int ir_rc5_encode(enum rc_proto protocol, u32 scancode, struct ir_raw_event *events, unsigned int max)

    Encode a scancode as a stream of raw events

    :param enum rc_proto protocol:
        protocol variant to encode

    :param u32 scancode:
        scancode to encode

    :param struct ir_raw_event \*events:
        array of raw ir events to write into

    :param unsigned int max:
        maximum size of \ ``events``\ 

.. _`ir_rc5_encode.return`:

Return
------

The number of events written.
-ENOBUFS if there isn't enough space in the array to fit the
encoding. In this case all \ ``max``\  events will have been written.
-EINVAL if the scancode is ambiguous or invalid.

.. This file was automatic generated / don't edit.

