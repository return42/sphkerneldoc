.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lnet/libcfs/linux/linux-cpu.c

.. _`cfs_cpt_choose_ncpus`:

cfs_cpt_choose_ncpus
====================

.. c:function:: int cfs_cpt_choose_ncpus(struct cfs_cpt_table *cptab, int cpt, cpumask_t *node, int number)

    We always prefer to choose CPU in the same core/socket.

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

    :param cpumask_t \*node:
        *undescribed*

    :param int number:
        *undescribed*

.. This file was automatic generated / don't edit.

