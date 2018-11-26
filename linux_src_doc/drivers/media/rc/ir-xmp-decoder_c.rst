.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/ir-xmp-decoder.c

.. _`ir_xmp_decode`:

ir_xmp_decode
=============

.. c:function:: int ir_xmp_decode(struct rc_dev *dev, struct ir_raw_event ev)

    Decode one XMP pulse or space

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

    :param ev:
        the struct ir_raw_event descriptor of the pulse/space
    :type ev: struct ir_raw_event

.. _`ir_xmp_decode.description`:

Description
-----------

This function returns -EINVAL if the pulse violates the state machine

.. This file was automatic generated / don't edit.

