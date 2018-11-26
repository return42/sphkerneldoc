.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_base.c

.. _`mpt3sas_base_check_cmd_timeout`:

mpt3sas_base_check_cmd_timeout
==============================

.. c:function:: u8 mpt3sas_base_check_cmd_timeout(struct MPT3SAS_ADAPTER *ioc, u8 status, void *mpi_request, int sz)

    Function to check timeout and command termination due to Host reset.

    :param ioc:
        per adapter object.
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param status:
        Status of issued command.
    :type status: u8

    :param mpi_request:
        mf request pointer.
    :type mpi_request: void \*

    :param sz:
        size of buffer.
    :type sz: int

.. _`mpt3sas_base_check_cmd_timeout.description`:

Description
-----------

\ ``Returns``\  - 1/0 Reset to be done or Not

.. _`_scsih_set_fwfault_debug`:

\_scsih_set_fwfault_debug
=========================

.. c:function:: int _scsih_set_fwfault_debug(const char *val, const struct kernel_param *kp)

    global setting of ioc->fwfault_debug.

    :param val:
        ?
    :type val: const char \*

    :param kp:
        ?
    :type kp: const struct kernel_param \*

.. _`_scsih_set_fwfault_debug.return`:

Return
------

?

.. _`_base_clone_reply_to_sys_mem`:

\_base_clone_reply_to_sys_mem
=============================

.. c:function:: void _base_clone_reply_to_sys_mem(struct MPT3SAS_ADAPTER *ioc, u32 reply, u32 index)

    copies reply to reply free iomem in BAR0 space.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param reply:
        reply message frame(lower 32bit addr)
    :type reply: u32

    :param index:
        System request message index.
    :type index: u32

.. _`_base_clone_mpi_to_sys_mem`:

\_base_clone_mpi_to_sys_mem
===========================

.. c:function:: void _base_clone_mpi_to_sys_mem(void *dst_iomem, void *src, u32 size)

    Writes/copies MPI frames to system/BAR0 region.

    :param dst_iomem:
        Pointer to the destination location in BAR0 space.
    :type dst_iomem: void \*

    :param src:
        Pointer to the Source data.
    :type src: void \*

    :param size:
        Size of data to be copied.
    :type size: u32

.. _`_base_clone_to_sys_mem`:

\_base_clone_to_sys_mem
=======================

.. c:function:: void _base_clone_to_sys_mem(void __iomem *dst_iomem, void *src, u32 size)

    Writes/copies data to system/BAR0 region

    :param dst_iomem:
        Pointer to the destination location in BAR0 space.
    :type dst_iomem: void __iomem \*

    :param src:
        Pointer to the Source data.
    :type src: void \*

    :param size:
        Size of data to be copied.
    :type size: u32

.. _`_base_get_chain`:

\_base_get_chain
================

.. c:function:: void __iomem* _base_get_chain(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 sge_chain_count)

    Calculates and Returns virtual chain address for the provided smid in BAR0 space.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param sge_chain_count:
        Scatter gather chain count.
    :type sge_chain_count: u8

.. _`_base_get_chain.return`:

Return
------

the chain address.

.. _`_base_get_chain_phys`:

\_base_get_chain_phys
=====================

.. c:function:: phys_addr_t _base_get_chain_phys(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 sge_chain_count)

    Calculates and Returns physical address in BAR0 for scatter gather chains, for the provided smid.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param sge_chain_count:
        Scatter gather chain count.
    :type sge_chain_count: u8

.. _`_base_get_chain_phys.return`:

Return
------

Physical chain address.

.. _`_base_get_buffer_bar0`:

\_base_get_buffer_bar0
======================

.. c:function:: void __iomem *_base_get_buffer_bar0(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    Calculates and Returns BAR0 mapped Host buffer address for the provided smid. (Each smid can have 64K starts from 17024)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

.. _`_base_get_buffer_bar0.return`:

Return
------

Pointer to buffer location in BAR0.

.. _`_base_get_buffer_phys_bar0`:

\_base_get_buffer_phys_bar0
===========================

.. c:function:: phys_addr_t _base_get_buffer_phys_bar0(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    Calculates and Returns BAR0 mapped Host buffer Physical address for the provided smid. (Each smid can have 64K starts from 17024)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

.. _`_base_get_buffer_phys_bar0.return`:

Return
------

Pointer to buffer location in BAR0.

.. _`_base_get_chain_buffer_dma_to_chain_buffer`:

\_base_get_chain_buffer_dma_to_chain_buffer
===========================================

.. c:function:: void *_base_get_chain_buffer_dma_to_chain_buffer(struct MPT3SAS_ADAPTER *ioc, dma_addr_t chain_buffer_dma)

    Iterates chain lookup list and Provides chain_buffer address for the matching dma address. (Each smid can have 64K starts from 17024)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param chain_buffer_dma:
        Chain buffer dma address.
    :type chain_buffer_dma: dma_addr_t

.. _`_base_get_chain_buffer_dma_to_chain_buffer.return`:

Return
------

Pointer to chain buffer. Or Null on Failure.

.. _`_clone_sg_entries`:

\_clone_sg_entries
==================

.. c:function:: void _clone_sg_entries(struct MPT3SAS_ADAPTER *ioc, void *mpi_request, u16 smid)

    MPI EP's scsiio and config requests are handled here. Base function for double buffering, before submitting the requests.

    :param ioc:
        per adapter object.
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_request:
        mf request pointer.
    :type mpi_request: void \*

    :param smid:
        system request message index.
    :type smid: u16

.. _`mpt3sas_remove_dead_ioc_func`:

mpt3sas_remove_dead_ioc_func
============================

.. c:function:: int mpt3sas_remove_dead_ioc_func(void *arg)

    kthread context to remove dead ioc

    :param arg:
        input argument, used to derive ioc
    :type arg: void \*

.. _`mpt3sas_remove_dead_ioc_func.return`:

Return
------

0 if controller is removed from pci subsystem.
-1 for other case.

.. _`_base_fault_reset_work`:

\_base_fault_reset_work
=======================

.. c:function:: void _base_fault_reset_work(struct work_struct *work)

    workq handling ioc fault conditions

    :param work:
        input argument, used to derive ioc
    :type work: struct work_struct \*

.. _`_base_fault_reset_work.context`:

Context
-------

sleep.

.. _`mpt3sas_base_start_watchdog`:

mpt3sas_base_start_watchdog
===========================

.. c:function:: void mpt3sas_base_start_watchdog(struct MPT3SAS_ADAPTER *ioc)

    start the fault_reset_work_q

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_base_start_watchdog.context`:

Context
-------

sleep.

.. _`mpt3sas_base_stop_watchdog`:

mpt3sas_base_stop_watchdog
==========================

.. c:function:: void mpt3sas_base_stop_watchdog(struct MPT3SAS_ADAPTER *ioc)

    stop the fault_reset_work_q

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_base_stop_watchdog.context`:

Context
-------

sleep.

.. _`mpt3sas_base_fault_info`:

mpt3sas_base_fault_info
=======================

.. c:function:: void mpt3sas_base_fault_info(struct MPT3SAS_ADAPTER *ioc, u16 fault_code)

    verbose translation of firmware FAULT code

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param fault_code:
        fault code
    :type fault_code: u16

.. _`mpt3sas_halt_firmware`:

mpt3sas_halt_firmware
=====================

.. c:function:: void mpt3sas_halt_firmware(struct MPT3SAS_ADAPTER *ioc)

    halt's mpt controller firmware

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_halt_firmware.description`:

Description
-----------

For debugging timeout related issues.  Writing 0xCOFFEE00
to the doorbell register will halt controller firmware. With
the purpose to stop both driver and firmware, the enduser can
obtain a ring buffer from controller UART.

.. _`_base_sas_ioc_info`:

\_base_sas_ioc_info
===================

.. c:function:: void _base_sas_ioc_info(struct MPT3SAS_ADAPTER *ioc, MPI2DefaultReply_t *mpi_reply, MPI2RequestHeader_t *request_hdr)

    verbose translation of the ioc status

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: MPI2DefaultReply_t \*

    :param request_hdr:
        request mf
    :type request_hdr: MPI2RequestHeader_t \*

.. _`_base_display_event_data`:

\_base_display_event_data
=========================

.. c:function:: void _base_display_event_data(struct MPT3SAS_ADAPTER *ioc, Mpi2EventNotificationReply_t *mpi_reply)

    verbose translation of firmware asyn events

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2EventNotificationReply_t \*

.. _`_base_sas_log_info`:

\_base_sas_log_info
===================

.. c:function:: void _base_sas_log_info(struct MPT3SAS_ADAPTER *ioc, u32 log_info)

    verbose translation of firmware log info

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param log_info:
        log info
    :type log_info: u32

.. _`_base_display_reply_info`:

\_base_display_reply_info
=========================

.. c:function:: void _base_display_reply_info(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param msix_index:
        MSIX table index supplied by the OS
    :type msix_index: u8

    :param reply:
        reply message frame(lower 32bit addr)
    :type reply: u32

.. _`mpt3sas_base_done`:

mpt3sas_base_done
=================

.. c:function:: u8 mpt3sas_base_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    base internal command completion routine

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param msix_index:
        MSIX table index supplied by the OS
    :type msix_index: u8

    :param reply:
        reply message frame(lower 32bit addr)
    :type reply: u32

.. _`mpt3sas_base_done.return`:

Return
------

1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_base_async_event`:

\_base_async_event
==================

.. c:function:: u8 _base_async_event(struct MPT3SAS_ADAPTER *ioc, u8 msix_index, u32 reply)

    main callback handler for firmware asyn events

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param msix_index:
        MSIX table index supplied by the OS
    :type msix_index: u8

    :param reply:
        reply message frame(lower 32bit addr)
    :type reply: u32

.. _`_base_async_event.return`:

Return
------

1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_base_get_cb_idx`:

\_base_get_cb_idx
=================

.. c:function:: u8 _base_get_cb_idx(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain the callback index

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

.. _`_base_get_cb_idx.return`:

Return
------

callback index.

.. _`_base_mask_interrupts`:

\_base_mask_interrupts
======================

.. c:function:: void _base_mask_interrupts(struct MPT3SAS_ADAPTER *ioc)

    disable interrupts

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_mask_interrupts.description`:

Description
-----------

Disabling ResetIRQ, Reply and Doorbell Interrupts

.. _`_base_unmask_interrupts`:

\_base_unmask_interrupts
========================

.. c:function:: void _base_unmask_interrupts(struct MPT3SAS_ADAPTER *ioc)

    enable interrupts

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_unmask_interrupts.description`:

Description
-----------

Enabling only Reply Interrupts

.. _`_base_interrupt`:

\_base_interrupt
================

.. c:function:: irqreturn_t _base_interrupt(int irq, void *bus_id)

    MPT adapter (IOC) specific interrupt handler.

    :param irq:
        irq number (not used)
    :type irq: int

    :param bus_id:
        bus identifier cookie == pointer to MPT_ADAPTER structure
    :type bus_id: void \*

.. _`_base_interrupt.return`:

Return
------

IRQ_HANDLED if processed, else IRQ_NONE.

.. _`_base_is_controller_msix_enabled`:

\_base_is_controller_msix_enabled
=================================

.. c:function:: int _base_is_controller_msix_enabled(struct MPT3SAS_ADAPTER *ioc)

    is controller support muli-reply queues

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_is_controller_msix_enabled.return`:

Return
------

Whether or not MSI/X is enabled.

.. _`mpt3sas_base_sync_reply_irqs`:

mpt3sas_base_sync_reply_irqs
============================

.. c:function:: void mpt3sas_base_sync_reply_irqs(struct MPT3SAS_ADAPTER *ioc)

    flush pending MSIX interrupts

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_base_sync_reply_irqs.context`:

Context
-------

non ISR conext

.. _`mpt3sas_base_sync_reply_irqs.description`:

Description
-----------

Called when a Task Management request has completed.

.. _`mpt3sas_base_release_callback_handler`:

mpt3sas_base_release_callback_handler
=====================================

.. c:function:: void mpt3sas_base_release_callback_handler(u8 cb_idx)

    clear interrupt callback handler

    :param cb_idx:
        callback index
    :type cb_idx: u8

.. _`mpt3sas_base_register_callback_handler`:

mpt3sas_base_register_callback_handler
======================================

.. c:function:: u8 mpt3sas_base_register_callback_handler(MPT_CALLBACK cb_func)

    obtain index for the interrupt callback handler

    :param cb_func:
        callback function
    :type cb_func: MPT_CALLBACK

.. _`mpt3sas_base_register_callback_handler.return`:

Return
------

Index of \ ``cb_func``\ .

.. _`mpt3sas_base_initialize_callback_handler`:

mpt3sas_base_initialize_callback_handler
========================================

.. c:function:: void mpt3sas_base_initialize_callback_handler( void)

    initialize the interrupt callback handler

    :param void:
        no arguments
    :type void: 

.. _`_base_build_zero_len_sge`:

\_base_build_zero_len_sge
=========================

.. c:function:: void _base_build_zero_len_sge(struct MPT3SAS_ADAPTER *ioc, void *paddr)

    build zero length sg entry

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param paddr:
        virtual address for SGE
    :type paddr: void \*

.. _`_base_build_zero_len_sge.description`:

Description
-----------

Create a zero length scatter gather entry to insure the IOCs hardware has
something to use if the target device goes brain dead and tries
to send data even when none is asked for.

.. _`_base_add_sg_single_32`:

\_base_add_sg_single_32
=======================

.. c:function:: void _base_add_sg_single_32(void *paddr, u32 flags_length, dma_addr_t dma_addr)

    Place a simple 32 bit SGE at address pAddr.

    :param paddr:
        virtual address for SGE
    :type paddr: void \*

    :param flags_length:
        SGE flags and data transfer length
    :type flags_length: u32

    :param dma_addr:
        Physical address
    :type dma_addr: dma_addr_t

.. _`_base_add_sg_single_64`:

\_base_add_sg_single_64
=======================

.. c:function:: void _base_add_sg_single_64(void *paddr, u32 flags_length, dma_addr_t dma_addr)

    Place a simple 64 bit SGE at address pAddr.

    :param paddr:
        virtual address for SGE
    :type paddr: void \*

    :param flags_length:
        SGE flags and data transfer length
    :type flags_length: u32

    :param dma_addr:
        Physical address
    :type dma_addr: dma_addr_t

.. _`_base_get_chain_buffer_tracker`:

\_base_get_chain_buffer_tracker
===============================

.. c:function:: struct chain_tracker *_base_get_chain_buffer_tracker(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd)

    obtain chain tracker

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param scmd:
        SCSI commands of the IO request
    :type scmd: struct scsi_cmnd \*

.. _`_base_get_chain_buffer_tracker.return`:

Return
------

chain tracker from chain_lookup table using key as
smid and smid's chain_offset.

.. _`_base_build_sg`:

\_base_build_sg
===============

.. c:function:: void _base_build_sg(struct MPT3SAS_ADAPTER *ioc, void *psge, dma_addr_t data_out_dma, size_t data_out_sz, dma_addr_t data_in_dma, size_t data_in_sz)

    build generic sg

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param psge:
        virtual address for SGE
    :type psge: void \*

    :param data_out_dma:
        physical address for WRITES
    :type data_out_dma: dma_addr_t

    :param data_out_sz:
        data xfer size for WRITES
    :type data_out_sz: size_t

    :param data_in_dma:
        physical address for READS
    :type data_in_dma: dma_addr_t

    :param data_in_sz:
        data xfer size for READS
    :type data_in_sz: size_t

.. _`_base_build_nvme_prp`:

\_base_build_nvme_prp
=====================

.. c:function:: void _base_build_nvme_prp(struct MPT3SAS_ADAPTER *ioc, u16 smid, Mpi26NVMeEncapsulatedRequest_t *nvme_encap_request, dma_addr_t data_out_dma, size_t data_out_sz, dma_addr_t data_in_dma, size_t data_in_sz)

    This function is called for NVMe end devices to build a native SGL (NVMe PRP). The native SGL is built starting in the first PRP entry of the NVMe message (PRP1).  If the data buffer is small enough to be described entirely using PRP1, then PRP2 is not used.  If needed, PRP2 is used to describe a larger data buffer.  If the data buffer is too large to describe using the two PRP entriess inside the NVMe message, then PRP1 describes the first data memory segment, and PRP2 contains a pointer to a PRP list located elsewhere in memory to describe the remaining data memory segments.  The PRP list will be contiguous.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index for getting asscociated SGL
    :type smid: u16

    :param nvme_encap_request:
        the NVMe request msg frame pointer
    :type nvme_encap_request: Mpi26NVMeEncapsulatedRequest_t \*

    :param data_out_dma:
        physical address for WRITES
    :type data_out_dma: dma_addr_t

    :param data_out_sz:
        data xfer size for WRITES
    :type data_out_sz: size_t

    :param data_in_dma:
        physical address for READS
    :type data_in_dma: dma_addr_t

    :param data_in_sz:
        data xfer size for READS
    :type data_in_sz: size_t

.. _`_base_build_nvme_prp.description`:

Description
-----------

The native SGL for NVMe devices is a Physical Region Page (PRP).  A PRP
consists of a list of PRP entries to describe a number of noncontigous
physical memory segments as a single memory buffer, just as a SGL does.  Note
however, that this function is only used by the IOCTL call, so the memory
given will be guaranteed to be contiguous.  There is no need to translate
non-contiguous SGL into a PRP in this case.  All PRPs will describe
contiguous space that is one page size each.

Each NVMe message contains two PRP entries.  The first (PRP1) either contains
a PRP list pointer or a PRP element, depending upon the command.  PRP2
contains the second PRP element if the memory being described fits within 2
PRP entries, or a PRP list pointer if the PRP spans more than two entries.

A PRP list pointer contains the address of a PRP list, structured as a linear
array of PRP entries.  Each PRP entry in this list describes a segment of
physical memory.

Each 64-bit PRP entry comprises an address and an offset field.  The address
always points at the beginning of a 4KB physical memory page, and the offset
describes where within that 4KB page the memory segment begins.  Only the
first element in a PRP list may contain a non-zero offest, implying that all
memory segments following the first begin at the start of a 4KB page.

Each PRP element normally describes 4KB of physical memory, with exceptions
for the first and last elements in the list.  If the memory being described
by the list begins at a non-zero offset within the first 4KB page, then the
first PRP element will contain a non-zero offset indicating where the region
begins within the 4KB page.  The last memory segment may end before the end
of the 4KB segment, depending upon the overall size of the memory being
described by the PRP list.

Since PRP entries lack any indication of size, the overall data buffer length
is used to determine where the end of the data memory buffer is located, and
how many PRP entries are required to describe it.

.. _`base_make_prp_nvme`:

base_make_prp_nvme
==================

.. c:function:: void base_make_prp_nvme(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd, Mpi25SCSIIORequest_t *mpi_request, u16 smid, int sge_count)

    Prepare PRPs(Physical Region Page)- SGLs specific to NVMe drives only

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param scmd:
        SCSI command from the mid-layer
    :type scmd: struct scsi_cmnd \*

    :param mpi_request:
        mpi request
    :type mpi_request: Mpi25SCSIIORequest_t \*

    :param smid:
        msg Index
    :type smid: u16

    :param sge_count:
        scatter gather element count.
    :type sge_count: int

.. _`base_make_prp_nvme.return`:

Return
------

true: PRPs are built
false: IEEE SGLs needs to be built

.. _`_base_check_pcie_native_sgl`:

\_base_check_pcie_native_sgl
============================

.. c:function:: int _base_check_pcie_native_sgl(struct MPT3SAS_ADAPTER *ioc, Mpi25SCSIIORequest_t *mpi_request, u16 smid, struct scsi_cmnd *scmd, struct _pcie_device *pcie_device)

    This function is called for PCIe end devices to determine if the driver needs to build a native SGL.  If so, that native SGL is built in the special contiguous buffers allocated especially for PCIe SGL creation.  If the driver will not build a native SGL, return TRUE and a normal IEEE SGL will be built.  Currently this routine supports NVMe.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_request:
        mf request pointer
    :type mpi_request: Mpi25SCSIIORequest_t \*

    :param smid:
        system request message index
    :type smid: u16

    :param scmd:
        scsi command
    :type scmd: struct scsi_cmnd \*

    :param pcie_device:
        points to the PCIe device's info
    :type pcie_device: struct _pcie_device \*

.. _`_base_check_pcie_native_sgl.return`:

Return
------

0 if native SGL was built, 1 if no SGL was built

.. _`_base_add_sg_single_ieee`:

\_base_add_sg_single_ieee
=========================

.. c:function:: void _base_add_sg_single_ieee(void *paddr, u8 flags, u8 chain_offset, u32 length, dma_addr_t dma_addr)

    add sg element for IEEE format

    :param paddr:
        virtual address for SGE
    :type paddr: void \*

    :param flags:
        SGE flags
    :type flags: u8

    :param chain_offset:
        number of 128 byte elements from start of segment
    :type chain_offset: u8

    :param length:
        data transfer length
    :type length: u32

    :param dma_addr:
        Physical address
    :type dma_addr: dma_addr_t

.. _`_base_build_zero_len_sge_ieee`:

\_base_build_zero_len_sge_ieee
==============================

.. c:function:: void _base_build_zero_len_sge_ieee(struct MPT3SAS_ADAPTER *ioc, void *paddr)

    build zero length sg entry for IEEE format

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param paddr:
        virtual address for SGE
    :type paddr: void \*

.. _`_base_build_zero_len_sge_ieee.description`:

Description
-----------

Create a zero length scatter gather entry to insure the IOCs hardware has
something to use if the target device goes brain dead and tries
to send data even when none is asked for.

.. _`_base_build_sg_scmd`:

\_base_build_sg_scmd
====================

.. c:function:: int _base_build_sg_scmd(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd, u16 smid, struct _pcie_device *unused)

    main sg creation routine pcie_device is unused here!

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param scmd:
        scsi command
    :type scmd: struct scsi_cmnd \*

    :param smid:
        system request message index
    :type smid: u16

    :param unused:
        unused pcie_device pointer
    :type unused: struct _pcie_device \*

.. _`_base_build_sg_scmd.context`:

Context
-------

none.

.. _`_base_build_sg_scmd.description`:

Description
-----------

The main routine that builds scatter gather table from a given
scsi request sent via the .queuecommand main handler.

.. _`_base_build_sg_scmd.return`:

Return
------

0 success, anything else error

.. _`_base_build_sg_scmd_ieee`:

\_base_build_sg_scmd_ieee
=========================

.. c:function:: int _base_build_sg_scmd_ieee(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd, u16 smid, struct _pcie_device *pcie_device)

    main sg creation routine for IEEE format

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param scmd:
        scsi command
    :type scmd: struct scsi_cmnd \*

    :param smid:
        system request message index
    :type smid: u16

    :param pcie_device:
        Pointer to pcie_device. If set, the pcie native sgl will be
        constructed on need.
    :type pcie_device: struct _pcie_device \*

.. _`_base_build_sg_scmd_ieee.context`:

Context
-------

none.

.. _`_base_build_sg_scmd_ieee.description`:

Description
-----------

The main routine that builds scatter gather table from a given
scsi request sent via the .queuecommand main handler.

.. _`_base_build_sg_scmd_ieee.return`:

Return
------

0 success, anything else error

.. _`_base_build_sg_ieee`:

\_base_build_sg_ieee
====================

.. c:function:: void _base_build_sg_ieee(struct MPT3SAS_ADAPTER *ioc, void *psge, dma_addr_t data_out_dma, size_t data_out_sz, dma_addr_t data_in_dma, size_t data_in_sz)

    build generic sg for IEEE format

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param psge:
        virtual address for SGE
    :type psge: void \*

    :param data_out_dma:
        physical address for WRITES
    :type data_out_dma: dma_addr_t

    :param data_out_sz:
        data xfer size for WRITES
    :type data_out_sz: size_t

    :param data_in_dma:
        physical address for READS
    :type data_in_dma: dma_addr_t

    :param data_in_sz:
        data xfer size for READS
    :type data_in_sz: size_t

.. _`_base_config_dma_addressing`:

\_base_config_dma_addressing
============================

.. c:function:: int _base_config_dma_addressing(struct MPT3SAS_ADAPTER *ioc, struct pci_dev *pdev)

    set dma addressing

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param pdev:
        PCI device struct
    :type pdev: struct pci_dev \*

.. _`_base_config_dma_addressing.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_check_enable_msix`:

\_base_check_enable_msix
========================

.. c:function:: int _base_check_enable_msix(struct MPT3SAS_ADAPTER *ioc)

    checks MSIX capabable.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_check_enable_msix.description`:

Description
-----------

Check to see if card is capable of MSIX, and set number
of available msix vectors

.. _`_base_free_irq`:

\_base_free_irq
===============

.. c:function:: void _base_free_irq(struct MPT3SAS_ADAPTER *ioc)

    free irq

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_free_irq.description`:

Description
-----------

Freeing respective reply_queue from the list.

.. _`_base_request_irq`:

\_base_request_irq
==================

.. c:function:: int _base_request_irq(struct MPT3SAS_ADAPTER *ioc, u8 index)

    request irq

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param index:
        msix index into vector table
    :type index: u8

.. _`_base_request_irq.description`:

Description
-----------

Inserting respective reply_queue into the list.

.. _`_base_assign_reply_queues`:

\_base_assign_reply_queues
==========================

.. c:function:: void _base_assign_reply_queues(struct MPT3SAS_ADAPTER *ioc)

    assigning msix index for each cpu

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_assign_reply_queues.description`:

Description
-----------

The enduser would need to set the affinity via /proc/irq/#/smp_affinity

It would nice if we could call irq_set_affinity, however it is not
an exported symbol

.. _`_base_disable_msix`:

\_base_disable_msix
===================

.. c:function:: void _base_disable_msix(struct MPT3SAS_ADAPTER *ioc)

    disables msix

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_enable_msix`:

\_base_enable_msix
==================

.. c:function:: int _base_enable_msix(struct MPT3SAS_ADAPTER *ioc)

    enables msix, failback to io_apic

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_base_unmap_resources`:

mpt3sas_base_unmap_resources
============================

.. c:function:: void mpt3sas_base_unmap_resources(struct MPT3SAS_ADAPTER *ioc)

    free controller resources

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_base_map_resources`:

mpt3sas_base_map_resources
==========================

.. c:function:: int mpt3sas_base_map_resources(struct MPT3SAS_ADAPTER *ioc)

    map in controller resources (io/irq/memap)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_base_map_resources.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_base_get_msg_frame`:

mpt3sas_base_get_msg_frame
==========================

.. c:function:: void *mpt3sas_base_get_msg_frame(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain request mf pointer

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index(smid zero is invalid)
    :type smid: u16

.. _`mpt3sas_base_get_msg_frame.return`:

Return
------

virt pointer to message frame.

.. _`mpt3sas_base_get_sense_buffer`:

mpt3sas_base_get_sense_buffer
=============================

.. c:function:: void *mpt3sas_base_get_sense_buffer(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain a sense buffer virt addr

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

.. _`mpt3sas_base_get_sense_buffer.return`:

Return
------

virt pointer to sense buffer.

.. _`mpt3sas_base_get_sense_buffer_dma`:

mpt3sas_base_get_sense_buffer_dma
=================================

.. c:function:: __le32 mpt3sas_base_get_sense_buffer_dma(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain a sense buffer dma addr

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

.. _`mpt3sas_base_get_sense_buffer_dma.return`:

Return
------

phys pointer to the low 32bit address of the sense buffer.

.. _`mpt3sas_base_get_pcie_sgl`:

mpt3sas_base_get_pcie_sgl
=========================

.. c:function:: void *mpt3sas_base_get_pcie_sgl(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain a PCIe SGL virt addr

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

.. _`mpt3sas_base_get_pcie_sgl.return`:

Return
------

virt pointer to a PCIe SGL.

.. _`mpt3sas_base_get_pcie_sgl_dma`:

mpt3sas_base_get_pcie_sgl_dma
=============================

.. c:function:: dma_addr_t mpt3sas_base_get_pcie_sgl_dma(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain a PCIe SGL dma addr

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

.. _`mpt3sas_base_get_pcie_sgl_dma.return`:

Return
------

phys pointer to the address of the PCIe buffer.

.. _`mpt3sas_base_get_reply_virt_addr`:

mpt3sas_base_get_reply_virt_addr
================================

.. c:function:: void *mpt3sas_base_get_reply_virt_addr(struct MPT3SAS_ADAPTER *ioc, u32 phys_addr)

    obtain reply frames virt address

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param phys_addr:
        lower 32 physical addr of the reply
    :type phys_addr: u32

.. _`mpt3sas_base_get_reply_virt_addr.description`:

Description
-----------

Converts 32bit lower physical addr into a virt address.

.. _`mpt3sas_base_get_smid`:

mpt3sas_base_get_smid
=====================

.. c:function:: u16 mpt3sas_base_get_smid(struct MPT3SAS_ADAPTER *ioc, u8 cb_idx)

    obtain a free smid from internal queue

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param cb_idx:
        callback index
    :type cb_idx: u8

.. _`mpt3sas_base_get_smid.return`:

Return
------

smid (zero is invalid)

.. _`mpt3sas_base_get_smid_scsiio`:

mpt3sas_base_get_smid_scsiio
============================

.. c:function:: u16 mpt3sas_base_get_smid_scsiio(struct MPT3SAS_ADAPTER *ioc, u8 cb_idx, struct scsi_cmnd *scmd)

    obtain a free smid from scsiio queue

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param cb_idx:
        callback index
    :type cb_idx: u8

    :param scmd:
        pointer to scsi command object
    :type scmd: struct scsi_cmnd \*

.. _`mpt3sas_base_get_smid_scsiio.return`:

Return
------

smid (zero is invalid)

.. _`mpt3sas_base_get_smid_hpr`:

mpt3sas_base_get_smid_hpr
=========================

.. c:function:: u16 mpt3sas_base_get_smid_hpr(struct MPT3SAS_ADAPTER *ioc, u8 cb_idx)

    obtain a free smid from hi-priority queue

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param cb_idx:
        callback index
    :type cb_idx: u8

.. _`mpt3sas_base_get_smid_hpr.return`:

Return
------

smid (zero is invalid)

.. _`mpt3sas_base_free_smid`:

mpt3sas_base_free_smid
======================

.. c:function:: void mpt3sas_base_free_smid(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    put smid back on free_list

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

.. _`_base_mpi_ep_writeq`:

\_base_mpi_ep_writeq
====================

.. c:function:: void _base_mpi_ep_writeq(__u64 b, volatile void __iomem *addr, spinlock_t *writeq_lock)

    32 bit write to MMIO

    :param b:
        data payload
    :type b: __u64

    :param addr:
        address in MMIO space
    :type addr: volatile void __iomem \*

    :param writeq_lock:
        spin lock
    :type writeq_lock: spinlock_t \*

.. _`_base_mpi_ep_writeq.description`:

Description
-----------

This special handling for MPI EP to take care of 32 bit
environment where its not quarenteed to send the entire word
in one transfer.

.. _`_base_writeq`:

\_base_writeq
=============

.. c:function:: void _base_writeq(__u64 b, volatile void __iomem *addr, spinlock_t *writeq_lock)

    64 bit write to MMIO

    :param b:
        data payload
    :type b: __u64

    :param addr:
        address in MMIO space
    :type addr: volatile void __iomem \*

    :param writeq_lock:
        spin lock
    :type writeq_lock: spinlock_t \*

.. _`_base_writeq.description`:

Description
-----------

Glue for handling an atomic 64 bit word to MMIO. This special handling takes
care of 32 bit environment where its not quarenteed to send the entire word
in one transfer.

.. _`_base_put_smid_mpi_ep_scsi_io`:

\_base_put_smid_mpi_ep_scsi_io
==============================

.. c:function:: void _base_put_smid_mpi_ep_scsi_io(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 handle)

    send SCSI_IO request to firmware

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param handle:
        device handle
    :type handle: u16

.. _`_base_put_smid_scsi_io`:

\_base_put_smid_scsi_io
=======================

.. c:function:: void _base_put_smid_scsi_io(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 handle)

    send SCSI_IO request to firmware

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param handle:
        device handle
    :type handle: u16

.. _`mpt3sas_base_put_smid_fast_path`:

mpt3sas_base_put_smid_fast_path
===============================

.. c:function:: void mpt3sas_base_put_smid_fast_path(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 handle)

    send fast path request to firmware

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param handle:
        device handle
    :type handle: u16

.. _`mpt3sas_base_put_smid_hi_priority`:

mpt3sas_base_put_smid_hi_priority
=================================

.. c:function:: void mpt3sas_base_put_smid_hi_priority(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 msix_task)

    send Task Management request to firmware

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param msix_task:
        msix_task will be same as msix of IO incase of task abort else 0.
    :type msix_task: u16

.. _`mpt3sas_base_put_smid_nvme_encap`:

mpt3sas_base_put_smid_nvme_encap
================================

.. c:function:: void mpt3sas_base_put_smid_nvme_encap(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    send NVMe encapsulated request to firmware

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

.. _`mpt3sas_base_put_smid_default`:

mpt3sas_base_put_smid_default
=============================

.. c:function:: void mpt3sas_base_put_smid_default(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    Default, primarily used for config pages

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

.. _`_base_display_oems_branding`:

\_base_display_OEMs_branding
============================

.. c:function:: void _base_display_OEMs_branding(struct MPT3SAS_ADAPTER *ioc)

    Display branding string

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_display_fwpkg_version`:

\_base_display_fwpkg_version
============================

.. c:function:: int _base_display_fwpkg_version(struct MPT3SAS_ADAPTER *ioc)

    sends FWUpload request to pull FWPkg version from FW Image Header.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_display_fwpkg_version.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_display_ioc_capabilities`:

\_base_display_ioc_capabilities
===============================

.. c:function:: void _base_display_ioc_capabilities(struct MPT3SAS_ADAPTER *ioc)

    Disply IOC's capabilities.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_base_update_missing_delay`:

mpt3sas_base_update_missing_delay
=================================

.. c:function:: void mpt3sas_base_update_missing_delay(struct MPT3SAS_ADAPTER *ioc, u16 device_missing_delay, u8 io_missing_delay)

    change the missing delay timers

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param device_missing_delay:
        amount of time till device is reported missing
    :type device_missing_delay: u16

    :param io_missing_delay:
        interval IO is returned when there is a missing device
    :type io_missing_delay: u8

.. _`mpt3sas_base_update_missing_delay.description`:

Description
-----------

Passed on the command line, this function will modify the device missing
delay, as well as the io missing delay. This should be called at driver
load time.

.. _`_base_static_config_pages`:

\_base_static_config_pages
==========================

.. c:function:: void _base_static_config_pages(struct MPT3SAS_ADAPTER *ioc)

    static start of day config pages

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_free_enclosure_list`:

mpt3sas_free_enclosure_list
===========================

.. c:function:: void mpt3sas_free_enclosure_list(struct MPT3SAS_ADAPTER *ioc)

    release memory

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_free_enclosure_list.description`:

Description
-----------

Free memory allocated during encloure add.

.. _`_base_release_memory_pools`:

\_base_release_memory_pools
===========================

.. c:function:: void _base_release_memory_pools(struct MPT3SAS_ADAPTER *ioc)

    release memory

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_release_memory_pools.description`:

Description
-----------

Free memory allocated from \_base_allocate_memory_pools.

.. _`is_msb_are_same`:

is_MSB_are_same
===============

.. c:function:: int is_MSB_are_same(long reply_pool_start_address, u32 pool_sz)

    checks whether all reply queues in a set are having same upper 32bits in their base memory address.

    :param reply_pool_start_address:
        Base address of a reply queue set
    :type reply_pool_start_address: long

    :param pool_sz:
        Size of single Reply Descriptor Post Queues pool size
    :type pool_sz: u32

.. _`is_msb_are_same.return`:

Return
------

1 if reply queues in a set have a same upper 32bits in their base
memory address, else 0.

.. _`_base_allocate_memory_pools`:

\_base_allocate_memory_pools
============================

.. c:function:: int _base_allocate_memory_pools(struct MPT3SAS_ADAPTER *ioc)

    allocate start of day memory pools

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_allocate_memory_pools.return`:

Return
------

0 success, anything else error.

.. _`mpt3sas_base_get_iocstate`:

mpt3sas_base_get_iocstate
=========================

.. c:function:: u32 mpt3sas_base_get_iocstate(struct MPT3SAS_ADAPTER *ioc, int cooked)

    Get the current state of a MPT adapter.

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param cooked:
        Request raw or cooked IOC state
    :type cooked: int

.. _`mpt3sas_base_get_iocstate.return`:

Return
------

all IOC Doorbell register bits if cooked==0, else just the
Doorbell bits in MPI_IOC_STATE_MASK.

.. _`_base_wait_on_iocstate`:

\_base_wait_on_iocstate
=======================

.. c:function:: int _base_wait_on_iocstate(struct MPT3SAS_ADAPTER *ioc, u32 ioc_state, int timeout)

    waiting on a particular ioc state

    :param ioc:
        ?
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param ioc_state:
        controller state { READY, OPERATIONAL, or RESET }
    :type ioc_state: u32

    :param timeout:
        timeout in second
    :type timeout: int

.. _`_base_wait_on_iocstate.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_diag_reset`:

\_base_diag_reset
=================

.. c:function:: int _base_diag_reset(struct MPT3SAS_ADAPTER *ioc)

    waiting for controller interrupt(generated by a write to the doorbell)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_diag_reset.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_diag_reset.notes`:

Notes
-----

MPI2_HIS_IOC2SYS_DB_STATUS - set to one when IOC writes to doorbell.

.. _`_base_wait_for_doorbell_ack`:

\_base_wait_for_doorbell_ack
============================

.. c:function:: int _base_wait_for_doorbell_ack(struct MPT3SAS_ADAPTER *ioc, int timeout)

    waiting for controller to read the doorbell.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param timeout:
        timeout in second
    :type timeout: int

.. _`_base_wait_for_doorbell_ack.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_wait_for_doorbell_ack.notes`:

Notes
-----

MPI2_HIS_SYS2IOC_DB_STATUS - set to one when host writes to
doorbell.

.. _`_base_wait_for_doorbell_not_used`:

\_base_wait_for_doorbell_not_used
=================================

.. c:function:: int _base_wait_for_doorbell_not_used(struct MPT3SAS_ADAPTER *ioc, int timeout)

    waiting for doorbell to not be in use

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param timeout:
        timeout in second
    :type timeout: int

.. _`_base_wait_for_doorbell_not_used.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_send_ioc_reset`:

\_base_send_ioc_reset
=====================

.. c:function:: int _base_send_ioc_reset(struct MPT3SAS_ADAPTER *ioc, u8 reset_type, int timeout)

    send doorbell reset

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param reset_type:
        currently only supports: MPI2_FUNCTION_IOC_MESSAGE_UNIT_RESET
    :type reset_type: u8

    :param timeout:
        timeout in second
    :type timeout: int

.. _`_base_send_ioc_reset.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_handshake_req_reply_wait`:

\_base_handshake_req_reply_wait
===============================

.. c:function:: int _base_handshake_req_reply_wait(struct MPT3SAS_ADAPTER *ioc, int request_bytes, u32 *request, int reply_bytes, u16 *reply, int timeout)

    send request thru doorbell interface

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param request_bytes:
        request length
    :type request_bytes: int

    :param request:
        pointer having request payload
    :type request: u32 \*

    :param reply_bytes:
        reply length
    :type reply_bytes: int

    :param reply:
        pointer to reply payload
    :type reply: u16 \*

    :param timeout:
        timeout in second
    :type timeout: int

.. _`_base_handshake_req_reply_wait.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_base_sas_iounit_control`:

mpt3sas_base_sas_iounit_control
===============================

.. c:function:: int mpt3sas_base_sas_iounit_control(struct MPT3SAS_ADAPTER *ioc, Mpi2SasIoUnitControlReply_t *mpi_reply, Mpi2SasIoUnitControlRequest_t *mpi_request)

    send sas iounit control to FW

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        the reply payload from FW
    :type mpi_reply: Mpi2SasIoUnitControlReply_t \*

    :param mpi_request:
        the request payload sent to FW
    :type mpi_request: Mpi2SasIoUnitControlRequest_t \*

.. _`mpt3sas_base_sas_iounit_control.description`:

Description
-----------

The SAS IO Unit Control Request message allows the host to perform low-level
operations, such as resets on the PHYs of the IO Unit, also allows the host
to obtain the IOC assigned device handles for a device if it has other
identifying information about the device, in addition allows the host to
remove IOC resources associated with the device.

.. _`mpt3sas_base_sas_iounit_control.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_base_scsi_enclosure_processor`:

mpt3sas_base_scsi_enclosure_processor
=====================================

.. c:function:: int mpt3sas_base_scsi_enclosure_processor(struct MPT3SAS_ADAPTER *ioc, Mpi2SepReply_t *mpi_reply, Mpi2SepRequest_t *mpi_request)

    sending request to sep device

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        the reply payload from FW
    :type mpi_reply: Mpi2SepReply_t \*

    :param mpi_request:
        the request payload sent to FW
    :type mpi_request: Mpi2SepRequest_t \*

.. _`mpt3sas_base_scsi_enclosure_processor.description`:

Description
-----------

The SCSI Enclosure Processor request message causes the IOC to
communicate with SES devices to control LED status signals.

.. _`mpt3sas_base_scsi_enclosure_processor.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_get_port_facts`:

\_base_get_port_facts
=====================

.. c:function:: int _base_get_port_facts(struct MPT3SAS_ADAPTER *ioc, int port)

    obtain port facts reply and save in ioc

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param port:
        ?
    :type port: int

.. _`_base_get_port_facts.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_wait_for_iocstate`:

\_base_wait_for_iocstate
========================

.. c:function:: int _base_wait_for_iocstate(struct MPT3SAS_ADAPTER *ioc, int timeout)

    Wait until the card is in READY or OPERATIONAL

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param timeout:
        *undescribed*
    :type timeout: int

.. _`_base_wait_for_iocstate.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_get_ioc_facts`:

\_base_get_ioc_facts
====================

.. c:function:: int _base_get_ioc_facts(struct MPT3SAS_ADAPTER *ioc)

    obtain ioc facts reply and save in ioc

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_get_ioc_facts.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_send_ioc_init`:

\_base_send_ioc_init
====================

.. c:function:: int _base_send_ioc_init(struct MPT3SAS_ADAPTER *ioc)

    send ioc_init to firmware

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_send_ioc_init.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_port_enable_done`:

mpt3sas_port_enable_done
========================

.. c:function:: u8 mpt3sas_port_enable_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    command completion routine for port enable

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param msix_index:
        MSIX table index supplied by the OS
    :type msix_index: u8

    :param reply:
        reply message frame(lower 32bit addr)
    :type reply: u32

.. _`mpt3sas_port_enable_done.return`:

Return
------

1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_base_send_port_enable`:

\_base_send_port_enable
=======================

.. c:function:: int _base_send_port_enable(struct MPT3SAS_ADAPTER *ioc)

    send port_enable(discovery stuff) to firmware

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_send_port_enable.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_port_enable`:

mpt3sas_port_enable
===================

.. c:function:: int mpt3sas_port_enable(struct MPT3SAS_ADAPTER *ioc)

    initiate firmware discovery (don't wait for reply)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_port_enable.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_determine_wait_on_discovery`:

\_base_determine_wait_on_discovery
==================================

.. c:function:: int _base_determine_wait_on_discovery(struct MPT3SAS_ADAPTER *ioc)

    desposition

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_determine_wait_on_discovery.description`:

Description
-----------

Decide whether to wait on discovery to complete. Used to either
locate boot device, or report volumes ahead of physical devices.

.. _`_base_determine_wait_on_discovery.return`:

Return
------

1 for wait, 0 for don't wait.

.. _`_base_unmask_events`:

\_base_unmask_events
====================

.. c:function:: void _base_unmask_events(struct MPT3SAS_ADAPTER *ioc, u16 event)

    turn on notification for this event

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param event:
        firmware event
    :type event: u16

.. _`_base_unmask_events.description`:

Description
-----------

The mask is stored in ioc->event_masks.

.. _`_base_event_notification`:

\_base_event_notification
=========================

.. c:function:: int _base_event_notification(struct MPT3SAS_ADAPTER *ioc)

    send event notification

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_event_notification.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_base_validate_event_type`:

mpt3sas_base_validate_event_type
================================

.. c:function:: void mpt3sas_base_validate_event_type(struct MPT3SAS_ADAPTER *ioc, u32 *event_type)

    validating event types

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param event_type:
        firmware event
    :type event_type: u32 \*

.. _`mpt3sas_base_validate_event_type.description`:

Description
-----------

This will turn on firmware event notification when application
ask for that event. We don't mask events that are already enabled.

.. _`_base_diag_reset`:

\_base_diag_reset
=================

.. c:function:: int _base_diag_reset(struct MPT3SAS_ADAPTER *ioc)

    the "big hammer" start of day reset

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_diag_reset.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_make_ioc_ready`:

\_base_make_ioc_ready
=====================

.. c:function:: int _base_make_ioc_ready(struct MPT3SAS_ADAPTER *ioc, enum reset_type type)

    put controller in READY state

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param type:
        FORCE_BIG_HAMMER or SOFT_RESET
    :type type: enum reset_type

.. _`_base_make_ioc_ready.return`:

Return
------

0 for success, non-zero for failure.

.. _`_base_make_ioc_operational`:

\_base_make_ioc_operational
===========================

.. c:function:: int _base_make_ioc_operational(struct MPT3SAS_ADAPTER *ioc)

    put controller in OPERATIONAL state

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_make_ioc_operational.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_base_free_resources`:

mpt3sas_base_free_resources
===========================

.. c:function:: void mpt3sas_base_free_resources(struct MPT3SAS_ADAPTER *ioc)

    free resources controller resources

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_base_attach`:

mpt3sas_base_attach
===================

.. c:function:: int mpt3sas_base_attach(struct MPT3SAS_ADAPTER *ioc)

    attach controller instance

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_base_attach.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_base_detach`:

mpt3sas_base_detach
===================

.. c:function:: void mpt3sas_base_detach(struct MPT3SAS_ADAPTER *ioc)

    remove controller instance

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_pre_reset_handler`:

\_base_pre_reset_handler
========================

.. c:function:: void _base_pre_reset_handler(struct MPT3SAS_ADAPTER *ioc)

    pre reset handler

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_after_reset_handler`:

\_base_after_reset_handler
==========================

.. c:function:: void _base_after_reset_handler(struct MPT3SAS_ADAPTER *ioc)

    after reset handler

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`_base_reset_done_handler`:

\_base_reset_done_handler
=========================

.. c:function:: void _base_reset_done_handler(struct MPT3SAS_ADAPTER *ioc)

    reset done handler

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_wait_for_commands_to_complete`:

mpt3sas_wait_for_commands_to_complete
=====================================

.. c:function:: void mpt3sas_wait_for_commands_to_complete(struct MPT3SAS_ADAPTER *ioc)

    reset controller

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_wait_for_commands_to_complete.description`:

Description
-----------

This function is waiting 10s for all pending commands to complete
prior to putting controller in reset.

.. _`mpt3sas_base_hard_reset_handler`:

mpt3sas_base_hard_reset_handler
===============================

.. c:function:: int mpt3sas_base_hard_reset_handler(struct MPT3SAS_ADAPTER *ioc, enum reset_type type)

    reset controller

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param type:
        FORCE_BIG_HAMMER or SOFT_RESET
    :type type: enum reset_type

.. _`mpt3sas_base_hard_reset_handler.return`:

Return
------

0 for success, non-zero for failure.

.. This file was automatic generated / don't edit.

