.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/kernel/time.c

.. _`local_timer_interrupt`:

local_timer_interrupt
=====================

.. c:function:: irqreturn_t local_timer_interrupt( void)

    Local timer interrupt handler

    :param  void:
        no arguments

.. _`local_timer_interrupt.description`:

Description
-----------

Handle local timer interrupts for this CPU.  They may have been propagated
to this CPU from the CPU that actually gets them by way of an IPI.

.. This file was automatic generated / don't edit.

