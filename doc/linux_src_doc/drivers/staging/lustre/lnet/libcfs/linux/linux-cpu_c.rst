.. -*- coding: utf-8; mode: rst -*-

===========
linux-cpu.c
===========


.. _`cfs_cpt_choose_ncpus`:

cfs_cpt_choose_ncpus
====================

.. c:function:: int cfs_cpt_choose_ncpus (struct cfs_cpt_table *cptab, int cpt, cpumask_t *node, int number)

    :param struct cfs_cpt_table \*cptab:

        *undescribed*

    :param int cpt:

        *undescribed*

    :param cpumask_t \*node:

        *undescribed*

    :param int number:

        *undescribed*



.. _`cfs_cpt_choose_ncpus.description`:

Description
-----------

We always prefer to choose CPU in the same core/socket.

