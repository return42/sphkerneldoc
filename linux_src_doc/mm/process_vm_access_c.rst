.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/process_vm_access.c

.. _`process_vm_rw_pages`:

process_vm_rw_pages
===================

.. c:function:: int process_vm_rw_pages(struct page **pages, unsigned offset, size_t len, struct iov_iter *iter, int vm_write)

    read/write pages from task specified

    :param pages:
        array of pointers to pages we want to copy
    :type pages: struct page \*\*

    :param offset:
        offset in page to start copying from/to
    :type offset: unsigned

    :param len:
        number of bytes to copy
    :type len: size_t

    :param iter:
        where to copy to/from locally
    :type iter: struct iov_iter \*

    :param vm_write:
        0 means copy from, 1 means copy to
        Returns 0 on success, error code otherwise
    :type vm_write: int

.. _`process_vm_rw_single_vec`:

process_vm_rw_single_vec
========================

.. c:function:: int process_vm_rw_single_vec(unsigned long addr, unsigned long len, struct iov_iter *iter, struct page **process_pages, struct mm_struct *mm, struct task_struct *task, int vm_write)

    read/write pages from task specified

    :param addr:
        start memory address of target process
    :type addr: unsigned long

    :param len:
        size of area to copy to/from
    :type len: unsigned long

    :param iter:
        where to copy to/from locally
    :type iter: struct iov_iter \*

    :param process_pages:
        struct pages area that can store at least
        nr_pages_to_copy struct page pointers
    :type process_pages: struct page \*\*

    :param mm:
        mm for task
    :type mm: struct mm_struct \*

    :param task:
        task to read/write from
    :type task: struct task_struct \*

    :param vm_write:
        0 means copy from, 1 means copy to
        Returns 0 on success or on failure error code
    :type vm_write: int

.. _`process_vm_rw_core`:

process_vm_rw_core
==================

.. c:function:: ssize_t process_vm_rw_core(pid_t pid, struct iov_iter *iter, const struct iovec *rvec, unsigned long riovcnt, unsigned long flags, int vm_write)

    core of reading/writing pages from task specified

    :param pid:
        PID of process to read/write from/to
    :type pid: pid_t

    :param iter:
        where to copy to/from locally
    :type iter: struct iov_iter \*

    :param rvec:
        iovec array specifying where to copy to/from in the other process
    :type rvec: const struct iovec \*

    :param riovcnt:
        size of rvec array
    :type riovcnt: unsigned long

    :param flags:
        currently unused
    :type flags: unsigned long

    :param vm_write:
        0 if reading from other process, 1 if writing to other process
    :type vm_write: int

.. _`process_vm_rw_core.description`:

Description
-----------

Returns the number of bytes read/written or error code. May
return less bytes than expected if an error occurs during the copying
process.

.. _`process_vm_rw`:

process_vm_rw
=============

.. c:function:: ssize_t process_vm_rw(pid_t pid, const struct iovec __user *lvec, unsigned long liovcnt, const struct iovec __user *rvec, unsigned long riovcnt, unsigned long flags, int vm_write)

    check iovecs before calling core routine

    :param pid:
        PID of process to read/write from/to
    :type pid: pid_t

    :param lvec:
        iovec array specifying where to copy to/from locally
    :type lvec: const struct iovec __user \*

    :param liovcnt:
        size of lvec array
    :type liovcnt: unsigned long

    :param rvec:
        iovec array specifying where to copy to/from in the other process
    :type rvec: const struct iovec __user \*

    :param riovcnt:
        size of rvec array
    :type riovcnt: unsigned long

    :param flags:
        currently unused
    :type flags: unsigned long

    :param vm_write:
        0 if reading from other process, 1 if writing to other process
    :type vm_write: int

.. _`process_vm_rw.description`:

Description
-----------

Returns the number of bytes read/written or error code. May
return less bytes than expected if an error occurs during the copying
process.

.. This file was automatic generated / don't edit.

