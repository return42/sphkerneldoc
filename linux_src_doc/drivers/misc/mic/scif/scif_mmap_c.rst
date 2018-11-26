.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_mmap.c

.. _`scif_vma_open`:

scif_vma_open
=============

.. c:function:: void scif_vma_open(struct vm_area_struct *vma)

    VMA open driver callback

    :param vma:
        VMM memory area.
        The open method is called by the kernel to allow the subsystem implementing
        the VMA to initialize the area. This method is invoked any time a new
        reference to the VMA is made (when a process forks, for example).
        The one exception happens when the VMA is first created by mmap;
        in this case, the driver's mmap method is called instead.
        This function is also invoked when an existing VMA is split by the kernel
        due to a call to munmap on a subset of the VMA resulting in two VMAs.
        The kernel invokes this function only on one of the two VMAs.
    :type vma: struct vm_area_struct \*

.. _`scif_munmap`:

scif_munmap
===========

.. c:function:: void scif_munmap(struct vm_area_struct *vma)

    VMA close driver callback.

    :param vma:
        VMM memory area.
        When an area is destroyed, the kernel calls its close operation.
        Note that there's no usage count associated with VMA's; the area
        is opened and closed exactly once by each process that uses it.
    :type vma: struct vm_area_struct \*

.. _`scif_mmap`:

scif_mmap
=========

.. c:function:: int scif_mmap(struct vm_area_struct *vma, scif_epd_t epd)

    Map pages in virtual address space to a remote window.

    :param vma:
        VMM memory area.
    :type vma: struct vm_area_struct \*

    :param epd:
        endpoint descriptor
    :type epd: scif_epd_t

.. _`scif_mmap.return`:

Return
------

Upon successful completion, \ :c:func:`scif_mmap`\  returns zero
else an apt error is returned as documented in scif.h

.. This file was automatic generated / don't edit.

