.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/arm_arch_timer.c

.. _`arch_timer_select_ppi`:

arch_timer_select_ppi
=====================

.. c:function:: enum arch_timer_ppi_nr arch_timer_select_ppi( void)

    Select suitable PPI for the current system.

    :param  void:
        no arguments

.. _`arch_timer_select_ppi.description`:

Description
-----------

If HYP mode is available, we know that the physical timer
has been configured to be accessible from PL1. Use it, so
that a guest can use the virtual timer instead.

On ARMv8.1 with VH extensions, the kernel runs in HYP. VHE
accesses to CNTP\_\*\_EL1 registers are silently redirected to
their CNTHP\_\*\_EL2 counterparts, and use a different PPI
number.

If no interrupt provided for virtual timer, we'll have to
stick to the physical timer. It'd better be accessible...
For arm64 we never use the secure interrupt.

.. _`arch_timer_select_ppi.return`:

Return
------

a suitable PPI type for the current system.

.. This file was automatic generated / don't edit.

