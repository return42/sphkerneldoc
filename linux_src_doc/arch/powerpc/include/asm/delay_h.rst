.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/delay.h

.. _`spin_event_timeout`:

spin_event_timeout
==================

.. c:function::  spin_event_timeout( condition,  timeout,  delay)

    spin until a condition gets true or a timeout elapses

    :param  condition:
        a C expression to evalate

    :param  timeout:
        timeout, in microseconds

    :param  delay:
        the number of microseconds to delay between each evaluation of
        \ ``condition``\ 

.. _`spin_event_timeout.description`:

Description
-----------

The process spins until the condition evaluates to true (non-zero) or the
timeout elapses.  The return value of this macro is the value of
\ ``condition``\  when the loop terminates. This allows you to determine the cause
of the loop terminates.  If the return value is zero, then you know a
timeout has occurred.

This primary purpose of this macro is to poll on a hardware register
until a status bit changes.  The timeout ensures that the loop still
terminates even if the bit never changes.  The delay is for devices that
need a delay in between successive reads.

gcc will optimize out the if-statement if \ ``delay``\  is a constant.

.. This file was automatic generated / don't edit.

