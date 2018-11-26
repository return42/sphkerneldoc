.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/matrix.c

.. _`irq_alloc_matrix`:

irq_alloc_matrix
================

.. c:function:: struct irq_matrix *irq_alloc_matrix(unsigned int matrix_bits, unsigned int alloc_start, unsigned int alloc_end)

    Allocate a irq_matrix structure and initialize it

    :param matrix_bits:
        Number of matrix bits must be <= IRQ_MATRIX_BITS
    :type matrix_bits: unsigned int

    :param alloc_start:
        From which bit the allocation search starts
    :type alloc_start: unsigned int

    :param alloc_end:
        At which bit the allocation search ends, i.e first
        invalid bit
    :type alloc_end: unsigned int

.. _`irq_matrix_online`:

irq_matrix_online
=================

.. c:function:: void irq_matrix_online(struct irq_matrix *m)

    Bring the local CPU matrix online

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

.. _`irq_matrix_offline`:

irq_matrix_offline
==================

.. c:function:: void irq_matrix_offline(struct irq_matrix *m)

    Bring the local CPU matrix offline

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

.. _`irq_matrix_assign_system`:

irq_matrix_assign_system
========================

.. c:function:: void irq_matrix_assign_system(struct irq_matrix *m, unsigned int bit, bool replace)

    Assign system wide entry in the matrix

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

    :param bit:
        Which bit to reserve
    :type bit: unsigned int

    :param replace:
        Replace an already allocated vector with a system
        vector at the same bit position.
    :type replace: bool

.. _`irq_matrix_assign_system.description`:

Description
-----------

The \ :c:func:`BUG_ON`\ s below are on purpose. If this goes wrong in the
early boot process, then the chance to survive is about zero.
If this happens when the system is life, it's not much better.

.. _`irq_matrix_reserve_managed`:

irq_matrix_reserve_managed
==========================

.. c:function:: int irq_matrix_reserve_managed(struct irq_matrix *m, const struct cpumask *msk)

    Reserve a managed interrupt in a CPU map

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

    :param msk:
        On which CPUs the bits should be reserved.
    :type msk: const struct cpumask \*

.. _`irq_matrix_reserve_managed.description`:

Description
-----------

Can be called for offline CPUs. Note, this will only reserve one bit
on all CPUs in \ ``msk``\ , but it's not guaranteed that the bits are at the
same offset on all CPUs

.. _`irq_matrix_remove_managed`:

irq_matrix_remove_managed
=========================

.. c:function:: void irq_matrix_remove_managed(struct irq_matrix *m, const struct cpumask *msk)

    Remove managed interrupts in a CPU map

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

    :param msk:
        On which CPUs the bits should be removed
    :type msk: const struct cpumask \*

.. _`irq_matrix_remove_managed.description`:

Description
-----------

Can be called for offline CPUs

This removes not allocated managed interrupts from the map. It does
not matter which one because the managed interrupts free their
allocation when they shut down. If not, the accounting is screwed,
but all what can be done at this point is warn about it.

.. _`irq_matrix_alloc_managed`:

irq_matrix_alloc_managed
========================

.. c:function:: int irq_matrix_alloc_managed(struct irq_matrix *m, const struct cpumask *msk, unsigned int *mapped_cpu)

    Allocate a managed interrupt in a CPU map

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

    :param msk:
        *undescribed*
    :type msk: const struct cpumask \*

    :param mapped_cpu:
        *undescribed*
    :type mapped_cpu: unsigned int \*

.. _`irq_matrix_assign`:

irq_matrix_assign
=================

.. c:function:: void irq_matrix_assign(struct irq_matrix *m, unsigned int bit)

    Assign a preallocated interrupt in the local CPU map

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

    :param bit:
        Which bit to mark
    :type bit: unsigned int

.. _`irq_matrix_assign.description`:

Description
-----------

This should only be used to mark preallocated vectors

.. _`irq_matrix_reserve`:

irq_matrix_reserve
==================

.. c:function:: void irq_matrix_reserve(struct irq_matrix *m)

    Reserve interrupts

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

.. _`irq_matrix_reserve.description`:

Description
-----------

This is merily a book keeping call. It increments the number of globally
reserved interrupt bits w/o actually allocating them. This allows to
setup interrupt descriptors w/o assigning low level resources to it.
The actual allocation happens when the interrupt gets activated.

.. _`irq_matrix_remove_reserved`:

irq_matrix_remove_reserved
==========================

.. c:function:: void irq_matrix_remove_reserved(struct irq_matrix *m)

    Remove interrupt reservation

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

.. _`irq_matrix_remove_reserved.description`:

Description
-----------

This is merily a book keeping call. It decrements the number of globally
reserved interrupt bits. This is used to undo \ :c:func:`irq_matrix_reserve`\  when the
interrupt was never in use and a real vector allocated, which undid the
reservation.

.. _`irq_matrix_alloc`:

irq_matrix_alloc
================

.. c:function:: int irq_matrix_alloc(struct irq_matrix *m, const struct cpumask *msk, bool reserved, unsigned int *mapped_cpu)

    Allocate a regular interrupt in a CPU map

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

    :param msk:
        Which CPUs to search in
    :type msk: const struct cpumask \*

    :param reserved:
        Allocate previously reserved interrupts
    :type reserved: bool

    :param mapped_cpu:
        Pointer to store the CPU for which the irq was allocated
    :type mapped_cpu: unsigned int \*

.. _`irq_matrix_free`:

irq_matrix_free
===============

.. c:function:: void irq_matrix_free(struct irq_matrix *m, unsigned int cpu, unsigned int bit, bool managed)

    Free allocated interrupt in the matrix

    :param m:
        Matrix pointer
    :type m: struct irq_matrix \*

    :param cpu:
        Which CPU map needs be updated
    :type cpu: unsigned int

    :param bit:
        The bit to remove
    :type bit: unsigned int

    :param managed:
        If true, the interrupt is managed and not accounted
        as available.
    :type managed: bool

.. _`irq_matrix_available`:

irq_matrix_available
====================

.. c:function:: unsigned int irq_matrix_available(struct irq_matrix *m, bool cpudown)

    Get the number of globally available irqs

    :param m:
        Pointer to the matrix to query
    :type m: struct irq_matrix \*

    :param cpudown:
        If true, the local CPU is about to go down, adjust
        the number of available irqs accordingly
    :type cpudown: bool

.. _`irq_matrix_reserved`:

irq_matrix_reserved
===================

.. c:function:: unsigned int irq_matrix_reserved(struct irq_matrix *m)

    Get the number of globally reserved irqs

    :param m:
        Pointer to the matrix to query
    :type m: struct irq_matrix \*

.. _`irq_matrix_allocated`:

irq_matrix_allocated
====================

.. c:function:: unsigned int irq_matrix_allocated(struct irq_matrix *m)

    Get the number of allocated irqs on the local cpu

    :param m:
        Pointer to the matrix to search
    :type m: struct irq_matrix \*

.. _`irq_matrix_allocated.description`:

Description
-----------

This returns number of allocated irqs

.. _`irq_matrix_debug_show`:

irq_matrix_debug_show
=====================

.. c:function:: void irq_matrix_debug_show(struct seq_file *sf, struct irq_matrix *m, int ind)

    Show detailed allocation information

    :param sf:
        Pointer to the seq_file to print to
    :type sf: struct seq_file \*

    :param m:
        Pointer to the matrix allocator
    :type m: struct irq_matrix \*

    :param ind:
        Indentation for the print format
    :type ind: int

.. _`irq_matrix_debug_show.description`:

Description
-----------

Note, this is a lockless snapshot.

.. This file was automatic generated / don't edit.

