.. -*- coding: utf-8; mode: rst -*-

================
ir-rc6-decoder.c
================



.. _xref_ir_rc6_decode:

ir_rc6_decode
=============

.. c:function:: int ir_rc6_decode (struct rc_dev * dev, struct ir_raw_event ev)

    Decode one RC6 pulse or space

    :param struct rc_dev * dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:
        the struct ir_raw_event descriptor of the pulse/space



Description
-----------

This function returns -EINVAL if the pulse violates the state machine


