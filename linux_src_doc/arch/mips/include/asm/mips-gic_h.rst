.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/mips-gic.h

.. _`mips_gic_local_interrupt`:

enum mips_gic_local_interrupt
=============================

.. c:type:: enum mips_gic_local_interrupt

    GIC local interrupts

.. _`mips_gic_local_interrupt.definition`:

Definition
----------

.. code-block:: c

    enum mips_gic_local_interrupt {
        GIC_LOCAL_INT_WD,
        GIC_LOCAL_INT_COMPARE,
        GIC_LOCAL_INT_TIMER,
        GIC_LOCAL_INT_PERFCTR,
        GIC_LOCAL_INT_SWINT0,
        GIC_LOCAL_INT_SWINT1,
        GIC_LOCAL_INT_FDC,
        GIC_NUM_LOCAL_INTRS
    };

.. _`mips_gic_local_interrupt.constants`:

Constants
---------

GIC_LOCAL_INT_WD
    GIC watchdog timer interrupt

GIC_LOCAL_INT_COMPARE
    GIC count/compare interrupt

GIC_LOCAL_INT_TIMER
    CP0 count/compare interrupt

GIC_LOCAL_INT_PERFCTR
    Performance counter interrupt

GIC_LOCAL_INT_SWINT0
    Software interrupt 0

GIC_LOCAL_INT_SWINT1
    Software interrupt 1

GIC_LOCAL_INT_FDC
    Fast debug channel interrupt

GIC_NUM_LOCAL_INTRS
    The number of local interrupts

.. _`mips_gic_local_interrupt.description`:

Description
-----------

Enumerates interrupts provided by the GIC that are local to a VP.

.. _`mips_gic_present`:

mips_gic_present
================

.. c:function:: bool mips_gic_present( void)

    Determine whether a GIC is present

    :param void:
        no arguments
    :type void: 

.. _`mips_gic_present.description`:

Description
-----------

Determines whether a MIPS Global Interrupt Controller (GIC) is present in
the system that the kernel is running on.

Return true if a GIC is present, else false.

.. _`gic_get_c0_compare_int`:

gic_get_c0_compare_int
======================

.. c:function:: int gic_get_c0_compare_int( void)

    Return cp0 count/compare interrupt virq

    :param void:
        no arguments
    :type void: 

.. _`gic_get_c0_compare_int.description`:

Description
-----------

Determine the virq number to use for the coprocessor 0 count/compare
interrupt, which may be routed via the GIC.

Returns the virq number or a negative error number.

.. _`gic_get_c0_perfcount_int`:

gic_get_c0_perfcount_int
========================

.. c:function:: int gic_get_c0_perfcount_int( void)

    Return performance counter interrupt virq

    :param void:
        no arguments
    :type void: 

.. _`gic_get_c0_perfcount_int.description`:

Description
-----------

Determine the virq number to use for CPU performance counter interrupts,
which may be routed via the GIC.

Returns the virq number or a negative error number.

.. _`gic_get_c0_fdc_int`:

gic_get_c0_fdc_int
==================

.. c:function:: int gic_get_c0_fdc_int( void)

    Return fast debug channel interrupt virq

    :param void:
        no arguments
    :type void: 

.. _`gic_get_c0_fdc_int.description`:

Description
-----------

Determine the virq number to use for fast debug channel (FDC) interrupts,
which may be routed via the GIC.

Returns the virq number or a negative error number.

.. This file was automatic generated / don't edit.

