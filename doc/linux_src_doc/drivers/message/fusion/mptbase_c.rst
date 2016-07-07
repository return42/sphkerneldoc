.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/message/fusion/mptbase.c

.. _`mpt_get_cb_idx`:

mpt_get_cb_idx
==============

.. c:function:: u8 mpt_get_cb_idx(MPT_DRIVER_CLASS dclass)

    obtain cb_idx for registered driver

    :param MPT_DRIVER_CLASS dclass:
        class driver enum

.. _`mpt_get_cb_idx.description`:

Description
-----------

Returns cb_idx, or zero means it wasn't found

.. _`mpt_is_discovery_complete`:

mpt_is_discovery_complete
=========================

.. c:function:: int mpt_is_discovery_complete(MPT_ADAPTER *ioc)

    determine if discovery has completed

    :param MPT_ADAPTER \*ioc:
        per adatper instance

.. _`mpt_is_discovery_complete.description`:

Description
-----------

Returns 1 when discovery completed, else zero.

.. _`mpt_remove_dead_ioc_func`:

mpt_remove_dead_ioc_func
========================

.. c:function:: int mpt_remove_dead_ioc_func(void *arg)

    kthread context to remove dead ioc

    :param void \*arg:
        input argument, used to derive ioc

.. _`mpt_remove_dead_ioc_func.description`:

Description
-----------

Return 0 if controller is removed from pci subsystem.
Return -1 for other case.

.. _`mpt_fault_reset_work`:

mpt_fault_reset_work
====================

.. c:function:: void mpt_fault_reset_work(struct work_struct *work)

    work performed on workq after ioc fault

    :param struct work_struct \*work:
        input argument, used to derive ioc

.. _`mpt_interrupt`:

mpt_interrupt
=============

.. c:function:: irqreturn_t mpt_interrupt(int irq, void *bus_id)

    MPT adapter (IOC) specific interrupt handler.

    :param int irq:
        irq number (not used)

    :param void \*bus_id:
        bus identifier cookie == pointer to MPT_ADAPTER structure

.. _`mpt_interrupt.description`:

Description
-----------

This routine is registered via the \ :c:func:`request_irq`\  kernel API call,
and handles all interrupts generated from a specific MPT adapter
(also referred to as a IO Controller or IOC).
This routine must clear the interrupt from the adapter and does
so by reading the reply FIFO.  Multiple replies may be processed
per single call to this routine.

This routine handles register-level access of the adapter but
dispatches (calls) a protocol-specific callback routine to handle
the protocol-specific details of the MPT request completion.

.. _`mptbase_reply`:

mptbase_reply
=============

.. c:function:: int mptbase_reply(MPT_ADAPTER *ioc, MPT_FRAME_HDR *req, MPT_FRAME_HDR *reply)

    MPT base driver's callback routine

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param MPT_FRAME_HDR \*req:
        Pointer to original MPT request frame

    :param MPT_FRAME_HDR \*reply:
        Pointer to MPT reply frame (NULL if TurboReply)

.. _`mptbase_reply.description`:

Description
-----------

MPT base driver's callback routine; all base driver
"internal" request/reply processing is routed here.
Currently used for EventNotification and EventAck handling.

Returns 1 indicating original alloc'd request frame ptr
should be freed, or 0 if it shouldn't.

.. _`mpt_register`:

mpt_register
============

.. c:function:: u8 mpt_register(MPT_CALLBACK cbfunc, MPT_DRIVER_CLASS dclass, char *func_name)

    Register protocol-specific main callback handler.

    :param MPT_CALLBACK cbfunc:
        callback function pointer

    :param MPT_DRIVER_CLASS dclass:
        Protocol driver's class (\ ``MPT_DRIVER_CLASS``\  enum value)

    :param char \*func_name:
        call function's name

.. _`mpt_register.description`:

Description
-----------

This routine is called by a protocol-specific driver (SCSI host,
LAN, SCSI target) to register its reply callback routine.  Each
protocol-specific driver must do this before it will be able to
use any IOC resources, such as obtaining request frames.

.. _`mpt_register.notes`:

NOTES
-----

The SCSI protocol driver currently calls this routine thrice
in order to register separate callbacks; one for "normal" SCSI IO;
one for MptScsiTaskMgmt requests; one for Scan/DV requests.

Returns u8 valued "handle" in the range (and S.O.D. order)
{N,...,7,6,5,...,1} if successful.
A return value of MPT_MAX_PROTOCOL_DRIVERS (including zero!) should be
considered an error by the caller.

.. _`mpt_deregister`:

mpt_deregister
==============

.. c:function:: void mpt_deregister(u8 cb_idx)

    Deregister a protocol drivers resources.

    :param u8 cb_idx:
        previously registered callback handle

.. _`mpt_deregister.description`:

Description
-----------

Each protocol-specific driver should call this routine when its
module is unloaded.

.. _`mpt_event_register`:

mpt_event_register
==================

.. c:function:: int mpt_event_register(u8 cb_idx, MPT_EVHANDLER ev_cbfunc)

    Register protocol-specific event callback handler.

    :param u8 cb_idx:
        previously registered (via mpt_register) callback handle

    :param MPT_EVHANDLER ev_cbfunc:
        callback function

.. _`mpt_event_register.description`:

Description
-----------

This routine can be called by one or more protocol-specific drivers
if/when they choose to be notified of MPT events.

Returns 0 for success.

.. _`mpt_event_deregister`:

mpt_event_deregister
====================

.. c:function:: void mpt_event_deregister(u8 cb_idx)

    Deregister protocol-specific event callback handler

    :param u8 cb_idx:
        previously registered callback handle

.. _`mpt_event_deregister.description`:

Description
-----------

Each protocol-specific driver should call this routine
when it does not (or can no longer) handle events,
or when its module is unloaded.

.. _`mpt_reset_register`:

mpt_reset_register
==================

.. c:function:: int mpt_reset_register(u8 cb_idx, MPT_RESETHANDLER reset_func)

    Register protocol-specific IOC reset handler.

    :param u8 cb_idx:
        previously registered (via mpt_register) callback handle

    :param MPT_RESETHANDLER reset_func:
        reset function

.. _`mpt_reset_register.description`:

Description
-----------

This routine can be called by one or more protocol-specific drivers
if/when they choose to be notified of IOC resets.

Returns 0 for success.

.. _`mpt_reset_deregister`:

mpt_reset_deregister
====================

.. c:function:: void mpt_reset_deregister(u8 cb_idx)

    Deregister protocol-specific IOC reset handler.

    :param u8 cb_idx:
        previously registered callback handle

.. _`mpt_reset_deregister.description`:

Description
-----------

Each protocol-specific driver should call this routine
when it does not (or can no longer) handle IOC reset handling,
or when its module is unloaded.

.. _`mpt_device_driver_register`:

mpt_device_driver_register
==========================

.. c:function:: int mpt_device_driver_register(struct mpt_pci_driver *dd_cbfunc, u8 cb_idx)

    Register device driver hooks

    :param struct mpt_pci_driver \*dd_cbfunc:
        driver callbacks struct

    :param u8 cb_idx:
        MPT protocol driver index

.. _`mpt_device_driver_deregister`:

mpt_device_driver_deregister
============================

.. c:function:: void mpt_device_driver_deregister(u8 cb_idx)

    DeRegister device driver hooks

    :param u8 cb_idx:
        MPT protocol driver index

.. _`mpt_get_msg_frame`:

mpt_get_msg_frame
=================

.. c:function:: MPT_FRAME_HDR*mpt_get_msg_frame(u8 cb_idx, MPT_ADAPTER *ioc)

    Obtain an MPT request frame from the pool

    :param u8 cb_idx:
        Handle of registered MPT protocol driver

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

.. _`mpt_get_msg_frame.description`:

Description
-----------

Obtain an MPT request frame from the pool (of 1024) that are
allocated per MPT adapter.

Returns pointer to a MPT request frame or \ ``NULL``\  if none are available
or IOC is not active.

.. _`mpt_put_msg_frame`:

mpt_put_msg_frame
=================

.. c:function:: void mpt_put_msg_frame(u8 cb_idx, MPT_ADAPTER *ioc, MPT_FRAME_HDR *mf)

    Send a protocol-specific MPT request frame to an IOC

    :param u8 cb_idx:
        Handle of registered MPT protocol driver

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

    :param MPT_FRAME_HDR \*mf:
        Pointer to MPT request frame

.. _`mpt_put_msg_frame.description`:

Description
-----------

This routine posts an MPT request frame to the request post FIFO of a
specific MPT adapter.

.. _`mpt_put_msg_frame_hi_pri`:

mpt_put_msg_frame_hi_pri
========================

.. c:function:: void mpt_put_msg_frame_hi_pri(u8 cb_idx, MPT_ADAPTER *ioc, MPT_FRAME_HDR *mf)

    Send a hi-pri protocol-specific MPT request frame

    :param u8 cb_idx:
        Handle of registered MPT protocol driver

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

    :param MPT_FRAME_HDR \*mf:
        Pointer to MPT request frame

.. _`mpt_put_msg_frame_hi_pri.description`:

Description
-----------

Send a protocol-specific MPT request frame to an IOC using
hi-priority request queue.

This routine posts an MPT request frame to the request post FIFO of a
specific MPT adapter.

.. _`mpt_free_msg_frame`:

mpt_free_msg_frame
==================

.. c:function:: void mpt_free_msg_frame(MPT_ADAPTER *ioc, MPT_FRAME_HDR *mf)

    Place MPT request frame back on FreeQ.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

    :param MPT_FRAME_HDR \*mf:
        Pointer to MPT request frame

.. _`mpt_free_msg_frame.description`:

Description
-----------

This routine places a MPT request frame back on the MPT adapter's
FreeQ.

.. _`mpt_add_sge`:

mpt_add_sge
===========

.. c:function:: void mpt_add_sge(void *pAddr, u32 flagslength, dma_addr_t dma_addr)

    Place a simple 32 bit SGE at address pAddr.

    :param void \*pAddr:
        virtual address for SGE

    :param u32 flagslength:
        SGE flags and data transfer length

    :param dma_addr_t dma_addr:
        Physical address

.. _`mpt_add_sge.description`:

Description
-----------

This routine places a MPT request frame back on the MPT adapter's
FreeQ.

.. _`mpt_add_sge_64bit`:

mpt_add_sge_64bit
=================

.. c:function:: void mpt_add_sge_64bit(void *pAddr, u32 flagslength, dma_addr_t dma_addr)

    Place a simple 64 bit SGE at address pAddr.

    :param void \*pAddr:
        virtual address for SGE

    :param u32 flagslength:
        SGE flags and data transfer length

    :param dma_addr_t dma_addr:
        Physical address

.. _`mpt_add_sge_64bit.description`:

Description
-----------

This routine places a MPT request frame back on the MPT adapter's
FreeQ.

.. _`mpt_add_sge_64bit_1078`:

mpt_add_sge_64bit_1078
======================

.. c:function:: void mpt_add_sge_64bit_1078(void *pAddr, u32 flagslength, dma_addr_t dma_addr)

    Place a simple 64 bit SGE at address pAddr (1078 workaround).

    :param void \*pAddr:
        virtual address for SGE

    :param u32 flagslength:
        SGE flags and data transfer length

    :param dma_addr_t dma_addr:
        Physical address

.. _`mpt_add_sge_64bit_1078.description`:

Description
-----------

This routine places a MPT request frame back on the MPT adapter's
FreeQ.

.. _`mpt_add_chain`:

mpt_add_chain
=============

.. c:function:: void mpt_add_chain(void *pAddr, u8 next, u16 length, dma_addr_t dma_addr)

    Place a 32 bit chain SGE at address pAddr.

    :param void \*pAddr:
        virtual address for SGE

    :param u8 next:
        nextChainOffset value (u32's)

    :param u16 length:
        length of next SGL segment

    :param dma_addr_t dma_addr:
        Physical address

.. _`mpt_add_chain_64bit`:

mpt_add_chain_64bit
===================

.. c:function:: void mpt_add_chain_64bit(void *pAddr, u8 next, u16 length, dma_addr_t dma_addr)

    Place a 64 bit chain SGE at address pAddr.

    :param void \*pAddr:
        virtual address for SGE

    :param u8 next:
        nextChainOffset value (u32's)

    :param u16 length:
        length of next SGL segment

    :param dma_addr_t dma_addr:
        Physical address

.. _`mpt_send_handshake_request`:

mpt_send_handshake_request
==========================

.. c:function:: int mpt_send_handshake_request(u8 cb_idx, MPT_ADAPTER *ioc, int reqBytes, u32 *req, int sleepFlag)

    Send MPT request via doorbell handshake method.

    :param u8 cb_idx:
        Handle of registered MPT protocol driver

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

    :param int reqBytes:
        Size of the request in bytes

    :param u32 \*req:
        Pointer to MPT request frame

    :param int sleepFlag:
        Use schedule if CAN_SLEEP else use udelay.

.. _`mpt_send_handshake_request.description`:

Description
-----------

This routine is used exclusively to send MptScsiTaskMgmt
requests since they are required to be sent via doorbell handshake.

.. _`mpt_send_handshake_request.note`:

NOTE
----

It is the callers responsibility to byte-swap fields in the
request which are greater than 1 byte in size.

Returns 0 for success, non-zero for failure.

.. _`mpt_host_page_access_control`:

mpt_host_page_access_control
============================

.. c:function:: int mpt_host_page_access_control(MPT_ADAPTER *ioc, u8 access_control_value, int sleepFlag)

    control the IOC's Host Page Buffer access

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

    :param u8 access_control_value:
        define bits below

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`mpt_host_page_access_control.description`:

Description
-----------

Provides mechanism for the host driver to control the IOC's
Host Page Buffer access.

Access Control Value - bits[15:12]
0h Reserved
1h Enable Access { MPI_DB_HPBAC_ENABLE_ACCESS }
2h Disable Access { MPI_DB_HPBAC_DISABLE_ACCESS }
3h Free Buffer { MPI_DB_HPBAC_FREE_BUFFER }

Returns 0 for success, non-zero for failure.

.. _`mpt_host_page_alloc`:

mpt_host_page_alloc
===================

.. c:function:: int mpt_host_page_alloc(MPT_ADAPTER *ioc, pIOCInit_t ioc_init)

    allocate system memory for the fw

    :param MPT_ADAPTER \*ioc:
        Pointer to pointer to IOC adapter

    :param pIOCInit_t ioc_init:
        Pointer to ioc init config page

.. _`mpt_host_page_alloc.description`:

Description
-----------

If we already allocated memory in past, then resend the same pointer.
Returns 0 for success, non-zero for failure.

.. _`mpt_verify_adapter`:

mpt_verify_adapter
==================

.. c:function:: int mpt_verify_adapter(int iocid, MPT_ADAPTER **iocpp)

    Given IOC identifier, set pointer to its adapter structure.

    :param int iocid:
        IOC unique identifier (integer)

    :param MPT_ADAPTER \*\*iocpp:
        Pointer to pointer to IOC adapter

.. _`mpt_verify_adapter.description`:

Description
-----------

Given a unique IOC identifier, set pointer to the associated MPT
adapter structure.

Returns iocid and sets iocpp if iocid is found.
Returns -1 if iocid is not found.

.. _`mpt_get_product_name`:

mpt_get_product_name
====================

.. c:function:: const char*mpt_get_product_name(u16 vendor, u16 device, u8 revision)

    returns product string

    :param u16 vendor:
        pci vendor id

    :param u16 device:
        pci device id

    :param u8 revision:
        pci revision id

.. _`mpt_get_product_name.description`:

Description
-----------

Returns product string displayed when driver loads,
in /proc/mpt/summary and /sysfs/class/scsi_host/host<X>/version_product

.. _`mpt_mapresources`:

mpt_mapresources
================

.. c:function:: int mpt_mapresources(MPT_ADAPTER *ioc)

    map in memory mapped io

    :param MPT_ADAPTER \*ioc:
        Pointer to pointer to IOC adapter

.. _`mpt_attach`:

mpt_attach
==========

.. c:function:: int mpt_attach(struct pci_dev *pdev, const struct pci_device_id *id)

    Install a PCI intelligent MPT adapter.

    :param struct pci_dev \*pdev:
        Pointer to pci_dev structure

    :param const struct pci_device_id \*id:
        PCI device ID information

.. _`mpt_attach.description`:

Description
-----------

This routine performs all the steps necessary to bring the IOC of
a MPT adapter to a OPERATIONAL state.  This includes registering
memory regions, registering the interrupt, and allocating request
and reply memory pools.

This routine also pre-fetches the LAN MAC address of a Fibre Channel
MPT adapter.

Returns 0 for success, non-zero for failure.

.. _`mpt_attach.todo`:

TODO
----

Add support for polled controllers

.. _`mpt_detach`:

mpt_detach
==========

.. c:function:: void mpt_detach(struct pci_dev *pdev)

    Remove a PCI intelligent MPT adapter.

    :param struct pci_dev \*pdev:
        Pointer to pci_dev structure

.. _`mpt_suspend`:

mpt_suspend
===========

.. c:function:: int mpt_suspend(struct pci_dev *pdev, pm_message_t state)

    Fusion MPT base driver suspend routine.

    :param struct pci_dev \*pdev:
        Pointer to pci_dev structure

    :param pm_message_t state:
        new state to enter

.. _`mpt_resume`:

mpt_resume
==========

.. c:function:: int mpt_resume(struct pci_dev *pdev)

    Fusion MPT base driver resume routine.

    :param struct pci_dev \*pdev:
        Pointer to pci_dev structure

.. _`mpt_do_ioc_recovery`:

mpt_do_ioc_recovery
===================

.. c:function:: int mpt_do_ioc_recovery(MPT_ADAPTER *ioc, u32 reason, int sleepFlag)

    Initialize or recover MPT adapter.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

    :param u32 reason:
        Event word / reason

    :param int sleepFlag:
        Use schedule if CAN_SLEEP else use udelay.

.. _`mpt_do_ioc_recovery.description`:

Description
-----------

This routine performs all the steps necessary to bring the IOC
to a OPERATIONAL state.

This routine also pre-fetches the LAN MAC address of a Fibre Channel
MPT adapter.

.. _`mpt_do_ioc_recovery.return`:

Return
------

0 for success
-1 if failed to get board READY
-2 if READY but IOCFacts Failed
-3 if READY but PrimeIOCFifos Failed
-4 if READY but IOCInit Failed
-5 if failed to enable_device and/or request_selected_regions
-6 if failed to upload firmware

.. _`mpt_detect_bound_ports`:

mpt_detect_bound_ports
======================

.. c:function:: void mpt_detect_bound_ports(MPT_ADAPTER *ioc, struct pci_dev *pdev)

    Search for matching PCI bus/dev_function

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

    :param struct pci_dev \*pdev:
        Pointer to (struct pci_dev) structure

.. _`mpt_detect_bound_ports.description`:

Description
-----------

Search for PCI bus/dev_function which matches
PCI bus/dev_function (+/-1) for newly discovered 929,
929X, 1030 or 1035.

If match on PCI dev_function +/-1 is found, bind the two MPT adapters
using alt_ioc pointer fields in their \ ``MPT_ADAPTER``\  structures.

.. _`mpt_adapter_disable`:

mpt_adapter_disable
===================

.. c:function:: void mpt_adapter_disable(MPT_ADAPTER *ioc)

    Disable misbehaving MPT adapter.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

.. _`mpt_adapter_dispose`:

mpt_adapter_dispose
===================

.. c:function:: void mpt_adapter_dispose(MPT_ADAPTER *ioc)

    Free all resources associated with an MPT adapter

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

.. _`mpt_adapter_dispose.description`:

Description
-----------

This routine unregisters h/w resources and frees all alloc'd memory
associated with a MPT adapter structure.

.. _`mptdisplayioccapabilities`:

MptDisplayIocCapabilities
=========================

.. c:function:: void MptDisplayIocCapabilities(MPT_ADAPTER *ioc)

    Disply IOC's capabilities.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT adapter structure

.. _`makeiocready`:

MakeIocReady
============

.. c:function:: int MakeIocReady(MPT_ADAPTER *ioc, int force, int sleepFlag)

    Get IOC to a READY state, using KickStart if needed.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int force:
        Force hard KickStart of IOC

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`makeiocready.return`:

Return
------

1 - DIAG reset and READY
0 - READY initially OR soft reset and READY
-1 - Any failure on KickStart
-2 - Msg Unit Reset Failed
-3 - IO Unit Reset Failed
-4 - IOC owned by a PEER

.. _`mpt_getiocstate`:

mpt_GetIocState
===============

.. c:function:: u32 mpt_GetIocState(MPT_ADAPTER *ioc, int cooked)

    Get the current state of a MPT adapter.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int cooked:
        Request raw or cooked IOC state

.. _`mpt_getiocstate.description`:

Description
-----------

Returns all IOC Doorbell register bits if cooked==0, else just the
Doorbell bits in MPI_IOC_STATE_MASK.

.. _`getiocfacts`:

GetIocFacts
===========

.. c:function:: int GetIocFacts(MPT_ADAPTER *ioc, int sleepFlag, int reason)

    Send IOCFacts request to MPT adapter.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int sleepFlag:
        Specifies whether the process can sleep

    :param int reason:
        If recovery, only update facts.

.. _`getiocfacts.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`getportfacts`:

GetPortFacts
============

.. c:function:: int GetPortFacts(MPT_ADAPTER *ioc, int portnum, int sleepFlag)

    Send PortFacts request to MPT adapter.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int portnum:
        Port number

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`getportfacts.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`sendiocinit`:

SendIocInit
===========

.. c:function:: int SendIocInit(MPT_ADAPTER *ioc, int sleepFlag)

    Send IOCInit request to MPT adapter.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`sendiocinit.description`:

Description
-----------

Send IOCInit followed by PortEnable to bring IOC to OPERATIONAL state.

Returns 0 for success, non-zero for failure.

.. _`sendportenable`:

SendPortEnable
==============

.. c:function:: int SendPortEnable(MPT_ADAPTER *ioc, int portnum, int sleepFlag)

    Send PortEnable request to MPT adapter port.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int portnum:
        Port number to enable

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`sendportenable.description`:

Description
-----------

Send PortEnable to bring IOC to OPERATIONAL state.

Returns 0 for success, non-zero for failure.

.. _`mpt_alloc_fw_memory`:

mpt_alloc_fw_memory
===================

.. c:function:: int mpt_alloc_fw_memory(MPT_ADAPTER *ioc, int size)

    allocate firmware memory

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int size:
        total FW bytes

.. _`mpt_alloc_fw_memory.description`:

Description
-----------

If memory has already been allocated, the same (cached) value
is returned.

Return 0 if successful, or non-zero for failure

.. _`mpt_free_fw_memory`:

mpt_free_fw_memory
==================

.. c:function:: void mpt_free_fw_memory(MPT_ADAPTER *ioc)

    free firmware memory

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

.. _`mpt_free_fw_memory.description`:

Description
-----------

If alt_img is NULL, delete from ioc structure.
Else, delete a secondary image in same format.

.. _`mpt_do_upload`:

mpt_do_upload
=============

.. c:function:: int mpt_do_upload(MPT_ADAPTER *ioc, int sleepFlag)

    Construct and Send FWUpload request to MPT adapter port.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`mpt_do_upload.description`:

Description
-----------

Returns 0 for success, >0 for handshake failure
<0 for fw upload failure.

.. _`mpt_do_upload.remark`:

Remark
------

If bound IOC and a successful FWUpload was performed
on the bound IOC, the second image is discarded
and memory is free'd. Both channels must upload to prevent
IOC from running in degraded mode.

.. _`mpt_downloadboot`:

mpt_downloadboot
================

.. c:function:: int mpt_downloadboot(MPT_ADAPTER *ioc, MpiFwHeader_t *pFwHeader, int sleepFlag)

    DownloadBoot code

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param MpiFwHeader_t \*pFwHeader:
        Pointer to firmware header info

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`mpt_downloadboot.description`:

Description
-----------

FwDownloadBoot requires Programmed IO access.

Returns 0 for success
-1 FW Image size is 0
-2 No valid cached_fw Pointer
<0 for fw upload failure.

.. _`kickstart`:

KickStart
=========

.. c:function:: int KickStart(MPT_ADAPTER *ioc, int force, int sleepFlag)

    Perform hard reset of MPT adapter.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int force:
        Force hard reset

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`kickstart.description`:

Description
-----------

This routine places MPT adapter in diagnostic mode via the
WriteSequence register, and then performs a hard reset of adapter
via the Diagnostic register.

.. _`kickstart.inputs`:

Inputs
------

sleepflag - CAN_SLEEP (non-interrupt thread)
or NO_SLEEP (interrupt thread, use mdelay)
force - 1 if doorbell active, board fault state
board operational, IOC_RECOVERY or
IOC_BRINGUP and there is an alt_ioc.
0 else

.. _`kickstart.return`:

Return
------

1 - hard reset, READY
0 - no reset due to History bit, READY
-1 - no reset due to History bit but not READY
OR reset but failed to come READY
-2 - no reset, could not enter DIAG mode
-3 - reset but bad FW bit

.. _`mpt_diag_reset`:

mpt_diag_reset
==============

.. c:function:: int mpt_diag_reset(MPT_ADAPTER *ioc, int ignore, int sleepFlag)

    Perform hard reset of the adapter.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int ignore:
        Set if to honor and clear to ignore
        the reset history bit

    :param int sleepFlag:
        CAN_SLEEP if called in a non-interrupt thread,
        else set to NO_SLEEP (use mdelay instead)

.. _`mpt_diag_reset.description`:

Description
-----------

This routine places the adapter in diagnostic mode via the
WriteSequence register and then performs a hard reset of adapter
via the Diagnostic register. Adapter should be in ready state
upon successful completion.

.. _`mpt_diag_reset.return`:

Return
------

1  hard reset successful
0  no reset performed because reset history bit set
-2  enabling diagnostic mode failed
-3  diagnostic reset failed

.. _`sendiocreset`:

SendIocReset
============

.. c:function:: int SendIocReset(MPT_ADAPTER *ioc, u8 reset_type, int sleepFlag)

    Send IOCReset request to MPT adapter.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param u8 reset_type:
        reset type, expected values are
        \ ``MPI_FUNCTION_IOC_MESSAGE_UNIT_RESET``\  or \ ``MPI_FUNCTION_IO_UNIT_RESET``\ 

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`sendiocreset.description`:

Description
-----------

Send IOCReset request to the MPT adapter.

Returns 0 for success, non-zero for failure.

.. _`initchainbuffers`:

initChainBuffers
================

.. c:function:: int initChainBuffers(MPT_ADAPTER *ioc)

    Allocate memory for and initialize chain buffers

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

.. _`initchainbuffers.description`:

Description
-----------

Allocates memory for and initializes chain buffers,
chain buffer control arrays and spinlock.

.. _`primeiocfifos`:

PrimeIocFifos
=============

.. c:function:: int PrimeIocFifos(MPT_ADAPTER *ioc)

    Initialize IOC request and reply FIFOs.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

.. _`primeiocfifos.description`:

Description
-----------

This routine allocates memory for the MPT reply and request frame
pools (if necessary), and primes the IOC reply FIFO with
reply frames.

Returns 0 for success, non-zero for failure.

.. _`mpt_handshake_req_reply_wait`:

mpt_handshake_req_reply_wait
============================

.. c:function:: int mpt_handshake_req_reply_wait(MPT_ADAPTER *ioc, int reqBytes, u32 *req, int replyBytes, u16 *u16reply, int maxwait, int sleepFlag)

    Send MPT request to and receive reply from IOC via doorbell handshake method.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int reqBytes:
        Size of the request in bytes

    :param u32 \*req:
        Pointer to MPT request frame

    :param int replyBytes:
        Expected size of the reply in bytes

    :param u16 \*u16reply:
        Pointer to area where reply should be written

    :param int maxwait:
        Max wait time for a reply (in seconds)

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`mpt_handshake_req_reply_wait.notes`:

NOTES
-----

It is the callers responsibility to byte-swap fields in the
request which are greater than 1 byte in size.  It is also the
callers responsibility to byte-swap response fields which are
greater than 1 byte in size.

Returns 0 for success, non-zero for failure.

.. _`waitfordoorbellack`:

WaitForDoorbellAck
==================

.. c:function:: int WaitForDoorbellAck(MPT_ADAPTER *ioc, int howlong, int sleepFlag)

    Wait for IOC doorbell handshake acknowledge

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int howlong:
        How long to wait (in seconds)

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`waitfordoorbellack.description`:

Description
-----------

This routine waits (up to ~2 seconds max) for IOC doorbell
handshake ACKnowledge, indicated by the IOP_DOORBELL_STATUS
bit in its IntStatus register being clear.

Returns a negative value on failure, else wait loop count.

.. _`waitfordoorbellint`:

WaitForDoorbellInt
==================

.. c:function:: int WaitForDoorbellInt(MPT_ADAPTER *ioc, int howlong, int sleepFlag)

    Wait for IOC to set its doorbell interrupt bit

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int howlong:
        How long to wait (in seconds)

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`waitfordoorbellint.description`:

Description
-----------

This routine waits (up to ~2 seconds max) for IOC doorbell interrupt
(MPI_HIS_DOORBELL_INTERRUPT) to be set in the IntStatus register.

Returns a negative value on failure, else wait loop count.

.. _`waitfordoorbellreply`:

WaitForDoorbellReply
====================

.. c:function:: int WaitForDoorbellReply(MPT_ADAPTER *ioc, int howlong, int sleepFlag)

    Wait for and capture an IOC handshake reply.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int howlong:
        How long to wait (in seconds)

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`waitfordoorbellreply.description`:

Description
-----------

This routine polls the IOC for a handshake reply, 16 bits at a time.
Reply is cached to IOC private area large enough to hold a maximum
of 128 bytes of reply data.

Returns a negative value on failure, else size of reply in WORDS.

.. _`getlanconfigpages`:

GetLanConfigPages
=================

.. c:function:: int GetLanConfigPages(MPT_ADAPTER *ioc)

    Fetch LANConfig pages.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

.. _`getlanconfigpages.return`:

Return
------

0 for success
-ENOMEM if no memory available
-EPERM if not allowed due to ISR context
-EAGAIN if no msg frames currently available
-EFAULT for non-successful reply or no reply (timeout)

.. _`mptbase_sas_persist_operation`:

mptbase_sas_persist_operation
=============================

.. c:function:: int mptbase_sas_persist_operation(MPT_ADAPTER *ioc, u8 persist_opcode)

    Perform operation on SAS Persistent Table

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param u8 persist_opcode:
        see below

.. _`mptbase_sas_persist_operation.description`:

Description
-----------

MPI_SAS_OP_CLEAR_NOT_PRESENT - Free all persist TargetID mappings for
devices not currently present.
MPI_SAS_OP_CLEAR_ALL_PERSISTENT - Clear al persist TargetID mappings

.. _`mptbase_sas_persist_operation.note`:

NOTE
----

Don't use not this function during interrupt time.

Returns 0 for success, non-zero error

.. _`getiounitpage2`:

GetIoUnitPage2
==============

.. c:function:: int GetIoUnitPage2(MPT_ADAPTER *ioc)

    Retrieve BIOS version and boot order information.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

.. _`getiounitpage2.return`:

Return
------

0 for success
-ENOMEM if no memory available
-EPERM if not allowed due to ISR context
-EAGAIN if no msg frames currently available
-EFAULT for non-successful reply or no reply (timeout)

.. _`mpt_getscsiportsettings`:

mpt_GetScsiPortSettings
=======================

.. c:function:: int mpt_GetScsiPortSettings(MPT_ADAPTER *ioc, int portnum)

    read SCSI Port Page 0 and 2

    :param MPT_ADAPTER \*ioc:
        Pointer to a Adapter Strucutre

    :param int portnum:
        IOC port number

.. _`mpt_getscsiportsettings.return`:

Return
------

-EFAULT if read of config page header fails
or if no nvram
If read of SCSI Port Page 0 fails,
NVRAM = MPT_HOST_NVRAM_INVALID  (0xFFFFFFFF)
Adapter settings: async, narrow
Return 1
If read of SCSI Port Page 2 fails,
Adapter settings valid
NVRAM = MPT_HOST_NVRAM_INVALID  (0xFFFFFFFF)
Return 1
Else
Both valid
Return 0
CHECK - what type of locking mechanisms should be used????

.. _`mpt_readscsidevicepageheaders`:

mpt_readScsiDevicePageHeaders
=============================

.. c:function:: int mpt_readScsiDevicePageHeaders(MPT_ADAPTER *ioc, int portnum)

    save version and length of SDP1

    :param MPT_ADAPTER \*ioc:
        Pointer to a Adapter Strucutre

    :param int portnum:
        IOC port number

.. _`mpt_readscsidevicepageheaders.return`:

Return
------

-EFAULT if read of config page header fails
or 0 if success.

.. _`mpt_inactive_raid_list_free`:

mpt_inactive_raid_list_free
===========================

.. c:function:: void mpt_inactive_raid_list_free(MPT_ADAPTER *ioc)

    This clears this link list.

    :param MPT_ADAPTER \*ioc:
        pointer to per adapter structure

.. _`mpt_inactive_raid_volumes`:

mpt_inactive_raid_volumes
=========================

.. c:function:: void mpt_inactive_raid_volumes(MPT_ADAPTER *ioc, u8 channel, u8 id)

    sets up link list of phy_disk_nums for devices belonging in an inactive volume

    :param MPT_ADAPTER \*ioc:
        pointer to per adapter structure

    :param u8 channel:
        volume channel

    :param u8 id:
        volume target id

.. _`mpt_raid_phys_disk_pg0`:

mpt_raid_phys_disk_pg0
======================

.. c:function:: int mpt_raid_phys_disk_pg0(MPT_ADAPTER *ioc, u8 phys_disk_num, RaidPhysDiskPage0_t *phys_disk)

    returns phys disk page zero

    :param MPT_ADAPTER \*ioc:
        Pointer to a Adapter Structure

    :param u8 phys_disk_num:
        io unit unique phys disk num generated by the ioc

    :param RaidPhysDiskPage0_t \*phys_disk:
        requested payload data returned

.. _`mpt_raid_phys_disk_pg0.return`:

Return
------

0 on success
-EFAULT if read of config page header fails or data pointer not NULL
-ENOMEM if pci_alloc failed

.. _`mpt_raid_phys_disk_get_num_paths`:

mpt_raid_phys_disk_get_num_paths
================================

.. c:function:: int mpt_raid_phys_disk_get_num_paths(MPT_ADAPTER *ioc, u8 phys_disk_num)

    returns number paths associated to this phys_num

    :param MPT_ADAPTER \*ioc:
        Pointer to a Adapter Structure

    :param u8 phys_disk_num:
        io unit unique phys disk num generated by the ioc

.. _`mpt_raid_phys_disk_get_num_paths.return`:

Return
------

returns number paths

.. _`mpt_raid_phys_disk_pg1`:

mpt_raid_phys_disk_pg1
======================

.. c:function:: int mpt_raid_phys_disk_pg1(MPT_ADAPTER *ioc, u8 phys_disk_num, RaidPhysDiskPage1_t *phys_disk)

    returns phys disk page 1

    :param MPT_ADAPTER \*ioc:
        Pointer to a Adapter Structure

    :param u8 phys_disk_num:
        io unit unique phys disk num generated by the ioc

    :param RaidPhysDiskPage1_t \*phys_disk:
        requested payload data returned

.. _`mpt_raid_phys_disk_pg1.return`:

Return
------

0 on success
-EFAULT if read of config page header fails or data pointer not NULL
-ENOMEM if pci_alloc failed

.. _`mpt_findimvolumes`:

mpt_findImVolumes
=================

.. c:function:: int mpt_findImVolumes(MPT_ADAPTER *ioc)

    Identify IDs of hidden disks and RAID Volumes

    :param MPT_ADAPTER \*ioc:
        Pointer to a Adapter Strucutre

.. _`mpt_findimvolumes.return`:

Return
------

0 on success
-EFAULT if read of config page header fails or data pointer not NULL
-ENOMEM if pci_alloc failed

.. _`sendeventnotification`:

SendEventNotification
=====================

.. c:function:: int SendEventNotification(MPT_ADAPTER *ioc, u8 EvSwitch, int sleepFlag)

    Send EventNotification (on or off) request to adapter

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param u8 EvSwitch:
        Event switch flags

    :param int sleepFlag:
        Specifies whether the process can sleep

.. _`sendeventack`:

SendEventAck
============

.. c:function:: int SendEventAck(MPT_ADAPTER *ioc, EventNotificationReply_t *evnp)

    Send EventAck request to MPT adapter.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param EventNotificationReply_t \*evnp:
        Pointer to original EventNotification request

.. _`mpt_config`:

mpt_config
==========

.. c:function:: int mpt_config(MPT_ADAPTER *ioc, CONFIGPARMS *pCfg)

    Generic function to issue config message

    :param MPT_ADAPTER \*ioc:
        Pointer to an adapter structure

    :param CONFIGPARMS \*pCfg:
        Pointer to a configuration structure. Struct contains
        action, page address, direction, physical address
        and pointer to a configuration page header
        Page header is updated.

.. _`mpt_config.description`:

Description
-----------

Returns 0 for success
-EPERM if not allowed due to ISR context
-EAGAIN if no msg frames currently available
-EFAULT for non-successful reply or no reply (timeout)

.. _`mpt_ioc_reset`:

mpt_ioc_reset
=============

.. c:function:: int mpt_ioc_reset(MPT_ADAPTER *ioc, int reset_phase)

    Base cleanup for hard reset

    :param MPT_ADAPTER \*ioc:
        Pointer to the adapter structure

    :param int reset_phase:
        Indicates pre- or post-reset functionality

.. _`mpt_ioc_reset.remark`:

Remark
------

Frees resources with internally generated commands.

.. _`procmpt_create`:

procmpt_create
==============

.. c:function:: int procmpt_create( void)

    Create \ ``MPT_PROCFS_MPTBASEDIR``\  entries.

    :param  void:
        no arguments

.. _`procmpt_create.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`procmpt_destroy`:

procmpt_destroy
===============

.. c:function:: void procmpt_destroy( void)

    Tear down \ ``MPT_PROCFS_MPTBASEDIR``\  entries.

    :param  void:
        no arguments

.. _`procmpt_destroy.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt_print_ioc_summary`:

mpt_print_ioc_summary
=====================

.. c:function:: void mpt_print_ioc_summary(MPT_ADAPTER *ioc, char *buffer, int *size, int len, int showlan)

    Write ASCII summary of IOC to a buffer.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param char \*buffer:
        Pointer to buffer where IOC summary info should be written

    :param int \*size:
        Pointer to number of bytes we wrote (set by this routine)

    :param int len:
        Offset at which to start writing in buffer

    :param int showlan:
        Display LAN stuff?

.. _`mpt_print_ioc_summary.description`:

Description
-----------

This routine writes (english readable) ASCII text, which represents
a summary of IOC information, to a buffer.

.. _`mpt_set_taskmgmt_in_progress_flag`:

mpt_set_taskmgmt_in_progress_flag
=================================

.. c:function:: int mpt_set_taskmgmt_in_progress_flag(MPT_ADAPTER *ioc)

    set flags associated with task management

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

.. _`mpt_set_taskmgmt_in_progress_flag.description`:

Description
-----------

Returns 0 for SUCCESS or -1 if FAILED.

If -1 is return, then it was not possible to set the flags

.. _`mpt_clear_taskmgmt_in_progress_flag`:

mpt_clear_taskmgmt_in_progress_flag
===================================

.. c:function:: void mpt_clear_taskmgmt_in_progress_flag(MPT_ADAPTER *ioc)

    clear flags associated with task management

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

.. _`mpt_halt_firmware`:

mpt_halt_firmware
=================

.. c:function:: void mpt_halt_firmware(MPT_ADAPTER *ioc)

    Halts the firmware if it is operational and panic the kernel

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

.. _`mpt_softresethandler`:

mpt_SoftResetHandler
====================

.. c:function:: int mpt_SoftResetHandler(MPT_ADAPTER *ioc, int sleepFlag)

    Issues a less expensive reset

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int sleepFlag:
        Indicates if sleep or schedule must be called.

.. _`mpt_softresethandler.description`:

Description
-----------

Returns 0 for SUCCESS or -1 if FAILED.

Message Unit Reset - instructs the IOC to reset the Reply Post and
Free FIFO's. All the Message Frames on Reply Free FIFO are discarded.
All posted buffers are freed, and event notification is turned off.
IOC doesn't reply to any outstanding request. This will transfer IOC
to READY state.

.. _`mpt_soft_hard_resethandler`:

mpt_Soft_Hard_ResetHandler
==========================

.. c:function:: int mpt_Soft_Hard_ResetHandler(MPT_ADAPTER *ioc, int sleepFlag)

    Try less expensive reset

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int sleepFlag:
        Indicates if sleep or schedule must be called.

.. _`mpt_soft_hard_resethandler.description`:

Description
-----------

Returns 0 for SUCCESS or -1 if FAILED.
Try for softreset first, only if it fails go for expensive
HardReset.

.. _`mpt_hardresethandler`:

mpt_HardResetHandler
====================

.. c:function:: int mpt_HardResetHandler(MPT_ADAPTER *ioc, int sleepFlag)

    Generic reset handler

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param int sleepFlag:
        Indicates if sleep or schedule must be called.

.. _`mpt_hardresethandler.description`:

Description
-----------

Issues SCSI Task Management call based on input arg values.
If TaskMgmt fails, returns associated SCSI request.

.. _`mpt_hardresethandler.remark`:

Remark
------

_HardResetHandler can be invoked from an interrupt thread (timer)
or a non-interrupt thread.  In the former, must not call \ :c:func:`schedule`\ .

.. _`mpt_hardresethandler.note`:

Note
----

A return of -1 is a FATAL error case, as it means a
FW reload/initialization failed.

Returns 0 for SUCCESS or -1 if FAILED.

.. _`processeventnotification`:

ProcessEventNotification
========================

.. c:function:: int ProcessEventNotification(MPT_ADAPTER *ioc, EventNotificationReply_t *pEventReply, int *evHandlers)

    Route EventNotificationReply to all event handlers

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param EventNotificationReply_t \*pEventReply:
        Pointer to EventNotification reply frame

    :param int \*evHandlers:
        Pointer to integer, number of event handlers

.. _`processeventnotification.description`:

Description
-----------

Routes a received EventNotificationReply to all currently registered
event handlers.
Returns sum of event handlers return values.

.. _`mpt_fc_log_info`:

mpt_fc_log_info
===============

.. c:function:: void mpt_fc_log_info(MPT_ADAPTER *ioc, u32 log_info)

    Log information returned from Fibre Channel IOC.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param u32 log_info:
        U32 LogInfo reply word from the IOC

.. _`mpt_fc_log_info.description`:

Description
-----------

Refer to lsi/mpi_log_fc.h.

.. _`mpt_spi_log_info`:

mpt_spi_log_info
================

.. c:function:: void mpt_spi_log_info(MPT_ADAPTER *ioc, u32 log_info)

    Log information returned from SCSI Parallel IOC.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param u32 log_info:
        U32 LogInfo word from the IOC

.. _`mpt_spi_log_info.description`:

Description
-----------

Refer to lsi/sp_log.h.

.. _`mpt_sas_log_info`:

mpt_sas_log_info
================

.. c:function:: void mpt_sas_log_info(MPT_ADAPTER *ioc, u32 log_info, u8 cb_idx)

    Log information returned from SAS IOC.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param u32 log_info:
        U32 LogInfo reply word from the IOC

    :param u8 cb_idx:
        callback function's handle

.. _`mpt_sas_log_info.description`:

Description
-----------

Refer to lsi/mpi_log_sas.h.

.. _`mpt_iocstatus_info_config`:

mpt_iocstatus_info_config
=========================

.. c:function:: void mpt_iocstatus_info_config(MPT_ADAPTER *ioc, u32 ioc_status, MPT_FRAME_HDR *mf)

    IOCSTATUS information for config pages

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param u32 ioc_status:
        U32 IOCStatus word from IOC

    :param MPT_FRAME_HDR \*mf:
        Pointer to MPT request frame

.. _`mpt_iocstatus_info_config.description`:

Description
-----------

Refer to lsi/mpi.h.

.. _`mpt_iocstatus_info`:

mpt_iocstatus_info
==================

.. c:function:: void mpt_iocstatus_info(MPT_ADAPTER *ioc, u32 ioc_status, MPT_FRAME_HDR *mf)

    IOCSTATUS information returned from IOC.

    :param MPT_ADAPTER \*ioc:
        Pointer to MPT_ADAPTER structure

    :param u32 ioc_status:
        U32 IOCStatus word from IOC

    :param MPT_FRAME_HDR \*mf:
        Pointer to MPT request frame

.. _`mpt_iocstatus_info.description`:

Description
-----------

Refer to lsi/mpi.h.

.. _`fusion_init`:

fusion_init
===========

.. c:function:: int fusion_init( void)

    Fusion MPT base driver initialization routine.

    :param  void:
        no arguments

.. _`fusion_init.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`fusion_exit`:

fusion_exit
===========

.. c:function:: void __exit fusion_exit( void)

    Perform driver unload cleanup.

    :param  void:
        no arguments

.. _`fusion_exit.description`:

Description
-----------

This routine frees all resources associated with each MPT adapter
and removes all \ ``MPT_PROCFS_MPTBASEDIR``\  entries.

.. This file was automatic generated / don't edit.

