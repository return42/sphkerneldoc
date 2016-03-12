.. -*- coding: utf-8; mode: rst -*-

================
ir-jvc-decoder.c
================



.. _xref_ir_jvc_decode:

ir_jvc_decode
=============

.. c:function:: int ir_jvc_decode (struct rc_dev * dev, struct ir_raw_event ev)

    Decode one JVC pulse or space

    :param struct rc_dev * dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:

        _undescribed_



Description
-----------

This function returns -EINVAL if the pulse violates the state machine


