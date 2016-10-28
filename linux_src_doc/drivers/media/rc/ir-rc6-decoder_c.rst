.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/ir-rc6-decoder.c

.. _`ir_rc6_decode`:

ir_rc6_decode
=============

.. c:function:: int ir_rc6_decode(struct rc_dev *dev, struct ir_raw_event ev)

    Decode one RC6 pulse or space

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:
        the struct ir_raw_event descriptor of the pulse/space

.. _`ir_rc6_decode.description`:

Description
-----------

This function returns -EINVAL if the pulse violates the state machine

.. This file was automatic generated / don't edit.

