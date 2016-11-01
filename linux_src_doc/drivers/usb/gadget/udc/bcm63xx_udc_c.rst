.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/udc/bcm63xx_udc.c

.. _`iudma_ch_cfg`:

struct iudma_ch_cfg
===================

.. c:type:: struct iudma_ch_cfg

    Static configuration for an IUDMA channel.

.. _`iudma_ch_cfg.definition`:

Definition
----------

.. code-block:: c

    struct iudma_ch_cfg {
        int ep_num;
        int n_bds;
        int ep_type;
        int dir;
        int n_fifo_slots;
        int max_pkt_hs;
        int max_pkt_fs;
    }

.. _`iudma_ch_cfg.members`:

Members
-------

ep_num
    USB endpoint number.

n_bds
    Number of buffer descriptors in the ring.

ep_type
    Endpoint type (control, bulk, interrupt).

dir
    Direction (in, out).

n_fifo_slots
    Number of FIFO entries to allocate for this channel.

max_pkt_hs
    Maximum packet size in high speed mode.

max_pkt_fs
    Maximum packet size in full speed mode.

.. _`iudma_ch`:

struct iudma_ch
===============

.. c:type:: struct iudma_ch

    Represents the current state of a single IUDMA channel.

.. _`iudma_ch.definition`:

Definition
----------

.. code-block:: c

    struct iudma_ch {
        unsigned int ch_idx;
        int ep_num;
        bool enabled;
        int max_pkt;
        bool is_tx;
        struct bcm63xx_ep *bep;
        struct bcm63xx_udc *udc;
        struct bcm_enet_desc *read_bd;
        struct bcm_enet_desc *write_bd;
        struct bcm_enet_desc *end_bd;
        int n_bds_used;
        struct bcm_enet_desc *bd_ring;
        dma_addr_t bd_ring_dma;
        unsigned int n_bds;
    }

.. _`iudma_ch.members`:

Members
-------

ch_idx
    IUDMA channel index (0 to BCM63XX_NUM_IUDMA-1).

ep_num
    USB endpoint number.  -1 for ep0 RX.

enabled
    Whether \ :c:func:`bcm63xx_ep_enable`\  has been called.

max_pkt
    "Chunk size" on the USB interface.  Based on interface speed.

is_tx
    true for TX, false for RX.

bep
    Pointer to the associated endpoint.  NULL for ep0 RX.

udc
    Reference to the device controller.

read_bd
    Next buffer descriptor to reap from the hardware.

write_bd
    Next BD available for a new packet.

end_bd
    Points to the final BD in the ring.

n_bds_used
    Number of BD entries currently occupied.

bd_ring
    Base pointer to the BD ring.

bd_ring_dma
    Physical (DMA) address of bd_ring.

n_bds
    Total number of BDs in the ring.

.. _`iudma_ch.description`:

Description
-----------

ep0 has two IUDMA channels (IUDMA_EP0_RXCHAN and IUDMA_EP0_TXCHAN), as it is
bidirectional.  The "struct usb_ep" associated with ep0 is for TX (IN)
only.

Each bulk/intr endpoint has a single IUDMA channel and a single
struct usb_ep.

.. _`bcm63xx_ep`:

struct bcm63xx_ep
=================

.. c:type:: struct bcm63xx_ep

    Internal (driver) state of a single endpoint.

.. _`bcm63xx_ep.definition`:

Definition
----------

.. code-block:: c

    struct bcm63xx_ep {
        unsigned int ep_num;
        struct iudma_ch *iudma;
        struct usb_ep ep;
        struct bcm63xx_udc *udc;
        struct list_head queue;
        unsigned halted:1;
    }

.. _`bcm63xx_ep.members`:

Members
-------

ep_num
    USB endpoint number.

iudma
    Pointer to IUDMA channel state.

ep
    USB gadget layer representation of the EP.

udc
    Reference to the device controller.

queue
    Linked list of outstanding requests for this EP.

halted
    1 if the EP is stalled; 0 otherwise.

.. _`bcm63xx_req`:

struct bcm63xx_req
==================

.. c:type:: struct bcm63xx_req

    Internal (driver) state of a single request.

.. _`bcm63xx_req.definition`:

Definition
----------

.. code-block:: c

    struct bcm63xx_req {
        struct list_head queue;
        struct usb_request req;
        unsigned int offset;
        unsigned int bd_bytes;
        struct iudma_ch *iudma;
    }

.. _`bcm63xx_req.members`:

Members
-------

queue
    Links back to the EP's request list.

req
    USB gadget layer representation of the request.

offset
    Current byte offset into the data buffer (next byte to queue).

bd_bytes
    Number of data bytes in outstanding BD entries.

iudma
    IUDMA channel used for the request.

.. _`bcm63xx_udc`:

struct bcm63xx_udc
==================

.. c:type:: struct bcm63xx_udc

    Driver/hardware private context.

.. _`bcm63xx_udc.definition`:

Definition
----------

.. code-block:: c

    struct bcm63xx_udc {
        spinlock_t lock;
        struct device *dev;
        struct bcm63xx_usbd_platform_data *pd;
        struct clk *usbd_clk;
        struct clk *usbh_clk;
        struct usb_gadget gadget;
        struct usb_gadget_driver *driver;
        void __iomem *usbd_regs;
        void __iomem *iudma_regs;
        struct bcm63xx_ep bep[BCM63XX_NUM_EP];
        struct iudma_ch iudma[BCM63XX_NUM_IUDMA];
        int cfg;
        int iface;
        int alt_iface;
        struct bcm63xx_req ep0_ctrl_req;
        u8 *ep0_ctrl_buf;
        int ep0state;
        struct work_struct ep0_wq;
        unsigned long wedgemap;
        unsigned ep0_req_reset:1;
        unsigned ep0_req_set_cfg:1;
        unsigned ep0_req_set_iface:1;
        unsigned ep0_req_shutdown:1;
        unsigned ep0_req_completed:1;
        struct usb_request *ep0_reply;
        struct usb_request *ep0_request;
        struct dentry *debugfs_root;
        struct dentry *debugfs_usbd;
        struct dentry *debugfs_iudma;
    }

.. _`bcm63xx_udc.members`:

Members
-------

lock
    Spinlock to mediate access to this struct, and (most) HW regs.

dev
    Generic Linux device structure.

pd
    Platform data (board/port info).

usbd_clk
    Clock descriptor for the USB device block.

usbh_clk
    Clock descriptor for the USB host block.

gadget
    USB slave device.

driver
    Driver for USB slave devices.

usbd_regs
    Base address of the USBD/USB20D block.

iudma_regs
    Base address of the USBD's associated IUDMA block.

bep
    Array of endpoints, including ep0.

iudma
    Array of all IUDMA channels used by this controller.

cfg
    USB configuration number, from SET_CONFIGURATION wValue.

iface
    USB interface number, from SET_INTERFACE wIndex.

alt_iface
    USB alt interface number, from SET_INTERFACE wValue.

ep0_ctrl_req
    Request object for bcm63xx_udc-initiated ep0 transactions.

ep0_ctrl_buf
    Data buffer for ep0_ctrl_req.

ep0state
    Current state of the ep0 state machine.

ep0_wq
    Workqueue struct used to wake up the ep0 state machine.

wedgemap
    Bitmap of wedged endpoints.

ep0_req_reset
    USB reset is pending.

ep0_req_set_cfg
    Need to spoof a SET_CONFIGURATION packet.

ep0_req_set_iface
    Need to spoof a SET_INTERFACE packet.

ep0_req_shutdown
    Driver is shutting down; requesting ep0 to halt activity.

ep0_req_completed
    ep0 request has completed; worker has not seen it yet.

ep0_reply
    Pending reply from gadget driver.

ep0_request
    Outstanding ep0 request.

debugfs_root
    debugfs directory: /sys/kernel/debug/<DRV_MODULE_NAME>.

debugfs_usbd
    debugfs file "usbd" for controller state.

debugfs_iudma
    debugfs file "usbd" for IUDMA state.

.. _`bcm63xx_ep_dma_select`:

bcm63xx_ep_dma_select
=====================

.. c:function:: void bcm63xx_ep_dma_select(struct bcm63xx_udc *udc, int idx)

    Helper function to set up the init_sel signal.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param int idx:
        Desired init_sel value.

.. _`bcm63xx_ep_dma_select.description`:

Description
-----------

The "init_sel" signal is used as a selection index for both endpoints
and IUDMA channels.  Since these do not map 1:1, the use of this signal
depends on the context.

.. _`bcm63xx_set_stall`:

bcm63xx_set_stall
=================

.. c:function:: void bcm63xx_set_stall(struct bcm63xx_udc *udc, struct bcm63xx_ep *bep, bool is_stalled)

    Enable/disable stall on one endpoint.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param struct bcm63xx_ep \*bep:
        Endpoint on which to operate.

    :param bool is_stalled:
        true to enable stall, false to disable.

.. _`bcm63xx_set_stall.description`:

Description
-----------

See notes in \ :c:func:`bcm63xx_update_wedge`\  regarding automatic clearing of
halt/stall conditions.

.. _`bcm63xx_fifo_setup`:

bcm63xx_fifo_setup
==================

.. c:function:: void bcm63xx_fifo_setup(struct bcm63xx_udc *udc)

    (Re)initialize FIFO boundaries and settings.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_fifo_setup.description`:

Description
-----------

These parameters depend on the USB link speed.  Settings are
per-IUDMA-channel-pair.

.. _`bcm63xx_fifo_reset_ep`:

bcm63xx_fifo_reset_ep
=====================

.. c:function:: void bcm63xx_fifo_reset_ep(struct bcm63xx_udc *udc, int ep_num)

    Flush a single endpoint's FIFO.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param int ep_num:
        Endpoint number.

.. _`bcm63xx_fifo_reset`:

bcm63xx_fifo_reset
==================

.. c:function:: void bcm63xx_fifo_reset(struct bcm63xx_udc *udc)

    Flush all hardware FIFOs.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_ep_init`:

bcm63xx_ep_init
===============

.. c:function:: void bcm63xx_ep_init(struct bcm63xx_udc *udc)

    Initial (one-time) endpoint initialization.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_ep_setup`:

bcm63xx_ep_setup
================

.. c:function:: void bcm63xx_ep_setup(struct bcm63xx_udc *udc)

    Configure per-endpoint settings.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_ep_setup.description`:

Description
-----------

This needs to be rerun if the speed/cfg/intf/altintf changes.

.. _`iudma_write`:

iudma_write
===========

.. c:function:: void iudma_write(struct bcm63xx_udc *udc, struct iudma_ch *iudma, struct bcm63xx_req *breq)

    Queue a single IUDMA transaction.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param struct iudma_ch \*iudma:
        IUDMA channel to use.

    :param struct bcm63xx_req \*breq:
        Request containing the transaction data.

.. _`iudma_write.description`:

Description
-----------

For RX IUDMA, this will queue a single buffer descriptor, as RX IUDMA
does not honor SOP/EOP so the handling of multiple buffers is ambiguous.
So \ :c:func:`iudma_write`\  may be called several times to fulfill a single
usb_request.

For TX IUDMA, this can queue multiple buffer descriptors if needed.

.. _`iudma_read`:

iudma_read
==========

.. c:function:: int iudma_read(struct bcm63xx_udc *udc, struct iudma_ch *iudma)

    Check for IUDMA buffer completion.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param struct iudma_ch \*iudma:
        IUDMA channel to use.

.. _`iudma_read.description`:

Description
-----------

This checks to see if ALL of the outstanding BDs on the DMA channel
have been filled.  If so, it returns the actual transfer length;
otherwise it returns -EBUSY.

.. _`iudma_reset_channel`:

iudma_reset_channel
===================

.. c:function:: void iudma_reset_channel(struct bcm63xx_udc *udc, struct iudma_ch *iudma)

    Stop DMA on a single channel.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param struct iudma_ch \*iudma:
        IUDMA channel to reset.

.. _`iudma_init_channel`:

iudma_init_channel
==================

.. c:function:: int iudma_init_channel(struct bcm63xx_udc *udc, unsigned int ch_idx)

    One-time IUDMA channel initialization.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param unsigned int ch_idx:
        Channel to initialize.

.. _`iudma_init`:

iudma_init
==========

.. c:function:: int iudma_init(struct bcm63xx_udc *udc)

    One-time initialization of all IUDMA channels.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`iudma_init.description`:

Description
-----------

Enable DMA, flush channels, and enable global IUDMA IRQs.

.. _`iudma_uninit`:

iudma_uninit
============

.. c:function:: void iudma_uninit(struct bcm63xx_udc *udc)

    Uninitialize IUDMA channels.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`iudma_uninit.description`:

Description
-----------

Kill global IUDMA IRQs, flush channels, and kill DMA.

.. _`bcm63xx_set_ctrl_irqs`:

bcm63xx_set_ctrl_irqs
=====================

.. c:function:: void bcm63xx_set_ctrl_irqs(struct bcm63xx_udc *udc, bool enable_irqs)

    Mask/unmask control path interrupts.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param bool enable_irqs:
        true to enable, false to disable.

.. _`bcm63xx_select_phy_mode`:

bcm63xx_select_phy_mode
=======================

.. c:function:: void bcm63xx_select_phy_mode(struct bcm63xx_udc *udc, bool is_device)

    Select between USB device and host mode.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param bool is_device:
        true for device, false for host.

.. _`bcm63xx_select_phy_mode.description`:

Description
-----------

This should probably be reworked to use the drivers/usb/otg
infrastructure.

By default, the AFE/pullups are disabled in device mode, until
\ :c:func:`bcm63xx_select_pullup`\  is called.

.. _`bcm63xx_select_pullup`:

bcm63xx_select_pullup
=====================

.. c:function:: void bcm63xx_select_pullup(struct bcm63xx_udc *udc, bool is_on)

    Enable/disable the pullup on D+

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param bool is_on:
        true to enable the pullup, false to disable.

.. _`bcm63xx_select_pullup.description`:

Description
-----------

If the pullup is active, the host will sense a FS/HS device connected to
the port.  If the pullup is inactive, the host will think the USB
device has been disconnected.

.. _`bcm63xx_uninit_udc_hw`:

bcm63xx_uninit_udc_hw
=====================

.. c:function:: void bcm63xx_uninit_udc_hw(struct bcm63xx_udc *udc)

    Shut down the hardware prior to driver removal.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_uninit_udc_hw.description`:

Description
-----------

This just masks the IUDMA IRQs and releases the clocks.  It is assumed
that \ :c:func:`bcm63xx_udc_stop`\  has already run, and the clocks are stopped.

.. _`bcm63xx_init_udc_hw`:

bcm63xx_init_udc_hw
===================

.. c:function:: int bcm63xx_init_udc_hw(struct bcm63xx_udc *udc)

    Initialize the controller hardware and data structures.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_ep_enable`:

bcm63xx_ep_enable
=================

.. c:function:: int bcm63xx_ep_enable(struct usb_ep *ep, const struct usb_endpoint_descriptor *desc)

    Enable one endpoint.

    :param struct usb_ep \*ep:
        Endpoint to enable.

    :param const struct usb_endpoint_descriptor \*desc:
        Contains max packet, direction, etc.

.. _`bcm63xx_ep_enable.description`:

Description
-----------

Most of the endpoint parameters are fixed in this controller, so there
isn't much for this function to do.

.. _`bcm63xx_ep_disable`:

bcm63xx_ep_disable
==================

.. c:function:: int bcm63xx_ep_disable(struct usb_ep *ep)

    Disable one endpoint.

    :param struct usb_ep \*ep:
        Endpoint to disable.

.. _`bcm63xx_udc_alloc_request`:

bcm63xx_udc_alloc_request
=========================

.. c:function:: struct usb_request *bcm63xx_udc_alloc_request(struct usb_ep *ep, gfp_t mem_flags)

    Allocate a new request.

    :param struct usb_ep \*ep:
        Endpoint associated with the request.

    :param gfp_t mem_flags:
        Flags to pass to \ :c:func:`kzalloc`\ .

.. _`bcm63xx_udc_free_request`:

bcm63xx_udc_free_request
========================

.. c:function:: void bcm63xx_udc_free_request(struct usb_ep *ep, struct usb_request *req)

    Free a request.

    :param struct usb_ep \*ep:
        Endpoint associated with the request.

    :param struct usb_request \*req:
        Request to free.

.. _`bcm63xx_udc_queue`:

bcm63xx_udc_queue
=================

.. c:function:: int bcm63xx_udc_queue(struct usb_ep *ep, struct usb_request *req, gfp_t mem_flags)

    Queue up a new request.

    :param struct usb_ep \*ep:
        Endpoint associated with the request.

    :param struct usb_request \*req:
        Request to add.

    :param gfp_t mem_flags:
        Unused.

.. _`bcm63xx_udc_queue.description`:

Description
-----------

If the queue is empty, start this request immediately.  Otherwise, add
it to the list.

ep0 replies are sent through this function from the gadget driver, but
they are treated differently because they need to be handled by the ep0
state machine.  (Sometimes they are replies to control requests that
were spoofed by this driver, and so they shouldn't be transmitted at all.)

.. _`bcm63xx_udc_dequeue`:

bcm63xx_udc_dequeue
===================

.. c:function:: int bcm63xx_udc_dequeue(struct usb_ep *ep, struct usb_request *req)

    Remove a pending request from the queue.

    :param struct usb_ep \*ep:
        Endpoint associated with the request.

    :param struct usb_request \*req:
        Request to remove.

.. _`bcm63xx_udc_dequeue.description`:

Description
-----------

If the request is not at the head of the queue, this is easy - just nuke
it.  If the request is at the head of the queue, we'll need to stop the
DMA transaction and then queue up the successor.

.. _`bcm63xx_udc_set_halt`:

bcm63xx_udc_set_halt
====================

.. c:function:: int bcm63xx_udc_set_halt(struct usb_ep *ep, int value)

    Enable/disable STALL flag in the hardware.

    :param struct usb_ep \*ep:
        Endpoint to halt.

    :param int value:
        Zero to clear halt; nonzero to set halt.

.. _`bcm63xx_udc_set_halt.description`:

Description
-----------

See comments in \ :c:func:`bcm63xx_update_wedge`\ .

.. _`bcm63xx_udc_set_wedge`:

bcm63xx_udc_set_wedge
=====================

.. c:function:: int bcm63xx_udc_set_wedge(struct usb_ep *ep)

    Stall the endpoint until the next reset.

    :param struct usb_ep \*ep:
        Endpoint to wedge.

.. _`bcm63xx_udc_set_wedge.description`:

Description
-----------

See comments in \ :c:func:`bcm63xx_update_wedge`\ .

.. _`bcm63xx_ep0_setup_callback`:

bcm63xx_ep0_setup_callback
==========================

.. c:function:: int bcm63xx_ep0_setup_callback(struct bcm63xx_udc *udc, struct usb_ctrlrequest *ctrl)

    Drop spinlock to invoke ->setup callback.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param struct usb_ctrlrequest \*ctrl:
        8-byte SETUP request.

.. _`bcm63xx_ep0_spoof_set_cfg`:

bcm63xx_ep0_spoof_set_cfg
=========================

.. c:function:: int bcm63xx_ep0_spoof_set_cfg(struct bcm63xx_udc *udc)

    Synthesize a SET_CONFIGURATION request.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_ep0_spoof_set_cfg.description`:

Description
-----------

Many standard requests are handled automatically in the hardware, but
we still need to pass them to the gadget driver so that it can
reconfigure the interfaces/endpoints if necessary.

Unfortunately we are not able to send a STALL response if the host
requests an invalid configuration.  If this happens, we'll have to be
content with printing a warning.

.. _`bcm63xx_ep0_spoof_set_iface`:

bcm63xx_ep0_spoof_set_iface
===========================

.. c:function:: int bcm63xx_ep0_spoof_set_iface(struct bcm63xx_udc *udc)

    Synthesize a SET_INTERFACE request.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_ep0_map_write`:

bcm63xx_ep0_map_write
=====================

.. c:function:: void bcm63xx_ep0_map_write(struct bcm63xx_udc *udc, int ch_idx, struct usb_request *req)

    dma_map and iudma_write a single request.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param int ch_idx:
        IUDMA channel number.

    :param struct usb_request \*req:
        USB gadget layer representation of the request.

.. _`bcm63xx_ep0_complete`:

bcm63xx_ep0_complete
====================

.. c:function:: void bcm63xx_ep0_complete(struct bcm63xx_udc *udc, struct usb_request *req, int status)

    Set completion status and "stage" the callback.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param struct usb_request \*req:
        USB gadget layer representation of the request.

    :param int status:
        Status to return to the gadget driver.

.. _`bcm63xx_ep0_nuke_reply`:

bcm63xx_ep0_nuke_reply
======================

.. c:function:: void bcm63xx_ep0_nuke_reply(struct bcm63xx_udc *udc, int is_tx)

    Abort request from the gadget driver due to reset/shutdown.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param int is_tx:
        Nonzero for TX (IN), zero for RX (OUT).

.. _`bcm63xx_ep0_read_complete`:

bcm63xx_ep0_read_complete
=========================

.. c:function:: int bcm63xx_ep0_read_complete(struct bcm63xx_udc *udc)

    Close out the pending ep0 request; return transfer len.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_ep0_internal_request`:

bcm63xx_ep0_internal_request
============================

.. c:function:: void bcm63xx_ep0_internal_request(struct bcm63xx_udc *udc, int ch_idx, int length)

    Helper function to submit an ep0 request.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param int ch_idx:
        IUDMA channel number.

    :param int length:
        Number of bytes to TX/RX.

.. _`bcm63xx_ep0_internal_request.description`:

Description
-----------

Used for simple transfers performed by the ep0 worker.  This will always
use ep0_ctrl_req / ep0_ctrl_buf.

.. _`bcm63xx_ep0_do_setup`:

bcm63xx_ep0_do_setup
====================

.. c:function:: enum bcm63xx_ep0_state bcm63xx_ep0_do_setup(struct bcm63xx_udc *udc)

    Parse new SETUP packet and decide how to handle it.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_ep0_do_setup.description`:

Description
-----------

EP0_IDLE probably shouldn't ever happen.  EP0_REQUEUE means we're ready
for the next packet.  Anything else means the transaction requires multiple
stages of handling.

.. _`bcm63xx_ep0_do_idle`:

bcm63xx_ep0_do_idle
===================

.. c:function:: int bcm63xx_ep0_do_idle(struct bcm63xx_udc *udc)

    Check for outstanding requests if ep0 is idle.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_ep0_do_idle.description`:

Description
-----------

In state EP0_IDLE, the RX descriptor is either pending, or has been
filled with a SETUP packet from the host.  This function handles new
SETUP packets, control IRQ events (which can generate fake SETUP packets),
and reset/shutdown events.

Returns 0 if work was done; -EAGAIN if nothing to do.

.. _`bcm63xx_ep0_one_round`:

bcm63xx_ep0_one_round
=====================

.. c:function:: int bcm63xx_ep0_one_round(struct bcm63xx_udc *udc)

    Handle the current ep0 state.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_ep0_one_round.description`:

Description
-----------

Returns 0 if work was done; -EAGAIN if nothing to do.

.. _`bcm63xx_ep0_process`:

bcm63xx_ep0_process
===================

.. c:function:: void bcm63xx_ep0_process(struct work_struct *w)

    ep0 worker thread / state machine.

    :param struct work_struct \*w:
        Workqueue struct.

.. _`bcm63xx_ep0_process.description`:

Description
-----------

bcm63xx_ep0_process is triggered any time an event occurs on ep0.  It
is used to synchronize ep0 events and ensure that both HW and SW events
occur in a well-defined order.  When the ep0 IUDMA queues are idle, it may
synthesize SET_CONFIGURATION / SET_INTERFACE requests that were consumed
by the USBD hardware.

The worker function will continue iterating around the state machine
until there is nothing left to do.  Usually "nothing left to do" means
that we're waiting for a new event from the hardware.

.. _`bcm63xx_udc_get_frame`:

bcm63xx_udc_get_frame
=====================

.. c:function:: int bcm63xx_udc_get_frame(struct usb_gadget *gadget)

    Read current SOF frame number from the HW.

    :param struct usb_gadget \*gadget:
        USB slave device.

.. _`bcm63xx_udc_pullup`:

bcm63xx_udc_pullup
==================

.. c:function:: int bcm63xx_udc_pullup(struct usb_gadget *gadget, int is_on)

    Enable/disable pullup on D+ line.

    :param struct usb_gadget \*gadget:
        USB slave device.

    :param int is_on:
        0 to disable pullup, 1 to enable.

.. _`bcm63xx_udc_pullup.description`:

Description
-----------

See notes in \ :c:func:`bcm63xx_select_pullup`\ .

.. _`bcm63xx_udc_start`:

bcm63xx_udc_start
=================

.. c:function:: int bcm63xx_udc_start(struct usb_gadget *gadget, struct usb_gadget_driver *driver)

    Start the controller.

    :param struct usb_gadget \*gadget:
        USB slave device.

    :param struct usb_gadget_driver \*driver:
        Driver for USB slave devices.

.. _`bcm63xx_udc_stop`:

bcm63xx_udc_stop
================

.. c:function:: int bcm63xx_udc_stop(struct usb_gadget *gadget)

    Shut down the controller.

    :param struct usb_gadget \*gadget:
        USB slave device.

.. _`bcm63xx_update_cfg_iface`:

bcm63xx_update_cfg_iface
========================

.. c:function:: void bcm63xx_update_cfg_iface(struct bcm63xx_udc *udc)

    Read current configuration/interface settings.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_update_cfg_iface.description`:

Description
-----------

This controller intercepts SET_CONFIGURATION and SET_INTERFACE messages.
The driver never sees the raw control packets coming in on the ep0
IUDMA channel, but at least we get an interrupt event to tell us that
new values are waiting in the USBD_STATUS register.

.. _`bcm63xx_update_link_speed`:

bcm63xx_update_link_speed
=========================

.. c:function:: int bcm63xx_update_link_speed(struct bcm63xx_udc *udc)

    Check to see if the link speed has changed.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_update_link_speed.description`:

Description
-----------

The link speed update coincides with a SETUP IRQ.  Returns 1 if the
speed has changed, so that the caller can update the endpoint settings.

.. _`bcm63xx_update_wedge`:

bcm63xx_update_wedge
====================

.. c:function:: void bcm63xx_update_wedge(struct bcm63xx_udc *udc, bool new_status)

    Iterate through wedged endpoints.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

    :param bool new_status:
        true to "refresh" wedge status; false to clear it.

.. _`bcm63xx_update_wedge.description`:

Description
-----------

On a SETUP interrupt, we need to manually "refresh" the wedge status
because the controller hardware is designed to automatically clear
stalls in response to a CLEAR_FEATURE request from the host.

On a RESET interrupt, we do want to restore all wedged endpoints.

.. _`bcm63xx_udc_ctrl_isr`:

bcm63xx_udc_ctrl_isr
====================

.. c:function:: irqreturn_t bcm63xx_udc_ctrl_isr(int irq, void *dev_id)

    ISR for control path events (USBD).

    :param int irq:
        IRQ number (unused).

    :param void \*dev_id:
        Reference to the device controller.

.. _`bcm63xx_udc_ctrl_isr.description`:

Description
-----------

This is where we handle link (VBUS) down, USB reset, speed changes,
SET_CONFIGURATION, and SET_INTERFACE events.

.. _`bcm63xx_udc_data_isr`:

bcm63xx_udc_data_isr
====================

.. c:function:: irqreturn_t bcm63xx_udc_data_isr(int irq, void *dev_id)

    ISR for data path events (IUDMA).

    :param int irq:
        IRQ number (unused).

    :param void \*dev_id:
        Reference to the IUDMA channel that generated the interrupt.

.. _`bcm63xx_udc_data_isr.description`:

Description
-----------

For the two ep0 channels, we have special handling that triggers the
ep0 worker thread.  For normal bulk/intr channels, either queue up
the next buffer descriptor for the transaction (incomplete transaction),
or invoke the completion callback (complete transactions).

.. _`bcm63xx_udc_init_debugfs`:

bcm63xx_udc_init_debugfs
========================

.. c:function:: void bcm63xx_udc_init_debugfs(struct bcm63xx_udc *udc)

    Create debugfs entries.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_udc_cleanup_debugfs`:

bcm63xx_udc_cleanup_debugfs
===========================

.. c:function:: void bcm63xx_udc_cleanup_debugfs(struct bcm63xx_udc *udc)

    Remove debugfs entries.

    :param struct bcm63xx_udc \*udc:
        Reference to the device controller.

.. _`bcm63xx_udc_cleanup_debugfs.description`:

Description
-----------

debugfs_remove() is safe to call with a NULL argument.

.. _`bcm63xx_udc_probe`:

bcm63xx_udc_probe
=================

.. c:function:: int bcm63xx_udc_probe(struct platform_device *pdev)

    Initialize a new instance of the UDC.

    :param struct platform_device \*pdev:
        Platform device struct from the bcm63xx BSP code.

.. _`bcm63xx_udc_probe.description`:

Description
-----------

Note that platform data is required, because pd.port_no varies from chip
to chip and is used to switch the correct USB port to device mode.

.. _`bcm63xx_udc_remove`:

bcm63xx_udc_remove
==================

.. c:function:: int bcm63xx_udc_remove(struct platform_device *pdev)

    Remove the device from the system.

    :param struct platform_device \*pdev:
        Platform device struct from the bcm63xx BSP code.

.. This file was automatic generated / don't edit.

