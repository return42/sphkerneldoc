.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/affinity.c

.. _`irq_create_affinity_masks`:

irq_create_affinity_masks
=========================

.. c:function:: struct cpumask *irq_create_affinity_masks(const struct cpumask *affinity, int nvec)

    Create affinity masks for multiqueue spreading

    :param const struct cpumask \*affinity:
        The affinity mask to spread. If NULL cpu_online_mask
        is used

    :param int nvec:
        *undescribed*

.. _`irq_create_affinity_masks.description`:

Description
-----------

Returns the masks pointer or NULL if allocation failed.

.. _`irq_calc_affinity_vectors`:

irq_calc_affinity_vectors
=========================

.. c:function:: int irq_calc_affinity_vectors(const struct cpumask *affinity, int maxvec)

    Calculate to optimal number of vectors for a given affinity mask

    :param const struct cpumask \*affinity:
        The affinity mask to spread. If NULL cpu_online_mask
        is used

    :param int maxvec:
        The maximum number of vectors available

.. This file was automatic generated / don't edit.

