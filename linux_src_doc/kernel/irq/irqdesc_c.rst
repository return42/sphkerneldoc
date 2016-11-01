.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/irqdesc.c

.. _`generic_handle_irq`:

generic_handle_irq
==================

.. c:function:: int generic_handle_irq(unsigned int irq)

    Invoke the handler for a particular irq

    :param unsigned int irq:
        The irq number to handle

.. _`__handle_domain_irq`:

__handle_domain_irq
===================

.. c:function:: int __handle_domain_irq(struct irq_domain *domain, unsigned int hwirq, bool lookup, struct pt_regs *regs)

    Invoke the handler for a HW irq belonging to a domain

    :param struct irq_domain \*domain:
        The domain where to perform the lookup

    :param unsigned int hwirq:
        The HW irq number to convert to a logical one

    :param bool lookup:
        Whether to perform the domain lookup or not

    :param struct pt_regs \*regs:
        Register file coming from the low-level handling code

.. _`__handle_domain_irq.return`:

Return
------

0 on success, or -EINVAL if conversion has failed

.. _`irq_free_descs`:

irq_free_descs
==============

.. c:function:: void irq_free_descs(unsigned int from, unsigned int cnt)

    free irq descriptors

    :param unsigned int from:
        Start of descriptor range

    :param unsigned int cnt:
        Number of consecutive irqs to free

.. _`__irq_alloc_descs`:

__irq_alloc_descs
=================

.. c:function:: int __ref __irq_alloc_descs(int irq, unsigned int from, unsigned int cnt, int node, struct module *owner, const struct cpumask *affinity)

    allocate and initialize a range of irq descriptors

    :param int irq:
        Allocate for specific irq number if irq >= 0

    :param unsigned int from:
        Start the search from this irq number

    :param unsigned int cnt:
        Number of consecutive irqs to allocate.

    :param int node:
        Preferred node on which the irq descriptor should be allocated

    :param struct module \*owner:
        Owning module (can be NULL)

    :param const struct cpumask \*affinity:
        Optional pointer to an affinity mask array of size \ ``cnt``\  which
        hints where the irq descriptors should be allocated and which
        default affinities to use

.. _`__irq_alloc_descs.description`:

Description
-----------

Returns the first irq number or error code

.. _`irq_alloc_hwirqs`:

irq_alloc_hwirqs
================

.. c:function:: unsigned int irq_alloc_hwirqs(int cnt, int node)

    Allocate an irq descriptor and initialize the hardware

    :param int cnt:
        number of interrupts to allocate

    :param int node:
        node on which to allocate

.. _`irq_alloc_hwirqs.description`:

Description
-----------

Returns an interrupt number > 0 or 0, if the allocation fails.

.. _`irq_free_hwirqs`:

irq_free_hwirqs
===============

.. c:function:: void irq_free_hwirqs(unsigned int from, int cnt)

    Free irq descriptor and cleanup the hardware

    :param unsigned int from:
        Free from irq number

    :param int cnt:
        number of interrupts to free

.. _`irq_get_next_irq`:

irq_get_next_irq
================

.. c:function:: unsigned int irq_get_next_irq(unsigned int offset)

    get next allocated irq number

    :param unsigned int offset:
        where to start the search

.. _`irq_get_next_irq.description`:

Description
-----------

Returns next irq number after offset or nr_irqs if none is found.

.. _`kstat_irqs_cpu`:

kstat_irqs_cpu
==============

.. c:function:: unsigned int kstat_irqs_cpu(unsigned int irq, int cpu)

    Get the statistics for an interrupt on a cpu

    :param unsigned int irq:
        The interrupt number

    :param int cpu:
        The cpu number

.. _`kstat_irqs_cpu.description`:

Description
-----------

Returns the sum of interrupt counts on \ ``cpu``\  since boot for
\ ``irq``\ . The caller must ensure that the interrupt is not removed
concurrently.

.. _`kstat_irqs`:

kstat_irqs
==========

.. c:function:: unsigned int kstat_irqs(unsigned int irq)

    Get the statistics for an interrupt

    :param unsigned int irq:
        The interrupt number

.. _`kstat_irqs.description`:

Description
-----------

Returns the sum of interrupt counts on all cpus since boot for
\ ``irq``\ . The caller must ensure that the interrupt is not removed
concurrently.

.. _`kstat_irqs_usr`:

kstat_irqs_usr
==============

.. c:function:: unsigned int kstat_irqs_usr(unsigned int irq)

    Get the statistics for an interrupt

    :param unsigned int irq:
        The interrupt number

.. _`kstat_irqs_usr.description`:

Description
-----------

Returns the sum of interrupt counts on all cpus since boot for
\ ``irq``\ . Contrary to \ :c:func:`kstat_irqs`\  this can be called from any
preemptible context. It's protected against concurrent removal of
an interrupt descriptor when sparse irqs are enabled.

.. This file was automatic generated / don't edit.

