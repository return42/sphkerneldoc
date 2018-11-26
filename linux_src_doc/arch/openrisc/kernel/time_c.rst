.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/openrisc/kernel/time.c

.. _`openrisc_timer_read`:

openrisc_timer_read
===================

.. c:function:: u64 openrisc_timer_read(struct clocksource *cs)

    Based on OpenRISC timer/counter

    :param cs:
        *undescribed*
    :type cs: struct clocksource \*

.. _`openrisc_timer_read.description`:

Description
-----------

This sets up the OpenRISC Tick Timer as a clock source.  The tick timer
is 32 bits wide and runs at the CPU clock frequency.

.. This file was automatic generated / don't edit.

