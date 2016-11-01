.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/prcm-common.h

.. _`omap_test_timeout`:

omap_test_timeout
=================

.. c:function::  omap_test_timeout( cond,  timeout,  index)

    busy-loop, testing a condition

    :param  cond:
        condition to test until it evaluates to true

    :param  timeout:
        maximum number of microseconds in the timeout

    :param  index:
        loop index (integer)

.. _`omap_test_timeout.description`:

Description
-----------

Loop waiting for \ ``cond``\  to become true or until at least \ ``timeout``\ 
microseconds have passed.  To use, define some integer \ ``index``\  in the
calling code.  After running, if \ ``index``\  == \ ``timeout``\ , then the loop has
timed out.

.. _`omap_prcm_irq`:

struct omap_prcm_irq
====================

.. c:type:: struct omap_prcm_irq

    describes a PRCM interrupt bit

.. _`omap_prcm_irq.definition`:

Definition
----------

.. code-block:: c

    struct omap_prcm_irq {
        const char *name;
        unsigned int offset;
        bool priority;
    }

.. _`omap_prcm_irq.members`:

Members
-------

name
    a short name describing the interrupt type, e.g. "wkup" or "io"

offset
    the bit shift of the interrupt inside the IRQ{ENABLE,STATUS} regs

priority
    should this interrupt be handled before \ ``priority``\ =false IRQs?

.. _`omap_prcm_irq.description`:

Description
-----------

Describes interrupt bits inside the PRM_IRQ{ENABLE,STATUS}_MPU\* registers.
On systems with multiple PRM MPU IRQ registers, the bitfields read from
the registers are concatenated, so \ ``offset``\  could be > 31 on these systems -
see \ :c:func:`omap_prm_irq_handler`\  for more details.  I/O ring interrupts should
have \ ``priority``\  set to true.

.. _`omap_prcm_irq_setup`:

struct omap_prcm_irq_setup
==========================

.. c:type:: struct omap_prcm_irq_setup

    PRCM interrupt controller details

.. _`omap_prcm_irq_setup.definition`:

Definition
----------

.. code-block:: c

    struct omap_prcm_irq_setup {
        u16 ack;
        u16 mask;
        u16 pm_ctrl;
        u8 nr_regs;
        u8 nr_irqs;
        const struct omap_prcm_irq *irqs;
        int irq;
        unsigned int (*xlate_irq)(unsigned int);
        void (*read_pending_irqs)(unsigned long *events);
        void (*ocp_barrier)(void);
        void (*save_and_clear_irqen)(u32 *saved_mask);
        void (*restore_irqen)(u32 *saved_mask);
        void (*reconfigure_io_chain)(void);
        u32 *saved_mask;
        u32 *priority_mask;
        int base_irq;
        bool suspended;
        bool suspend_save_flag;
    }

.. _`omap_prcm_irq_setup.members`:

Members
-------

ack
    PRM register offset for the first PRM_IRQSTATUS_MPU register

mask
    PRM register offset for the first PRM_IRQENABLE_MPU register

pm_ctrl
    PRM register offset for the PRM_IO_PMCTRL register

nr_regs
    number of PRM_IRQ{STATUS,ENABLE}_MPU\* registers

nr_irqs
    number of entries in the \ ``irqs``\  array

irqs
    ptr to an array of PRCM interrupt bits (see \ ``nr_irqs``\ )

irq
    MPU IRQ asserted when a PRCM interrupt arrives

xlate_irq
    *undescribed*

read_pending_irqs
    fn ptr to determine if any PRCM IRQs are pending

ocp_barrier
    fn ptr to force buffered PRM writes to complete

save_and_clear_irqen
    fn ptr to save and clear IRQENABLE regs

restore_irqen
    fn ptr to save and clear IRQENABLE regs

reconfigure_io_chain
    fn ptr to reconfigure IO chain

saved_mask
    IRQENABLE regs are saved here during suspend

priority_mask
    1 bit per IRQ, set to 1 if omap_prcm_irq.priority = true

base_irq
    base dynamic IRQ number, returned from \ :c:func:`irq_alloc_descs`\  in init

suspended
    set to true after Linux suspend code has called our ->prepare()

suspend_save_flag
    set to true after IRQ masks have been saved and disabled

.. _`omap_prcm_irq_setup.description`:

Description
-----------

@saved_mask, \ ``priority_mask``\ , \ ``base_irq``\ , \ ``suspended``\ , and
\ ``suspend_save_flag``\  are populated dynamically, and are not to be
specified in static initializers.

.. _`omap_prcm_init_data`:

struct omap_prcm_init_data
==========================

.. c:type:: struct omap_prcm_init_data

    PRCM driver init data

.. _`omap_prcm_init_data.definition`:

Definition
----------

.. code-block:: c

    struct omap_prcm_init_data {
        int index;
        void __iomem *mem;
        s16 offset;
        u16 flags;
        s32 device_inst_offset;
        int (*init)(const struct omap_prcm_init_data *data);
        struct device_node *np;
    }

.. _`omap_prcm_init_data.members`:

Members
-------

index
    clock memory mapping index to be used

mem
    IO mem pointer for this module

offset
    module base address offset from the IO base

flags
    PRCM module init flags

device_inst_offset
    device instance offset within the module address space

init
    low level PRCM init function for this module

np
    device node for this PRCM module

.. This file was automatic generated / don't edit.

