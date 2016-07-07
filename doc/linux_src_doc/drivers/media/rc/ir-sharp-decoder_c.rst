.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/ir-sharp-decoder.c

.. _`ir_sharp_decode`:

ir_sharp_decode
===============

.. c:function:: int ir_sharp_decode(struct rc_dev *dev, struct ir_raw_event ev)

    Decode one Sharp pulse or space

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:
        *undescribed*

.. _`ir_sharp_decode.description`:

Description
-----------

This function returns -EINVAL if the pulse violates the state machine

.. This file was automatic generated / don't edit.

