.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/irq-metag-ext.c

.. _`meta_intc_priv`:

struct meta_intc_priv
=====================

.. c:type:: struct meta_intc_priv

    private meta external interrupt data

.. _`meta_intc_priv.definition`:

Definition
----------

.. code-block:: c

    struct meta_intc_priv {
        unsigned int nr_banks;
        struct irq_domain *domain;
        unsigned long unmasked[4];
    #ifdef CONFIG_METAG_SUSPEND_MEM
        unsigned long levels_altered[4];
    #endif
    }

.. _`meta_intc_priv.members`:

Members
-------

nr_banks
    Number of interrupt banks

domain
    IRQ domain for all banks of external IRQs

unmasked
    Record of unmasked IRQs

levels_altered
    Record of altered level bits

.. _`meta_intc_offset`:

meta_intc_offset
================

.. c:function:: unsigned int meta_intc_offset(irq_hw_number_t hw)

    Get the offset into the bank of a hardware IRQ number

    :param irq_hw_number_t hw:
        Hardware IRQ number (within external trigger block)

.. _`meta_intc_offset.return`:

Return
------

Bit offset into the IRQ's bank registers

.. _`meta_intc_bank`:

meta_intc_bank
==============

.. c:function:: unsigned int meta_intc_bank(irq_hw_number_t hw)

    Get the bank number of a hardware IRQ number

    :param irq_hw_number_t hw:
        Hardware IRQ number (within external trigger block)

.. _`meta_intc_bank.return`:

Return
------

Bank number indicating which register the IRQ's bits are

.. _`meta_intc_stat_addr`:

meta_intc_stat_addr
===================

.. c:function:: void __iomem *meta_intc_stat_addr(irq_hw_number_t hw)

    Get the address of a HWSTATEXT register

    :param irq_hw_number_t hw:
        Hardware IRQ number (within external trigger block)

.. _`meta_intc_stat_addr.return`:

Return
------

Address of a HWSTATEXT register containing the status bit for
the specified hardware IRQ number

.. _`meta_intc_level_addr`:

meta_intc_level_addr
====================

.. c:function:: void __iomem *meta_intc_level_addr(irq_hw_number_t hw)

    Get the address of a HWLEVELEXT register

    :param irq_hw_number_t hw:
        Hardware IRQ number (within external trigger block)

.. _`meta_intc_level_addr.return`:

Return
------

Address of a HWLEVELEXT register containing the sense bit for
the specified hardware IRQ number

.. _`meta_intc_mask_addr`:

meta_intc_mask_addr
===================

.. c:function:: void __iomem *meta_intc_mask_addr(irq_hw_number_t hw)

    Get the address of a HWMASKEXT register

    :param irq_hw_number_t hw:
        Hardware IRQ number (within external trigger block)

.. _`meta_intc_mask_addr.return`:

Return
------

Address of a HWMASKEXT register containing the mask bit for the
specified hardware IRQ number

.. _`meta_intc_vec_addr`:

meta_intc_vec_addr
==================

.. c:function:: void __iomem *meta_intc_vec_addr(irq_hw_number_t hw)

    Get the vector address of a hardware interrupt

    :param irq_hw_number_t hw:
        Hardware IRQ number (within external trigger block)

.. _`meta_intc_vec_addr.return`:

Return
------

Address of a HWVECEXT register controlling the core trigger to
vector the IRQ onto

.. _`meta_intc_startup_irq`:

meta_intc_startup_irq
=====================

.. c:function:: unsigned int meta_intc_startup_irq(struct irq_data *data)

    set up an external irq

    :param struct irq_data \*data:
        data for the external irq to start up

.. _`meta_intc_startup_irq.description`:

Description
-----------

Multiplex interrupts for irq onto TR2. Clear any pending interrupts and
unmask irq, both using the appropriate callbacks.

.. _`meta_intc_shutdown_irq`:

meta_intc_shutdown_irq
======================

.. c:function:: void meta_intc_shutdown_irq(struct irq_data *data)

    turn off an external irq

    :param struct irq_data \*data:
        data for the external irq to turn off

.. _`meta_intc_shutdown_irq.description`:

Description
-----------

Mask irq using the appropriate callback and stop muxing it onto TR2.

.. _`meta_intc_ack_irq`:

meta_intc_ack_irq
=================

.. c:function:: void meta_intc_ack_irq(struct irq_data *data)

    acknowledge an external irq

    :param struct irq_data \*data:
        data for the external irq to ack

.. _`meta_intc_ack_irq.description`:

Description
-----------

Clear down an edge interrupt in the status register.

.. _`record_irq_is_masked`:

record_irq_is_masked
====================

.. c:function:: void record_irq_is_masked(struct irq_data *data)

    record the IRQ masked so it doesn't get handled

    :param struct irq_data \*data:
        data for the external irq to record

.. _`record_irq_is_masked.description`:

Description
-----------

This should get called whenever an external IRQ is masked (by whichever
callback is used). It records the IRQ masked so that it doesn't get handled
if it still shows up in the status register.

.. _`record_irq_is_unmasked`:

record_irq_is_unmasked
======================

.. c:function:: void record_irq_is_unmasked(struct irq_data *data)

    record the IRQ unmasked so it can be handled

    :param struct irq_data \*data:
        data for the external irq to record

.. _`record_irq_is_unmasked.description`:

Description
-----------

This should get called whenever an external IRQ is unmasked (by whichever
callback is used). It records the IRQ unmasked so that it gets handled if it
shows up in the status register.

.. _`meta_intc_mask_irq_simple`:

meta_intc_mask_irq_simple
=========================

.. c:function:: void meta_intc_mask_irq_simple(struct irq_data *data)

    minimal mask used by wrapper IRQ drivers

    :param struct irq_data \*data:
        data for the external irq being masked

.. _`meta_intc_mask_irq_simple.description`:

Description
-----------

This should be called by any wrapper IRQ driver mask functions. it doesn't do
any masking but records the IRQ as masked so that the core code knows the
mask has taken place. It is the callers responsibility to ensure that the IRQ
won't trigger an interrupt to the core.

.. _`meta_intc_unmask_irq_simple`:

meta_intc_unmask_irq_simple
===========================

.. c:function:: void meta_intc_unmask_irq_simple(struct irq_data *data)

    minimal unmask used by wrapper IRQ drivers

    :param struct irq_data \*data:
        data for the external irq being unmasked

.. _`meta_intc_unmask_irq_simple.description`:

Description
-----------

This should be called by any wrapper IRQ driver unmask functions. it doesn't
do any unmasking but records the IRQ as unmasked so that the core code knows
the unmask has taken place. It is the callers responsibility to ensure that
the IRQ can now trigger an interrupt to the core.

.. _`meta_intc_mask_irq`:

meta_intc_mask_irq
==================

.. c:function:: void meta_intc_mask_irq(struct irq_data *data)

    mask an external irq using HWMASKEXT

    :param struct irq_data \*data:
        data for the external irq to mask

.. _`meta_intc_mask_irq.description`:

Description
-----------

This is a default implementation of a mask function which makes use of the
HWMASKEXT registers available in newer versions.

Earlier versions without these registers should use SoC level IRQ masking
which call the meta_intc\_\*\\ :c:func:`_simple`\  functions above, or if that isn't
available should use the fallback meta_intc\_\*\\ :c:func:`_nomask`\  functions below.

.. _`meta_intc_unmask_irq`:

meta_intc_unmask_irq
====================

.. c:function:: void meta_intc_unmask_irq(struct irq_data *data)

    unmask an external irq using HWMASKEXT

    :param struct irq_data \*data:
        data for the external irq to unmask

.. _`meta_intc_unmask_irq.description`:

Description
-----------

This is a default implementation of an unmask function which makes use of the
HWMASKEXT registers available on new versions. It should be paired with
\ :c:func:`meta_intc_mask_irq`\  above.

.. _`meta_intc_mask_irq_nomask`:

meta_intc_mask_irq_nomask
=========================

.. c:function:: void meta_intc_mask_irq_nomask(struct irq_data *data)

    mask an external irq by unvectoring

    :param struct irq_data \*data:
        data for the external irq to mask

.. _`meta_intc_mask_irq_nomask.description`:

Description
-----------

This is the version of the mask function for older versions which don't have
HWMASKEXT registers, or a SoC level means of masking IRQs. Instead the IRQ is
unvectored from the core and retriggered if necessary later.

.. _`meta_intc_unmask_edge_irq_nomask`:

meta_intc_unmask_edge_irq_nomask
================================

.. c:function:: void meta_intc_unmask_edge_irq_nomask(struct irq_data *data)

    unmask an edge irq by revectoring

    :param struct irq_data \*data:
        data for the external irq to unmask

.. _`meta_intc_unmask_edge_irq_nomask.description`:

Description
-----------

This is the version of the unmask function for older versions which don't
have HWMASKEXT registers, or a SoC level means of masking IRQs. Instead the
IRQ is revectored back to the core and retriggered if necessary.

The retriggering done by this function is specific to edge interrupts.

.. _`meta_intc_unmask_level_irq_nomask`:

meta_intc_unmask_level_irq_nomask
=================================

.. c:function:: void meta_intc_unmask_level_irq_nomask(struct irq_data *data)

    unmask a level irq by revectoring

    :param struct irq_data \*data:
        data for the external irq to unmask

.. _`meta_intc_unmask_level_irq_nomask.description`:

Description
-----------

This is the version of the unmask function for older versions which don't
have HWMASKEXT registers, or a SoC level means of masking IRQs. Instead the
IRQ is revectored back to the core and retriggered if necessary.

The retriggering done by this function is specific to level interrupts.

.. _`meta_intc_irq_set_type`:

meta_intc_irq_set_type
======================

.. c:function:: int meta_intc_irq_set_type(struct irq_data *data, unsigned int flow_type)

    set the type of an external irq

    :param struct irq_data \*data:
        data for the external irq to set the type of

    :param unsigned int flow_type:
        new irq flow type

.. _`meta_intc_irq_set_type.description`:

Description
-----------

Set the flow type of an external interrupt. This updates the irq chip and irq
handler depending on whether the irq is edge or level sensitive (the polarity
is ignored), and also sets up the bit in HWLEVELEXT so the hardware knows
when to trigger.

.. _`meta_intc_irq_demux`:

meta_intc_irq_demux
===================

.. c:function:: void meta_intc_irq_demux(struct irq_desc *desc)

    external irq de-multiplexer

    :param struct irq_desc \*desc:
        the interrupt description structure for this irq

.. _`meta_intc_irq_demux.description`:

Description
-----------

The cpu receives an interrupt on TR2 when a SoC interrupt has occurred. It is
this function's job to demux this irq and figure out exactly which external
irq needs servicing.

Whilst using TR2 to detect external interrupts is a software convention it is
(hopefully) unlikely to change.

.. _`meta_intc_set_affinity`:

meta_intc_set_affinity
======================

.. c:function:: int meta_intc_set_affinity(struct irq_data *data, const struct cpumask *cpumask, bool force)

    set the affinity for an interrupt

    :param struct irq_data \*data:
        data for the external irq to set the affinity of

    :param const struct cpumask \*cpumask:
        cpu mask representing cpus which can handle the interrupt

    :param bool force:
        whether to force (ignored)

.. _`meta_intc_set_affinity.description`:

Description
-----------

Revector the specified external irq onto a specific cpu's TR2 trigger, so
that that cpu tends to be the one who handles it.

.. _`meta_intc_map`:

meta_intc_map
=============

.. c:function:: int meta_intc_map(struct irq_domain *d, unsigned int irq, irq_hw_number_t hw)

    map an external irq

    :param struct irq_domain \*d:
        irq domain of external trigger block

    :param unsigned int irq:
        virtual irq number

    :param irq_hw_number_t hw:
        hardware irq number within external trigger block

.. _`meta_intc_map.description`:

Description
-----------

This sets up a virtual irq for a specified hardware interrupt. The irq chip
and handler is configured, using the HWLEVELEXT registers to determine
edge/level flow type. These registers will have been set when the irq type is
set (or set to a default at init time).

.. _`meta_intc_context`:

struct meta_intc_context
========================

.. c:type:: struct meta_intc_context

    suspend context

.. _`meta_intc_context.definition`:

Definition
----------

.. code-block:: c

    struct meta_intc_context {
        u32 levels[4];
        u32 masks[4];
        u8 vectors[4*32];
        u8 txvecint[4][4];
    }

.. _`meta_intc_context.members`:

Members
-------

levels
    State of HWLEVELEXT registers

masks
    State of HWMASKEXT registers

vectors
    State of HWVECEXT registers

txvecint
    State of TxVECINT registers

.. _`meta_intc_context.description`:

Description
-----------

This structure stores the IRQ state across suspend.

.. _`meta_intc_suspend`:

meta_intc_suspend
=================

.. c:function:: int meta_intc_suspend( void)

    store irq state

    :param  void:
        no arguments

.. _`meta_intc_suspend.description`:

Description
-----------

To avoid interfering with other threads we only save the IRQ state of IRQs in
use by Linux.

.. _`meta_intc_resume`:

meta_intc_resume
================

.. c:function:: void meta_intc_resume( void)

    restore saved irq state

    :param  void:
        no arguments

.. _`meta_intc_resume.description`:

Description
-----------

Restore the saved IRQ state and drop it.

.. _`meta_intc_init_cpu`:

meta_intc_init_cpu
==================

.. c:function:: void meta_intc_init_cpu(struct meta_intc_priv *priv, int cpu)

    register with a Meta cpu

    :param struct meta_intc_priv \*priv:
        private interrupt controller data

    :param int cpu:
        the CPU to register on

.. _`meta_intc_init_cpu.description`:

Description
-----------

Configure \ ``cpu``\ 's TR2 irq so that we can demux external irqs.

.. _`meta_intc_no_mask`:

meta_intc_no_mask
=================

.. c:function:: void meta_intc_no_mask( void)

    indicate lack of HWMASKEXT registers

    :param  void:
        no arguments

.. _`meta_intc_no_mask.description`:

Description
-----------

Called from SoC code (or init code below) to dynamically indicate the lack of
HWMASKEXT registers (for example depending on some SoC revision register).
This alters the irq mask and unmask callbacks to use the fallback
unvectoring/retriggering technique instead of using HWMASKEXT registers.

.. _`init_external_irq`:

init_external_IRQ
=================

.. c:function:: int init_external_IRQ( void)

    initialise the external irq controller

    :param  void:
        no arguments

.. _`init_external_irq.description`:

Description
-----------

Set up the external irq controller using device tree properties. This is
called from \ :c:func:`init_IRQ`\ .

.. This file was automatic generated / don't edit.

