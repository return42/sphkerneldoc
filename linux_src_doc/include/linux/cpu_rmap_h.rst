.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cpu_rmap.h

.. _`cpu_rmap`:

struct cpu_rmap
===============

.. c:type:: struct cpu_rmap

    CPU affinity reverse-map

.. _`cpu_rmap.definition`:

Definition
----------

.. code-block:: c

    struct cpu_rmap {
        struct kref refcount;
        u16 size;
        u16 used;
        void **obj;
        struct near[0];
    }

.. _`cpu_rmap.members`:

Members
-------

refcount
    kref for object

size
    Number of objects to be reverse-mapped

used
    Number of objects added

obj
    Pointer to array of object pointers

near
    For each CPU, the index and distance to the nearest object,
    based on affinity masks

.. _`alloc_irq_cpu_rmap`:

alloc_irq_cpu_rmap
==================

.. c:function:: struct cpu_rmap *alloc_irq_cpu_rmap(unsigned int size)

    allocate CPU affinity reverse-map for IRQs

    :param unsigned int size:
        Number of objects to be mapped

.. _`alloc_irq_cpu_rmap.description`:

Description
-----------

Must be called in process context.

.. This file was automatic generated / don't edit.

