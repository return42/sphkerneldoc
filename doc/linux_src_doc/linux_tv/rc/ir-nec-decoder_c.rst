.. -*- coding: utf-8; mode: rst -*-

================
ir-nec-decoder.c
================



.. _xref_ir_nec_decode:

ir_nec_decode
=============

.. c:function:: int ir_nec_decode (struct rc_dev * dev, struct ir_raw_event ev)

    Decode one NEC pulse or space

    :param struct rc_dev * dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:

        _undescribed_



Description
-----------

This function returns -EINVAL if the pulse violates the state machine


