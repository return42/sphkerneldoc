.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/cxlflash/ocxl_hw.c

.. _`ocxlflash_psa_map`:

ocxlflash_psa_map
=================

.. c:function:: void __iomem *ocxlflash_psa_map(void *ctx_cookie)

    map the process specific MMIO space

    :param void \*ctx_cookie:
        Adapter context for which the mapping needs to be done.

.. _`ocxlflash_psa_map.return`:

Return
------

MMIO pointer of the mapped region

.. _`ocxlflash_psa_unmap`:

ocxlflash_psa_unmap
===================

.. c:function:: void ocxlflash_psa_unmap(void __iomem *addr)

    unmap the process specific MMIO space

    :param void __iomem \*addr:
        MMIO pointer to unmap.

.. _`ocxlflash_process_element`:

ocxlflash_process_element
=========================

.. c:function:: int ocxlflash_process_element(void *ctx_cookie)

    get process element of the adapter context

    :param void \*ctx_cookie:
        Adapter context associated with the process element.

.. _`ocxlflash_process_element.return`:

Return
------

process element of the adapter context

.. _`afu_map_irq`:

afu_map_irq
===========

.. c:function:: int afu_map_irq(u64 flags, struct ocxlflash_context *ctx, int num, irq_handler_t handler, void *cookie, char *name)

    map the interrupt of the adapter context

    :param u64 flags:
        Flags.

    :param struct ocxlflash_context \*ctx:
        Adapter context.

    :param int num:
        Per-context AFU interrupt number.

    :param irq_handler_t handler:
        Interrupt handler to register.

    :param void \*cookie:
        Interrupt handler private data.

    :param char \*name:
        Name of the interrupt.

.. _`afu_map_irq.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_map_afu_irq`:

ocxlflash_map_afu_irq
=====================

.. c:function:: int ocxlflash_map_afu_irq(void *ctx_cookie, int num, irq_handler_t handler, void *cookie, char *name)

    map the interrupt of the adapter context

    :param void \*ctx_cookie:
        Adapter context.

    :param int num:
        Per-context AFU interrupt number.

    :param irq_handler_t handler:
        Interrupt handler to register.

    :param void \*cookie:
        Interrupt handler private data.

    :param char \*name:
        Name of the interrupt.

.. _`ocxlflash_map_afu_irq.return`:

Return
------

0 on success, -errno on failure

.. _`afu_unmap_irq`:

afu_unmap_irq
=============

.. c:function:: void afu_unmap_irq(u64 flags, struct ocxlflash_context *ctx, int num, void *cookie)

    unmap the interrupt

    :param u64 flags:
        Flags.

    :param struct ocxlflash_context \*ctx:
        Adapter context.

    :param int num:
        Per-context AFU interrupt number.

    :param void \*cookie:
        Interrupt handler private data.

.. _`ocxlflash_unmap_afu_irq`:

ocxlflash_unmap_afu_irq
=======================

.. c:function:: void ocxlflash_unmap_afu_irq(void *ctx_cookie, int num, void *cookie)

    unmap the interrupt

    :param void \*ctx_cookie:
        Adapter context.

    :param int num:
        Per-context AFU interrupt number.

    :param void \*cookie:
        Interrupt handler private data.

.. _`ocxlflash_get_irq_objhndl`:

ocxlflash_get_irq_objhndl
=========================

.. c:function:: u64 ocxlflash_get_irq_objhndl(void *ctx_cookie, int irq)

    get the object handle for an interrupt

    :param void \*ctx_cookie:
        Context associated with the interrupt.

    :param int irq:
        Interrupt number.

.. _`ocxlflash_get_irq_objhndl.return`:

Return
------

effective address of the mapped region

.. _`ocxlflash_xsl_fault`:

ocxlflash_xsl_fault
===================

.. c:function:: void ocxlflash_xsl_fault(void *data, u64 addr, u64 dsisr)

    callback when translation error is triggered

    :param void \*data:
        Private data provided at callback registration, the context.

    :param u64 addr:
        Address that triggered the error.

    :param u64 dsisr:
        Value of dsisr register.

.. _`start_context`:

start_context
=============

.. c:function:: int start_context(struct ocxlflash_context *ctx)

    local routine to start a context

    :param struct ocxlflash_context \*ctx:
        Adapter context to be started.

.. _`start_context.description`:

Description
-----------

Assign the context specific MMIO space, add and enable the PE.

.. _`start_context.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_start_context`:

ocxlflash_start_context
=======================

.. c:function:: int ocxlflash_start_context(void *ctx_cookie)

    start a kernel context

    :param void \*ctx_cookie:
        Adapter context to be started.

.. _`ocxlflash_start_context.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_stop_context`:

ocxlflash_stop_context
======================

.. c:function:: int ocxlflash_stop_context(void *ctx_cookie)

    stop a context

    :param void \*ctx_cookie:
        Adapter context to be stopped.

.. _`ocxlflash_stop_context.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_afu_reset`:

ocxlflash_afu_reset
===================

.. c:function:: int ocxlflash_afu_reset(void *ctx_cookie)

    reset the AFU

    :param void \*ctx_cookie:
        Adapter context.

.. _`ocxlflash_set_master`:

ocxlflash_set_master
====================

.. c:function:: void ocxlflash_set_master(void *ctx_cookie)

    sets the context as master

    :param void \*ctx_cookie:
        Adapter context to set as master.

.. _`ocxlflash_get_context`:

ocxlflash_get_context
=====================

.. c:function:: void *ocxlflash_get_context(struct pci_dev *pdev, void *afu_cookie)

    obtains the context associated with the host

    :param struct pci_dev \*pdev:
        PCI device associated with the host.

    :param void \*afu_cookie:
        Hardware AFU associated with the host.

.. _`ocxlflash_get_context.return`:

Return
------

returns the pointer to host adapter context

.. _`ocxlflash_dev_context_init`:

ocxlflash_dev_context_init
==========================

.. c:function:: void *ocxlflash_dev_context_init(struct pci_dev *pdev, void *afu_cookie)

    allocate and initialize an adapter context

    :param struct pci_dev \*pdev:
        PCI device associated with the host.

    :param void \*afu_cookie:
        Hardware AFU associated with the host.

.. _`ocxlflash_dev_context_init.return`:

Return
------

returns the adapter context on success, ERR_PTR on failure

.. _`ocxlflash_release_context`:

ocxlflash_release_context
=========================

.. c:function:: int ocxlflash_release_context(void *ctx_cookie)

    releases an adapter context

    :param void \*ctx_cookie:
        Adapter context to be released.

.. _`ocxlflash_release_context.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_perst_reloads_same_image`:

ocxlflash_perst_reloads_same_image
==================================

.. c:function:: void ocxlflash_perst_reloads_same_image(void *afu_cookie, bool image)

    sets the image reload policy

    :param void \*afu_cookie:
        Hardware AFU associated with the host.

    :param bool image:
        Whether to load the same image on PERST.

.. _`ocxlflash_read_adapter_vpd`:

ocxlflash_read_adapter_vpd
==========================

.. c:function:: ssize_t ocxlflash_read_adapter_vpd(struct pci_dev *pdev, void *buf, size_t count)

    reads the adapter VPD

    :param struct pci_dev \*pdev:
        PCI device associated with the host.

    :param void \*buf:
        Buffer to get the VPD data.

    :param size_t count:
        Size of buffer (maximum bytes that can be read).

.. _`ocxlflash_read_adapter_vpd.return`:

Return
------

size of VPD on success, -errno on failure

.. _`free_afu_irqs`:

free_afu_irqs
=============

.. c:function:: void free_afu_irqs(struct ocxlflash_context *ctx)

    internal service to free interrupts

    :param struct ocxlflash_context \*ctx:
        Adapter context.

.. _`alloc_afu_irqs`:

alloc_afu_irqs
==============

.. c:function:: int alloc_afu_irqs(struct ocxlflash_context *ctx, int num)

    internal service to allocate interrupts

    :param struct ocxlflash_context \*ctx:
        Context associated with the request.

    :param int num:
        Number of interrupts requested.

.. _`alloc_afu_irqs.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_allocate_afu_irqs`:

ocxlflash_allocate_afu_irqs
===========================

.. c:function:: int ocxlflash_allocate_afu_irqs(void *ctx_cookie, int num)

    allocates the requested number of interrupts

    :param void \*ctx_cookie:
        Context associated with the request.

    :param int num:
        Number of interrupts requested.

.. _`ocxlflash_allocate_afu_irqs.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_free_afu_irqs`:

ocxlflash_free_afu_irqs
=======================

.. c:function:: void ocxlflash_free_afu_irqs(void *ctx_cookie)

    frees the interrupts of an adapter context

    :param void \*ctx_cookie:
        Adapter context.

.. _`ocxlflash_unconfig_afu`:

ocxlflash_unconfig_afu
======================

.. c:function:: void ocxlflash_unconfig_afu(struct ocxl_hw_afu *afu)

    unconfigure the AFU

    :param struct ocxl_hw_afu \*afu:
        AFU associated with the host.

.. _`ocxlflash_destroy_afu`:

ocxlflash_destroy_afu
=====================

.. c:function:: void ocxlflash_destroy_afu(void *afu_cookie)

    destroy the AFU structure

    :param void \*afu_cookie:
        AFU to be freed.

.. _`ocxlflash_config_fn`:

ocxlflash_config_fn
===================

.. c:function:: int ocxlflash_config_fn(struct pci_dev *pdev, struct ocxl_hw_afu *afu)

    configure the host function

    :param struct pci_dev \*pdev:
        PCI device associated with the host.

    :param struct ocxl_hw_afu \*afu:
        AFU associated with the host.

.. _`ocxlflash_config_fn.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_unconfig_fn`:

ocxlflash_unconfig_fn
=====================

.. c:function:: void ocxlflash_unconfig_fn(struct pci_dev *pdev, struct ocxl_hw_afu *afu)

    unconfigure the host function

    :param struct pci_dev \*pdev:
        PCI device associated with the host.

    :param struct ocxl_hw_afu \*afu:
        AFU associated with the host.

.. _`ocxlflash_map_mmio`:

ocxlflash_map_mmio
==================

.. c:function:: int ocxlflash_map_mmio(struct ocxl_hw_afu *afu)

    map the AFU MMIO space

    :param struct ocxl_hw_afu \*afu:
        AFU associated with the host.

.. _`ocxlflash_map_mmio.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_config_afu`:

ocxlflash_config_afu
====================

.. c:function:: int ocxlflash_config_afu(struct pci_dev *pdev, struct ocxl_hw_afu *afu)

    configure the host AFU

    :param struct pci_dev \*pdev:
        PCI device associated with the host.

    :param struct ocxl_hw_afu \*afu:
        AFU associated with the host.

.. _`ocxlflash_config_afu.description`:

Description
-----------

Must be called \_after\_ host function configuration.

.. _`ocxlflash_config_afu.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_create_afu`:

ocxlflash_create_afu
====================

.. c:function:: void *ocxlflash_create_afu(struct pci_dev *pdev)

    create the AFU for OCXL

    :param struct pci_dev \*pdev:
        PCI device associated with the host.

.. _`ocxlflash_create_afu.return`:

Return
------

AFU on success, NULL on failure

.. _`ctx_event_pending`:

ctx_event_pending
=================

.. c:function:: bool ctx_event_pending(struct ocxlflash_context *ctx)

    check for any event pending on the context

    :param struct ocxlflash_context \*ctx:
        Context to be checked.

.. _`ctx_event_pending.return`:

Return
------

true if there is an event pending, false if none pending

.. _`afu_poll`:

afu_poll
========

.. c:function:: unsigned int afu_poll(struct file *file, struct poll_table_struct *poll)

    poll the AFU for events on the context

    :param struct file \*file:
        File associated with the adapter context.

    :param struct poll_table_struct \*poll:
        Poll structure from the user.

.. _`afu_poll.return`:

Return
------

poll mask

.. _`afu_read`:

afu_read
========

.. c:function:: ssize_t afu_read(struct file *file, char __user *buf, size_t count, loff_t *off)

    perform a read on the context for any event

    :param struct file \*file:
        File associated with the adapter context.

    :param char __user \*buf:
        Buffer to receive the data.

    :param size_t count:
        Size of buffer (maximum bytes that can be read).

    :param loff_t \*off:
        Offset.

.. _`afu_read.return`:

Return
------

size of the data read on success, -errno on failure

.. _`afu_release`:

afu_release
===========

.. c:function:: int afu_release(struct inode *inode, struct file *file)

    release and free the context

    :param struct inode \*inode:
        File inode pointer.

    :param struct file \*file:
        File associated with the context.

.. _`afu_release.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_mmap_fault`:

ocxlflash_mmap_fault
====================

.. c:function:: int ocxlflash_mmap_fault(struct vm_fault *vmf)

    mmap fault handler

    :param struct vm_fault \*vmf:
        VM fault associated with current fault.

.. _`ocxlflash_mmap_fault.return`:

Return
------

0 on success, -errno on failure

.. _`afu_mmap`:

afu_mmap
========

.. c:function:: int afu_mmap(struct file *file, struct vm_area_struct *vma)

    map the fault handler operations

    :param struct file \*file:
        File associated with the context.

    :param struct vm_area_struct \*vma:
        VM area associated with mapping.

.. _`afu_mmap.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_get_fd`:

ocxlflash_get_fd
================

.. c:function:: struct file *ocxlflash_get_fd(void *ctx_cookie, struct file_operations *fops, int *fd)

    get file descriptor for an adapter context

    :param void \*ctx_cookie:
        Adapter context.

    :param struct file_operations \*fops:
        File operations to be associated.

    :param int \*fd:
        File descriptor to be returned back.

.. _`ocxlflash_get_fd.return`:

Return
------

pointer to the file on success, ERR_PTR on failure

.. _`ocxlflash_fops_get_context`:

ocxlflash_fops_get_context
==========================

.. c:function:: void *ocxlflash_fops_get_context(struct file *file)

    get the context associated with the file

    :param struct file \*file:
        File associated with the adapter context.

.. _`ocxlflash_fops_get_context.return`:

Return
------

pointer to the context

.. _`ocxlflash_afu_irq`:

ocxlflash_afu_irq
=================

.. c:function:: irqreturn_t ocxlflash_afu_irq(int irq, void *data)

    interrupt handler for user contexts

    :param int irq:
        Interrupt number.

    :param void \*data:
        Private data provided at interrupt registration, the context.

.. _`ocxlflash_afu_irq.return`:

Return
------

Always return IRQ_HANDLED.

.. _`ocxlflash_start_work`:

ocxlflash_start_work
====================

.. c:function:: int ocxlflash_start_work(void *ctx_cookie, u64 num_irqs)

    start a user context

    :param void \*ctx_cookie:
        Context to be started.

    :param u64 num_irqs:
        Number of interrupts requested.

.. _`ocxlflash_start_work.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_fd_mmap`:

ocxlflash_fd_mmap
=================

.. c:function:: int ocxlflash_fd_mmap(struct file *file, struct vm_area_struct *vma)

    mmap handler for adapter file descriptor

    :param struct file \*file:
        File installed with adapter file descriptor.

    :param struct vm_area_struct \*vma:
        VM area associated with mapping.

.. _`ocxlflash_fd_mmap.return`:

Return
------

0 on success, -errno on failure

.. _`ocxlflash_fd_release`:

ocxlflash_fd_release
====================

.. c:function:: int ocxlflash_fd_release(struct inode *inode, struct file *file)

    release the context associated with the file

    :param struct inode \*inode:
        File inode pointer.

    :param struct file \*file:
        File associated with the adapter context.

.. _`ocxlflash_fd_release.return`:

Return
------

0 on success, -errno on failure

.. This file was automatic generated / don't edit.

