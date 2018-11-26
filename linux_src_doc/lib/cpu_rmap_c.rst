.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/cpu_rmap.c

.. _`alloc_cpu_rmap`:

alloc_cpu_rmap
==============

.. c:function:: struct cpu_rmap *alloc_cpu_rmap(unsigned int size, gfp_t flags)

    allocate CPU affinity reverse-map

    :param size:
        Number of objects to be mapped
    :type size: unsigned int

    :param flags:
        Allocation flags e.g. \ ``GFP_KERNEL``\ 
    :type flags: gfp_t

.. _`cpu_rmap_release`:

cpu_rmap_release
================

.. c:function:: void cpu_rmap_release(struct kref *ref)

    internal reclaiming helper called from kref_put

    :param ref:
        kref to struct cpu_rmap
    :type ref: struct kref \*

.. _`cpu_rmap_get`:

cpu_rmap_get
============

.. c:function:: void cpu_rmap_get(struct cpu_rmap *rmap)

    internal helper to get new ref on a cpu_rmap

    :param rmap:
        reverse-map allocated with \ :c:func:`alloc_cpu_rmap`\ 
    :type rmap: struct cpu_rmap \*

.. _`cpu_rmap_put`:

cpu_rmap_put
============

.. c:function:: int cpu_rmap_put(struct cpu_rmap *rmap)

    release ref on a cpu_rmap

    :param rmap:
        reverse-map allocated with \ :c:func:`alloc_cpu_rmap`\ 
    :type rmap: struct cpu_rmap \*

.. _`cpu_rmap_add`:

cpu_rmap_add
============

.. c:function:: int cpu_rmap_add(struct cpu_rmap *rmap, void *obj)

    add object to a rmap

    :param rmap:
        CPU rmap allocated with \ :c:func:`alloc_cpu_rmap`\ 
    :type rmap: struct cpu_rmap \*

    :param obj:
        Object to add to rmap
    :type obj: void \*

.. _`cpu_rmap_add.description`:

Description
-----------

Return index of object.

.. _`cpu_rmap_update`:

cpu_rmap_update
===============

.. c:function:: int cpu_rmap_update(struct cpu_rmap *rmap, u16 index, const struct cpumask *affinity)

    update CPU rmap following a change of object affinity

    :param rmap:
        CPU rmap to update
    :type rmap: struct cpu_rmap \*

    :param index:
        Index of object whose affinity changed
    :type index: u16

    :param affinity:
        New CPU affinity of object
    :type affinity: const struct cpumask \*

.. _`free_irq_cpu_rmap`:

free_irq_cpu_rmap
=================

.. c:function:: void free_irq_cpu_rmap(struct cpu_rmap *rmap)

    free a CPU affinity reverse-map used for IRQs

    :param rmap:
        Reverse-map allocated with \ :c:func:`alloc_irq_cpu_map`\ , or \ ``NULL``\ 
    :type rmap: struct cpu_rmap \*

.. _`free_irq_cpu_rmap.description`:

Description
-----------

Must be called in process context, before freeing the IRQs.

.. _`irq_cpu_rmap_notify`:

irq_cpu_rmap_notify
===================

.. c:function:: void irq_cpu_rmap_notify(struct irq_affinity_notify *notify, const cpumask_t *mask)

    callback for IRQ subsystem when IRQ affinity updated

    :param notify:
        struct irq_affinity_notify passed by irq/manage.c
    :type notify: struct irq_affinity_notify \*

    :param mask:
        cpu mask for new SMP affinity
    :type mask: const cpumask_t \*

.. _`irq_cpu_rmap_notify.description`:

Description
-----------

This is executed in workqueue context.

.. _`irq_cpu_rmap_release`:

irq_cpu_rmap_release
====================

.. c:function:: void irq_cpu_rmap_release(struct kref *ref)

    reclaiming callback for IRQ subsystem

    :param ref:
        kref to struct irq_affinity_notify passed by irq/manage.c
    :type ref: struct kref \*

.. _`irq_cpu_rmap_add`:

irq_cpu_rmap_add
================

.. c:function:: int irq_cpu_rmap_add(struct cpu_rmap *rmap, int irq)

    add an IRQ to a CPU affinity reverse-map

    :param rmap:
        The reverse-map
    :type rmap: struct cpu_rmap \*

    :param irq:
        The IRQ number
    :type irq: int

.. _`irq_cpu_rmap_add.description`:

Description
-----------

This adds an IRQ affinity notifier that will update the reverse-map
automatically.

Must be called in process context, after the IRQ is allocated but
before it is bound with \ :c:func:`request_irq`\ .

.. This file was automatic generated / don't edit.

