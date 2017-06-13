.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/ir-nec-decoder.c

.. _`ir_nec_decode`:

ir_nec_decode
=============

.. c:function:: int ir_nec_decode(struct rc_dev *dev, struct ir_raw_event ev)

    Decode one NEC pulse or space

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:
        *undescribed*

.. _`ir_nec_decode.description`:

Description
-----------

This function returns -EINVAL if the pulse violates the state machine

.. _`ir_nec_scancode_to_raw`:

ir_nec_scancode_to_raw
======================

.. c:function:: u32 ir_nec_scancode_to_raw(enum rc_type protocol, u32 scancode)

    encode an NEC scancode ready for modulation.

    :param enum rc_type protocol:
        specific protocol to use

    :param u32 scancode:
        a single NEC scancode.

.. _`ir_nec_encode`:

ir_nec_encode
=============

.. c:function:: int ir_nec_encode(enum rc_type protocol, u32 scancode, struct ir_raw_event *events, unsigned int max)

    Encode a scancode as a stream of raw events

    :param enum rc_type protocol:
        protocol to encode

    :param u32 scancode:
        scancode to encode

    :param struct ir_raw_event \*events:
        array of raw ir events to write into

    :param unsigned int max:
        maximum size of \ ``events``\ 

.. _`ir_nec_encode.return`:

Return
------

The number of events written.
-ENOBUFS if there isn't enough space in the array to fit the
encoding. In this case all \ ``max``\  events will have been written.

.. This file was automatic generated / don't edit.

