.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_base.c

.. _`_scsih_set_fwfault_debug`:

_scsih_set_fwfault_debug
========================

.. c:function:: int _scsih_set_fwfault_debug(const char *val, struct kernel_param *kp)

    global setting of ioc->fwfault_debug.

    :param const char \*val:
        *undescribed*

    :param struct kernel_param \*kp:
        *undescribed*

.. _`mpt3sas_remove_dead_ioc_func`:

mpt3sas_remove_dead_ioc_func
============================

.. c:function:: int mpt3sas_remove_dead_ioc_func(void *arg)

    kthread context to remove dead ioc

    :param void \*arg:
        input argument, used to derive ioc

.. _`mpt3sas_remove_dead_ioc_func.description`:

Description
-----------

Return 0 if controller is removed from pci subsystem.
Return -1 for other case.

.. _`_base_fault_reset_work`:

_base_fault_reset_work
======================

.. c:function:: void _base_fault_reset_work(struct work_struct *work)

    workq handling ioc fault conditions

    :param struct work_struct \*work:
        input argument, used to derive ioc

.. _`_base_fault_reset_work.context`:

Context
-------

sleep.

.. _`_base_fault_reset_work.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_base_start_watchdog`:

mpt3sas_base_start_watchdog
===========================

.. c:function:: void mpt3sas_base_start_watchdog(struct MPT3SAS_ADAPTER *ioc)

    start the fault_reset_work_q

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_base_start_watchdog.context`:

Context
-------

sleep.

.. _`mpt3sas_base_start_watchdog.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_base_stop_watchdog`:

mpt3sas_base_stop_watchdog
==========================

.. c:function:: void mpt3sas_base_stop_watchdog(struct MPT3SAS_ADAPTER *ioc)

    stop the fault_reset_work_q

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_base_stop_watchdog.context`:

Context
-------

sleep.

.. _`mpt3sas_base_stop_watchdog.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_base_fault_info`:

mpt3sas_base_fault_info
=======================

.. c:function:: void mpt3sas_base_fault_info(struct MPT3SAS_ADAPTER *ioc, u16 fault_code)

    verbose translation of firmware FAULT code

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 fault_code:
        fault code

.. _`mpt3sas_base_fault_info.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_halt_firmware`:

mpt3sas_halt_firmware
=====================

.. c:function:: void mpt3sas_halt_firmware(struct MPT3SAS_ADAPTER *ioc)

    halt's mpt controller firmware

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_halt_firmware.description`:

Description
-----------

For debugging timeout related issues.  Writing 0xCOFFEE00
to the doorbell register will halt controller firmware. With
the purpose to stop both driver and firmware, the enduser can
obtain a ring buffer from controller UART.

.. _`_base_sas_ioc_info`:

_base_sas_ioc_info
==================

.. c:function:: void _base_sas_ioc_info(struct MPT3SAS_ADAPTER *ioc, MPI2DefaultReply_t *mpi_reply, MPI2RequestHeader_t *request_hdr)

    verbose translation of the ioc status

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param MPI2DefaultReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param MPI2RequestHeader_t \*request_hdr:
        request mf

.. _`_base_sas_ioc_info.description`:

Description
-----------

Return nothing.

.. _`_base_display_event_data`:

_base_display_event_data
========================

.. c:function:: void _base_display_event_data(struct MPT3SAS_ADAPTER *ioc, Mpi2EventNotificationReply_t *mpi_reply)

    verbose translation of firmware asyn events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventNotificationReply_t \*mpi_reply:
        reply mf payload returned from firmware

.. _`_base_display_event_data.description`:

Description
-----------

Return nothing.

.. _`_base_sas_log_info`:

_base_sas_log_info
==================

.. c:function:: void _base_sas_log_info(struct MPT3SAS_ADAPTER *ioc, u32 log_info)

    verbose translation of firmware log info

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u32 log_info:
        log info

.. _`_base_sas_log_info.description`:

Description
-----------

Return nothing.

.. _`_base_display_reply_info`:

_base_display_reply_info
========================

.. c:function:: void _base_display_reply_info(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`_base_display_reply_info.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_base_done`:

mpt3sas_base_done
=================

.. c:function:: u8 mpt3sas_base_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    base internal command completion routine

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`mpt3sas_base_done.description`:

Description
-----------

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_base_async_event`:

_base_async_event
=================

.. c:function:: u8 _base_async_event(struct MPT3SAS_ADAPTER *ioc, u8 msix_index, u32 reply)

    main callback handler for firmware asyn events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`_base_async_event.description`:

Description
-----------

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_base_get_cb_idx`:

_base_get_cb_idx
================

.. c:function:: u8 _base_get_cb_idx(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain the callback index

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`_base_get_cb_idx.description`:

Description
-----------

Return callback index.

.. _`_base_mask_interrupts`:

_base_mask_interrupts
=====================

.. c:function:: void _base_mask_interrupts(struct MPT3SAS_ADAPTER *ioc)

    disable interrupts

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_mask_interrupts.description`:

Description
-----------

Disabling ResetIRQ, Reply and Doorbell Interrupts

Return nothing.

.. _`_base_unmask_interrupts`:

_base_unmask_interrupts
=======================

.. c:function:: void _base_unmask_interrupts(struct MPT3SAS_ADAPTER *ioc)

    enable interrupts

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_unmask_interrupts.description`:

Description
-----------

Enabling only Reply Interrupts

Return nothing.

.. _`_base_interrupt`:

_base_interrupt
===============

.. c:function:: irqreturn_t _base_interrupt(int irq, void *bus_id)

    MPT adapter (IOC) specific interrupt handler.

    :param int irq:
        irq number (not used)

    :param void \*bus_id:
        bus identifier cookie == pointer to MPT_ADAPTER structure

.. _`_base_interrupt.description`:

Description
-----------

Return IRQ_HANDLE if processed, else IRQ_NONE.

.. _`_base_is_controller_msix_enabled`:

_base_is_controller_msix_enabled
================================

.. c:function:: int _base_is_controller_msix_enabled(struct MPT3SAS_ADAPTER *ioc)

    is controller support muli-reply queues

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_base_sync_reply_irqs`:

mpt3sas_base_sync_reply_irqs
============================

.. c:function:: void mpt3sas_base_sync_reply_irqs(struct MPT3SAS_ADAPTER *ioc)

    flush pending MSIX interrupts

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_base_sync_reply_irqs.context`:

Context
-------

non ISR conext

.. _`mpt3sas_base_sync_reply_irqs.description`:

Description
-----------

Called when a Task Management request has completed.

Return nothing.

.. _`mpt3sas_base_release_callback_handler`:

mpt3sas_base_release_callback_handler
=====================================

.. c:function:: void mpt3sas_base_release_callback_handler(u8 cb_idx)

    clear interrupt callback handler

    :param u8 cb_idx:
        callback index

.. _`mpt3sas_base_release_callback_handler.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_base_register_callback_handler`:

mpt3sas_base_register_callback_handler
======================================

.. c:function:: u8 mpt3sas_base_register_callback_handler(MPT_CALLBACK cb_func)

    obtain index for the interrupt callback handler

    :param MPT_CALLBACK cb_func:
        callback function

.. _`mpt3sas_base_register_callback_handler.description`:

Description
-----------

Returns cb_func.

.. _`mpt3sas_base_initialize_callback_handler`:

mpt3sas_base_initialize_callback_handler
========================================

.. c:function:: void mpt3sas_base_initialize_callback_handler( void)

    initialize the interrupt callback handler

    :param  void:
        no arguments

.. _`mpt3sas_base_initialize_callback_handler.description`:

Description
-----------

Return nothing.

.. _`_base_build_zero_len_sge`:

_base_build_zero_len_sge
========================

.. c:function:: void _base_build_zero_len_sge(struct MPT3SAS_ADAPTER *ioc, void *paddr)

    build zero length sg entry

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param void \*paddr:
        virtual address for SGE

.. _`_base_build_zero_len_sge.description`:

Description
-----------

Create a zero length scatter gather entry to insure the IOCs hardware has
something to use if the target device goes brain dead and tries
to send data even when none is asked for.

Return nothing.

.. _`_base_add_sg_single_32`:

_base_add_sg_single_32
======================

.. c:function:: void _base_add_sg_single_32(void *paddr, u32 flags_length, dma_addr_t dma_addr)

    Place a simple 32 bit SGE at address pAddr.

    :param void \*paddr:
        virtual address for SGE

    :param u32 flags_length:
        SGE flags and data transfer length

    :param dma_addr_t dma_addr:
        Physical address

.. _`_base_add_sg_single_32.description`:

Description
-----------

Return nothing.

.. _`_base_add_sg_single_64`:

_base_add_sg_single_64
======================

.. c:function:: void _base_add_sg_single_64(void *paddr, u32 flags_length, dma_addr_t dma_addr)

    Place a simple 64 bit SGE at address pAddr.

    :param void \*paddr:
        virtual address for SGE

    :param u32 flags_length:
        SGE flags and data transfer length

    :param dma_addr_t dma_addr:
        Physical address

.. _`_base_add_sg_single_64.description`:

Description
-----------

Return nothing.

.. _`_base_get_chain_buffer_tracker`:

_base_get_chain_buffer_tracker
==============================

.. c:function:: struct chain_tracker *_base_get_chain_buffer_tracker(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain chain tracker

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        smid associated to an IO request

.. _`_base_get_chain_buffer_tracker.description`:

Description
-----------

Returns chain tracker(from ioc->free_chain_list)

.. _`_base_build_sg`:

_base_build_sg
==============

.. c:function:: void _base_build_sg(struct MPT3SAS_ADAPTER *ioc, void *psge, dma_addr_t data_out_dma, size_t data_out_sz, dma_addr_t data_in_dma, size_t data_in_sz)

    build generic sg

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param void \*psge:
        virtual address for SGE

    :param dma_addr_t data_out_dma:
        physical address for WRITES

    :param size_t data_out_sz:
        data xfer size for WRITES

    :param dma_addr_t data_in_dma:
        physical address for READS

    :param size_t data_in_sz:
        data xfer size for READS

.. _`_base_build_sg.description`:

Description
-----------

Return nothing.

.. _`_base_add_sg_single_ieee`:

_base_add_sg_single_ieee
========================

.. c:function:: void _base_add_sg_single_ieee(void *paddr, u8 flags, u8 chain_offset, u32 length, dma_addr_t dma_addr)

    add sg element for IEEE format

    :param void \*paddr:
        virtual address for SGE

    :param u8 flags:
        SGE flags

    :param u8 chain_offset:
        number of 128 byte elements from start of segment

    :param u32 length:
        data transfer length

    :param dma_addr_t dma_addr:
        Physical address

.. _`_base_add_sg_single_ieee.description`:

Description
-----------

Return nothing.

.. _`_base_build_zero_len_sge_ieee`:

_base_build_zero_len_sge_ieee
=============================

.. c:function:: void _base_build_zero_len_sge_ieee(struct MPT3SAS_ADAPTER *ioc, void *paddr)

    build zero length sg entry for IEEE format

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param void \*paddr:
        virtual address for SGE

.. _`_base_build_zero_len_sge_ieee.description`:

Description
-----------

Create a zero length scatter gather entry to insure the IOCs hardware has
something to use if the target device goes brain dead and tries
to send data even when none is asked for.

Return nothing.

.. _`_base_build_sg_scmd`:

_base_build_sg_scmd
===================

.. c:function:: int _base_build_sg_scmd(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd, u16 smid)

    main sg creation routine

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct scsi_cmnd \*scmd:
        scsi command

    :param u16 smid:
        system request message index

.. _`_base_build_sg_scmd.context`:

Context
-------

none.

.. _`_base_build_sg_scmd.description`:

Description
-----------

The main routine that builds scatter gather table from a given
scsi request sent via the .queuecommand main handler.

Returns 0 success, anything else error

.. _`_base_build_sg_scmd_ieee`:

_base_build_sg_scmd_ieee
========================

.. c:function:: int _base_build_sg_scmd_ieee(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd, u16 smid)

    main sg creation routine for IEEE format

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct scsi_cmnd \*scmd:
        scsi command

    :param u16 smid:
        system request message index

.. _`_base_build_sg_scmd_ieee.context`:

Context
-------

none.

.. _`_base_build_sg_scmd_ieee.description`:

Description
-----------

The main routine that builds scatter gather table from a given
scsi request sent via the .queuecommand main handler.

Returns 0 success, anything else error

.. _`_base_build_sg_ieee`:

_base_build_sg_ieee
===================

.. c:function:: void _base_build_sg_ieee(struct MPT3SAS_ADAPTER *ioc, void *psge, dma_addr_t data_out_dma, size_t data_out_sz, dma_addr_t data_in_dma, size_t data_in_sz)

    build generic sg for IEEE format

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param void \*psge:
        virtual address for SGE

    :param dma_addr_t data_out_dma:
        physical address for WRITES

    :param size_t data_out_sz:
        data xfer size for WRITES

    :param dma_addr_t data_in_dma:
        physical address for READS

    :param size_t data_in_sz:
        data xfer size for READS

.. _`_base_build_sg_ieee.description`:

Description
-----------

Return nothing.

.. _`_base_config_dma_addressing`:

_base_config_dma_addressing
===========================

.. c:function:: int _base_config_dma_addressing(struct MPT3SAS_ADAPTER *ioc, struct pci_dev *pdev)

    set dma addressing

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct pci_dev \*pdev:
        PCI device struct

.. _`_base_config_dma_addressing.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_check_enable_msix`:

_base_check_enable_msix
=======================

.. c:function:: int _base_check_enable_msix(struct MPT3SAS_ADAPTER *ioc)

    checks MSIX capabable.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_check_enable_msix.description`:

Description
-----------

Check to see if card is capable of MSIX, and set number
of available msix vectors

.. _`_base_free_irq`:

_base_free_irq
==============

.. c:function:: void _base_free_irq(struct MPT3SAS_ADAPTER *ioc)

    free irq

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_free_irq.description`:

Description
-----------

Freeing respective reply_queue from the list.

.. _`_base_request_irq`:

_base_request_irq
=================

.. c:function:: int _base_request_irq(struct MPT3SAS_ADAPTER *ioc, u8 index, u32 vector)

    request irq

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u8 index:
        msix index into vector table

    :param u32 vector:
        irq vector

.. _`_base_request_irq.description`:

Description
-----------

Inserting respective reply_queue into the list.

.. _`_base_assign_reply_queues`:

_base_assign_reply_queues
=========================

.. c:function:: void _base_assign_reply_queues(struct MPT3SAS_ADAPTER *ioc)

    assigning msix index for each cpu

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_assign_reply_queues.description`:

Description
-----------

The enduser would need to set the affinity via /proc/irq/#/smp_affinity

It would nice if we could call irq_set_affinity, however it is not
an exported symbol

.. _`_base_disable_msix`:

_base_disable_msix
==================

.. c:function:: void _base_disable_msix(struct MPT3SAS_ADAPTER *ioc)

    disables msix

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_enable_msix`:

_base_enable_msix
=================

.. c:function:: int _base_enable_msix(struct MPT3SAS_ADAPTER *ioc)

    enables msix, failback to io_apic

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_base_unmap_resources`:

mpt3sas_base_unmap_resources
============================

.. c:function:: void mpt3sas_base_unmap_resources(struct MPT3SAS_ADAPTER *ioc)

    free controller resources

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_base_map_resources`:

mpt3sas_base_map_resources
==========================

.. c:function:: int mpt3sas_base_map_resources(struct MPT3SAS_ADAPTER *ioc)

    map in controller resources (io/irq/memap)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_base_map_resources.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_base_get_msg_frame`:

mpt3sas_base_get_msg_frame
==========================

.. c:function:: void *mpt3sas_base_get_msg_frame(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain request mf pointer

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index(smid zero is invalid)

.. _`mpt3sas_base_get_msg_frame.description`:

Description
-----------

Returns virt pointer to message frame.

.. _`mpt3sas_base_get_sense_buffer`:

mpt3sas_base_get_sense_buffer
=============================

.. c:function:: void *mpt3sas_base_get_sense_buffer(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain a sense buffer virt addr

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`mpt3sas_base_get_sense_buffer.description`:

Description
-----------

Returns virt pointer to sense buffer.

.. _`mpt3sas_base_get_sense_buffer_dma`:

mpt3sas_base_get_sense_buffer_dma
=================================

.. c:function:: __le32 mpt3sas_base_get_sense_buffer_dma(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    obtain a sense buffer dma addr

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`mpt3sas_base_get_sense_buffer_dma.description`:

Description
-----------

Returns phys pointer to the low 32bit address of the sense buffer.

.. _`mpt3sas_base_get_reply_virt_addr`:

mpt3sas_base_get_reply_virt_addr
================================

.. c:function:: void *mpt3sas_base_get_reply_virt_addr(struct MPT3SAS_ADAPTER *ioc, u32 phys_addr)

    obtain reply frames virt address

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u32 phys_addr:
        lower 32 physical addr of the reply

.. _`mpt3sas_base_get_reply_virt_addr.description`:

Description
-----------

Converts 32bit lower physical addr into a virt address.

.. _`mpt3sas_base_get_smid`:

mpt3sas_base_get_smid
=====================

.. c:function:: u16 mpt3sas_base_get_smid(struct MPT3SAS_ADAPTER *ioc, u8 cb_idx)

    obtain a free smid from internal queue

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u8 cb_idx:
        callback index

.. _`mpt3sas_base_get_smid.description`:

Description
-----------

Returns smid (zero is invalid)

.. _`mpt3sas_base_get_smid_scsiio`:

mpt3sas_base_get_smid_scsiio
============================

.. c:function:: u16 mpt3sas_base_get_smid_scsiio(struct MPT3SAS_ADAPTER *ioc, u8 cb_idx, struct scsi_cmnd *scmd)

    obtain a free smid from scsiio queue

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u8 cb_idx:
        callback index

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

.. _`mpt3sas_base_get_smid_scsiio.description`:

Description
-----------

Returns smid (zero is invalid)

.. _`mpt3sas_base_get_smid_hpr`:

mpt3sas_base_get_smid_hpr
=========================

.. c:function:: u16 mpt3sas_base_get_smid_hpr(struct MPT3SAS_ADAPTER *ioc, u8 cb_idx)

    obtain a free smid from hi-priority queue

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u8 cb_idx:
        callback index

.. _`mpt3sas_base_get_smid_hpr.description`:

Description
-----------

Returns smid (zero is invalid)

.. _`mpt3sas_base_free_smid`:

mpt3sas_base_free_smid
======================

.. c:function:: void mpt3sas_base_free_smid(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    put smid back on free_list

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`mpt3sas_base_free_smid.description`:

Description
-----------

Return nothing.

.. _`_base_writeq`:

_base_writeq
============

.. c:function:: void _base_writeq(__u64 b, volatile void __iomem *addr, spinlock_t *writeq_lock)

    64 bit write to MMIO

    :param __u64 b:
        data payload

    :param volatile void __iomem \*addr:
        address in MMIO space

    :param spinlock_t \*writeq_lock:
        spin lock

.. _`_base_writeq.description`:

Description
-----------

Glue for handling an atomic 64 bit word to MMIO. This special handling takes
care of 32 bit environment where its not quarenteed to send the entire word
in one transfer.

.. _`_base_put_smid_scsi_io`:

_base_put_smid_scsi_io
======================

.. c:function:: void _base_put_smid_scsi_io(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 handle)

    send SCSI_IO request to firmware

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u16 handle:
        device handle

.. _`_base_put_smid_scsi_io.description`:

Description
-----------

Return nothing.

.. _`_base_put_smid_fast_path`:

_base_put_smid_fast_path
========================

.. c:function:: void _base_put_smid_fast_path(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 handle)

    send fast path request to firmware

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u16 handle:
        device handle

.. _`_base_put_smid_fast_path.description`:

Description
-----------

Return nothing.

.. _`_base_put_smid_hi_priority`:

_base_put_smid_hi_priority
==========================

.. c:function:: void _base_put_smid_hi_priority(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 msix_task)

    send Task Management request to firmware

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u16 msix_task:
        msix_task will be same as msix of IO incase of task abort else 0.
        Return nothing.

.. _`_base_put_smid_default`:

_base_put_smid_default
======================

.. c:function:: void _base_put_smid_default(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    Default, primarily used for config pages

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`_base_put_smid_default.description`:

Description
-----------

Return nothing.

.. _`_base_put_smid_scsi_io_atomic`:

_base_put_smid_scsi_io_atomic
=============================

.. c:function:: void _base_put_smid_scsi_io_atomic(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 handle)

    send SCSI_IO request to firmware using Atomic Request Descriptor

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u16 handle:
        device handle, unused in this function, for function type match

.. _`_base_put_smid_scsi_io_atomic.description`:

Description
-----------

Return nothing.

.. _`_base_put_smid_fast_path_atomic`:

_base_put_smid_fast_path_atomic
===============================

.. c:function:: void _base_put_smid_fast_path_atomic(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 handle)

    send fast path request to firmware using Atomic Request Descriptor

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u16 handle:
        device handle, unused in this function, for function type match
        Return nothing

.. _`_base_put_smid_hi_priority_atomic`:

_base_put_smid_hi_priority_atomic
=================================

.. c:function:: void _base_put_smid_hi_priority_atomic(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 msix_task)

    send Task Management request to firmware using Atomic Request Descriptor

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u16 msix_task:
        msix_task will be same as msix of IO incase of task abort else 0

.. _`_base_put_smid_hi_priority_atomic.description`:

Description
-----------

Return nothing.

.. _`_base_put_smid_default_atomic`:

_base_put_smid_default_atomic
=============================

.. c:function:: void _base_put_smid_default_atomic(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    Default, primarily used for config pages use Atomic Request Descriptor

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`_base_put_smid_default_atomic.description`:

Description
-----------

Return nothing.

.. _`_base_display_oems_branding`:

_base_display_OEMs_branding
===========================

.. c:function:: void _base_display_OEMs_branding(struct MPT3SAS_ADAPTER *ioc)

    Display branding string

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_display_oems_branding.description`:

Description
-----------

Return nothing.

.. _`_base_display_ioc_capabilities`:

_base_display_ioc_capabilities
==============================

.. c:function:: void _base_display_ioc_capabilities(struct MPT3SAS_ADAPTER *ioc)

    Disply IOC's capabilities.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_display_ioc_capabilities.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_base_update_missing_delay`:

mpt3sas_base_update_missing_delay
=================================

.. c:function:: void mpt3sas_base_update_missing_delay(struct MPT3SAS_ADAPTER *ioc, u16 device_missing_delay, u8 io_missing_delay)

    change the missing delay timers

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 device_missing_delay:
        amount of time till device is reported missing

    :param u8 io_missing_delay:
        interval IO is returned when there is a missing device

.. _`mpt3sas_base_update_missing_delay.description`:

Description
-----------

Return nothing.

Passed on the command line, this function will modify the device missing
delay, as well as the io missing delay. This should be called at driver
load time.

.. _`_base_static_config_pages`:

_base_static_config_pages
=========================

.. c:function:: void _base_static_config_pages(struct MPT3SAS_ADAPTER *ioc)

    static start of day config pages

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_static_config_pages.description`:

Description
-----------

Return nothing.

.. _`_base_release_memory_pools`:

_base_release_memory_pools
==========================

.. c:function:: void _base_release_memory_pools(struct MPT3SAS_ADAPTER *ioc)

    release memory

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_release_memory_pools.description`:

Description
-----------

Free memory allocated from \_base_allocate_memory_pools.

Return nothing.

.. _`_base_allocate_memory_pools`:

_base_allocate_memory_pools
===========================

.. c:function:: int _base_allocate_memory_pools(struct MPT3SAS_ADAPTER *ioc)

    allocate start of day memory pools

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_allocate_memory_pools.description`:

Description
-----------

Returns 0 success, anything else error

.. _`mpt3sas_base_get_iocstate`:

mpt3sas_base_get_iocstate
=========================

.. c:function:: u32 mpt3sas_base_get_iocstate(struct MPT3SAS_ADAPTER *ioc, int cooked)

    Get the current state of a MPT adapter.

    :param struct MPT3SAS_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int cooked:
        Request raw or cooked IOC state

.. _`mpt3sas_base_get_iocstate.description`:

Description
-----------

Returns all IOC Doorbell register bits if cooked==0, else just the
Doorbell bits in MPI_IOC_STATE_MASK.

.. _`_base_wait_on_iocstate`:

_base_wait_on_iocstate
======================

.. c:function:: int _base_wait_on_iocstate(struct MPT3SAS_ADAPTER *ioc, u32 ioc_state, int timeout)

    waiting on a particular ioc state

    :param struct MPT3SAS_ADAPTER \*ioc:
        *undescribed*

    :param u32 ioc_state:
        controller state { READY, OPERATIONAL, or RESET }

    :param int timeout:
        timeout in second

.. _`_base_wait_on_iocstate.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_diag_reset`:

_base_diag_reset
================

.. c:function:: int _base_diag_reset(struct MPT3SAS_ADAPTER *ioc)

    waiting for controller interrupt(generated by a write to the doorbell)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_diag_reset.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_diag_reset.notes`:

Notes
-----

MPI2_HIS_IOC2SYS_DB_STATUS - set to one when IOC writes to doorbell.

.. _`_base_wait_for_doorbell_ack`:

_base_wait_for_doorbell_ack
===========================

.. c:function:: int _base_wait_for_doorbell_ack(struct MPT3SAS_ADAPTER *ioc, int timeout)

    waiting for controller to read the doorbell.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param int timeout:
        timeout in second

.. _`_base_wait_for_doorbell_ack.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_wait_for_doorbell_ack.notes`:

Notes
-----

MPI2_HIS_SYS2IOC_DB_STATUS - set to one when host writes to
doorbell.

.. _`_base_wait_for_doorbell_not_used`:

_base_wait_for_doorbell_not_used
================================

.. c:function:: int _base_wait_for_doorbell_not_used(struct MPT3SAS_ADAPTER *ioc, int timeout)

    waiting for doorbell to not be in use

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param int timeout:
        timeout in second

.. _`_base_wait_for_doorbell_not_used.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_send_ioc_reset`:

_base_send_ioc_reset
====================

.. c:function:: int _base_send_ioc_reset(struct MPT3SAS_ADAPTER *ioc, u8 reset_type, int timeout)

    send doorbell reset

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u8 reset_type:
        currently only supports: MPI2_FUNCTION_IOC_MESSAGE_UNIT_RESET

    :param int timeout:
        timeout in second

.. _`_base_send_ioc_reset.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_handshake_req_reply_wait`:

_base_handshake_req_reply_wait
==============================

.. c:function:: int _base_handshake_req_reply_wait(struct MPT3SAS_ADAPTER *ioc, int request_bytes, u32 *request, int reply_bytes, u16 *reply, int timeout)

    send request thru doorbell interface

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param int request_bytes:
        request length

    :param u32 \*request:
        pointer having request payload

    :param int reply_bytes:
        reply length

    :param u16 \*reply:
        pointer to reply payload

    :param int timeout:
        timeout in second

.. _`_base_handshake_req_reply_wait.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_base_sas_iounit_control`:

mpt3sas_base_sas_iounit_control
===============================

.. c:function:: int mpt3sas_base_sas_iounit_control(struct MPT3SAS_ADAPTER *ioc, Mpi2SasIoUnitControlReply_t *mpi_reply, Mpi2SasIoUnitControlRequest_t *mpi_request)

    send sas iounit control to FW

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2SasIoUnitControlReply_t \*mpi_reply:
        the reply payload from FW

    :param Mpi2SasIoUnitControlRequest_t \*mpi_request:
        the request payload sent to FW

.. _`mpt3sas_base_sas_iounit_control.description`:

Description
-----------

The SAS IO Unit Control Request message allows the host to perform low-level
operations, such as resets on the PHYs of the IO Unit, also allows the host
to obtain the IOC assigned device handles for a device if it has other
identifying information about the device, in addition allows the host to
remove IOC resources associated with the device.

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_base_scsi_enclosure_processor`:

mpt3sas_base_scsi_enclosure_processor
=====================================

.. c:function:: int mpt3sas_base_scsi_enclosure_processor(struct MPT3SAS_ADAPTER *ioc, Mpi2SepReply_t *mpi_reply, Mpi2SepRequest_t *mpi_request)

    sending request to sep device

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2SepReply_t \*mpi_reply:
        the reply payload from FW

    :param Mpi2SepRequest_t \*mpi_request:
        the request payload sent to FW

.. _`mpt3sas_base_scsi_enclosure_processor.description`:

Description
-----------

The SCSI Enclosure Processor request message causes the IOC to
communicate with SES devices to control LED status signals.

Returns 0 for success, non-zero for failure.

.. _`_base_get_port_facts`:

_base_get_port_facts
====================

.. c:function:: int _base_get_port_facts(struct MPT3SAS_ADAPTER *ioc, int port)

    obtain port facts reply and save in ioc

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param int port:
        *undescribed*

.. _`_base_get_port_facts.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_wait_for_iocstate`:

_base_wait_for_iocstate
=======================

.. c:function:: int _base_wait_for_iocstate(struct MPT3SAS_ADAPTER *ioc, int timeout)

    Wait until the card is in READY or OPERATIONAL

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param int timeout:
        *undescribed*

.. _`_base_wait_for_iocstate.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_get_ioc_facts`:

_base_get_ioc_facts
===================

.. c:function:: int _base_get_ioc_facts(struct MPT3SAS_ADAPTER *ioc)

    obtain ioc facts reply and save in ioc

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_get_ioc_facts.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_send_ioc_init`:

_base_send_ioc_init
===================

.. c:function:: int _base_send_ioc_init(struct MPT3SAS_ADAPTER *ioc)

    send ioc_init to firmware

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_send_ioc_init.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_port_enable_done`:

mpt3sas_port_enable_done
========================

.. c:function:: u8 mpt3sas_port_enable_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    command completion routine for port enable

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`mpt3sas_port_enable_done.description`:

Description
-----------

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_base_send_port_enable`:

_base_send_port_enable
======================

.. c:function:: int _base_send_port_enable(struct MPT3SAS_ADAPTER *ioc)

    send port_enable(discovery stuff) to firmware

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_send_port_enable.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_port_enable`:

mpt3sas_port_enable
===================

.. c:function:: int mpt3sas_port_enable(struct MPT3SAS_ADAPTER *ioc)

    initiate firmware discovery (don't wait for reply)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_port_enable.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_determine_wait_on_discovery`:

_base_determine_wait_on_discovery
=================================

.. c:function:: int _base_determine_wait_on_discovery(struct MPT3SAS_ADAPTER *ioc)

    desposition

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_determine_wait_on_discovery.description`:

Description
-----------

Decide whether to wait on discovery to complete. Used to either
locate boot device, or report volumes ahead of physical devices.

Returns 1 for wait, 0 for don't wait

.. _`_base_unmask_events`:

_base_unmask_events
===================

.. c:function:: void _base_unmask_events(struct MPT3SAS_ADAPTER *ioc, u16 event)

    turn on notification for this event

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 event:
        firmware event

.. _`_base_unmask_events.description`:

Description
-----------

The mask is stored in ioc->event_masks.

.. _`_base_event_notification`:

_base_event_notification
========================

.. c:function:: int _base_event_notification(struct MPT3SAS_ADAPTER *ioc)

    send event notification

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_event_notification.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_base_validate_event_type`:

mpt3sas_base_validate_event_type
================================

.. c:function:: void mpt3sas_base_validate_event_type(struct MPT3SAS_ADAPTER *ioc, u32 *event_type)

    validating event types

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u32 \*event_type:
        *undescribed*

.. _`mpt3sas_base_validate_event_type.description`:

Description
-----------

This will turn on firmware event notification when application
ask for that event. We don't mask events that are already enabled.

.. _`_base_diag_reset`:

_base_diag_reset
================

.. c:function:: int _base_diag_reset(struct MPT3SAS_ADAPTER *ioc)

    the "big hammer" start of day reset

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_diag_reset.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_make_ioc_ready`:

_base_make_ioc_ready
====================

.. c:function:: int _base_make_ioc_ready(struct MPT3SAS_ADAPTER *ioc, enum reset_type type)

    put controller in READY state

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param enum reset_type type:
        FORCE_BIG_HAMMER or SOFT_RESET

.. _`_base_make_ioc_ready.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`_base_make_ioc_operational`:

_base_make_ioc_operational
==========================

.. c:function:: int _base_make_ioc_operational(struct MPT3SAS_ADAPTER *ioc)

    put controller in OPERATIONAL state

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_base_make_ioc_operational.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_base_free_resources`:

mpt3sas_base_free_resources
===========================

.. c:function:: void mpt3sas_base_free_resources(struct MPT3SAS_ADAPTER *ioc)

    free resources controller resources

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_base_free_resources.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_base_attach`:

mpt3sas_base_attach
===================

.. c:function:: int mpt3sas_base_attach(struct MPT3SAS_ADAPTER *ioc)

    attach controller instance

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_base_attach.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_base_detach`:

mpt3sas_base_detach
===================

.. c:function:: void mpt3sas_base_detach(struct MPT3SAS_ADAPTER *ioc)

    remove controller instance

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_base_detach.description`:

Description
-----------

Return nothing.

.. _`_base_reset_handler`:

_base_reset_handler
===================

.. c:function:: void _base_reset_handler(struct MPT3SAS_ADAPTER *ioc, int reset_phase)

    reset callback handler (for base)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param int reset_phase:
        phase

.. _`_base_reset_handler.description`:

Description
-----------

The handler for doing any required cleanup or initialization.

The reset phase can be MPT3_IOC_PRE_RESET, MPT3_IOC_AFTER_RESET,
MPT3_IOC_DONE_RESET

Return nothing.

.. _`_wait_for_commands_to_complete`:

_wait_for_commands_to_complete
==============================

.. c:function:: void _wait_for_commands_to_complete(struct MPT3SAS_ADAPTER *ioc)

    reset controller

    :param struct MPT3SAS_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

.. _`_wait_for_commands_to_complete.description`:

Description
-----------

This function waiting(3s) for all pending commands to complete
prior to putting controller in reset.

.. _`mpt3sas_base_hard_reset_handler`:

mpt3sas_base_hard_reset_handler
===============================

.. c:function:: int mpt3sas_base_hard_reset_handler(struct MPT3SAS_ADAPTER *ioc, enum reset_type type)

    reset controller

    :param struct MPT3SAS_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param enum reset_type type:
        FORCE_BIG_HAMMER or SOFT_RESET

.. _`mpt3sas_base_hard_reset_handler.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. This file was automatic generated / don't edit.

