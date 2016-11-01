.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/chip.c

.. _`irq_set_chip`:

irq_set_chip
============

.. c:function:: int irq_set_chip(unsigned int irq, struct irq_chip *chip)

    set the irq chip for an irq

    :param unsigned int irq:
        irq number

    :param struct irq_chip \*chip:
        pointer to irq chip description structure

.. _`irq_set_irq_type`:

irq_set_irq_type
================

.. c:function:: int irq_set_irq_type(unsigned int irq, unsigned int type)

    set the irq trigger type for an irq

    :param unsigned int irq:
        irq number

    :param unsigned int type:
        IRQ_TYPE_{LEVEL,EDGE}_\* value - see include/linux/irq.h

.. _`irq_set_handler_data`:

irq_set_handler_data
====================

.. c:function:: int irq_set_handler_data(unsigned int irq, void *data)

    set irq handler data for an irq

    :param unsigned int irq:
        Interrupt number

    :param void \*data:
        Pointer to interrupt specific data

.. _`irq_set_handler_data.description`:

Description
-----------

Set the hardware irq controller data for an irq

.. _`irq_set_msi_desc_off`:

irq_set_msi_desc_off
====================

.. c:function:: int irq_set_msi_desc_off(unsigned int irq_base, unsigned int irq_offset, struct msi_desc *entry)

    set MSI descriptor data for an irq at offset

    :param unsigned int irq_base:
        Interrupt number base

    :param unsigned int irq_offset:
        Interrupt number offset

    :param struct msi_desc \*entry:
        Pointer to MSI descriptor data

.. _`irq_set_msi_desc_off.description`:

Description
-----------

Set the MSI descriptor entry for an irq at offset

.. _`irq_set_msi_desc`:

irq_set_msi_desc
================

.. c:function:: int irq_set_msi_desc(unsigned int irq, struct msi_desc *entry)

    set MSI descriptor data for an irq

    :param unsigned int irq:
        Interrupt number

    :param struct msi_desc \*entry:
        Pointer to MSI descriptor data

.. _`irq_set_msi_desc.description`:

Description
-----------

Set the MSI descriptor entry for an irq

.. _`irq_set_chip_data`:

irq_set_chip_data
=================

.. c:function:: int irq_set_chip_data(unsigned int irq, void *data)

    set irq chip data for an irq

    :param unsigned int irq:
        Interrupt number

    :param void \*data:
        Pointer to chip specific data

.. _`irq_set_chip_data.description`:

Description
-----------

Set the hardware irq chip data for an irq

.. _`irq_disable`:

irq_disable
===========

.. c:function:: void irq_disable(struct irq_desc *desc)

    Mark interrupt disabled

    :param struct irq_desc \*desc:
        irq descriptor which should be disabled

.. _`irq_disable.description`:

Description
-----------

If the chip does not implement the irq_disable callback, we
use a lazy disable approach. That means we mark the interrupt
disabled, but leave the hardware unmasked. That's an
optimization because we avoid the hardware access for the
common case where no interrupt happens after we marked it
disabled. If an interrupt happens, then the interrupt flow
handler masks the line at the hardware level and marks it
pending.

If the interrupt chip does not implement the irq_disable callback,
a driver can disable the lazy approach for a particular irq line by
calling 'irq_set_status_flags(irq, IRQ_DISABLE_UNLAZY)'. This can
be used for devices which cannot disable the interrupt at the
device level under certain circumstances and have to use
disable_irq[_nosync] instead.

.. _`handle_simple_irq`:

handle_simple_irq
=================

.. c:function:: void handle_simple_irq(struct irq_desc *desc)

    Simple and software-decoded IRQs.

    :param struct irq_desc \*desc:
        the interrupt description structure for this irq

.. _`handle_simple_irq.description`:

Description
-----------

Simple interrupts are either sent from a demultiplexing interrupt
handler or come from hardware, where no interrupt hardware control
is necessary.

.. _`handle_simple_irq.note`:

Note
----

The caller is expected to handle the ack, clear, mask and
unmask issues if necessary.

.. _`handle_untracked_irq`:

handle_untracked_irq
====================

.. c:function:: void handle_untracked_irq(struct irq_desc *desc)

    Simple and software-decoded IRQs.

    :param struct irq_desc \*desc:
        the interrupt description structure for this irq

.. _`handle_untracked_irq.description`:

Description
-----------

Untracked interrupts are sent from a demultiplexing interrupt
handler when the demultiplexer does not know which device it its
multiplexed irq domain generated the interrupt. IRQ's handled
through here are not subjected to stats tracking, randomness, or
spurious interrupt detection.

.. _`handle_untracked_irq.note`:

Note
----

Like handle_simple_irq, the caller is expected to handle
the ack, clear, mask and unmask issues if necessary.

.. _`handle_level_irq`:

handle_level_irq
================

.. c:function:: void handle_level_irq(struct irq_desc *desc)

    Level type irq handler

    :param struct irq_desc \*desc:
        the interrupt description structure for this irq

.. _`handle_level_irq.description`:

Description
-----------

Level type interrupts are active as long as the hardware line has
the active level. This may require to mask the interrupt and unmask
it after the associated handler has acknowledged the device, so the
interrupt line is back to inactive.

.. _`handle_fasteoi_irq`:

handle_fasteoi_irq
==================

.. c:function:: void handle_fasteoi_irq(struct irq_desc *desc)

    irq handler for transparent controllers

    :param struct irq_desc \*desc:
        the interrupt description structure for this irq

.. _`handle_fasteoi_irq.only-a-single-callback-will-be-issued-to-the-chip`:

Only a single callback will be issued to the chip
-------------------------------------------------

an ->eoi()
call when the interrupt has been serviced. This enables support
for modern forms of interrupt handlers, which handle the flow
details in hardware, transparently.

.. _`handle_edge_irq`:

handle_edge_irq
===============

.. c:function:: void handle_edge_irq(struct irq_desc *desc)

    edge type IRQ handler

    :param struct irq_desc \*desc:
        the interrupt description structure for this irq

.. _`handle_edge_irq.description`:

Description
-----------

Interrupt occures on the falling and/or rising edge of a hardware
signal. The occurrence is latched into the irq controller hardware
and must be acked in order to be reenabled. After the ack another
interrupt can happen on the same source even before the first one
is handled by the associated event handler. If this happens it
might be necessary to disable (mask) the interrupt depending on the
controller hardware. This requires to reenable the interrupt inside
of the loop which handles the interrupts which have arrived while
the handler was running. If all pending interrupts are handled, the
loop is left.

.. _`handle_edge_eoi_irq`:

handle_edge_eoi_irq
===================

.. c:function:: void handle_edge_eoi_irq(struct irq_desc *desc)

    edge eoi type IRQ handler

    :param struct irq_desc \*desc:
        the interrupt description structure for this irq

.. _`handle_edge_eoi_irq.description`:

Description
-----------

Similar as the above handle_edge_irq, but using eoi and w/o the
mask/unmask logic.

.. _`handle_percpu_irq`:

handle_percpu_irq
=================

.. c:function:: void handle_percpu_irq(struct irq_desc *desc)

    Per CPU local irq handler

    :param struct irq_desc \*desc:
        the interrupt description structure for this irq

.. _`handle_percpu_irq.description`:

Description
-----------

Per CPU interrupts on SMP machines without locking requirements

.. _`handle_percpu_devid_irq`:

handle_percpu_devid_irq
=======================

.. c:function:: void handle_percpu_devid_irq(struct irq_desc *desc)

    Per CPU local irq handler with per cpu dev ids

    :param struct irq_desc \*desc:
        the interrupt description structure for this irq

.. _`handle_percpu_devid_irq.description`:

Description
-----------

Per CPU interrupts on SMP machines without locking requirements. Same as
\ :c:func:`handle_percpu_irq`\  above but with the following extras:

action->percpu_dev_id is a pointer to percpu variables which
contain the real device id for the cpu on which this handler is
called

.. _`irq_cpu_online`:

irq_cpu_online
==============

.. c:function:: void irq_cpu_online( void)

    Invoke all irq_cpu_online functions.

    :param  void:
        no arguments

.. _`irq_cpu_online.description`:

Description
-----------

Iterate through all irqs and invoke the chip.irq_cpu_online()
for each.

.. _`irq_cpu_offline`:

irq_cpu_offline
===============

.. c:function:: void irq_cpu_offline( void)

    Invoke all irq_cpu_offline functions.

    :param  void:
        no arguments

.. _`irq_cpu_offline.description`:

Description
-----------

Iterate through all irqs and invoke the chip.irq_cpu_offline()
for each.

.. _`irq_chip_enable_parent`:

irq_chip_enable_parent
======================

.. c:function:: void irq_chip_enable_parent(struct irq_data *data)

    Enable the parent interrupt (defaults to unmask if NULL)

    :param struct irq_data \*data:
        Pointer to interrupt specific data

.. _`irq_chip_disable_parent`:

irq_chip_disable_parent
=======================

.. c:function:: void irq_chip_disable_parent(struct irq_data *data)

    Disable the parent interrupt (defaults to mask if NULL)

    :param struct irq_data \*data:
        Pointer to interrupt specific data

.. _`irq_chip_ack_parent`:

irq_chip_ack_parent
===================

.. c:function:: void irq_chip_ack_parent(struct irq_data *data)

    Acknowledge the parent interrupt

    :param struct irq_data \*data:
        Pointer to interrupt specific data

.. _`irq_chip_mask_parent`:

irq_chip_mask_parent
====================

.. c:function:: void irq_chip_mask_parent(struct irq_data *data)

    Mask the parent interrupt

    :param struct irq_data \*data:
        Pointer to interrupt specific data

.. _`irq_chip_unmask_parent`:

irq_chip_unmask_parent
======================

.. c:function:: void irq_chip_unmask_parent(struct irq_data *data)

    Unmask the parent interrupt

    :param struct irq_data \*data:
        Pointer to interrupt specific data

.. _`irq_chip_eoi_parent`:

irq_chip_eoi_parent
===================

.. c:function:: void irq_chip_eoi_parent(struct irq_data *data)

    Invoke EOI on the parent interrupt

    :param struct irq_data \*data:
        Pointer to interrupt specific data

.. _`irq_chip_set_affinity_parent`:

irq_chip_set_affinity_parent
============================

.. c:function:: int irq_chip_set_affinity_parent(struct irq_data *data, const struct cpumask *dest, bool force)

    Set affinity on the parent interrupt

    :param struct irq_data \*data:
        Pointer to interrupt specific data

    :param const struct cpumask \*dest:
        The affinity mask to set

    :param bool force:
        Flag to enforce setting (disable online checks)

.. _`irq_chip_set_affinity_parent.description`:

Description
-----------

Conditinal, as the underlying parent chip might not implement it.

.. _`irq_chip_set_type_parent`:

irq_chip_set_type_parent
========================

.. c:function:: int irq_chip_set_type_parent(struct irq_data *data, unsigned int type)

    Set IRQ type on the parent interrupt

    :param struct irq_data \*data:
        Pointer to interrupt specific data

    :param unsigned int type:
        IRQ_TYPE_{LEVEL,EDGE}_\* value - see include/linux/irq.h

.. _`irq_chip_set_type_parent.description`:

Description
-----------

Conditional, as the underlying parent chip might not implement it.

.. _`irq_chip_retrigger_hierarchy`:

irq_chip_retrigger_hierarchy
============================

.. c:function:: int irq_chip_retrigger_hierarchy(struct irq_data *data)

    Retrigger an interrupt in hardware

    :param struct irq_data \*data:
        Pointer to interrupt specific data

.. _`irq_chip_retrigger_hierarchy.description`:

Description
-----------

Iterate through the domain hierarchy of the interrupt and check
whether a hw retrigger function exists. If yes, invoke it.

.. _`irq_chip_set_vcpu_affinity_parent`:

irq_chip_set_vcpu_affinity_parent
=================================

.. c:function:: int irq_chip_set_vcpu_affinity_parent(struct irq_data *data, void *vcpu_info)

    Set vcpu affinity on the parent interrupt

    :param struct irq_data \*data:
        Pointer to interrupt specific data

    :param void \*vcpu_info:
        The vcpu affinity information

.. _`irq_chip_set_wake_parent`:

irq_chip_set_wake_parent
========================

.. c:function:: int irq_chip_set_wake_parent(struct irq_data *data, unsigned int on)

    Set/reset wake-up on the parent interrupt

    :param struct irq_data \*data:
        Pointer to interrupt specific data

    :param unsigned int on:
        Whether to set or reset the wake-up capability of this irq

.. _`irq_chip_set_wake_parent.description`:

Description
-----------

Conditional, as the underlying parent chip might not implement it.

.. _`irq_chip_compose_msi_msg`:

irq_chip_compose_msi_msg
========================

.. c:function:: int irq_chip_compose_msi_msg(struct irq_data *data, struct msi_msg *msg)

    Componse msi message for a irq chip

    :param struct irq_data \*data:
        Pointer to interrupt specific data

    :param struct msi_msg \*msg:
        Pointer to the MSI message

.. _`irq_chip_compose_msi_msg.description`:

Description
-----------

For hierarchical domains we find the first chip in the hierarchy
which implements the irq_compose_msi_msg callback. For non
hierarchical we use the top level chip.

.. _`irq_chip_pm_get`:

irq_chip_pm_get
===============

.. c:function:: int irq_chip_pm_get(struct irq_data *data)

    Enable power for an IRQ chip

    :param struct irq_data \*data:
        Pointer to interrupt specific data

.. _`irq_chip_pm_get.description`:

Description
-----------

Enable the power to the IRQ chip referenced by the interrupt data
structure.

.. _`irq_chip_pm_put`:

irq_chip_pm_put
===============

.. c:function:: int irq_chip_pm_put(struct irq_data *data)

    Disable power for an IRQ chip

    :param struct irq_data \*data:
        Pointer to interrupt specific data

.. _`irq_chip_pm_put.description`:

Description
-----------

Disable the power to the IRQ chip referenced by the interrupt data
structure, belongs. Note that power will only be disabled, once this
function has been called for all IRQs that have called \ :c:func:`irq_chip_pm_get`\ .

.. This file was automatic generated / don't edit.

