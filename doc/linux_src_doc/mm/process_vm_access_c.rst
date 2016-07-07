.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/process_vm_access.c

.. _`process_vm_rw_pages`:

process_vm_rw_pages
===================

.. c:function:: int process_vm_rw_pages(struct page **pages, unsigned offset, size_t len, struct iov_iter *iter, int vm_write)

    read/write pages from task specified

    :param struct page \*\*pages:
        array of pointers to pages we want to copy

    :param unsigned offset:
        *undescribed*

    :param size_t len:
        number of bytes to copy

    :param struct iov_iter \*iter:
        where to copy to/from locally

    :param int vm_write:
        0 means copy from, 1 means copy to
        Returns 0 on success, error code otherwise

.. _`process_vm_rw_single_vec`:

process_vm_rw_single_vec
========================

.. c:function:: int process_vm_rw_single_vec(unsigned long addr, unsigned long len, struct iov_iter *iter, struct page **process_pages, struct mm_struct *mm, struct task_struct *task, int vm_write)

    read/write pages from task specified

    :param unsigned long addr:
        start memory address of target process

    :param unsigned long len:
        size of area to copy to/from

    :param struct iov_iter \*iter:
        where to copy to/from locally

    :param struct page \*\*process_pages:
        struct pages area that can store at least
        nr_pages_to_copy struct page pointers

    :param struct mm_struct \*mm:
        mm for task

    :param struct task_struct \*task:
        task to read/write from

    :param int vm_write:
        0 means copy from, 1 means copy to
        Returns 0 on success or on failure error code

.. _`process_vm_rw_core`:

process_vm_rw_core
==================

.. c:function:: ssize_t process_vm_rw_core(pid_t pid, struct iov_iter *iter, const struct iovec *rvec, unsigned long riovcnt, unsigned long flags, int vm_write)

    core of reading/writing pages from task specified

    :param pid_t pid:
        PID of process to read/write from/to

    :param struct iov_iter \*iter:
        where to copy to/from locally

    :param const struct iovec \*rvec:
        iovec array specifying where to copy to/from in the other process

    :param unsigned long riovcnt:
        size of rvec array

    :param unsigned long flags:
        currently unused

    :param int vm_write:
        0 if reading from other process, 1 if writing to other process
        Returns the number of bytes read/written or error code. May
        return less bytes than expected if an error occurs during the copying
        process.

.. _`process_vm_rw`:

process_vm_rw
=============

.. c:function:: ssize_t process_vm_rw(pid_t pid, const struct iovec __user *lvec, unsigned long liovcnt, const struct iovec __user *rvec, unsigned long riovcnt, unsigned long flags, int vm_write)

    check iovecs before calling core routine

    :param pid_t pid:
        PID of process to read/write from/to

    :param const struct iovec __user \*lvec:
        iovec array specifying where to copy to/from locally

    :param unsigned long liovcnt:
        size of lvec array

    :param const struct iovec __user \*rvec:
        iovec array specifying where to copy to/from in the other process

    :param unsigned long riovcnt:
        size of rvec array

    :param unsigned long flags:
        currently unused

    :param int vm_write:
        0 if reading from other process, 1 if writing to other process
        Returns the number of bytes read/written or error code. May
        return less bytes than expected if an error occurs during the copying
        process.

.. This file was automatic generated / don't edit.

