.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/mmap.c

.. _`rvt_mmap_init`:

rvt_mmap_init
=============

.. c:function:: void rvt_mmap_init(struct rvt_dev_info *rdi)

    init link list and lock for mem map

    :param rdi:
        rvt dev struct
    :type rdi: struct rvt_dev_info \*

.. _`rvt_release_mmap_info`:

rvt_release_mmap_info
=====================

.. c:function:: void rvt_release_mmap_info(struct kref *ref)

    free mmap info structure

    :param ref:
        a pointer to the kref within struct rvt_mmap_info
    :type ref: struct kref \*

.. _`rvt_mmap`:

rvt_mmap
========

.. c:function:: int rvt_mmap(struct ib_ucontext *context, struct vm_area_struct *vma)

    create a new mmap region

    :param context:
        the IB user context of the process making the \ :c:func:`mmap`\  call
    :type context: struct ib_ucontext \*

    :param vma:
        the VMA to be initialized
    :type vma: struct vm_area_struct \*

.. _`rvt_mmap.return`:

Return
------

zero if the mmap is OK. Otherwise, return an errno.

.. _`rvt_create_mmap_info`:

rvt_create_mmap_info
====================

.. c:function:: struct rvt_mmap_info *rvt_create_mmap_info(struct rvt_dev_info *rdi, u32 size, struct ib_ucontext *context, void *obj)

    allocate information for hfi1_mmap

    :param rdi:
        rvt dev struct
    :type rdi: struct rvt_dev_info \*

    :param size:
        size in bytes to map
    :type size: u32

    :param context:
        user context
    :type context: struct ib_ucontext \*

    :param obj:
        opaque pointer to a cq, wq etc
    :type obj: void \*

.. _`rvt_create_mmap_info.return`:

Return
------

rvt_mmap struct on success

.. _`rvt_update_mmap_info`:

rvt_update_mmap_info
====================

.. c:function:: void rvt_update_mmap_info(struct rvt_dev_info *rdi, struct rvt_mmap_info *ip, u32 size, void *obj)

    update a mem map

    :param rdi:
        rvt dev struct
    :type rdi: struct rvt_dev_info \*

    :param ip:
        mmap info pointer
    :type ip: struct rvt_mmap_info \*

    :param size:
        size to grow by
    :type size: u32

    :param obj:
        opaque pointer to cq, wq, etc.
    :type obj: void \*

.. This file was automatic generated / don't edit.

