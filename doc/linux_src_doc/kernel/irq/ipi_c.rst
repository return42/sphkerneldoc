.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/ipi.c

.. _`irq_reserve_ipi`:

irq_reserve_ipi
===============

.. c:function:: int irq_reserve_ipi(struct irq_domain *domain, const struct cpumask *dest)

    Setup an IPI to destination cpumask

    :param struct irq_domain \*domain:
        IPI domain

    :param const struct cpumask \*dest:
        cpumask of cpus which can receive the IPI

.. _`irq_reserve_ipi.description`:

Description
-----------

Allocate a virq that can be used to send IPI to any CPU in dest mask.

On success it'll return linux irq number and error code on failure

.. _`irq_destroy_ipi`:

irq_destroy_ipi
===============

.. c:function:: int irq_destroy_ipi(unsigned int irq, const struct cpumask *dest)

    unreserve an IPI that was previously allocated

    :param unsigned int irq:
        linux irq number to be destroyed

    :param const struct cpumask \*dest:
        cpumask of cpus which should have the IPI removed

.. _`irq_destroy_ipi.description`:

Description
-----------

The IPIs allocated with \ :c:func:`irq_reserve_ipi`\  are retuerned to the system
destroying all virqs associated with them.

Return 0 on success or error code on failure.

.. _`ipi_get_hwirq`:

ipi_get_hwirq
=============

.. c:function:: irq_hw_number_t ipi_get_hwirq(unsigned int irq, unsigned int cpu)

    Get the hwirq associated with an IPI to a cpu

    :param unsigned int irq:
        linux irq number

    :param unsigned int cpu:
        the target cpu

.. _`ipi_get_hwirq.description`:

Description
-----------

When dealing with coprocessors IPI, we need to inform the coprocessor of
the hwirq it needs to use to receive and send IPIs.

Returns hwirq value on success and INVALID_HWIRQ on failure.

.. _`__ipi_send_single`:

__ipi_send_single
=================

.. c:function:: int __ipi_send_single(struct irq_desc *desc, unsigned int cpu)

    send an IPI to a target Linux SMP CPU

    :param struct irq_desc \*desc:
        pointer to irq_desc of the IRQ

    :param unsigned int cpu:
        destination CPU, must in the destination mask passed to
        \ :c:func:`irq_reserve_ipi`\ 

.. _`__ipi_send_single.description`:

Description
-----------

This function is for architecture or core code to speed up IPI sending. Not
usable from driver code.

Returns zero on success and negative error number on failure.

.. _`__ipi_send_mask`:

__ipi_send_mask
===============

.. c:function:: int __ipi_send_mask(struct irq_desc *desc, const struct cpumask *dest)

    send an IPI to target Linux SMP CPU(s)

    :param struct irq_desc \*desc:
        pointer to irq_desc of the IRQ

    :param const struct cpumask \*dest:
        dest CPU(s), must be a subset of the mask passed to
        \ :c:func:`irq_reserve_ipi`\ 

.. _`__ipi_send_mask.description`:

Description
-----------

This function is for architecture or core code to speed up IPI sending. Not
usable from driver code.

Returns zero on success and negative error number on failure.

.. _`ipi_send_single`:

ipi_send_single
===============

.. c:function:: int ipi_send_single(unsigned int virq, unsigned int cpu)

    Send an IPI to a single CPU

    :param unsigned int virq:
        linux irq number from \ :c:func:`irq_reserve_ipi`\ 

    :param unsigned int cpu:
        destination CPU, must in the destination mask passed to
        \ :c:func:`irq_reserve_ipi`\ 

.. _`ipi_send_single.description`:

Description
-----------

Returns zero on success and negative error number on failure.

.. _`ipi_send_mask`:

ipi_send_mask
=============

.. c:function:: int ipi_send_mask(unsigned int virq, const struct cpumask *dest)

    Send an IPI to target CPU(s)

    :param unsigned int virq:
        linux irq number from \ :c:func:`irq_reserve_ipi`\ 

    :param const struct cpumask \*dest:
        dest CPU(s), must be a subset of the mask passed to
        \ :c:func:`irq_reserve_ipi`\ 

.. _`ipi_send_mask.description`:

Description
-----------

Returns zero on success and negative error number on failure.

.. This file was automatic generated / don't edit.

