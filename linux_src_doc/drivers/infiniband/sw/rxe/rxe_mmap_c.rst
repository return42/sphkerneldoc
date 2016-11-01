.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rxe/rxe_mmap.c

.. _`rxe_mmap`:

rxe_mmap
========

.. c:function:: int rxe_mmap(struct ib_ucontext *context, struct vm_area_struct *vma)

    create a new mmap region

    :param struct ib_ucontext \*context:
        the IB user context of the process making the \ :c:func:`mmap`\  call

    :param struct vm_area_struct \*vma:
        the VMA to be initialized
        Return zero if the mmap is OK. Otherwise, return an errno.

.. This file was automatic generated / don't edit.

