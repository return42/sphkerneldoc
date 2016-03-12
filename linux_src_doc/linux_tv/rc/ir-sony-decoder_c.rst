.. -*- coding: utf-8; mode: rst -*-

=================
ir-sony-decoder.c
=================



.. _xref_ir_sony_decode:

ir_sony_decode
==============

.. c:function:: int ir_sony_decode (struct rc_dev * dev, struct ir_raw_event ev)

    Decode one Sony pulse or space

    :param struct rc_dev * dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:
        the struct ir_raw_event descriptor of the pulse/space



Description
-----------

This function returns -EINVAL if the pulse violates the state machine


