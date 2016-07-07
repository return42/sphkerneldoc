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

.. This file was automatic generated / don't edit.

