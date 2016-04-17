.. -*- coding: utf-8; mode: rst -*-

==========
cpu_rmap.c
==========


.. _`alloc_cpu_rmap`:

alloc_cpu_rmap
==============

.. c:function:: struct cpu_rmap *alloc_cpu_rmap (unsigned int size, gfp_t flags)

    allocate CPU affinity reverse-map

    :param unsigned int size:
        Number of objects to be mapped

    :param gfp_t flags:
        Allocation flags e.g. ``GFP_KERNEL``



.. _`cpu_rmap_release`:

cpu_rmap_release
================

.. c:function:: void cpu_rmap_release (struct kref *ref)

    internal reclaiming helper called from kref_put

    :param struct kref \*ref:
        kref to struct cpu_rmap



.. _`cpu_rmap_get`:

cpu_rmap_get
============

.. c:function:: void cpu_rmap_get (struct cpu_rmap *rmap)

    internal helper to get new ref on a cpu_rmap

    :param struct cpu_rmap \*rmap:
        reverse-map allocated with :c:func:`alloc_cpu_rmap`



.. _`cpu_rmap_put`:

cpu_rmap_put
============

.. c:function:: int cpu_rmap_put (struct cpu_rmap *rmap)

    release ref on a cpu_rmap

    :param struct cpu_rmap \*rmap:
        reverse-map allocated with :c:func:`alloc_cpu_rmap`



.. _`cpu_rmap_add`:

cpu_rmap_add
============

.. c:function:: int cpu_rmap_add (struct cpu_rmap *rmap, void *obj)

    add object to a rmap

    :param struct cpu_rmap \*rmap:
        CPU rmap allocated with :c:func:`alloc_cpu_rmap`

    :param void \*obj:
        Object to add to rmap



.. _`cpu_rmap_add.description`:

Description
-----------

Return index of object.



.. _`cpu_rmap_update`:

cpu_rmap_update
===============

.. c:function:: int cpu_rmap_update (struct cpu_rmap *rmap, u16 index, const struct cpumask *affinity)

    update CPU rmap following a change of object affinity

    :param struct cpu_rmap \*rmap:
        CPU rmap to update

    :param u16 index:
        Index of object whose affinity changed

    :param const struct cpumask \*affinity:
        New CPU affinity of object



.. _`free_irq_cpu_rmap`:

free_irq_cpu_rmap
=================

.. c:function:: void free_irq_cpu_rmap (struct cpu_rmap *rmap)

    free a CPU affinity reverse-map used for IRQs

    :param struct cpu_rmap \*rmap:
        Reverse-map allocated with :c:func:`alloc_irq_cpu_map`, or ``NULL``



.. _`free_irq_cpu_rmap.description`:

Description
-----------

Must be called in process context, before freeing the IRQs.



.. _`irq_cpu_rmap_notify`:

irq_cpu_rmap_notify
===================

.. c:function:: void irq_cpu_rmap_notify (struct irq_affinity_notify *notify, const cpumask_t *mask)

    callback for IRQ subsystem when IRQ affinity updated

    :param struct irq_affinity_notify \*notify:
        struct irq_affinity_notify passed by irq/manage.c

    :param const cpumask_t \*mask:
        cpu mask for new SMP affinity



.. _`irq_cpu_rmap_notify.description`:

Description
-----------

This is executed in workqueue context.



.. _`irq_cpu_rmap_release`:

irq_cpu_rmap_release
====================

.. c:function:: void irq_cpu_rmap_release (struct kref *ref)

    reclaiming callback for IRQ subsystem

    :param struct kref \*ref:
        kref to struct irq_affinity_notify passed by irq/manage.c



.. _`irq_cpu_rmap_add`:

irq_cpu_rmap_add
================

.. c:function:: int irq_cpu_rmap_add (struct cpu_rmap *rmap, int irq)

    add an IRQ to a CPU affinity reverse-map

    :param struct cpu_rmap \*rmap:
        The reverse-map

    :param int irq:
        The IRQ number



.. _`irq_cpu_rmap_add.description`:

Description
-----------

This adds an IRQ affinity notifier that will update the reverse-map
automatically.

Must be called in process context, after the IRQ is allocated but
before it is bound with :c:func:`request_irq`.

