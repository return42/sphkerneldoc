.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/udc/s3c-hsudc.c

.. _`s3c_hsudc_ep`:

struct s3c_hsudc_ep
===================

.. c:type:: struct s3c_hsudc_ep

    Endpoint representation used by driver.

.. _`s3c_hsudc_ep.definition`:

Definition
----------

.. code-block:: c

    struct s3c_hsudc_ep {
        struct usb_ep ep;
        char name[20];
        struct s3c_hsudc *dev;
        struct list_head queue;
        u8 stopped;
        u8 wedge;
        u8 bEndpointAddress;
        void __iomem *fifo;
    }

.. _`s3c_hsudc_ep.members`:

Members
-------

ep
    USB gadget layer representation of device endpoint.

name
    Endpoint name (as required by ep autoconfiguration).

dev
    Reference to the device controller to which this EP belongs.

queue
    Transfer request queue for the endpoint.

stopped
    Maintains state of endpoint, set if EP is halted.

wedge
    *undescribed*

bEndpointAddress
    EP address (including direction bit).

fifo
    Base address of EP FIFO.

.. _`s3c_hsudc_req`:

struct s3c_hsudc_req
====================

.. c:type:: struct s3c_hsudc_req

    Driver encapsulation of USB gadget transfer request.

.. _`s3c_hsudc_req.definition`:

Definition
----------

.. code-block:: c

    struct s3c_hsudc_req {
        struct usb_request req;
        struct list_head queue;
    }

.. _`s3c_hsudc_req.members`:

Members
-------

req
    Reference to USB gadget transfer request.

queue
    Used for inserting this request to the endpoint request queue.

.. _`s3c_hsudc`:

struct s3c_hsudc
================

.. c:type:: struct s3c_hsudc

    Driver's abstraction of the device controller.

.. _`s3c_hsudc.definition`:

Definition
----------

.. code-block:: c

    struct s3c_hsudc {
        struct usb_gadget gadget;
        struct usb_gadget_driver *driver;
        struct device *dev;
        struct s3c24xx_hsudc_platdata *pd;
        struct usb_phy *transceiver;
        struct regulator_bulk_data supplies[ARRAY_SIZE(s3c_hsudc_supply_names)];
        spinlock_t lock;
        void __iomem *regs;
        int irq;
        struct clk *uclk;
        int ep0state;
        struct s3c_hsudc_ep ep[];
    }

.. _`s3c_hsudc.members`:

Members
-------

gadget
    Instance of usb_gadget which is referenced by gadget driver.

driver
    Reference to currenty active gadget driver.

dev
    The device reference used by probe function.

pd
    *undescribed*

transceiver
    *undescribed*

supplies
    *undescribed*

lock
    Lock to synchronize the usage of Endpoints (EP's are indexed).

regs
    Remapped base address of controller's register space.

irq
    *undescribed*

uclk
    *undescribed*

ep0state
    *undescribed*

ep
    *undescribed*

.. _`s3c_hsudc.irq`:

irq
---

IRQ number used by the controller.

.. _`s3c_hsudc.uclk`:

uclk
----

Reference to the controller clock.

.. _`s3c_hsudc.ep0state`:

ep0state
--------

Current state of EP0.
ep: List of endpoints supported by the controller.

.. _`s3c_hsudc_complete_request`:

s3c_hsudc_complete_request
==========================

.. c:function:: void s3c_hsudc_complete_request(struct s3c_hsudc_ep *hsep, struct s3c_hsudc_req *hsreq, int status)

    Complete a transfer request.

    :param struct s3c_hsudc_ep \*hsep:
        Endpoint to which the request belongs.

    :param struct s3c_hsudc_req \*hsreq:
        Transfer request to be completed.

    :param int status:
        Transfer completion status for the transfer request.

.. _`s3c_hsudc_nuke_ep`:

s3c_hsudc_nuke_ep
=================

.. c:function:: void s3c_hsudc_nuke_ep(struct s3c_hsudc_ep *hsep, int status)

    Terminate all requests queued for a endpoint.

    :param struct s3c_hsudc_ep \*hsep:
        Endpoint for which queued requests have to be terminated.

    :param int status:
        Transfer completion status for the transfer request.

.. _`s3c_hsudc_stop_activity`:

s3c_hsudc_stop_activity
=======================

.. c:function:: void s3c_hsudc_stop_activity(struct s3c_hsudc *hsudc)

    Stop activity on all endpoints.

    :param struct s3c_hsudc \*hsudc:
        Device controller for which EP activity is to be stopped.

.. _`s3c_hsudc_stop_activity.description`:

Description
-----------

All the endpoints are stopped and any pending transfer requests if any on
the endpoint are terminated.

.. _`s3c_hsudc_read_setup_pkt`:

s3c_hsudc_read_setup_pkt
========================

.. c:function:: void s3c_hsudc_read_setup_pkt(struct s3c_hsudc *hsudc, u16 *buf)

    Read the received setup packet from EP0 fifo.

    :param struct s3c_hsudc \*hsudc:
        Device controller from which setup packet is to be read.

    :param u16 \*buf:
        The buffer into which the setup packet is read.

.. _`s3c_hsudc_read_setup_pkt.description`:

Description
-----------

The setup packet received in the EP0 fifo is read and stored into a
given buffer address.

.. _`s3c_hsudc_write_fifo`:

s3c_hsudc_write_fifo
====================

.. c:function:: int s3c_hsudc_write_fifo(struct s3c_hsudc_ep *hsep, struct s3c_hsudc_req *hsreq)

    Write next chunk of transfer data to EP fifo.

    :param struct s3c_hsudc_ep \*hsep:
        Endpoint to which the data is to be written.

    :param struct s3c_hsudc_req \*hsreq:
        Transfer request from which the next chunk of data is written.

.. _`s3c_hsudc_write_fifo.description`:

Description
-----------

Write the next chunk of data from a transfer request to the endpoint FIFO.
If the transfer request completes, 1 is returned, otherwise 0 is returned.

.. _`s3c_hsudc_read_fifo`:

s3c_hsudc_read_fifo
===================

.. c:function:: int s3c_hsudc_read_fifo(struct s3c_hsudc_ep *hsep, struct s3c_hsudc_req *hsreq)

    Read the next chunk of data from EP fifo.

    :param struct s3c_hsudc_ep \*hsep:
        Endpoint from which the data is to be read.

    :param struct s3c_hsudc_req \*hsreq:
        Transfer request to which the next chunk of data read is written.

.. _`s3c_hsudc_read_fifo.description`:

Description
-----------

Read the next chunk of data from the endpoint FIFO and a write it to the
transfer request buffer. If the transfer request completes, 1 is returned,
otherwise 0 is returned.

.. _`s3c_hsudc_epin_intr`:

s3c_hsudc_epin_intr
===================

.. c:function:: void s3c_hsudc_epin_intr(struct s3c_hsudc *hsudc, u32 ep_idx)

    Handle in-endpoint interrupt. \ ``hsudc``\  - Device controller for which the interrupt is to be handled. \ ``ep_idx``\  - Endpoint number on which an interrupt is pending.

    :param struct s3c_hsudc \*hsudc:
        *undescribed*

    :param u32 ep_idx:
        *undescribed*

.. _`s3c_hsudc_epin_intr.description`:

Description
-----------

Handles interrupt for a in-endpoint. The interrupts that are handled are
stall and data transmit complete interrupt.

.. _`s3c_hsudc_epout_intr`:

s3c_hsudc_epout_intr
====================

.. c:function:: void s3c_hsudc_epout_intr(struct s3c_hsudc *hsudc, u32 ep_idx)

    Handle out-endpoint interrupt. \ ``hsudc``\  - Device controller for which the interrupt is to be handled. \ ``ep_idx``\  - Endpoint number on which an interrupt is pending.

    :param struct s3c_hsudc \*hsudc:
        *undescribed*

    :param u32 ep_idx:
        *undescribed*

.. _`s3c_hsudc_epout_intr.description`:

Description
-----------

Handles interrupt for a out-endpoint. The interrupts that are handled are
stall, flush and data ready interrupt.

.. _`s3c_hsudc_process_req_status`:

s3c_hsudc_process_req_status
============================

.. c:function:: void s3c_hsudc_process_req_status(struct s3c_hsudc *hsudc, struct usb_ctrlrequest *ctrl)

    Handle get status control request.

    :param struct s3c_hsudc \*hsudc:
        Device controller on which get status request has be handled.

    :param struct usb_ctrlrequest \*ctrl:
        Control request as received on the endpoint 0.

.. _`s3c_hsudc_process_req_status.description`:

Description
-----------

Handle get status control request received on control endpoint.

.. _`s3c_hsudc_process_setup`:

s3c_hsudc_process_setup
=======================

.. c:function:: void s3c_hsudc_process_setup(struct s3c_hsudc *hsudc)

    Process control request received on endpoint 0.

    :param struct s3c_hsudc \*hsudc:
        Device controller on which control request has been received.

.. _`s3c_hsudc_process_setup.description`:

Description
-----------

Read the control request received on endpoint 0, decode it and handle
the request.

.. _`s3c_hsudc_ep_enable`:

s3c_hsudc_ep_enable
===================

.. c:function:: int s3c_hsudc_ep_enable(struct usb_ep *_ep, const struct usb_endpoint_descriptor *desc)

    Enable a endpoint.

    :param struct usb_ep \*_ep:
        The endpoint to be enabled.

    :param const struct usb_endpoint_descriptor \*desc:
        Endpoint descriptor.

.. _`s3c_hsudc_ep_enable.description`:

Description
-----------

Enables a endpoint when called from the gadget driver. Endpoint stall if
any is cleared, transfer type is configured and endpoint interrupt is
enabled.

.. _`s3c_hsudc_ep_disable`:

s3c_hsudc_ep_disable
====================

.. c:function:: int s3c_hsudc_ep_disable(struct usb_ep *_ep)

    Disable a endpoint.

    :param struct usb_ep \*_ep:
        The endpoint to be disabled.

.. _`s3c_hsudc_ep_disable.description`:

Description
-----------

Disables a endpoint when called from the gadget driver.

.. _`s3c_hsudc_alloc_request`:

s3c_hsudc_alloc_request
=======================

.. c:function:: struct usb_request *s3c_hsudc_alloc_request(struct usb_ep *_ep, gfp_t gfp_flags)

    Allocate a new request.

    :param struct usb_ep \*_ep:
        Endpoint for which request is allocated (not used).

    :param gfp_t gfp_flags:
        Flags used for the allocation.

.. _`s3c_hsudc_alloc_request.description`:

Description
-----------

Allocates a single transfer request structure when called from gadget driver.

.. _`s3c_hsudc_free_request`:

s3c_hsudc_free_request
======================

.. c:function:: void s3c_hsudc_free_request(struct usb_ep *ep, struct usb_request *_req)

    Deallocate a request.

    :param struct usb_ep \*ep:
        Endpoint for which request is deallocated (not used).

    :param struct usb_request \*_req:
        Request to be deallocated.

.. _`s3c_hsudc_free_request.description`:

Description
-----------

Allocates a single transfer request structure when called from gadget driver.

.. _`s3c_hsudc_queue`:

s3c_hsudc_queue
===============

.. c:function:: int s3c_hsudc_queue(struct usb_ep *_ep, struct usb_request *_req, gfp_t gfp_flags)

    Queue a transfer request for the endpoint.

    :param struct usb_ep \*_ep:
        Endpoint for which the request is queued.

    :param struct usb_request \*_req:
        Request to be queued.

    :param gfp_t gfp_flags:
        Not used.

.. _`s3c_hsudc_queue.description`:

Description
-----------

Start or enqueue a request for a endpoint when called from gadget driver.

.. _`s3c_hsudc_dequeue`:

s3c_hsudc_dequeue
=================

.. c:function:: int s3c_hsudc_dequeue(struct usb_ep *_ep, struct usb_request *_req)

    Dequeue a transfer request from an endpoint.

    :param struct usb_ep \*_ep:
        Endpoint from which the request is dequeued.

    :param struct usb_request \*_req:
        Request to be dequeued.

.. _`s3c_hsudc_dequeue.description`:

Description
-----------

Dequeue a request from a endpoint when called from gadget driver.

.. _`s3c_hsudc_initep`:

s3c_hsudc_initep
================

.. c:function:: void s3c_hsudc_initep(struct s3c_hsudc *hsudc, struct s3c_hsudc_ep *hsep, int epnum)

    Initialize a endpoint to default state. \ ``hsudc``\  - Reference to the device controller. \ ``hsep``\  - Endpoint to be initialized. \ ``epnum``\  - Address to be assigned to the endpoint.

    :param struct s3c_hsudc \*hsudc:
        *undescribed*

    :param struct s3c_hsudc_ep \*hsep:
        *undescribed*

    :param int epnum:
        *undescribed*

.. _`s3c_hsudc_initep.description`:

Description
-----------

Initialize a endpoint with default configuration.

.. _`s3c_hsudc_setup_ep`:

s3c_hsudc_setup_ep
==================

.. c:function:: void s3c_hsudc_setup_ep(struct s3c_hsudc *hsudc)

    Configure all endpoints to default state.

    :param struct s3c_hsudc \*hsudc:
        Reference to device controller.

.. _`s3c_hsudc_setup_ep.description`:

Description
-----------

Configures all endpoints to default state.

.. _`s3c_hsudc_reconfig`:

s3c_hsudc_reconfig
==================

.. c:function:: void s3c_hsudc_reconfig(struct s3c_hsudc *hsudc)

    Reconfigure the device controller to default state.

    :param struct s3c_hsudc \*hsudc:
        Reference to device controller.

.. _`s3c_hsudc_reconfig.description`:

Description
-----------

Reconfigures the device controller registers to a default state.

.. _`s3c_hsudc_irq`:

s3c_hsudc_irq
=============

.. c:function:: irqreturn_t s3c_hsudc_irq(int irq, void *_dev)

    Interrupt handler for device controller.

    :param int irq:
        Not used.

    :param void \*_dev:
        Reference to the device controller.

.. _`s3c_hsudc_irq.description`:

Description
-----------

Interrupt handler for the device controller. This handler handles controller
interrupts and endpoint interrupts.

.. This file was automatic generated / don't edit.

