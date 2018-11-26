.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/affinity.c

.. _`irq_create_affinity_masks`:

irq_create_affinity_masks
=========================

.. c:function:: struct cpumask *irq_create_affinity_masks(int nvecs, const struct irq_affinity *affd)

    Create affinity masks for multiqueue spreading

    :param nvecs:
        The total number of vectors
    :type nvecs: int

    :param affd:
        Description of the affinity requirements
    :type affd: const struct irq_affinity \*

.. _`irq_create_affinity_masks.description`:

Description
-----------

Returns the masks pointer or NULL if allocation failed.

.. _`irq_calc_affinity_vectors`:

irq_calc_affinity_vectors
=========================

.. c:function:: int irq_calc_affinity_vectors(int minvec, int maxvec, const struct irq_affinity *affd)

    Calculate the optimal number of vectors

    :param minvec:
        The minimum number of vectors available
    :type minvec: int

    :param maxvec:
        The maximum number of vectors available
    :type maxvec: int

    :param affd:
        Description of the affinity requirements
    :type affd: const struct irq_affinity \*

.. This file was automatic generated / don't edit.

