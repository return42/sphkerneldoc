.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/irqdesc.c

.. _`generic_handle_irq`:

generic_handle_irq
==================

.. c:function:: int generic_handle_irq(unsigned int irq)

    Invoke the handler for a particular irq

    :param irq:
        The irq number to handle
    :type irq: unsigned int

.. _`__handle_domain_irq`:

__handle_domain_irq
===================

.. c:function:: int __handle_domain_irq(struct irq_domain *domain, unsigned int hwirq, bool lookup, struct pt_regs *regs)

    Invoke the handler for a HW irq belonging to a domain

    :param domain:
        The domain where to perform the lookup
    :type domain: struct irq_domain \*

    :param hwirq:
        The HW irq number to convert to a logical one
    :type hwirq: unsigned int

    :param lookup:
        Whether to perform the domain lookup or not
    :type lookup: bool

    :param regs:
        Register file coming from the low-level handling code
    :type regs: struct pt_regs \*

.. _`__handle_domain_irq.return`:

Return
------

0 on success, or -EINVAL if conversion has failed

.. _`irq_free_descs`:

irq_free_descs
==============

.. c:function:: void irq_free_descs(unsigned int from, unsigned int cnt)

    free irq descriptors

    :param from:
        Start of descriptor range
    :type from: unsigned int

    :param cnt:
        Number of consecutive irqs to free
    :type cnt: unsigned int

.. _`__irq_alloc_descs`:

__irq_alloc_descs
=================

.. c:function:: int __ref __irq_alloc_descs(int irq, unsigned int from, unsigned int cnt, int node, struct module *owner, const struct cpumask *affinity)

    allocate and initialize a range of irq descriptors

    :param irq:
        Allocate for specific irq number if irq >= 0
    :type irq: int

    :param from:
        Start the search from this irq number
    :type from: unsigned int

    :param cnt:
        Number of consecutive irqs to allocate.
    :type cnt: unsigned int

    :param node:
        Preferred node on which the irq descriptor should be allocated
    :type node: int

    :param owner:
        Owning module (can be NULL)
    :type owner: struct module \*

    :param affinity:
        Optional pointer to an affinity mask array of size \ ``cnt``\  which
        hints where the irq descriptors should be allocated and which
        default affinities to use
    :type affinity: const struct cpumask \*

.. _`__irq_alloc_descs.description`:

Description
-----------

Returns the first irq number or error code

.. _`irq_alloc_hwirqs`:

irq_alloc_hwirqs
================

.. c:function:: unsigned int irq_alloc_hwirqs(int cnt, int node)

    Allocate an irq descriptor and initialize the hardware

    :param cnt:
        number of interrupts to allocate
    :type cnt: int

    :param node:
        node on which to allocate
    :type node: int

.. _`irq_alloc_hwirqs.description`:

Description
-----------

Returns an interrupt number > 0 or 0, if the allocation fails.

.. _`irq_free_hwirqs`:

irq_free_hwirqs
===============

.. c:function:: void irq_free_hwirqs(unsigned int from, int cnt)

    Free irq descriptor and cleanup the hardware

    :param from:
        Free from irq number
    :type from: unsigned int

    :param cnt:
        number of interrupts to free
    :type cnt: int

.. _`irq_get_next_irq`:

irq_get_next_irq
================

.. c:function:: unsigned int irq_get_next_irq(unsigned int offset)

    get next allocated irq number

    :param offset:
        where to start the search
    :type offset: unsigned int

.. _`irq_get_next_irq.description`:

Description
-----------

Returns next irq number after offset or nr_irqs if none is found.

.. _`kstat_irqs_cpu`:

kstat_irqs_cpu
==============

.. c:function:: unsigned int kstat_irqs_cpu(unsigned int irq, int cpu)

    Get the statistics for an interrupt on a cpu

    :param irq:
        The interrupt number
    :type irq: unsigned int

    :param cpu:
        The cpu number
    :type cpu: int

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

    :param irq:
        The interrupt number
    :type irq: unsigned int

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

    :param irq:
        The interrupt number
    :type irq: unsigned int

.. _`kstat_irqs_usr.description`:

Description
-----------

Returns the sum of interrupt counts on all cpus since boot for \ ``irq``\ .
Contrary to \ :c:func:`kstat_irqs`\  this can be called from any context.
It uses rcu since a concurrent removal of an interrupt descriptor is
observing an rcu grace period before \ :c:func:`delayed_free_desc`\ /irq_kobj_release().

.. This file was automatic generated / don't edit.

