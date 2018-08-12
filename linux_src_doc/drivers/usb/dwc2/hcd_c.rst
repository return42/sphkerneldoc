.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/hcd.c

.. _`dwc2_enable_common_interrupts`:

dwc2_enable_common_interrupts
=============================

.. c:function:: void dwc2_enable_common_interrupts(struct dwc2_hsotg *hsotg)

    Initializes the commmon interrupts, used in both device and host modes

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

.. _`dwc2_enable_host_interrupts`:

dwc2_enable_host_interrupts
===========================

.. c:function:: void dwc2_enable_host_interrupts(struct dwc2_hsotg *hsotg)

    Enables the Host mode interrupts

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

.. _`dwc2_disable_host_interrupts`:

dwc2_disable_host_interrupts
============================

.. c:function:: void dwc2_disable_host_interrupts(struct dwc2_hsotg *hsotg)

    Disables the Host Mode interrupts

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

.. _`dwc2_calc_frame_interval`:

dwc2_calc_frame_interval
========================

.. c:function:: u32 dwc2_calc_frame_interval(struct dwc2_hsotg *hsotg)

    Calculates the correct frame Interval value for the HFIR register according to PHY type and speed

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

.. _`dwc2_calc_frame_interval.note`:

NOTE
----

The caller can modify the value of the HFIR register only after the
Port Enable bit of the Host Port Control and Status register (HPRT.EnaPort)
has been set

.. _`dwc2_read_packet`:

dwc2_read_packet
================

.. c:function:: void dwc2_read_packet(struct dwc2_hsotg *hsotg, u8 *dest, u16 bytes)

    Reads a packet from the Rx FIFO into the destination buffer

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param u8 \*dest:
        Destination buffer for the packet

    :param u16 bytes:
        Number of bytes to copy to the destination

.. _`dwc2_dump_channel_info`:

dwc2_dump_channel_info
======================

.. c:function:: void dwc2_dump_channel_info(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan)

    Prints the state of a host channel

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param struct dwc2_host_chan \*chan:
        Pointer to the channel to dump

.. _`dwc2_dump_channel_info.description`:

Description
-----------

Must be called with interrupt disabled and spinlock held

.. _`dwc2_dump_channel_info.note`:

NOTE
----

This function will be removed once the peripheral controller code
is integrated and the driver is stable

.. _`dwc2_hc_init`:

dwc2_hc_init
============

.. c:function:: void dwc2_hc_init(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan)

    Prepares a host channel for transferring packets to/from a specific endpoint

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param struct dwc2_host_chan \*chan:
        Information needed to initialize the host channel

.. _`dwc2_hc_init.description`:

Description
-----------

The HCCHARn register is set up with the characteristics specified in chan.
Host channel interrupts that may need to be serviced while this transfer is
in progress are enabled.

.. _`dwc2_hc_halt`:

dwc2_hc_halt
============

.. c:function:: void dwc2_hc_halt(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan, enum dwc2_halt_status halt_status)

    Attempts to halt a host channel

    :param struct dwc2_hsotg \*hsotg:
        Controller register interface

    :param struct dwc2_host_chan \*chan:
        Host channel to halt

    :param enum dwc2_halt_status halt_status:
        Reason for halting the channel

.. _`dwc2_hc_halt.description`:

Description
-----------

This function should only be called in Slave mode or to abort a transfer in
either Slave mode or DMA mode. Under normal circumstances in DMA mode, the
controller halts the channel when the transfer is complete or a condition
occurs that requires application intervention.

In slave mode, checks for a free request queue entry, then sets the Channel
Enable and Channel Disable bits of the Host Channel Characteristics
register of the specified channel to intiate the halt. If there is no free
request queue entry, sets only the Channel Disable bit of the HCCHARn
register to flush requests for this channel. In the latter case, sets a
flag to indicate that the host channel needs to be halted when a request
queue slot is open.

In DMA mode, always sets the Channel Enable and Channel Disable bits of the
HCCHARn register. The controller ensures there is space in the request
queue before submitting the halt request.

Some time may elapse before the core flushes any posted requests for this
host channel and halts. The Channel Halted interrupt handler completes the
deactivation of the host channel.

.. _`dwc2_hc_cleanup`:

dwc2_hc_cleanup
===============

.. c:function:: void dwc2_hc_cleanup(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan)

    Clears the transfer state for a host channel

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param struct dwc2_host_chan \*chan:
        Identifies the host channel to clean up

.. _`dwc2_hc_cleanup.description`:

Description
-----------

This function is normally called after a transfer is done and the host
channel is being released

.. _`dwc2_hc_set_even_odd_frame`:

dwc2_hc_set_even_odd_frame
==========================

.. c:function:: void dwc2_hc_set_even_odd_frame(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan, u32 *hcchar)

    Sets the channel property that indicates in which frame a periodic transfer should occur

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param struct dwc2_host_chan \*chan:
        Identifies the host channel to set up and its properties

    :param u32 \*hcchar:
        Current value of the HCCHAR register for the specified host channel

.. _`dwc2_hc_set_even_odd_frame.description`:

Description
-----------

This function has no effect on non-periodic transfers

.. _`dwc2_hc_write_packet`:

dwc2_hc_write_packet
====================

.. c:function:: void dwc2_hc_write_packet(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan)

    Writes a packet into the Tx FIFO associated with the Host Channel

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param struct dwc2_host_chan \*chan:
        Information needed to initialize the host channel

.. _`dwc2_hc_write_packet.description`:

Description
-----------

This function should only be called in Slave mode. For a channel associated
with a non-periodic EP, the non-periodic Tx FIFO is written. For a channel
associated with a periodic EP, the periodic Tx FIFO is written.

Upon return the xfer_buf and xfer_count fields in chan are incremented by
the number of bytes written to the Tx FIFO.

.. _`dwc2_hc_do_ping`:

dwc2_hc_do_ping
===============

.. c:function:: void dwc2_hc_do_ping(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan)

    Starts a PING transfer

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param struct dwc2_host_chan \*chan:
        Information needed to initialize the host channel

.. _`dwc2_hc_do_ping.description`:

Description
-----------

This function should only be called in Slave mode. The Do Ping bit is set in
the HCTSIZ register, then the channel is enabled.

.. _`dwc2_hc_start_transfer`:

dwc2_hc_start_transfer
======================

.. c:function:: void dwc2_hc_start_transfer(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan)

    Does the setup for a data transfer for a host channel and starts the transfer

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param struct dwc2_host_chan \*chan:
        Information needed to initialize the host channel. The xfer_len value
        may be reduced to accommodate the max widths of the XferSize and
        PktCnt fields in the HCTSIZn register. The multi_count value may be
        changed to reflect the final xfer_len value.

.. _`dwc2_hc_start_transfer.description`:

Description
-----------

This function may be called in either Slave mode or DMA mode. In Slave mode,
the caller must ensure that there is sufficient space in the request queue
and Tx Data FIFO.

For an OUT transfer in Slave mode, it loads a data packet into the
appropriate FIFO. If necessary, additional data packets are loaded in the
Host ISR.

For an IN transfer in Slave mode, a data packet is requested. The data
packets are unloaded from the Rx FIFO in the Host ISR. If necessary,
additional data packets are requested in the Host ISR.

For a PING transfer in Slave mode, the Do Ping bit is set in the HCTSIZ
register along with a packet count of 1 and the channel is enabled. This
causes a single PING transaction to occur. Other fields in HCTSIZ are
simply set to 0 since no data transfer occurs in this case.

For a PING transfer in DMA mode, the HCTSIZ register is initialized with
all the information required to perform the subsequent data transfer. In
addition, the Do Ping bit is set in the HCTSIZ register. In this case, the
controller performs the entire PING protocol, then starts the data
transfer.

.. _`dwc2_hc_start_transfer_ddma`:

dwc2_hc_start_transfer_ddma
===========================

.. c:function:: void dwc2_hc_start_transfer_ddma(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan)

    Does the setup for a data transfer for a host channel and starts the transfer in Descriptor DMA mode

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param struct dwc2_host_chan \*chan:
        Information needed to initialize the host channel

.. _`dwc2_hc_start_transfer_ddma.description`:

Description
-----------

Initializes HCTSIZ register. For a PING transfer the Do Ping bit is set.
Sets PID and NTD values. For periodic transfers initializes SCHED_INFO field
with micro-frame bitmap.

Initializes HCDMA register with descriptor list address and CTD value then
starts the transfer via enabling the channel.

.. _`dwc2_hc_continue_transfer`:

dwc2_hc_continue_transfer
=========================

.. c:function:: int dwc2_hc_continue_transfer(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan)

    Continues a data transfer that was started by a previous call to \ :c:func:`dwc2_hc_start_transfer`\ 

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

    :param struct dwc2_host_chan \*chan:
        Information needed to initialize the host channel

.. _`dwc2_hc_continue_transfer.description`:

Description
-----------

The caller must ensure there is sufficient space in the request queue and Tx
Data FIFO. This function should only be called in Slave mode. In DMA mode,
the controller acts autonomously to complete transfers programmed to a host
channel.

For an OUT transfer, a new data packet is loaded into the appropriate FIFO
if there is any data remaining to be queued. For an IN transfer, another
data packet is always requested. For the SETUP phase of a control transfer,
this function does nothing.

.. _`dwc2_hc_continue_transfer.return`:

Return
------

1 if a new request is queued, 0 if no more requests are required
for this transfer

.. _`dwc2_hcd_start`:

dwc2_hcd_start
==============

.. c:function:: void dwc2_hcd_start(struct dwc2_hsotg *hsotg)

    Starts the HCD when switching to Host mode

    :param struct dwc2_hsotg \*hsotg:
        Pointer to struct dwc2_hsotg

.. _`dwc2_hcd_connect`:

dwc2_hcd_connect
================

.. c:function:: void dwc2_hcd_connect(struct dwc2_hsotg *hsotg)

    Handles connect of the HCD

    :param struct dwc2_hsotg \*hsotg:
        Pointer to struct dwc2_hsotg

.. _`dwc2_hcd_connect.description`:

Description
-----------

Must be called with interrupt disabled and spinlock held

.. _`dwc2_hcd_disconnect`:

dwc2_hcd_disconnect
===================

.. c:function:: void dwc2_hcd_disconnect(struct dwc2_hsotg *hsotg, bool force)

    Handles disconnect of the HCD

    :param struct dwc2_hsotg \*hsotg:
        Pointer to struct dwc2_hsotg

    :param bool force:
        If true, we won't try to reconnect even if we see device connected.

.. _`dwc2_hcd_disconnect.description`:

Description
-----------

Must be called with interrupt disabled and spinlock held

.. _`dwc2_hcd_rem_wakeup`:

dwc2_hcd_rem_wakeup
===================

.. c:function:: void dwc2_hcd_rem_wakeup(struct dwc2_hsotg *hsotg)

    Handles Remote Wakeup

    :param struct dwc2_hsotg \*hsotg:
        Pointer to struct dwc2_hsotg

.. _`dwc2_hcd_stop`:

dwc2_hcd_stop
=============

.. c:function:: void dwc2_hcd_stop(struct dwc2_hsotg *hsotg)

    Halts the DWC_otg host mode operations in a clean manner

    :param struct dwc2_hsotg \*hsotg:
        Pointer to struct dwc2_hsotg

.. _`dwc2_hcd_stop.description`:

Description
-----------

Must be called with interrupt disabled and spinlock held

.. _`dwc2_core_init`:

dwc2_core_init
==============

.. c:function:: int dwc2_core_init(struct dwc2_hsotg *hsotg, bool initial_setup)

    Initializes the DWC_otg controller registers and prepares the core for device mode or host mode operation

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

    :param bool initial_setup:
        If true then this is the first init for this instance.

.. _`dwc2_core_host_init`:

dwc2_core_host_init
===================

.. c:function:: void dwc2_core_host_init(struct dwc2_hsotg *hsotg)

    Initializes the DWC_otg controller registers for Host mode

    :param struct dwc2_hsotg \*hsotg:
        Programming view of DWC_otg controller

.. _`dwc2_core_host_init.description`:

Description
-----------

This function flushes the Tx and Rx FIFOs and flushes any entries in the
request queues. Host channels are reset to ensure that they are ready for
performing transfers.

.. _`dwc2_assign_and_init_hc`:

dwc2_assign_and_init_hc
=======================

.. c:function:: int dwc2_assign_and_init_hc(struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Assigns transactions from a QTD to a free host channel and initializes the host channel to perform the transactions. The host channel is removed from the free list.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure

    :param struct dwc2_qh \*qh:
        Transactions from the first QTD for this QH are selected and assigned
        to a free host channel

.. _`dwc2_hcd_select_transactions`:

dwc2_hcd_select_transactions
============================

.. c:function:: enum dwc2_transaction_type dwc2_hcd_select_transactions(struct dwc2_hsotg *hsotg)

    Selects transactions from the HCD transfer schedule and assigns them to available host channels. Called from the HCD interrupt handler functions.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure

.. _`dwc2_hcd_select_transactions.return`:

Return
------

The types of new transactions that were assigned to host channels

.. _`dwc2_queue_transaction`:

dwc2_queue_transaction
======================

.. c:function:: int dwc2_queue_transaction(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan, u16 fifo_dwords_avail)

    Attempts to queue a single transaction request for a host channel associated with either a periodic or non-periodic transfer

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure

    :param struct dwc2_host_chan \*chan:
        Host channel descriptor associated with either a periodic or
        non-periodic transfer

    :param u16 fifo_dwords_avail:
        Number of DWORDs available in the periodic Tx FIFO
        for periodic transfers or the non-periodic Tx FIFO
        for non-periodic transfers

.. _`dwc2_queue_transaction.return`:

Return
------

1 if a request is queued and more requests may be needed to
complete the transfer, 0 if no more requests are required for this
transfer, -1 if there is insufficient space in the Tx FIFO

This function assumes that there is space available in the appropriate
request queue. For an OUT transfer or SETUP transaction in Slave mode,
it checks whether space is available in the appropriate Tx FIFO.

Must be called with interrupt disabled and spinlock held

.. _`dwc2_hcd_queue_transactions`:

dwc2_hcd_queue_transactions
===========================

.. c:function:: void dwc2_hcd_queue_transactions(struct dwc2_hsotg *hsotg, enum dwc2_transaction_type tr_type)

    Processes the currently active host channels and queues transactions for these channels to the DWC_otg controller. Called from the HCD interrupt handler functions.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure

    :param enum dwc2_transaction_type tr_type:
        The type(s) of transactions to queue (non-periodic, periodic,
        or both)

.. _`dwc2_hcd_queue_transactions.description`:

Description
-----------

Must be called with interrupt disabled and spinlock held

.. _`dwc2_host_get_tt_info`:

dwc2_host_get_tt_info
=====================

.. c:function:: struct dwc2_tt *dwc2_host_get_tt_info(struct dwc2_hsotg *hsotg, void *context, gfp_t mem_flags, int *ttport)

    Get the dwc2_tt associated with context

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param void \*context:
        The priv pointer from a struct dwc2_hcd_urb.

    :param gfp_t mem_flags:
        Flags for allocating memory.

    :param int \*ttport:
        We'll return this device's port number here.  That's used to
        reference into the bitmap if we're on a multi_tt hub.

.. _`dwc2_host_get_tt_info.description`:

Description
-----------

This will get the dwc2_tt structure (and ttport) associated with the given
context (which is really just a struct urb pointer).

The first time this is called for a given TT we allocate memory for our
structure.  When everyone is done and has called \ :c:func:`dwc2_host_put_tt_info`\ 
then the refcount for the structure will go to 0 and we'll free it.

.. _`dwc2_host_get_tt_info.return`:

Return
------

a pointer to a struct dwc2_tt.  Don't forget to call
\ :c:func:`dwc2_host_put_tt_info`\ !  Returns NULL upon memory alloc failure.

.. _`dwc2_host_put_tt_info`:

dwc2_host_put_tt_info
=====================

.. c:function:: void dwc2_host_put_tt_info(struct dwc2_hsotg *hsotg, struct dwc2_tt *dwc_tt)

    Put the dwc2_tt from \ :c:func:`dwc2_host_get_tt_info`\ 

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller.

    :param struct dwc2_tt \*dwc_tt:
        The pointer returned by dwc2_host_get_tt_info.

.. _`dwc2_host_put_tt_info.description`:

Description
-----------

Frees resources allocated by \ :c:func:`dwc2_host_get_tt_info`\  if all current holders
of the structure are done.

It's OK to call this with NULL.

.. _`dwc2_backup_host_registers`:

dwc2_backup_host_registers
==========================

.. c:function:: int dwc2_backup_host_registers(struct dwc2_hsotg *hsotg)

    Backup controller host registers. When suspending usb bus, registers needs to be backuped if controller power is disabled once suspended.

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

.. _`dwc2_restore_host_registers`:

dwc2_restore_host_registers
===========================

.. c:function:: int dwc2_restore_host_registers(struct dwc2_hsotg *hsotg)

    Restore controller host registers. When resuming usb bus, device registers needs to be restored if controller power were disabled.

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

.. _`dwc2_host_enter_hibernation`:

dwc2_host_enter_hibernation
===========================

.. c:function:: int dwc2_host_enter_hibernation(struct dwc2_hsotg *hsotg)

    Put controller in Hibernation.

    :param struct dwc2_hsotg \*hsotg:
        Programming view of the DWC_otg controller

.. This file was automatic generated / don't edit.

