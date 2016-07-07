.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lnet/libcfs/libcfs_lock.c

.. _`cfs_percpt_lock_create`:

cfs_percpt_lock_create
======================

.. c:function:: struct cfs_percpt_lock *cfs_percpt_lock_create(struct cfs_cpt_table *cptab, struct lock_class_key *keys)

    partition lock, see libcfs_private.h for more detail.

    :param struct cfs_cpt_table \*cptab:
        *undescribed*

    :param struct lock_class_key \*keys:
        *undescribed*

.. _`cfs_percpt_lock_create.description`:

Description
-----------

cpu-partition lock is designed for large-scale SMP system, so we need to
reduce cacheline conflict as possible as we can, that's the
reason we always allocate cacheline-aligned memory block.

.. _`cfs_percpt_lock`:

cfs_percpt_lock
===============

.. c:function:: void cfs_percpt_lock(struct cfs_percpt_lock *pcl, int index)

    :param struct cfs_percpt_lock \*pcl:
        *undescribed*

    :param int index:
        *undescribed*

.. _`cfs_percpt_lock.description`:

Description
-----------

\a index != CFS_PERCPT_LOCK_EX
hold private lock indexed by \a index

\a index == CFS_PERCPT_LOCK_EX
exclusively lock \ ``pcl``\  and nobody can take private lock

.. This file was automatic generated / don't edit.

