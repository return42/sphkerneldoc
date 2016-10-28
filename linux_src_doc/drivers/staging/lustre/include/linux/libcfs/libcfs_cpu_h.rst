.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/include/linux/libcfs/libcfs_cpu.h

.. _`cfs_cpt_cpumask`:

cfs_cpt_cpumask
===============

.. c:function:: cpumask_t *cfs_cpt_cpumask(struct cfs_cpt_table *cptab, int cpt)

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

.. _`cfs_cpt_table_print`:

cfs_cpt_table_print
===================

.. c:function:: int cfs_cpt_table_print(struct cfs_cpt_table *cptab, char *buf, int len)

    table

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param char \*buf:
        *undescribed*

    :param int len:
        *undescribed*

.. _`cfs_cpt_table_free`:

cfs_cpt_table_free
==================

.. c:function:: void cfs_cpt_table_free(struct cfs_cpt_table *cptab)

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

.. _`cfs_cpt_table_alloc`:

cfs_cpt_table_alloc
===================

.. c:function:: struct cfs_cpt_table *cfs_cpt_table_alloc(unsigned int ncpt)

    :param unsigned int ncpt:
        *undescribed*

.. _`cfs_cpt_number`:

cfs_cpt_number
==============

.. c:function:: int cfs_cpt_number(struct cfs_cpt_table *cptab)

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

.. _`cfs_cpt_weight`:

cfs_cpt_weight
==============

.. c:function:: int cfs_cpt_weight(struct cfs_cpt_table *cptab, int cpt)

    threadings in a CPU partition \a cpt

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

.. _`cfs_cpt_online`:

cfs_cpt_online
==============

.. c:function:: int cfs_cpt_online(struct cfs_cpt_table *cptab, int cpt)

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

.. _`cfs_cpt_nodemask`:

cfs_cpt_nodemask
================

.. c:function:: nodemask_t *cfs_cpt_nodemask(struct cfs_cpt_table *cptab, int cpt)

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

.. _`cfs_cpt_current`:

cfs_cpt_current
===============

.. c:function:: int cfs_cpt_current(struct cfs_cpt_table *cptab, int remap)

    partition ID of \a cptab

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int remap:
        *undescribed*

.. _`cfs_cpt_of_cpu`:

cfs_cpt_of_cpu
==============

.. c:function:: int cfs_cpt_of_cpu(struct cfs_cpt_table *cptab, int cpu)

    partition ID by \a cptab

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpu:
        *undescribed*

.. _`cfs_cpt_bind`:

cfs_cpt_bind
============

.. c:function:: int cfs_cpt_bind(struct cfs_cpt_table *cptab, int cpt)

    partition \a cpt of \a cptab

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

.. _`cfs_cpt_set_cpu`:

cfs_cpt_set_cpu
===============

.. c:function:: int cfs_cpt_set_cpu(struct cfs_cpt_table *cptab, int cpt, int cpu)

    otherwise 0 is returned

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

    :param int cpu:
        *undescribed*

.. _`cfs_cpt_unset_cpu`:

cfs_cpt_unset_cpu
=================

.. c:function:: void cfs_cpt_unset_cpu(struct cfs_cpt_table *cptab, int cpt, int cpu)

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

    :param int cpu:
        *undescribed*

.. _`cfs_cpt_set_cpumask`:

cfs_cpt_set_cpumask
===================

.. c:function:: int cfs_cpt_set_cpumask(struct cfs_cpt_table *cptab, int cpt, cpumask_t *mask)

    return 1 if successfully set all CPUs, otherwise return 0

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

    :param cpumask_t \*mask:
        *undescribed*

.. _`cfs_cpt_unset_cpumask`:

cfs_cpt_unset_cpumask
=====================

.. c:function:: void cfs_cpt_unset_cpumask(struct cfs_cpt_table *cptab, int cpt, cpumask_t *mask)

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

    :param cpumask_t \*mask:
        *undescribed*

.. _`cfs_cpt_set_node`:

cfs_cpt_set_node
================

.. c:function:: int cfs_cpt_set_node(struct cfs_cpt_table *cptab, int cpt, int node)

    return 1 if successfully set all CPUs, otherwise return 0

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

    :param int node:
        *undescribed*

.. _`cfs_cpt_unset_node`:

cfs_cpt_unset_node
==================

.. c:function:: void cfs_cpt_unset_node(struct cfs_cpt_table *cptab, int cpt, int node)

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

    :param int node:
        *undescribed*

.. _`cfs_cpt_set_nodemask`:

cfs_cpt_set_nodemask
====================

.. c:function:: int cfs_cpt_set_nodemask(struct cfs_cpt_table *cptab, int cpt, nodemask_t *mask)

    return 1 if successfully set all CPUs, otherwise return 0

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

    :param nodemask_t \*mask:
        *undescribed*

.. _`cfs_cpt_unset_nodemask`:

cfs_cpt_unset_nodemask
======================

.. c:function:: void cfs_cpt_unset_nodemask(struct cfs_cpt_table *cptab, int cpt, nodemask_t *mask)

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

    :param nodemask_t \*mask:
        *undescribed*

.. _`cfs_cpt_clear`:

cfs_cpt_clear
=============

.. c:function:: void cfs_cpt_clear(struct cfs_cpt_table *cptab, int cpt)

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

.. _`cfs_cpt_spread_node`:

cfs_cpt_spread_node
===================

.. c:function:: int cfs_cpt_spread_node(struct cfs_cpt_table *cptab, int cpt)

    nodes in this partition, it might return a different node id each time.

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param int cpt:
        *undescribed*

.. _`cfs_cpu_ht_nsiblings`:

cfs_cpu_ht_nsiblings
====================

.. c:function:: int cfs_cpu_ht_nsiblings(int cpu)

    :param int cpu:
        *undescribed*

.. _`cfs_cpt_for_each`:

cfs_cpt_for_each
================

.. c:function::  cfs_cpt_for_each( i,  cptab)

    :param  i:
        *undescribed*

    :param  cptab:
        *undescribed*

.. This file was automatic generated / don't edit.

