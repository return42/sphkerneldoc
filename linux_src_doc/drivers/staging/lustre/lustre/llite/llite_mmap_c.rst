.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/llite_mmap.c

.. _`ll_fault_io_init`:

ll_fault_io_init
================

.. c:function:: struct cl_io *ll_fault_io_init(struct lu_env *env, struct vm_area_struct *vma, pgoff_t index, unsigned long *ra_flags)

    \param vma - virtual memory area addressed to page fault \param env - corespondent lu_env to processing \param index - page index corespondent to fault. \parm ra_flags - vma readahead flags.

    :param struct lu_env \*env:
        *undescribed*

    :param struct vm_area_struct \*vma:
        *undescribed*

    :param pgoff_t index:
        *undescribed*

    :param unsigned long \*ra_flags:
        *undescribed*

.. _`ll_fault_io_init.description`:

Description
-----------

\return error codes from cl_io_init.

.. _`ll_fault0`:

ll_fault0
=========

.. c:function:: int ll_fault0(struct vm_area_struct *vma, struct vm_fault *vmf)

    :fault() method, called by VM to server page fault (both in kernel and user space).

    :param struct vm_area_struct \*vma:
        *undescribed*

    :param struct vm_fault \*vmf:
        *undescribed*

.. _`ll_fault0.description`:

Description
-----------

\param vma - is virtual area struct related to page fault
\param vmf - structure which describe type and address where hit fault

\return allocated and filled \_locked\_ page for address
\retval VM_FAULT_ERROR on general error
\retval NOPAGE_OOM not have memory for allocate new page

.. _`ll_vm_open`:

ll_vm_open
==========

.. c:function:: void ll_vm_open(struct vm_area_struct *vma)

    we track the mapped vma count in vvp_object::vob_mmap_cnt.

    :param struct vm_area_struct \*vma:
        *undescribed*

.. _`ll_vm_close`:

ll_vm_close
===========

.. c:function:: void ll_vm_close(struct vm_area_struct *vma)

    :param struct vm_area_struct \*vma:
        *undescribed*

.. This file was automatic generated / don't edit.

