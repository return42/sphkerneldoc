.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/gadget.c

.. _`using_dma`:

using_dma
=========

.. c:function:: bool using_dma(struct dwc2_hsotg *hsotg)

    return the DMA status of the driver.

    :param hsotg:
        The driver state.
    :type hsotg: struct dwc2_hsotg \*

.. _`using_dma.description`:

Description
-----------

Return true if we're using DMA.

Currently, we have the DMA support code worked into everywhere
that needs it, but the AMBA DMA implementation in the hardware can
only DMA from 32bit aligned addresses. This means that gadgets such
as the CDC Ethernet cannot work as they often pass packets which are
not 32bit aligned.

Unfortunately the choice to use DMA or not is global to the controller
and seems to be only settable when the controller is being put through
a core reset. This means we either need to fix the gadgets to take
account of DMA alignment, or add bounce buffers (yuerk).

g_using_dma is set depending on dts flag.

.. _`dwc2_gadget_incr_frame_num`:

dwc2_gadget_incr_frame_num
==========================

.. c:function:: void dwc2_gadget_incr_frame_num(struct dwc2_hsotg_ep *hs_ep)

    Increments the targeted frame number.

    :param hs_ep:
        The endpoint
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`dwc2_gadget_incr_frame_num.description`:

Description
-----------

This function will also check if the frame number overruns DSTS_SOFFN_LIMIT.
If an overrun occurs it will wrap the value and set the frame_overrun flag.

.. _`dwc2_gadget_dec_frame_num_by_one`:

dwc2_gadget_dec_frame_num_by_one
================================

.. c:function:: void dwc2_gadget_dec_frame_num_by_one(struct dwc2_hsotg_ep *hs_ep)

    Decrements the targeted frame number by one.

    :param hs_ep:
        The endpoint.
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`dwc2_gadget_dec_frame_num_by_one.description`:

Description
-----------

This function used in service interval based scheduling flow to calculate
descriptor frame number filed value. For service interval mode frame
number in descriptor should point to last (u)frame in the interval.

.. _`dwc2_hsotg_en_gsint`:

dwc2_hsotg_en_gsint
===================

.. c:function:: void dwc2_hsotg_en_gsint(struct dwc2_hsotg *hsotg, u32 ints)

    enable one or more of the general interrupt

    :param hsotg:
        The device state
    :type hsotg: struct dwc2_hsotg \*

    :param ints:
        A bitmask of the interrupts to enable
    :type ints: u32

.. _`dwc2_hsotg_disable_gsint`:

dwc2_hsotg_disable_gsint
========================

.. c:function:: void dwc2_hsotg_disable_gsint(struct dwc2_hsotg *hsotg, u32 ints)

    disable one or more of the general interrupt

    :param hsotg:
        The device state
    :type hsotg: struct dwc2_hsotg \*

    :param ints:
        A bitmask of the interrupts to enable
    :type ints: u32

.. _`dwc2_hsotg_ctrl_epint`:

dwc2_hsotg_ctrl_epint
=====================

.. c:function:: void dwc2_hsotg_ctrl_epint(struct dwc2_hsotg *hsotg, unsigned int ep, unsigned int dir_in, unsigned int en)

    enable/disable an endpoint irq

    :param hsotg:
        The device state
    :type hsotg: struct dwc2_hsotg \*

    :param ep:
        The endpoint index
    :type ep: unsigned int

    :param dir_in:
        True if direction is in.
    :type dir_in: unsigned int

    :param en:
        The enable value, true to enable
    :type en: unsigned int

.. _`dwc2_hsotg_ctrl_epint.description`:

Description
-----------

Set or clear the mask for an individual endpoint's interrupt
request.

.. _`dwc2_hsotg_tx_fifo_count`:

dwc2_hsotg_tx_fifo_count
========================

.. c:function:: int dwc2_hsotg_tx_fifo_count(struct dwc2_hsotg *hsotg)

    return count of TX FIFOs in device mode

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_tx_fifo_total_depth`:

dwc2_hsotg_tx_fifo_total_depth
==============================

.. c:function:: int dwc2_hsotg_tx_fifo_total_depth(struct dwc2_hsotg *hsotg)

    return total FIFO depth available for device mode TX FIFOs

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_gadget_wkup_alert_handler`:

dwc2_gadget_wkup_alert_handler
==============================

.. c:function:: void dwc2_gadget_wkup_alert_handler(struct dwc2_hsotg *hsotg)

    Handler for WKUP_ALERT interrupt

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_tx_fifo_average_depth`:

dwc2_hsotg_tx_fifo_average_depth
================================

.. c:function:: int dwc2_hsotg_tx_fifo_average_depth(struct dwc2_hsotg *hsotg)

    returns average depth of device mode TX FIFOs

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_init_fifo`:

dwc2_hsotg_init_fifo
====================

.. c:function:: void dwc2_hsotg_init_fifo(struct dwc2_hsotg *hsotg)

    initialise non-periodic FIFOs

    :param hsotg:
        The device instance.
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_ep_alloc_request`:

dwc2_hsotg_ep_alloc_request
===========================

.. c:function:: struct usb_request *dwc2_hsotg_ep_alloc_request(struct usb_ep *ep, gfp_t flags)

    allocate USB rerequest structure

    :param ep:
        USB endpoint to allocate request for.
    :type ep: struct usb_ep \*

    :param flags:
        Allocation flags
    :type flags: gfp_t

.. _`dwc2_hsotg_ep_alloc_request.description`:

Description
-----------

Allocate a new USB request structure appropriate for the specified endpoint

.. _`is_ep_periodic`:

is_ep_periodic
==============

.. c:function:: int is_ep_periodic(struct dwc2_hsotg_ep *hs_ep)

    return true if the endpoint is in periodic mode.

    :param hs_ep:
        The endpoint to query.
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`is_ep_periodic.description`:

Description
-----------

Returns true if the endpoint is in periodic mode, meaning it is being
used for an Interrupt or ISO transfer.

.. _`dwc2_hsotg_unmap_dma`:

dwc2_hsotg_unmap_dma
====================

.. c:function:: void dwc2_hsotg_unmap_dma(struct dwc2_hsotg *hsotg, struct dwc2_hsotg_ep *hs_ep, struct dwc2_hsotg_req *hs_req)

    unmap the DMA memory being used for the request

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

    :param hs_ep:
        The endpoint for the request
    :type hs_ep: struct dwc2_hsotg_ep \*

    :param hs_req:
        The request being processed.
    :type hs_req: struct dwc2_hsotg_req \*

.. _`dwc2_hsotg_unmap_dma.description`:

Description
-----------

This is the reverse of \ :c:func:`dwc2_hsotg_map_dma`\ , called for the completion
of a request to ensure the buffer is ready for access by the caller.

.. _`dwc2_hsotg_write_fifo`:

dwc2_hsotg_write_fifo
=====================

.. c:function:: int dwc2_hsotg_write_fifo(struct dwc2_hsotg *hsotg, struct dwc2_hsotg_ep *hs_ep, struct dwc2_hsotg_req *hs_req)

    write packet Data to the TxFIFO

    :param hsotg:
        The controller state.
    :type hsotg: struct dwc2_hsotg \*

    :param hs_ep:
        The endpoint we're going to write for.
    :type hs_ep: struct dwc2_hsotg_ep \*

    :param hs_req:
        The request to write data for.
    :type hs_req: struct dwc2_hsotg_req \*

.. _`dwc2_hsotg_write_fifo.description`:

Description
-----------

This is called when the TxFIFO has some space in it to hold a new
transmission and we have something to give it. The actual setup of
the data size is done elsewhere, so all we have to do is to actually
write the data.

The return value is zero if there is more space (or nothing was done)
otherwise -ENOSPC is returned if the FIFO space was used up.

This routine is only needed for PIO

.. _`get_ep_limit`:

get_ep_limit
============

.. c:function:: unsigned int get_ep_limit(struct dwc2_hsotg_ep *hs_ep)

    get the maximum data legnth for this endpoint

    :param hs_ep:
        The endpoint
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`get_ep_limit.description`:

Description
-----------

Return the maximum data that can be queued in one go on a given endpoint
so that transfers that are too long can be split.

.. _`dwc2_hsotg_read_frameno`:

dwc2_hsotg_read_frameno
=======================

.. c:function:: u32 dwc2_hsotg_read_frameno(struct dwc2_hsotg *hsotg)

    read current frame number

    :param hsotg:
        The device instance
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_read_frameno.description`:

Description
-----------

Return the current frame number

.. _`dwc2_gadget_get_chain_limit`:

dwc2_gadget_get_chain_limit
===========================

.. c:function:: unsigned int dwc2_gadget_get_chain_limit(struct dwc2_hsotg_ep *hs_ep)

    get the maximum data payload value of the DMA descriptor chain prepared for specific endpoint

    :param hs_ep:
        The endpoint
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`dwc2_gadget_get_chain_limit.description`:

Description
-----------

Return the maximum data that can be queued in one go on a given endpoint
depending on its descriptor chain capacity so that transfers that
are too long can be split.

.. _`dwc2_hsotg_start_req`:

dwc2_hsotg_start_req
====================

.. c:function:: void dwc2_hsotg_start_req(struct dwc2_hsotg *hsotg, struct dwc2_hsotg_ep *hs_ep, struct dwc2_hsotg_req *hs_req, bool continuing)

    start a USB request from an endpoint's queue

    :param hsotg:
        The controller state.
    :type hsotg: struct dwc2_hsotg \*

    :param hs_ep:
        The endpoint to process a request for
    :type hs_ep: struct dwc2_hsotg_ep \*

    :param hs_req:
        The request to start.
    :type hs_req: struct dwc2_hsotg_req \*

    :param continuing:
        True if we are doing more for the current request.
    :type continuing: bool

.. _`dwc2_hsotg_start_req.description`:

Description
-----------

Start the given request running by setting the endpoint registers
appropriately, and writing any data to the FIFOs.

.. _`dwc2_hsotg_map_dma`:

dwc2_hsotg_map_dma
==================

.. c:function:: int dwc2_hsotg_map_dma(struct dwc2_hsotg *hsotg, struct dwc2_hsotg_ep *hs_ep, struct usb_request *req)

    map the DMA memory being used for the request

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

    :param hs_ep:
        The endpoint the request is on.
    :type hs_ep: struct dwc2_hsotg_ep \*

    :param req:
        The request being processed.
    :type req: struct usb_request \*

.. _`dwc2_hsotg_map_dma.description`:

Description
-----------

We've been asked to queue a request, so ensure that the memory buffer
is correctly setup for DMA. If we've been passed an extant DMA address
then ensure the buffer has been synced to memory. If our buffer has no
DMA memory, then we map the memory and mark our request to allow us to
cleanup on completion.

.. _`dwc2_gadget_target_frame_elapsed`:

dwc2_gadget_target_frame_elapsed
================================

.. c:function:: bool dwc2_gadget_target_frame_elapsed(struct dwc2_hsotg_ep *hs_ep)

    Checks target frame

    :param hs_ep:
        The driver endpoint to check
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`dwc2_gadget_target_frame_elapsed.description`:

Description
-----------

Returns 1 if targeted frame elapsed. If returned 1 then we need to drop
corresponding transfer.

.. _`dwc2_hsotg_complete_oursetup`:

dwc2_hsotg_complete_oursetup
============================

.. c:function:: void dwc2_hsotg_complete_oursetup(struct usb_ep *ep, struct usb_request *req)

    setup completion callback

    :param ep:
        The endpoint the request was on.
    :type ep: struct usb_ep \*

    :param req:
        The request completed.
    :type req: struct usb_request \*

.. _`dwc2_hsotg_complete_oursetup.description`:

Description
-----------

Called on completion of any requests the driver itself
submitted that need cleaning up.

.. _`ep_from_windex`:

ep_from_windex
==============

.. c:function:: struct dwc2_hsotg_ep *ep_from_windex(struct dwc2_hsotg *hsotg, u32 windex)

    convert control wIndex value to endpoint

    :param hsotg:
        The driver state.
    :type hsotg: struct dwc2_hsotg \*

    :param windex:
        The control request wIndex field (in host order).
    :type windex: u32

.. _`ep_from_windex.description`:

Description
-----------

Convert the given wIndex into a pointer to an driver endpoint
structure, or return NULL if it is not a valid endpoint.

.. _`dwc2_hsotg_set_test_mode`:

dwc2_hsotg_set_test_mode
========================

.. c:function:: int dwc2_hsotg_set_test_mode(struct dwc2_hsotg *hsotg, int testmode)

    Enable usb Test Modes

    :param hsotg:
        The driver state.
    :type hsotg: struct dwc2_hsotg \*

    :param testmode:
        requested usb test mode
        Enable usb Test Mode requested by the Host.
    :type testmode: int

.. _`dwc2_hsotg_send_reply`:

dwc2_hsotg_send_reply
=====================

.. c:function:: int dwc2_hsotg_send_reply(struct dwc2_hsotg *hsotg, struct dwc2_hsotg_ep *ep, void *buff, int length)

    send reply to control request

    :param hsotg:
        The device state
    :type hsotg: struct dwc2_hsotg \*

    :param ep:
        Endpoint 0
    :type ep: struct dwc2_hsotg_ep \*

    :param buff:
        Buffer for request
    :type buff: void \*

    :param length:
        Length of reply.
    :type length: int

.. _`dwc2_hsotg_send_reply.description`:

Description
-----------

Create a request and queue it on the given endpoint. This is useful as
an internal method of sending replies to certain control requests, etc.

.. _`dwc2_hsotg_process_req_status`:

dwc2_hsotg_process_req_status
=============================

.. c:function:: int dwc2_hsotg_process_req_status(struct dwc2_hsotg *hsotg, struct usb_ctrlrequest *ctrl)

    process request GET_STATUS

    :param hsotg:
        The device state
    :type hsotg: struct dwc2_hsotg \*

    :param ctrl:
        USB control request
    :type ctrl: struct usb_ctrlrequest \*

.. _`get_ep_head`:

get_ep_head
===========

.. c:function:: struct dwc2_hsotg_req *get_ep_head(struct dwc2_hsotg_ep *hs_ep)

    return the first request on the endpoint

    :param hs_ep:
        The controller endpoint to get
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`get_ep_head.description`:

Description
-----------

Get the first request on the endpoint.

.. _`dwc2_gadget_start_next_request`:

dwc2_gadget_start_next_request
==============================

.. c:function:: void dwc2_gadget_start_next_request(struct dwc2_hsotg_ep *hs_ep)

    Starts next request from ep queue

    :param hs_ep:
        Endpoint structure
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`dwc2_gadget_start_next_request.description`:

Description
-----------

If queue is empty and EP is ISOC-OUT - unmasks OUTTKNEPDIS which is masked
in its handler. Hence we need to unmask it here to be able to do
resynchronization.

.. _`dwc2_hsotg_process_req_feature`:

dwc2_hsotg_process_req_feature
==============================

.. c:function:: int dwc2_hsotg_process_req_feature(struct dwc2_hsotg *hsotg, struct usb_ctrlrequest *ctrl)

    process request {SET,CLEAR}_FEATURE

    :param hsotg:
        The device state
    :type hsotg: struct dwc2_hsotg \*

    :param ctrl:
        USB control request
    :type ctrl: struct usb_ctrlrequest \*

.. _`dwc2_hsotg_stall_ep0`:

dwc2_hsotg_stall_ep0
====================

.. c:function:: void dwc2_hsotg_stall_ep0(struct dwc2_hsotg *hsotg)

    stall ep0

    :param hsotg:
        The device state
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_stall_ep0.description`:

Description
-----------

Set stall for ep0 as response for setup request.

.. _`dwc2_hsotg_process_control`:

dwc2_hsotg_process_control
==========================

.. c:function:: void dwc2_hsotg_process_control(struct dwc2_hsotg *hsotg, struct usb_ctrlrequest *ctrl)

    process a control request

    :param hsotg:
        The device state
    :type hsotg: struct dwc2_hsotg \*

    :param ctrl:
        The control request received
    :type ctrl: struct usb_ctrlrequest \*

.. _`dwc2_hsotg_process_control.description`:

Description
-----------

The controller has received the SETUP phase of a control request, and
needs to work out what to do next (and whether to pass it on to the
gadget driver).

.. _`dwc2_hsotg_complete_setup`:

dwc2_hsotg_complete_setup
=========================

.. c:function:: void dwc2_hsotg_complete_setup(struct usb_ep *ep, struct usb_request *req)

    completion of a setup transfer

    :param ep:
        The endpoint the request was on.
    :type ep: struct usb_ep \*

    :param req:
        The request completed.
    :type req: struct usb_request \*

.. _`dwc2_hsotg_complete_setup.description`:

Description
-----------

Called on completion of any requests the driver itself submitted for
EP0 setup packets

.. _`dwc2_hsotg_enqueue_setup`:

dwc2_hsotg_enqueue_setup
========================

.. c:function:: void dwc2_hsotg_enqueue_setup(struct dwc2_hsotg *hsotg)

    start a request for EP0 packets

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_enqueue_setup.description`:

Description
-----------

Enqueue a request on EP0 if necessary to received any SETUP packets
received from the host.

.. _`dwc2_hsotg_complete_request`:

dwc2_hsotg_complete_request
===========================

.. c:function:: void dwc2_hsotg_complete_request(struct dwc2_hsotg *hsotg, struct dwc2_hsotg_ep *hs_ep, struct dwc2_hsotg_req *hs_req, int result)

    complete a request given to us

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

    :param hs_ep:
        The endpoint the request was on.
    :type hs_ep: struct dwc2_hsotg_ep \*

    :param hs_req:
        The request to complete.
    :type hs_req: struct dwc2_hsotg_req \*

    :param result:
        The result code (0 => Ok, otherwise errno)
    :type result: int

.. _`dwc2_hsotg_complete_request.description`:

Description
-----------

The given request has finished, so call the necessary completion
if it has one and then look to see if we can start a new request
on the endpoint.

Note, expects the ep to already be locked as appropriate.

.. _`dwc2_hsotg_rx_data`:

dwc2_hsotg_rx_data
==================

.. c:function:: void dwc2_hsotg_rx_data(struct dwc2_hsotg *hsotg, int ep_idx, int size)

    receive data from the FIFO for an endpoint

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

    :param ep_idx:
        The endpoint index for the data
    :type ep_idx: int

    :param size:
        The size of data in the fifo, in bytes
    :type size: int

.. _`dwc2_hsotg_rx_data.description`:

Description
-----------

The FIFO status shows there is data to read from the FIFO for a given
endpoint, so sort out whether we need to read the data into a request
that has been made for that endpoint.

.. _`dwc2_hsotg_ep0_zlp`:

dwc2_hsotg_ep0_zlp
==================

.. c:function:: void dwc2_hsotg_ep0_zlp(struct dwc2_hsotg *hsotg, bool dir_in)

    send/receive zero-length packet on control endpoint

    :param hsotg:
        The device instance
    :type hsotg: struct dwc2_hsotg \*

    :param dir_in:
        If IN zlp
    :type dir_in: bool

.. _`dwc2_hsotg_ep0_zlp.description`:

Description
-----------

Generate a zero-length IN packet request for terminating a SETUP
transaction.

Note, since we don't write any data to the TxFIFO, then it is
currently believed that we do not need to wait for any space in
the TxFIFO.

.. _`dwc2_hsotg_handle_outdone`:

dwc2_hsotg_handle_outdone
=========================

.. c:function:: void dwc2_hsotg_handle_outdone(struct dwc2_hsotg *hsotg, int epnum)

    handle receiving OutDone/SetupDone from RXFIFO

    :param hsotg:
        The device instance
    :type hsotg: struct dwc2_hsotg \*

    :param epnum:
        The endpoint received from
    :type epnum: int

.. _`dwc2_hsotg_handle_outdone.description`:

Description
-----------

The RXFIFO has delivered an OutDone event, which means that the data
transfer for an OUT endpoint has been completed, either by a short
packet or by the finish of a transfer.

.. _`dwc2_hsotg_handle_rx`:

dwc2_hsotg_handle_rx
====================

.. c:function:: void dwc2_hsotg_handle_rx(struct dwc2_hsotg *hsotg)

    RX FIFO has data

    :param hsotg:
        The device instance
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_handle_rx.description`:

Description
-----------

The IRQ handler has detected that the RX FIFO has some data in it
that requires processing, so find out what is in there and do the
appropriate read.

The RXFIFO is a true FIFO, the packets coming out are still in packet
chunks, so if you have x packets received on an endpoint you'll get x
FIFO events delivered, each with a packet's worth of data in it.

When using DMA, we should not be processing events from the RXFIFO
as the actual data should be sent to the memory directly and we turn
on the completion interrupts to get notifications of transfer completion.

.. _`dwc2_hsotg_ep0_mps`:

dwc2_hsotg_ep0_mps
==================

.. c:function:: u32 dwc2_hsotg_ep0_mps(unsigned int mps)

    turn max packet size into register setting

    :param mps:
        The maximum packet size in bytes.
    :type mps: unsigned int

.. _`dwc2_hsotg_set_ep_maxpacket`:

dwc2_hsotg_set_ep_maxpacket
===========================

.. c:function:: void dwc2_hsotg_set_ep_maxpacket(struct dwc2_hsotg *hsotg, unsigned int ep, unsigned int mps, unsigned int mc, unsigned int dir_in)

    set endpoint's max-packet field

    :param hsotg:
        The driver state.
    :type hsotg: struct dwc2_hsotg \*

    :param ep:
        The index number of the endpoint
    :type ep: unsigned int

    :param mps:
        The maximum packet size in bytes
    :type mps: unsigned int

    :param mc:
        The multicount value
    :type mc: unsigned int

    :param dir_in:
        True if direction is in.
    :type dir_in: unsigned int

.. _`dwc2_hsotg_set_ep_maxpacket.description`:

Description
-----------

Configure the maximum packet size for the given endpoint, updating
the hardware control registers to reflect this.

.. _`dwc2_hsotg_txfifo_flush`:

dwc2_hsotg_txfifo_flush
=======================

.. c:function:: void dwc2_hsotg_txfifo_flush(struct dwc2_hsotg *hsotg, unsigned int idx)

    flush Tx FIFO

    :param hsotg:
        The driver state
    :type hsotg: struct dwc2_hsotg \*

    :param idx:
        The index for the endpoint (0..15)
    :type idx: unsigned int

.. _`dwc2_hsotg_trytx`:

dwc2_hsotg_trytx
================

.. c:function:: int dwc2_hsotg_trytx(struct dwc2_hsotg *hsotg, struct dwc2_hsotg_ep *hs_ep)

    check to see if anything needs transmitting

    :param hsotg:
        The driver state
    :type hsotg: struct dwc2_hsotg \*

    :param hs_ep:
        The driver endpoint to check.
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`dwc2_hsotg_trytx.description`:

Description
-----------

Check to see if there is a request that has data to send, and if so
make an attempt to write data into the FIFO.

.. _`dwc2_hsotg_complete_in`:

dwc2_hsotg_complete_in
======================

.. c:function:: void dwc2_hsotg_complete_in(struct dwc2_hsotg *hsotg, struct dwc2_hsotg_ep *hs_ep)

    complete IN transfer

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

    :param hs_ep:
        The endpoint that has just completed.
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`dwc2_hsotg_complete_in.description`:

Description
-----------

An IN transfer has been completed, update the transfer's state and then
call the relevant completion routines.

.. _`dwc2_gadget_read_ep_interrupts`:

dwc2_gadget_read_ep_interrupts
==============================

.. c:function:: u32 dwc2_gadget_read_ep_interrupts(struct dwc2_hsotg *hsotg, unsigned int idx, int dir_in)

    reads interrupts for given ep

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

    :param idx:
        Index of ep.
    :type idx: unsigned int

    :param dir_in:
        Endpoint direction 1-in 0-out.
    :type dir_in: int

.. _`dwc2_gadget_read_ep_interrupts.description`:

Description
-----------

Reads for endpoint with given index and direction, by masking
epint_reg with coresponding mask.

.. _`dwc2_gadget_handle_ep_disabled`:

dwc2_gadget_handle_ep_disabled
==============================

.. c:function:: void dwc2_gadget_handle_ep_disabled(struct dwc2_hsotg_ep *hs_ep)

    handle DXEPINT_EPDISBLD

    :param hs_ep:
        The endpoint on which interrupt is asserted.
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`dwc2_gadget_handle_ep_disabled.description`:

Description
-----------

This interrupt indicates that the endpoint has been disabled per the
application's request.

For IN endpoints flushes txfifo, in case of BULK clears DCTL_CGNPINNAK,
in case of ISOC completes current request.

For ISOC-OUT endpoints completes expired requests. If there is remaining
request starts it.

.. _`dwc2_gadget_handle_out_token_ep_disabled`:

dwc2_gadget_handle_out_token_ep_disabled
========================================

.. c:function:: void dwc2_gadget_handle_out_token_ep_disabled(struct dwc2_hsotg_ep *ep)

    handle DXEPINT_OUTTKNEPDIS

    :param ep:
        The endpoint on which interrupt is asserted.
    :type ep: struct dwc2_hsotg_ep \*

.. _`dwc2_gadget_handle_out_token_ep_disabled.description`:

Description
-----------

This is starting point for ISOC-OUT transfer, synchronization done with
first out token received from host while corresponding EP is disabled.

Device does not know initial frame in which out token will come. For this
HW generates OUTTKNEPDIS - out token is received while EP is disabled. Upon
getting this interrupt SW starts calculation for next transfer frame.

.. _`dwc2_gadget_handle_nak`:

dwc2_gadget_handle_nak
======================

.. c:function:: void dwc2_gadget_handle_nak(struct dwc2_hsotg_ep *hs_ep)

    handle NAK interrupt

    :param hs_ep:
        The endpoint on which interrupt is asserted.
    :type hs_ep: struct dwc2_hsotg_ep \*

.. _`dwc2_gadget_handle_nak.description`:

Description
-----------

This is starting point for ISOC-IN transfer, synchronization done with
first IN token received from host while corresponding EP is disabled.

Device does not know when first one token will arrive from host. On first

.. _`dwc2_gadget_handle_nak.token-arrival-hw-generates-2-interrupts`:

token arrival HW generates 2 interrupts
---------------------------------------

'in token received while FIFO empty'
and 'NAK'. NAK interrupt for ISOC-IN means that token has arrived and ZLP was
sent in response to that as there was no data in FIFO. SW is basing on this
interrupt to obtain frame in which token has come and then based on the
interval calculates next frame for transfer.

.. _`dwc2_hsotg_epint`:

dwc2_hsotg_epint
================

.. c:function:: void dwc2_hsotg_epint(struct dwc2_hsotg *hsotg, unsigned int idx, int dir_in)

    handle an in/out endpoint interrupt

    :param hsotg:
        The driver state
    :type hsotg: struct dwc2_hsotg \*

    :param idx:
        The index for the endpoint (0..15)
    :type idx: unsigned int

    :param dir_in:
        Set if this is an IN endpoint
    :type dir_in: int

.. _`dwc2_hsotg_epint.description`:

Description
-----------

Process and clear any interrupt pending for an individual endpoint

.. _`dwc2_hsotg_irq_enumdone`:

dwc2_hsotg_irq_enumdone
=======================

.. c:function:: void dwc2_hsotg_irq_enumdone(struct dwc2_hsotg *hsotg)

    Handle EnumDone interrupt (enumeration done)

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_irq_enumdone.description`:

Description
-----------

Handle updating the device settings after the enumeration phase has
been completed.

.. _`kill_all_requests`:

kill_all_requests
=================

.. c:function:: void kill_all_requests(struct dwc2_hsotg *hsotg, struct dwc2_hsotg_ep *ep, int result)

    remove all requests from the endpoint's queue

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

    :param ep:
        The endpoint the requests may be on.
    :type ep: struct dwc2_hsotg_ep \*

    :param result:
        The result code to use.
    :type result: int

.. _`kill_all_requests.description`:

Description
-----------

Go through the requests on the given endpoint and mark them
completed with the given result code.

.. _`dwc2_hsotg_disconnect`:

dwc2_hsotg_disconnect
=====================

.. c:function:: void dwc2_hsotg_disconnect(struct dwc2_hsotg *hsotg)

    disconnect service

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_disconnect.description`:

Description
-----------

The device has been disconnected. Remove all current
transactions and signal the gadget driver that this
has happened.

.. _`dwc2_hsotg_irq_fifoempty`:

dwc2_hsotg_irq_fifoempty
========================

.. c:function:: void dwc2_hsotg_irq_fifoempty(struct dwc2_hsotg *hsotg, bool periodic)

    TX FIFO empty interrupt handler

    :param hsotg:
        The device state:
    :type hsotg: struct dwc2_hsotg \*

    :param periodic:
        True if this is a periodic FIFO interrupt
    :type periodic: bool

.. _`dwc2_hsotg_core_init_disconnected`:

dwc2_hsotg_core_init_disconnected
=================================

.. c:function:: void dwc2_hsotg_core_init_disconnected(struct dwc2_hsotg *hsotg, bool is_usb_reset)

    issue softreset to the core

    :param hsotg:
        The device state
    :type hsotg: struct dwc2_hsotg \*

    :param is_usb_reset:
        Usb resetting flag
    :type is_usb_reset: bool

.. _`dwc2_hsotg_core_init_disconnected.description`:

Description
-----------

Issue a soft reset to the core, and await the core finishing it.

.. _`dwc2_gadget_handle_incomplete_isoc_in`:

dwc2_gadget_handle_incomplete_isoc_in
=====================================

.. c:function:: void dwc2_gadget_handle_incomplete_isoc_in(struct dwc2_hsotg *hsotg)

    handle incomplete ISO IN Interrupt.

    :param hsotg:
        The device state:
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_gadget_handle_incomplete_isoc_in.description`:

Description
-----------

This interrupt indicates one of the following conditions occurred while
transmitting an ISOC transaction.
- Corrupted IN Token for ISOC EP.
- Packet not complete in FIFO.

.. _`dwc2_gadget_handle_incomplete_isoc_in.the-following-actions-will-be-taken`:

The following actions will be taken
-----------------------------------

- Determine the EP
- Disable EP; when 'Endpoint Disabled' interrupt is received Flush FIFO

.. _`dwc2_gadget_handle_incomplete_isoc_out`:

dwc2_gadget_handle_incomplete_isoc_out
======================================

.. c:function:: void dwc2_gadget_handle_incomplete_isoc_out(struct dwc2_hsotg *hsotg)

    handle incomplete ISO OUT Interrupt

    :param hsotg:
        The device state:
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_gadget_handle_incomplete_isoc_out.description`:

Description
-----------

This interrupt indicates one of the following conditions occurred while
transmitting an ISOC transaction.
- Corrupted OUT Token for ISOC EP.
- Packet not complete in FIFO.

.. _`dwc2_gadget_handle_incomplete_isoc_out.the-following-actions-will-be-taken`:

The following actions will be taken
-----------------------------------

- Determine the EP
- Set DCTL_SGOUTNAK and unmask GOUTNAKEFF if target frame elapsed.

.. _`dwc2_hsotg_irq`:

dwc2_hsotg_irq
==============

.. c:function:: irqreturn_t dwc2_hsotg_irq(int irq, void *pw)

    handle device interrupt

    :param irq:
        The IRQ number triggered
    :type irq: int

    :param pw:
        The pw value when registered the handler.
    :type pw: void \*

.. _`dwc2_hsotg_ep_enable`:

dwc2_hsotg_ep_enable
====================

.. c:function:: int dwc2_hsotg_ep_enable(struct usb_ep *ep, const struct usb_endpoint_descriptor *desc)

    enable the given endpoint

    :param ep:
        The USB endpint to configure
    :type ep: struct usb_ep \*

    :param desc:
        The USB endpoint descriptor to configure with.
    :type desc: const struct usb_endpoint_descriptor \*

.. _`dwc2_hsotg_ep_enable.description`:

Description
-----------

This is called from the USB gadget code's \ :c:func:`usb_ep_enable`\ .

.. _`dwc2_hsotg_ep_disable`:

dwc2_hsotg_ep_disable
=====================

.. c:function:: int dwc2_hsotg_ep_disable(struct usb_ep *ep)

    disable given endpoint

    :param ep:
        The endpoint to disable.
    :type ep: struct usb_ep \*

.. _`on_list`:

on_list
=======

.. c:function:: bool on_list(struct dwc2_hsotg_ep *ep, struct dwc2_hsotg_req *test)

    check request is on the given endpoint

    :param ep:
        The endpoint to check.
    :type ep: struct dwc2_hsotg_ep \*

    :param test:
        The request to test if it is on the endpoint.
    :type test: struct dwc2_hsotg_req \*

.. _`dwc2_hsotg_ep_dequeue`:

dwc2_hsotg_ep_dequeue
=====================

.. c:function:: int dwc2_hsotg_ep_dequeue(struct usb_ep *ep, struct usb_request *req)

    dequeue given endpoint

    :param ep:
        The endpoint to dequeue.
    :type ep: struct usb_ep \*

    :param req:
        The request to be removed from a queue.
    :type req: struct usb_request \*

.. _`dwc2_hsotg_ep_sethalt`:

dwc2_hsotg_ep_sethalt
=====================

.. c:function:: int dwc2_hsotg_ep_sethalt(struct usb_ep *ep, int value, bool now)

    set halt on a given endpoint

    :param ep:
        The endpoint to set halt.
    :type ep: struct usb_ep \*

    :param value:
        Set or unset the halt.
    :type value: int

    :param now:
        If true, stall the endpoint now. Otherwise return -EAGAIN if
        the endpoint is busy processing requests.
    :type now: bool

.. _`dwc2_hsotg_ep_sethalt.description`:

Description
-----------

We need to stall the endpoint immediately if request comes from set_feature
protocol command handler.

.. _`dwc2_hsotg_ep_sethalt_lock`:

dwc2_hsotg_ep_sethalt_lock
==========================

.. c:function:: int dwc2_hsotg_ep_sethalt_lock(struct usb_ep *ep, int value)

    set halt on a given endpoint with lock held

    :param ep:
        The endpoint to set halt.
    :type ep: struct usb_ep \*

    :param value:
        Set or unset the halt.
    :type value: int

.. _`dwc2_hsotg_init`:

dwc2_hsotg_init
===============

.. c:function:: void dwc2_hsotg_init(struct dwc2_hsotg *hsotg)

    initialize the usb core

    :param hsotg:
        The driver state
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_udc_start`:

dwc2_hsotg_udc_start
====================

.. c:function:: int dwc2_hsotg_udc_start(struct usb_gadget *gadget, struct usb_gadget_driver *driver)

    prepare the udc for work

    :param gadget:
        The usb gadget state
    :type gadget: struct usb_gadget \*

    :param driver:
        The usb gadget driver
    :type driver: struct usb_gadget_driver \*

.. _`dwc2_hsotg_udc_start.description`:

Description
-----------

Perform initialization to prepare udc device and driver
to work.

.. _`dwc2_hsotg_udc_stop`:

dwc2_hsotg_udc_stop
===================

.. c:function:: int dwc2_hsotg_udc_stop(struct usb_gadget *gadget)

    stop the udc

    :param gadget:
        The usb gadget state
    :type gadget: struct usb_gadget \*

.. _`dwc2_hsotg_udc_stop.description`:

Description
-----------

Stop udc hw block and stay tunned for future transmissions

.. _`dwc2_hsotg_gadget_getframe`:

dwc2_hsotg_gadget_getframe
==========================

.. c:function:: int dwc2_hsotg_gadget_getframe(struct usb_gadget *gadget)

    read the frame number

    :param gadget:
        The usb gadget state
    :type gadget: struct usb_gadget \*

.. _`dwc2_hsotg_gadget_getframe.description`:

Description
-----------

Read the {micro} frame number

.. _`dwc2_hsotg_pullup`:

dwc2_hsotg_pullup
=================

.. c:function:: int dwc2_hsotg_pullup(struct usb_gadget *gadget, int is_on)

    connect/disconnect the USB PHY

    :param gadget:
        The usb gadget state
    :type gadget: struct usb_gadget \*

    :param is_on:
        Current state of the USB PHY
    :type is_on: int

.. _`dwc2_hsotg_pullup.description`:

Description
-----------

Connect/Disconnect the USB PHY pullup

.. _`dwc2_hsotg_vbus_draw`:

dwc2_hsotg_vbus_draw
====================

.. c:function:: int dwc2_hsotg_vbus_draw(struct usb_gadget *gadget, unsigned int mA)

    report bMaxPower field

    :param gadget:
        The usb gadget state
    :type gadget: struct usb_gadget \*

    :param mA:
        Amount of current
    :type mA: unsigned int

.. _`dwc2_hsotg_vbus_draw.description`:

Description
-----------

Report how much power the device may consume to the phy.

.. _`dwc2_hsotg_initep`:

dwc2_hsotg_initep
=================

.. c:function:: void dwc2_hsotg_initep(struct dwc2_hsotg *hsotg, struct dwc2_hsotg_ep *hs_ep, int epnum, bool dir_in)

    initialise a single endpoint

    :param hsotg:
        The device state.
    :type hsotg: struct dwc2_hsotg \*

    :param hs_ep:
        The endpoint to be initialised.
    :type hs_ep: struct dwc2_hsotg_ep \*

    :param epnum:
        The endpoint number
    :type epnum: int

    :param dir_in:
        True if direction is in.
    :type dir_in: bool

.. _`dwc2_hsotg_initep.description`:

Description
-----------

Initialise the given endpoint (as part of the probe and device state
creation) to give to the gadget driver. Setup the endpoint name, any
direction information and other state that may be required.

.. _`dwc2_hsotg_hw_cfg`:

dwc2_hsotg_hw_cfg
=================

.. c:function:: int dwc2_hsotg_hw_cfg(struct dwc2_hsotg *hsotg)

    read HW configuration registers

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_hw_cfg.description`:

Description
-----------

Read the USB core HW configuration registers

.. _`dwc2_hsotg_dump`:

dwc2_hsotg_dump
===============

.. c:function:: void dwc2_hsotg_dump(struct dwc2_hsotg *hsotg)

    dump state of the udc

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_gadget_init`:

dwc2_gadget_init
================

.. c:function:: int dwc2_gadget_init(struct dwc2_hsotg *hsotg)

    init function for gadget

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hsotg_remove`:

dwc2_hsotg_remove
=================

.. c:function:: int dwc2_hsotg_remove(struct dwc2_hsotg *hsotg)

    remove function for hsotg driver

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_backup_device_registers`:

dwc2_backup_device_registers
============================

.. c:function:: int dwc2_backup_device_registers(struct dwc2_hsotg *hsotg)

    Backup controller device registers. When suspending usb bus, registers needs to be backuped if controller power is disabled once suspended.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_restore_device_registers`:

dwc2_restore_device_registers
=============================

.. c:function:: int dwc2_restore_device_registers(struct dwc2_hsotg *hsotg, int remote_wakeup)

    Restore controller device registers. When resuming usb bus, device registers needs to be restored if controller power were disabled.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

    :param remote_wakeup:
        Indicates whether resume is initiated by Device or Host.
    :type remote_wakeup: int

.. _`dwc2_restore_device_registers.return`:

Return
------

0 if successful, negative error code otherwise

.. _`dwc2_gadget_init_lpm`:

dwc2_gadget_init_lpm
====================

.. c:function:: void dwc2_gadget_init_lpm(struct dwc2_hsotg *hsotg)

    Configure the core to support LPM in device mode

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_gadget_program_ref_clk`:

dwc2_gadget_program_ref_clk
===========================

.. c:function:: void dwc2_gadget_program_ref_clk(struct dwc2_hsotg *hsotg)

    Program GREFCLK register in device mode

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_gadget_enter_hibernation`:

dwc2_gadget_enter_hibernation
=============================

.. c:function:: int dwc2_gadget_enter_hibernation(struct dwc2_hsotg *hsotg)

    Put controller in Hibernation.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_gadget_enter_hibernation.description`:

Description
-----------

Return non-zero if failed to enter to hibernation.

.. _`dwc2_gadget_exit_hibernation`:

dwc2_gadget_exit_hibernation
============================

.. c:function:: int dwc2_gadget_exit_hibernation(struct dwc2_hsotg *hsotg, int rem_wakeup, int reset)

    This function is for exiting from Device mode hibernation by host initiated resume/reset and device initiated remote-wakeup.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

    :param rem_wakeup:
        indicates whether resume is initiated by Device or Host.
    :type rem_wakeup: int

    :param reset:
        indicates whether resume is initiated by Reset.
    :type reset: int

.. _`dwc2_gadget_exit_hibernation.description`:

Description
-----------

Return non-zero if failed to exit from hibernation.

.. This file was automatic generated / don't edit.

