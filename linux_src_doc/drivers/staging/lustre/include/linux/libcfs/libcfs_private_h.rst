.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/include/linux/libcfs/libcfs_private.h

.. _`linvrnt`:

LINVRNT
=======

.. c:function::  LINVRNT( exp)

    the time. \ :c:func:`LINVRNT`\  has to be explicitly enabled by CONFIG_LUSTRE_DEBUG_EXPENSIVE_CHECK option.

    :param  exp:
        *undescribed*

.. _`libcfs_alloc_gfp`:

LIBCFS_ALLOC_GFP
================

.. c:function::  LIBCFS_ALLOC_GFP( ptr,  size,  mask)

    :param  ptr:
        *undescribed*

    :param  size:
        *undescribed*

    :param  mask:
        *undescribed*

.. _`libcfs_alloc`:

LIBCFS_ALLOC
============

.. c:function::  LIBCFS_ALLOC( ptr,  size)

    :param  ptr:
        *undescribed*

    :param  size:
        *undescribed*

.. _`libcfs_alloc_atomic`:

LIBCFS_ALLOC_ATOMIC
===================

.. c:function::  LIBCFS_ALLOC_ATOMIC( ptr,  size)

    sleeping allocator

    :param  ptr:
        *undescribed*

    :param  size:
        *undescribed*

.. _`libcfs_cpt_alloc_gfp`:

LIBCFS_CPT_ALLOC_GFP
====================

.. c:function::  LIBCFS_CPT_ALLOC_GFP( ptr,  cptab,  cpt,  size,  mask)

    \a cptab != NULL, \a cpt is CPU partition id of \a cptab \a cptab == NULL, \a cpt is HW NUMA node id

    :param  ptr:
        *undescribed*

    :param  cptab:
        *undescribed*

    :param  cpt:
        *undescribed*

    :param  size:
        *undescribed*

    :param  mask:
        *undescribed*

.. This file was automatic generated / don't edit.

