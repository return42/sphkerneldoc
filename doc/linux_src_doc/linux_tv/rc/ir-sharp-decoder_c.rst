.. -*- coding: utf-8; mode: rst -*-

==================
ir-sharp-decoder.c
==================



.. _xref_ir_sharp_decode:

ir_sharp_decode
===============

.. c:function:: int ir_sharp_decode (struct rc_dev * dev, struct ir_raw_event ev)

    Decode one Sharp pulse or space

    :param struct rc_dev * dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:

        _undescribed_



Description
-----------

This function returns -EINVAL if the pulse violates the state machine


