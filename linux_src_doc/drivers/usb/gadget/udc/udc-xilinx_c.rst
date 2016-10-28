.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/udc/udc-xilinx.c

.. _`xusb_req`:

struct xusb_req
===============

.. c:type:: struct xusb_req

    Xilinx USB device request structure

.. _`xusb_req.definition`:

Definition
----------

.. code-block:: c

    struct xusb_req {
        struct usb_request usb_req;
        struct list_head queue;
        struct xusb_ep *ep;
    }

.. _`xusb_req.members`:

Members
-------

usb_req
    Linux usb request structure

queue
    usb device request queue

ep
    pointer to xusb_endpoint structure

.. _`xusb_ep`:

struct xusb_ep
==============

.. c:type:: struct xusb_ep

    USB end point structure.

.. _`xusb_ep.definition`:

Definition
----------

.. code-block:: c

    struct xusb_ep {
        struct usb_ep ep_usb;
        struct list_head queue;
        struct xusb_udc *udc;
        const struct usb_endpoint_descriptor *desc;
        u32 rambase;
        u32 offset;
        char name[4];
        u16 epnumber;
        u16 maxpacket;
        u16 buffer0count;
        u16 buffer1count;
        u8 curbufnum;
        bool buffer0ready;
        bool buffer1ready;
        bool is_in;
        bool is_iso;
    }

.. _`xusb_ep.members`:

Members
-------

ep_usb
    usb endpoint instance

queue
    endpoint message queue

udc
    xilinx usb peripheral driver instance pointer

desc
    pointer to the usb endpoint descriptor

rambase
    the endpoint buffer address

offset
    the endpoint register offset value

name
    name of the endpoint

epnumber
    endpoint number

maxpacket
    maximum packet size the endpoint can store

buffer0count
    the size of the packet recieved in the first buffer

buffer1count
    the size of the packet received in the second buffer

curbufnum
    current buffer of endpoint that will be processed next

buffer0ready
    the busy state of first buffer

buffer1ready
    the busy state of second buffer

is_in
    endpoint direction (IN or OUT)

is_iso
    endpoint type(isochronous or non isochronous)

.. _`xusb_udc`:

struct xusb_udc
===============

.. c:type:: struct xusb_udc

    USB peripheral driver structure

.. _`xusb_udc.definition`:

Definition
----------

.. code-block:: c

    struct xusb_udc {
        struct usb_gadget gadget;
        struct xusb_ep ep[8];
        struct usb_gadget_driver *driver;
        struct usb_ctrlrequest setup;
        struct xusb_req *req;
        struct device *dev;
        u32 usb_state;
        u32 remote_wkp;
        u32 setupseqtx;
        u32 setupseqrx;
        void __iomem *addr;
        spinlock_t lock;
        bool dma_enabled;
        unsigned int (*read_fn)(void __iomem *);
        void (*write_fn)(void __iomem *, u32, u32);
    }

.. _`xusb_udc.members`:

Members
-------

gadget
    USB gadget driver instance

ep
    an array of endpoint structures

driver
    pointer to the usb gadget driver instance

setup
    usb_ctrlrequest structure for control requests

req
    pointer to dummy request for get status command

dev
    pointer to device structure in gadget

usb_state
    device in suspended state or not

remote_wkp
    remote wakeup enabled by host

setupseqtx
    tx status

setupseqrx
    rx status

addr
    the usb device base address

lock
    instance of spinlock

dma_enabled
    flag indicating whether the dma is included in the system

read_fn
    function pointer to read device registers

write_fn
    function pointer to write to device registers

.. _`xudc_write32`:

xudc_write32
============

.. c:function:: void xudc_write32(void __iomem *addr, u32 offset, u32 val)

    little endian write to device registers

    :param void __iomem \*addr:
        base addr of device registers

    :param u32 offset:
        register offset

    :param u32 val:
        data to be written

.. _`xudc_read32`:

xudc_read32
===========

.. c:function:: unsigned int xudc_read32(void __iomem *addr)

    little endian read from device registers

    :param void __iomem \*addr:
        addr of device register

.. _`xudc_read32.return`:

Return
------

value at addr

.. _`xudc_write32_be`:

xudc_write32_be
===============

.. c:function:: void xudc_write32_be(void __iomem *addr, u32 offset, u32 val)

    big endian write to device registers

    :param void __iomem \*addr:
        base addr of device registers

    :param u32 offset:
        register offset

    :param u32 val:
        data to be written

.. _`xudc_read32_be`:

xudc_read32_be
==============

.. c:function:: unsigned int xudc_read32_be(void __iomem *addr)

    big endian read from device registers

    :param void __iomem \*addr:
        addr of device register

.. _`xudc_read32_be.return`:

Return
------

value at addr

.. _`xudc_wrstatus`:

xudc_wrstatus
=============

.. c:function:: void xudc_wrstatus(struct xusb_udc *udc)

    Sets up the usb device status stages.

    :param struct xusb_udc \*udc:
        pointer to the usb device controller structure.

.. _`xudc_epconfig`:

xudc_epconfig
=============

.. c:function:: void xudc_epconfig(struct xusb_ep *ep, struct xusb_udc *udc)

    Configures the given endpoint.

    :param struct xusb_ep \*ep:
        pointer to the usb device endpoint structure.

    :param struct xusb_udc \*udc:
        pointer to the usb peripheral controller structure.

.. _`xudc_epconfig.description`:

Description
-----------

This function configures a specific endpoint with the given configuration
data.

.. _`xudc_start_dma`:

xudc_start_dma
==============

.. c:function:: int xudc_start_dma(struct xusb_ep *ep, dma_addr_t src, dma_addr_t dst, u32 length)

    Starts DMA transfer.

    :param struct xusb_ep \*ep:
        pointer to the usb device endpoint structure.

    :param dma_addr_t src:
        DMA source address.

    :param dma_addr_t dst:
        DMA destination address.

    :param u32 length:
        number of bytes to transfer.

.. _`xudc_start_dma.return`:

Return
------

0 on success, error code on failure

This function starts DMA transfer by writing to DMA source,
destination and lenth registers.

.. _`xudc_dma_send`:

xudc_dma_send
=============

.. c:function:: int xudc_dma_send(struct xusb_ep *ep, struct xusb_req *req, u8 *buffer, u32 length)

    Sends IN data using DMA.

    :param struct xusb_ep \*ep:
        pointer to the usb device endpoint structure.

    :param struct xusb_req \*req:
        pointer to the usb request structure.

    :param u8 \*buffer:
        pointer to data to be sent.

    :param u32 length:
        number of bytes to send.

.. _`xudc_dma_send.return`:

Return
------

0 on success, -EAGAIN if no buffer is free and error
code on failure.

This function sends data using DMA.

.. _`xudc_dma_receive`:

xudc_dma_receive
================

.. c:function:: int xudc_dma_receive(struct xusb_ep *ep, struct xusb_req *req, u8 *buffer, u32 length)

    Receives OUT data using DMA.

    :param struct xusb_ep \*ep:
        pointer to the usb device endpoint structure.

    :param struct xusb_req \*req:
        pointer to the usb request structure.

    :param u8 \*buffer:
        pointer to storage buffer of received data.

    :param u32 length:
        number of bytes to receive.

.. _`xudc_dma_receive.return`:

Return
------

0 on success, -EAGAIN if no buffer is free and error
code on failure.

This function receives data using DMA.

.. _`xudc_eptxrx`:

xudc_eptxrx
===========

.. c:function:: int xudc_eptxrx(struct xusb_ep *ep, struct xusb_req *req, u8 *bufferptr, u32 bufferlen)

    Transmits or receives data to or from an endpoint.

    :param struct xusb_ep \*ep:
        pointer to the usb endpoint configuration structure.

    :param struct xusb_req \*req:
        pointer to the usb request structure.

    :param u8 \*bufferptr:
        pointer to buffer containing the data to be sent.

    :param u32 bufferlen:
        The number of data bytes to be sent.

.. _`xudc_eptxrx.return`:

Return
------

0 on success, -EAGAIN if no buffer is free.

This function copies the transmit/receive data to/from the end point buffer
and enables the buffer for transmission/reception.

.. _`xudc_done`:

xudc_done
=========

.. c:function:: void xudc_done(struct xusb_ep *ep, struct xusb_req *req, int status)

    Exeutes the endpoint data transfer completion tasks.

    :param struct xusb_ep \*ep:
        pointer to the usb device endpoint structure.

    :param struct xusb_req \*req:
        pointer to the usb request structure.

    :param int status:
        Status of the data transfer.

.. _`xudc_done.description`:

Description
-----------

Deletes the message from the queue and updates data transfer completion
status.

.. _`xudc_read_fifo`:

xudc_read_fifo
==============

.. c:function:: int xudc_read_fifo(struct xusb_ep *ep, struct xusb_req *req)

    Reads the data from the given endpoint buffer.

    :param struct xusb_ep \*ep:
        pointer to the usb device endpoint structure.

    :param struct xusb_req \*req:
        pointer to the usb request structure.

.. _`xudc_read_fifo.return`:

Return
------

0 if request is completed and -EAGAIN if not completed.

Pulls OUT packet data from the endpoint buffer.

.. _`xudc_write_fifo`:

xudc_write_fifo
===============

.. c:function:: int xudc_write_fifo(struct xusb_ep *ep, struct xusb_req *req)

    Writes data into the given endpoint buffer.

    :param struct xusb_ep \*ep:
        pointer to the usb device endpoint structure.

    :param struct xusb_req \*req:
        pointer to the usb request structure.

.. _`xudc_write_fifo.return`:

Return
------

0 if request is completed and -EAGAIN if not completed.

Loads endpoint buffer for an IN packet.

.. _`xudc_nuke`:

xudc_nuke
=========

.. c:function:: void xudc_nuke(struct xusb_ep *ep, int status)

    Cleans up the data transfer message list.

    :param struct xusb_ep \*ep:
        pointer to the usb device endpoint structure.

    :param int status:
        Status of the data transfer.

.. _`xudc_ep_set_halt`:

xudc_ep_set_halt
================

.. c:function:: int xudc_ep_set_halt(struct usb_ep *_ep, int value)

    Stalls/unstalls the given endpoint.

    :param struct usb_ep \*_ep:
        pointer to the usb device endpoint structure.

    :param int value:
        value to indicate stall/unstall.

.. _`xudc_ep_set_halt.return`:

Return
------

0 for success and error value on failure

.. _`__xudc_ep_enable`:

__xudc_ep_enable
================

.. c:function:: int __xudc_ep_enable(struct xusb_ep *ep, const struct usb_endpoint_descriptor *desc)

    Enables the given endpoint.

    :param struct xusb_ep \*ep:
        pointer to the xusb endpoint structure.

    :param const struct usb_endpoint_descriptor \*desc:
        pointer to usb endpoint descriptor.

.. _`__xudc_ep_enable.return`:

Return
------

0 for success and error value on failure

.. _`xudc_ep_enable`:

xudc_ep_enable
==============

.. c:function:: int xudc_ep_enable(struct usb_ep *_ep, const struct usb_endpoint_descriptor *desc)

    Enables the given endpoint.

    :param struct usb_ep \*_ep:
        pointer to the usb endpoint structure.

    :param const struct usb_endpoint_descriptor \*desc:
        pointer to usb endpoint descriptor.

.. _`xudc_ep_enable.return`:

Return
------

0 for success and error value on failure

.. _`xudc_ep_disable`:

xudc_ep_disable
===============

.. c:function:: int xudc_ep_disable(struct usb_ep *_ep)

    Disables the given endpoint.

    :param struct usb_ep \*_ep:
        pointer to the usb endpoint structure.

.. _`xudc_ep_disable.return`:

Return
------

0 for success and error value on failure

.. _`xudc_ep_alloc_request`:

xudc_ep_alloc_request
=====================

.. c:function:: struct usb_request *xudc_ep_alloc_request(struct usb_ep *_ep, gfp_t gfp_flags)

    Initializes the request queue.

    :param struct usb_ep \*_ep:
        pointer to the usb endpoint structure.

    :param gfp_t gfp_flags:
        Flags related to the request call.

.. _`xudc_ep_alloc_request.return`:

Return
------

pointer to request structure on success and a NULL on failure.

.. _`xudc_free_request`:

xudc_free_request
=================

.. c:function:: void xudc_free_request(struct usb_ep *_ep, struct usb_request *_req)

    Releases the request from queue.

    :param struct usb_ep \*_ep:
        pointer to the usb device endpoint structure.

    :param struct usb_request \*_req:
        pointer to the usb request structure.

.. _`__xudc_ep0_queue`:

__xudc_ep0_queue
================

.. c:function:: int __xudc_ep0_queue(struct xusb_ep *ep0, struct xusb_req *req)

    Adds the request to endpoint 0 queue.

    :param struct xusb_ep \*ep0:
        pointer to the xusb endpoint 0 structure.

    :param struct xusb_req \*req:
        pointer to the xusb request structure.

.. _`__xudc_ep0_queue.return`:

Return
------

0 for success and error value on failure

.. _`xudc_ep0_queue`:

xudc_ep0_queue
==============

.. c:function:: int xudc_ep0_queue(struct usb_ep *_ep, struct usb_request *_req, gfp_t gfp_flags)

    Adds the request to endpoint 0 queue.

    :param struct usb_ep \*_ep:
        pointer to the usb endpoint 0 structure.

    :param struct usb_request \*_req:
        pointer to the usb request structure.

    :param gfp_t gfp_flags:
        Flags related to the request call.

.. _`xudc_ep0_queue.return`:

Return
------

0 for success and error value on failure

.. _`xudc_ep_queue`:

xudc_ep_queue
=============

.. c:function:: int xudc_ep_queue(struct usb_ep *_ep, struct usb_request *_req, gfp_t gfp_flags)

    Adds the request to endpoint queue.

    :param struct usb_ep \*_ep:
        pointer to the usb endpoint structure.

    :param struct usb_request \*_req:
        pointer to the usb request structure.

    :param gfp_t gfp_flags:
        Flags related to the request call.

.. _`xudc_ep_queue.return`:

Return
------

0 for success and error value on failure

.. _`xudc_ep_dequeue`:

xudc_ep_dequeue
===============

.. c:function:: int xudc_ep_dequeue(struct usb_ep *_ep, struct usb_request *_req)

    Removes the request from the queue.

    :param struct usb_ep \*_ep:
        pointer to the usb device endpoint structure.

    :param struct usb_request \*_req:
        pointer to the usb request structure.

.. _`xudc_ep_dequeue.return`:

Return
------

0 for success and error value on failure

.. _`xudc_ep0_enable`:

xudc_ep0_enable
===============

.. c:function:: int xudc_ep0_enable(struct usb_ep *ep, const struct usb_endpoint_descriptor *desc)

    Enables the given endpoint.

    :param struct usb_ep \*ep:
        pointer to the usb endpoint structure.

    :param const struct usb_endpoint_descriptor \*desc:
        pointer to usb endpoint descriptor.

.. _`xudc_ep0_enable.return`:

Return
------

error always.

endpoint 0 enable should not be called by gadget layer.

.. _`xudc_ep0_disable`:

xudc_ep0_disable
================

.. c:function:: int xudc_ep0_disable(struct usb_ep *ep)

    Disables the given endpoint.

    :param struct usb_ep \*ep:
        pointer to the usb endpoint structure.

.. _`xudc_ep0_disable.return`:

Return
------

error always.

endpoint 0 disable should not be called by gadget layer.

.. _`xudc_get_frame`:

xudc_get_frame
==============

.. c:function:: int xudc_get_frame(struct usb_gadget *gadget)

    Reads the current usb frame number.

    :param struct usb_gadget \*gadget:
        pointer to the usb gadget structure.

.. _`xudc_get_frame.return`:

Return
------

current frame number for success and error value on failure.

.. _`xudc_wakeup`:

xudc_wakeup
===========

.. c:function:: int xudc_wakeup(struct usb_gadget *gadget)

    Send remote wakeup signal to host

    :param struct usb_gadget \*gadget:
        pointer to the usb gadget structure.

.. _`xudc_wakeup.return`:

Return
------

0 on success and error on failure

.. _`xudc_pullup`:

xudc_pullup
===========

.. c:function:: int xudc_pullup(struct usb_gadget *gadget, int is_on)

    start/stop USB traffic

    :param struct usb_gadget \*gadget:
        pointer to the usb gadget structure.

    :param int is_on:
        flag to start or stop

.. _`xudc_pullup.return`:

Return
------

0 always

This function starts/stops SIE engine of IP based on is_on.

.. _`xudc_eps_init`:

xudc_eps_init
=============

.. c:function:: void xudc_eps_init(struct xusb_udc *udc)

    initialize endpoints.

    :param struct xusb_udc \*udc:
        pointer to the usb device controller structure.

.. _`xudc_stop_activity`:

xudc_stop_activity
==================

.. c:function:: void xudc_stop_activity(struct xusb_udc *udc)

    Stops any further activity on the device.

    :param struct xusb_udc \*udc:
        pointer to the usb device controller structure.

.. _`xudc_start`:

xudc_start
==========

.. c:function:: int xudc_start(struct usb_gadget *gadget, struct usb_gadget_driver *driver)

    Starts the device.

    :param struct usb_gadget \*gadget:
        pointer to the usb gadget structure

    :param struct usb_gadget_driver \*driver:
        pointer to gadget driver structure

.. _`xudc_start.return`:

Return
------

zero on success and error on failure

.. _`xudc_stop`:

xudc_stop
=========

.. c:function:: int xudc_stop(struct usb_gadget *gadget)

    stops the device.

    :param struct usb_gadget \*gadget:
        pointer to the usb gadget structure

.. _`xudc_stop.return`:

Return
------

zero always

.. _`xudc_clear_stall_all_ep`:

xudc_clear_stall_all_ep
=======================

.. c:function:: void xudc_clear_stall_all_ep(struct xusb_udc *udc)

    clears stall of every endpoint.

    :param struct xusb_udc \*udc:
        pointer to the udc structure.

.. _`xudc_startup_handler`:

xudc_startup_handler
====================

.. c:function:: void xudc_startup_handler(struct xusb_udc *udc, u32 intrstatus)

    The usb device controller interrupt handler.

    :param struct xusb_udc \*udc:
        pointer to the udc structure.

    :param u32 intrstatus:
        The mask value containing the interrupt sources.

.. _`xudc_startup_handler.description`:

Description
-----------

This function handles the RESET,SUSPEND,RESUME and DISCONNECT interrupts.

.. _`xudc_ep0_stall`:

xudc_ep0_stall
==============

.. c:function:: void xudc_ep0_stall(struct xusb_udc *udc)

    Stall endpoint zero.

    :param struct xusb_udc \*udc:
        pointer to the udc structure.

.. _`xudc_ep0_stall.description`:

Description
-----------

This function stalls endpoint zero.

.. _`xudc_setaddress`:

xudc_setaddress
===============

.. c:function:: void xudc_setaddress(struct xusb_udc *udc)

    executes SET_ADDRESS command

    :param struct xusb_udc \*udc:
        pointer to the udc structure.

.. _`xudc_setaddress.description`:

Description
-----------

This function executes USB SET_ADDRESS command

.. _`xudc_getstatus`:

xudc_getstatus
==============

.. c:function:: void xudc_getstatus(struct xusb_udc *udc)

    executes GET_STATUS command

    :param struct xusb_udc \*udc:
        pointer to the udc structure.

.. _`xudc_getstatus.description`:

Description
-----------

This function executes USB GET_STATUS command

.. _`xudc_set_clear_feature`:

xudc_set_clear_feature
======================

.. c:function:: void xudc_set_clear_feature(struct xusb_udc *udc)

    Executes the set feature and clear feature commands.

    :param struct xusb_udc \*udc:
        pointer to the usb device controller structure.

.. _`xudc_set_clear_feature.description`:

Description
-----------

Processes the SET_FEATURE and CLEAR_FEATURE commands.

.. _`xudc_handle_setup`:

xudc_handle_setup
=================

.. c:function:: void xudc_handle_setup(struct xusb_udc *udc)

    Processes the setup packet.

    :param struct xusb_udc \*udc:
        pointer to the usb device controller structure.

.. _`xudc_handle_setup.description`:

Description
-----------

Process setup packet and delegate to gadget layer.

.. _`xudc_ep0_out`:

xudc_ep0_out
============

.. c:function:: void xudc_ep0_out(struct xusb_udc *udc)

    Processes the endpoint 0 OUT token.

    :param struct xusb_udc \*udc:
        pointer to the usb device controller structure.

.. _`xudc_ep0_in`:

xudc_ep0_in
===========

.. c:function:: void xudc_ep0_in(struct xusb_udc *udc)

    Processes the endpoint 0 IN token.

    :param struct xusb_udc \*udc:
        pointer to the usb device controller structure.

.. _`xudc_ctrl_ep_handler`:

xudc_ctrl_ep_handler
====================

.. c:function:: void xudc_ctrl_ep_handler(struct xusb_udc *udc, u32 intrstatus)

    Endpoint 0 interrupt handler.

    :param struct xusb_udc \*udc:
        pointer to the udc structure.

    :param u32 intrstatus:
        It's the mask value for the interrupt sources on endpoint 0.

.. _`xudc_ctrl_ep_handler.description`:

Description
-----------

Processes the commands received during enumeration phase.

.. _`xudc_nonctrl_ep_handler`:

xudc_nonctrl_ep_handler
=======================

.. c:function:: void xudc_nonctrl_ep_handler(struct xusb_udc *udc, u8 epnum, u32 intrstatus)

    Non control endpoint interrupt handler.

    :param struct xusb_udc \*udc:
        pointer to the udc structure.

    :param u8 epnum:
        End point number for which the interrupt is to be processed

    :param u32 intrstatus:
        mask value for interrupt sources of endpoints other
        than endpoint 0.

.. _`xudc_nonctrl_ep_handler.description`:

Description
-----------

Processes the buffer completion interrupts.

.. _`xudc_irq`:

xudc_irq
========

.. c:function:: irqreturn_t xudc_irq(int irq, void *_udc)

    The main interrupt handler.

    :param int irq:
        The interrupt number.

    :param void \*_udc:
        pointer to the usb device controller structure.

.. _`xudc_irq.return`:

Return
------

IRQ_HANDLED after the interrupt is handled.

.. _`xudc_probe`:

xudc_probe
==========

.. c:function:: int xudc_probe(struct platform_device *pdev)

    The device probe function for driver initialization.

    :param struct platform_device \*pdev:
        pointer to the platform device structure.

.. _`xudc_probe.return`:

Return
------

0 for success and error value on failure

.. _`xudc_remove`:

xudc_remove
===========

.. c:function:: int xudc_remove(struct platform_device *pdev)

    Releases the resources allocated during the initialization.

    :param struct platform_device \*pdev:
        pointer to the platform device structure.

.. _`xudc_remove.return`:

Return
------

0 always

.. This file was automatic generated / don't edit.

