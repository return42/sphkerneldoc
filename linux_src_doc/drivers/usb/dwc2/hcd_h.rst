.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/hcd.h

.. _`dwc2_host_chan`:

struct dwc2_host_chan
=====================

.. c:type:: struct dwc2_host_chan

    Software host channel descriptor

.. _`dwc2_host_chan.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_host_chan {
        u8 hc_num;
        unsigned dev_addr:7;
        unsigned ep_num:4;
        unsigned ep_is_in:1;
        unsigned speed:4;
        unsigned ep_type:2;
        unsigned max_packet:11;
        unsigned data_pid_start:2;
    #define DWC2_HC_PID_DATA0 TSIZ_SC_MC_PID_DATA0
    #define DWC2_HC_PID_DATA2 TSIZ_SC_MC_PID_DATA2
    #define DWC2_HC_PID_DATA1 TSIZ_SC_MC_PID_DATA1
    #define DWC2_HC_PID_MDATA TSIZ_SC_MC_PID_MDATA
    #define DWC2_HC_PID_SETUP TSIZ_SC_MC_PID_SETUP
        unsigned multi_count:2;
        u8 *xfer_buf;
        dma_addr_t xfer_dma;
        dma_addr_t align_buf;
        u32 xfer_len;
        u32 xfer_count;
        u16 start_pkt_count;
        u8 xfer_started;
        u8 do_ping;
        u8 error_state;
        u8 halt_on_queue;
        u8 halt_pending;
        u8 do_split;
        u8 complete_split;
        u8 hub_addr;
        u8 hub_port;
        u8 xact_pos;
    #define DWC2_HCSPLT_XACTPOS_MID HCSPLT_XACTPOS_MID
    #define DWC2_HCSPLT_XACTPOS_END HCSPLT_XACTPOS_END
    #define DWC2_HCSPLT_XACTPOS_BEGIN HCSPLT_XACTPOS_BEGIN
    #define DWC2_HCSPLT_XACTPOS_ALL HCSPLT_XACTPOS_ALL
        u8 requests;
        u8 schinfo;
        u16 ntd;
        enum dwc2_halt_status halt_status;
        u32 hcint;
        struct dwc2_qh *qh;
        struct list_head hc_list_entry;
        dma_addr_t desc_list_addr;
        u32 desc_list_sz;
        struct list_head split_order_list_entry;
    }

.. _`dwc2_host_chan.members`:

Members
-------

hc_num
    Host channel number, used for register address lookup

dev_addr
    Address of the device

ep_num
    Endpoint of the device

ep_is_in
    Endpoint direction

speed
    Device speed. One of the following values:
    - USB_SPEED_LOW
    - USB_SPEED_FULL
    - USB_SPEED_HIGH

ep_type
    Endpoint type. One of the following values:
    - USB_ENDPOINT_XFER_CONTROL: 0
    - USB_ENDPOINT_XFER_ISOC:    1
    - USB_ENDPOINT_XFER_BULK:    2
    - USB_ENDPOINT_XFER_INTR:    3

max_packet
    Max packet size in bytes

data_pid_start
    PID for initial transaction.
    0: DATA0
    1: DATA2
    2: DATA1
    3: MDATA (non-Control EP),
    SETUP (Control EP)

multi_count
    Number of additional periodic transactions per
    (micro)frame

xfer_buf
    Pointer to current transfer buffer position

xfer_dma
    DMA address of xfer_buf

align_buf
    In Buffer DMA mode this will be used if xfer_buf is not
    DWORD aligned

xfer_len
    Total number of bytes to transfer

xfer_count
    Number of bytes transferred so far

start_pkt_count
    Packet count at start of transfer

xfer_started
    True if the transfer has been started

do_ping
    True if a PING request should be issued on this channel

error_state
    True if the error count for this transaction is non-zero

halt_on_queue
    True if this channel should be halted the next time a
    request is queued for the channel. This is necessary in
    slave mode if no request queue space is available when
    an attempt is made to halt the channel.

halt_pending
    True if the host channel has been halted, but the core
    is not finished flushing queued requests

do_split
    Enable split for the channel

complete_split
    Enable complete split

hub_addr
    Address of high speed hub for the split

hub_port
    Port of the low/full speed device for the split

xact_pos
    Split transaction position. One of the following values:
    - DWC2_HCSPLT_XACTPOS_MID
    - DWC2_HCSPLT_XACTPOS_BEGIN
    - DWC2_HCSPLT_XACTPOS_END
    - DWC2_HCSPLT_XACTPOS_ALL

requests
    Number of requests issued for this channel since it was
    assigned to the current transfer (not counting PINGs)

schinfo
    Scheduling micro-frame bitmap

ntd
    Number of transfer descriptors for the transfer

halt_status
    Reason for halting the host channel

hcint
    Contents of the HCINT register when the interrupt came

qh
    QH for the transfer being processed by this channel

hc_list_entry
    For linking to list of host channels

desc_list_addr
    Current QH's descriptor list DMA address

desc_list_sz
    Current QH's descriptor list size

split_order_list_entry
    List entry for keeping track of the order of splits

.. _`dwc2_host_chan.description`:

Description
-----------

This structure represents the state of a single host channel when acting in
host mode. It contains the data items needed to transfer packets to an
endpoint via a host channel.

.. _`dwc2_tt`:

struct dwc2_tt
==============

.. c:type:: struct dwc2_tt

    dwc2 data associated with a usb_tt

.. _`dwc2_tt.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_tt {
        int refcount;
        struct usb_tt *usb_tt;
        unsigned long periodic_bitmaps[];
    }

.. _`dwc2_tt.members`:

Members
-------

refcount
    Number of Queue Heads (QHs) holding a reference.

usb_tt
    Pointer back to the official usb_tt.

periodic_bitmaps
    Bitmap for which parts of the 1ms frame are accounted
    for already.  Each is DWC2_ELEMENTS_PER_LS_BITMAP
    elements (so sizeof(long) times that in bytes).

.. _`dwc2_tt.description`:

Description
-----------

This structure is stored in the hcpriv of the official usb_tt.

.. _`dwc2_hs_transfer_time`:

struct dwc2_hs_transfer_time
============================

.. c:type:: struct dwc2_hs_transfer_time

    Info about a transfer on the high speed bus.

.. _`dwc2_hs_transfer_time.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_hs_transfer_time {
        u32 start_schedule_us;
        u16 duration_us;
    }

.. _`dwc2_hs_transfer_time.members`:

Members
-------

start_schedule_us
    The start time on the main bus schedule.  Note that
    the main bus schedule is tightly packed and this
    time should be interpreted as tightly packed (so
    uFrame 0 starts at 0 us, uFrame 1 starts at 100 us
    instead of 125 us).

duration_us
    How long this transfer goes.

.. _`dwc2_qh`:

struct dwc2_qh
==============

.. c:type:: struct dwc2_qh

    Software queue head structure

.. _`dwc2_qh.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_qh {
        struct dwc2_hsotg *hsotg;
        u8 ep_type;
        u8 ep_is_in;
        u16 maxp;
        u8 dev_speed;
        u8 data_toggle;
        u8 ping_state;
        u8 do_split;
        u8 td_first;
        u8 td_last;
        u16 host_us;
        u16 device_us;
        u16 host_interval;
        u16 device_interval;
        u16 next_active_frame;
        u16 start_active_frame;
        s16 num_hs_transfers;
        struct dwc2_hs_transfer_time hs_transfers[DWC2_HS_SCHEDULE_UFRAMES];
        u32 ls_start_schedule_slice;
        u16 ntd;
        u8 *dw_align_buf;
        dma_addr_t dw_align_buf_dma;
        struct list_head qtd_list;
        struct dwc2_host_chan *channel;
        struct list_head qh_list_entry;
        struct dwc2_dma_desc *desc_list;
        dma_addr_t desc_list_dma;
        u32 desc_list_sz;
        u32 *n_bytes;
        struct timer_list unreserve_timer;
        struct timer_list wait_timer;
        struct dwc2_tt *dwc_tt;
        int ttport;
        unsigned tt_buffer_dirty:1;
        unsigned unreserve_pending:1;
        unsigned schedule_low_speed:1;
        unsigned want_wait:1;
        unsigned wait_timer_cancel:1;
    }

.. _`dwc2_qh.members`:

Members
-------

hsotg
    The HCD state structure for the DWC OTG controller

ep_type
    Endpoint type. One of the following values:
    - USB_ENDPOINT_XFER_CONTROL
    - USB_ENDPOINT_XFER_BULK
    - USB_ENDPOINT_XFER_INT
    - USB_ENDPOINT_XFER_ISOC

ep_is_in
    Endpoint direction

maxp
    Value from wMaxPacketSize field of Endpoint Descriptor

dev_speed
    Device speed. One of the following values:
    - USB_SPEED_LOW
    - USB_SPEED_FULL
    - USB_SPEED_HIGH

data_toggle
    Determines the PID of the next data packet for
    non-controltransfers. Ignored for control transfers.
    One of the following values:
    - DWC2_HC_PID_DATA0
    - DWC2_HC_PID_DATA1

ping_state
    Ping state

do_split
    Full/low speed endpoint on high-speed hub requires split

td_first
    Index of first activated isochronous transfer descriptor

td_last
    Index of last activated isochronous transfer descriptor

host_us
    Bandwidth in microseconds per transfer as seen by host

device_us
    Bandwidth in microseconds per transfer as seen by device

host_interval
    Interval between transfers as seen by the host.  If
    the host is high speed and the device is low speed this
    will be 8 times device interval.

device_interval
    Interval between transfers as seen by the device.
    interval.

next_active_frame
    (Micro)frame \_before\_ we next need to put something on
    the bus.  We'll move the qh to active here.  If the
    host is in high speed mode this will be a uframe.  If
    the host is in low speed mode this will be a full frame.

start_active_frame
    If we are partway through a split transfer, this will be
    what next_active_frame was when we started.  Otherwise
    it should always be the same as next_active_frame.

num_hs_transfers
    Number of transfers in hs_transfers.
    Normally this is 1 but can be more than one for splits.
    Always >= 1 unless the host is in low/full speed mode.

hs_transfers
    Transfers that are scheduled as seen by the high speed
    bus.  Not used if host is in low or full speed mode (but
    note that it IS USED if the device is low or full speed
    as long as the HOST is in high speed mode).

ls_start_schedule_slice
    Start time (in slices) on the low speed bus
    schedule that's being used by this device.  This
    will be on the periodic_bitmap in a
    "struct dwc2_tt".  Not used if this device is high
    speed.  Note that this is in "schedule slice" which
    is tightly packed.

ntd
    Actual number of transfer descriptors in a list

dw_align_buf
    Used instead of original buffer if its physical address
    is not dword-aligned

dw_align_buf_dma
    DMA address for dw_align_buf

qtd_list
    List of QTDs for this QH

channel
    Host channel currently processing transfers for this QH

qh_list_entry
    Entry for QH in either the periodic or non-periodic
    schedule

desc_list
    List of transfer descriptors

desc_list_dma
    Physical address of desc_list

desc_list_sz
    Size of descriptors list

n_bytes
    Xfer Bytes array. Each element corresponds to a transfer
    descriptor and indicates original XferSize value for the
    descriptor

unreserve_timer
    Timer for releasing periodic reservation.

wait_timer
    Timer used to wait before re-queuing.

dwc_tt
    Pointer to our tt info (or NULL if no tt).

ttport
    Port number within our tt.
    \ ``tt_buffer_dirty``\      True if clear_tt_buffer_complete is pending

tt_buffer_dirty
    True if EP's TT buffer is not clean.
    A Queue Head (QH) holds the static characteristics of an endpoint and
    maintains a list of transfers (QTDs) for that endpoint. A QH structure may
    be entered in either the non-periodic or periodic schedule.

unreserve_pending
    True if we planned to unreserve but haven't yet.

schedule_low_speed
    True if we have a low/full speed component (either the
    host is in low/full speed mode or do_split).

want_wait
    We should wait before re-queuing; only matters for non-
    periodic transfers and is ignored for periodic ones.

wait_timer_cancel
    Set to true to cancel the wait_timer.

.. _`dwc2_qtd`:

struct dwc2_qtd
===============

.. c:type:: struct dwc2_qtd

    Software queue transfer descriptor (QTD)

.. _`dwc2_qtd.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_qtd {
        enum dwc2_control_phase control_phase;
        u8 in_process;
        u8 data_toggle;
        u8 complete_split;
        u8 isoc_split_pos;
        u16 isoc_frame_index;
        u16 isoc_split_offset;
        u16 isoc_td_last;
        u16 isoc_td_first;
        u32 ssplit_out_xfer_count;
        u8 error_count;
        u8 n_desc;
        u16 isoc_frame_index_last;
        u16 num_naks;
        struct dwc2_hcd_urb *urb;
        struct dwc2_qh *qh;
        struct list_head qtd_list_entry;
    }

.. _`dwc2_qtd.members`:

Members
-------

control_phase
    Current phase for control transfers (Setup, Data, or
    Status)

in_process
    Indicates if this QTD is currently processed by HW

data_toggle
    Determines the PID of the next data packet for the
    data phase of control transfers. Ignored for other
    transfer types. One of the following values:
    - DWC2_HC_PID_DATA0
    - DWC2_HC_PID_DATA1

complete_split
    Keeps track of the current split type for FS/LS
    endpoints on a HS Hub

isoc_split_pos
    Position of the ISOC split in full/low speed

isoc_frame_index
    Index of the next frame descriptor for an isochronous
    transfer. A frame descriptor describes the buffer
    position and length of the data to be transferred in the
    next scheduled (micro)frame of an isochronous transfer.
    It also holds status for that transaction. The frame
    index starts at 0.

isoc_split_offset
    Position of the ISOC split in the buffer for the
    current frame

isoc_td_last
    Index of last activated isochronous transfer
    descriptor in Descriptor DMA mode

isoc_td_first
    Index of first activated isochronous transfer
    descriptor in Descriptor DMA mode

ssplit_out_xfer_count
    How many bytes transferred during SSPLIT OUT

error_count
    Holds the number of bus errors that have occurred for
    a transaction within this transfer

n_desc
    Number of DMA descriptors for this QTD

isoc_frame_index_last
    Last activated frame (packet) index, used in
    descriptor DMA mode only

num_naks
    Number of NAKs received on this QTD.

urb
    URB for this transfer

qh
    Queue head for this QTD

qtd_list_entry
    For linking to the QH's list of QTDs

.. _`dwc2_qtd.description`:

Description
-----------

A Queue Transfer Descriptor (QTD) holds the state of a bulk, control,
interrupt, or isochronous transfer. A single QTD is created for each URB
(of one of these types) submitted to the HCD. The transfer associated with
a QTD may require one or multiple transactions.

A QTD is linked to a Queue Head, which is entered in either the
non-periodic or periodic schedule for execution. When a QTD is chosen for
execution, some or all of its transactions may be executed. After
execution, the state of the QTD is updated. The QTD may be retired if all
its transactions are complete or if an error occurred. Otherwise, it
remains in the schedule so more transactions can be executed later.

.. _`dwc2_handle_hcd_intr`:

dwc2_handle_hcd_intr
====================

.. c:function:: irqreturn_t dwc2_handle_hcd_intr(struct dwc2_hsotg *hsotg)

    Called on every hardware interrupt

    :param hsotg:
        The DWC2 HCD
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_handle_hcd_intr.description`:

Description
-----------

Returns IRQ_HANDLED if interrupt is handled
Return IRQ_NONE if interrupt is not handled

.. _`dwc2_hcd_stop`:

dwc2_hcd_stop
=============

.. c:function:: void dwc2_hcd_stop(struct dwc2_hsotg *hsotg)

    Halts the DWC_otg host mode operation

    :param hsotg:
        The DWC2 HCD
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hcd_is_b_host`:

dwc2_hcd_is_b_host
==================

.. c:function:: int dwc2_hcd_is_b_host(struct dwc2_hsotg *hsotg)

    Returns 1 if core currently is acting as B host, and 0 otherwise

    :param hsotg:
        The DWC2 HCD
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hcd_dump_state`:

dwc2_hcd_dump_state
===================

.. c:function:: void dwc2_hcd_dump_state(struct dwc2_hsotg *hsotg)

    Dumps hsotg state

    :param hsotg:
        The DWC2 HCD
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_hcd_dump_state.note`:

NOTE
----

This function will be removed once the peripheral controller code
is integrated and the driver is stable

.. This file was automatic generated / don't edit.

