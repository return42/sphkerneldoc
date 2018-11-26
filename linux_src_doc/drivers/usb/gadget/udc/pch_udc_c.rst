.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/udc/pch_udc.c

.. _`pch_udc_data_dma_desc`:

struct pch_udc_data_dma_desc
============================

.. c:type:: struct pch_udc_data_dma_desc

    Structure to hold DMA descriptor information for data

.. _`pch_udc_data_dma_desc.definition`:

Definition
----------

.. code-block:: c

    struct pch_udc_data_dma_desc {
        u32 status;
        u32 reserved;
        u32 dataptr;
        u32 next;
    }

.. _`pch_udc_data_dma_desc.members`:

Members
-------

status
    Status quadlet

reserved
    Reserved

dataptr
    Buffer descriptor

next
    Next descriptor

.. _`pch_udc_stp_dma_desc`:

struct pch_udc_stp_dma_desc
===========================

.. c:type:: struct pch_udc_stp_dma_desc

    Structure to hold DMA descriptor information for control data

.. _`pch_udc_stp_dma_desc.definition`:

Definition
----------

.. code-block:: c

    struct pch_udc_stp_dma_desc {
        u32 status;
        u32 reserved;
        struct usb_ctrlrequest request;
    }

.. _`pch_udc_stp_dma_desc.members`:

Members
-------

status
    Status

reserved
    Reserved

request
    *undescribed*

.. _`pch_udc_cfg_data`:

struct pch_udc_cfg_data
=======================

.. c:type:: struct pch_udc_cfg_data

    Structure to hold current configuration and interface information

.. _`pch_udc_cfg_data.definition`:

Definition
----------

.. code-block:: c

    struct pch_udc_cfg_data {
        u16 cur_cfg;
        u16 cur_intf;
        u16 cur_alt;
    }

.. _`pch_udc_cfg_data.members`:

Members
-------

cur_cfg
    current configuration in use

cur_intf
    current interface in use

cur_alt
    current alt interface in use

.. _`pch_udc_ep`:

struct pch_udc_ep
=================

.. c:type:: struct pch_udc_ep

    Structure holding a PCH USB device Endpoint information

.. _`pch_udc_ep.definition`:

Definition
----------

.. code-block:: c

    struct pch_udc_ep {
        struct usb_ep ep;
        dma_addr_t td_stp_phys;
        dma_addr_t td_data_phys;
        struct pch_udc_stp_dma_desc *td_stp;
        struct pch_udc_data_dma_desc *td_data;
        struct pch_udc_dev *dev;
        unsigned long offset_addr;
        struct list_head queue;
        unsigned num:5,in:1, halted:1;
        unsigned long epsts;
    }

.. _`pch_udc_ep.members`:

Members
-------

ep
    embedded ep request

td_stp_phys
    for setup request

td_data_phys
    for data request

td_stp
    for setup request

td_data
    for data request

dev
    reference to device struct

offset_addr
    offset address of ep register

queue
    queue for requests

num
    endpoint number

in
    endpoint is IN

halted
    endpoint halted?

epsts
    Endpoint status

.. _`pch_vbus_gpio_data`:

struct pch_vbus_gpio_data
=========================

.. c:type:: struct pch_vbus_gpio_data

    Structure holding GPIO informaton for detecting VBUS

.. _`pch_vbus_gpio_data.definition`:

Definition
----------

.. code-block:: c

    struct pch_vbus_gpio_data {
        int port;
        int intr;
        struct work_struct irq_work_fall;
        struct work_struct irq_work_rise;
    }

.. _`pch_vbus_gpio_data.members`:

Members
-------

port
    gpio port number

intr
    gpio interrupt number
    \ ``irq_work_fall``\        Structure for WorkQueue
    \ ``irq_work_rise``\        Structure for WorkQueue

irq_work_fall
    *undescribed*

irq_work_rise
    *undescribed*

.. _`pch_udc_dev`:

struct pch_udc_dev
==================

.. c:type:: struct pch_udc_dev

    Structure holding complete information of the PCH USB device

.. _`pch_udc_dev.definition`:

Definition
----------

.. code-block:: c

    struct pch_udc_dev {
        struct usb_gadget gadget;
        struct usb_gadget_driver *driver;
        struct pci_dev *pdev;
        struct pch_udc_ep ep[PCH_UDC_EP_NUM];
        spinlock_t lock;
        unsignedstall:1,prot_stall:1,suspended:1,connected:1,vbus_session:1,set_cfg_not_acked:1, waiting_zlp_ack:1;
        struct dma_pool *data_requests;
        struct dma_pool *stp_requests;
        dma_addr_t dma_addr;
        struct usb_ctrlrequest setup_data;
        void __iomem *base_addr;
        struct pch_udc_cfg_data cfg_data;
        struct pch_vbus_gpio_data vbus_gpio;
    }

.. _`pch_udc_dev.members`:

Members
-------

gadget
    gadget driver data

driver
    reference to gadget driver bound

pdev
    reference to the PCI device

ep
    array of endpoints

lock
    protects all state

data_requests
    DMA pool for data requests

stp_requests
    DMA pool for setup requests

dma_addr
    DMA pool for received

setup_data
    Received setup data

base_addr
    for mapped device memory

cfg_data
    current cfg, intf, and alt in use

vbus_gpio
    GPIO informaton for detecting VBUS

.. _`pch_udc_request`:

struct pch_udc_request
======================

.. c:type:: struct pch_udc_request

    Structure holding a PCH USB device request packet

.. _`pch_udc_request.definition`:

Definition
----------

.. code-block:: c

    struct pch_udc_request {
        struct usb_request req;
        dma_addr_t td_data_phys;
        struct pch_udc_data_dma_desc *td_data;
        struct pch_udc_data_dma_desc *td_data_last;
        struct list_head queue;
        unsigned dma_going:1,dma_mapped:1, dma_done:1;
        unsigned chain_len;
        void *buf;
        dma_addr_t dma;
    }

.. _`pch_udc_request.members`:

Members
-------

req
    embedded ep request

td_data_phys
    phys. address

td_data
    first dma desc. of chain

td_data_last
    last dma desc. of chain

queue
    associated queue

dma_going
    DMA in progress for request

dma_mapped
    DMA memory mapped for request

dma_done
    DMA completed for request

chain_len
    chain length

buf
    Buffer memory for align adjustment

dma
    DMA memory for align adjustment

.. _`pch_udc_csr_busy`:

pch_udc_csr_busy
================

.. c:function:: void pch_udc_csr_busy(struct pch_udc_dev *dev)

    Wait till idle.

    :param dev:
        Reference to pch_udc_dev structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_write_csr`:

pch_udc_write_csr
=================

.. c:function:: void pch_udc_write_csr(struct pch_udc_dev *dev, unsigned long val, unsigned int ep)

    Write the command and status registers.

    :param dev:
        Reference to pch_udc_dev structure
    :type dev: struct pch_udc_dev \*

    :param val:
        value to be written to CSR register
    :type val: unsigned long

    :param ep:
        *undescribed*
    :type ep: unsigned int

.. _`pch_udc_read_csr`:

pch_udc_read_csr
================

.. c:function:: u32 pch_udc_read_csr(struct pch_udc_dev *dev, unsigned int ep)

    Read the command and status registers.

    :param dev:
        Reference to pch_udc_dev structure
    :type dev: struct pch_udc_dev \*

    :param ep:
        *undescribed*
    :type ep: unsigned int

.. _`pch_udc_read_csr.return-codes`:

Return codes
------------

content of CSR register

.. _`pch_udc_rmt_wakeup`:

pch_udc_rmt_wakeup
==================

.. c:function:: void pch_udc_rmt_wakeup(struct pch_udc_dev *dev)

    Initiate for remote wakeup

    :param dev:
        Reference to pch_udc_dev structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_get_frame`:

pch_udc_get_frame
=================

.. c:function:: int pch_udc_get_frame(struct pch_udc_dev *dev)

    Get the current frame from device status register

    :param dev:
        Reference to pch_udc_dev structure
        Retern       current frame
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_clear_selfpowered`:

pch_udc_clear_selfpowered
=========================

.. c:function:: void pch_udc_clear_selfpowered(struct pch_udc_dev *dev)

    Clear the self power control

    :param dev:
        Reference to pch_udc_regs structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_set_selfpowered`:

pch_udc_set_selfpowered
=======================

.. c:function:: void pch_udc_set_selfpowered(struct pch_udc_dev *dev)

    Set the self power control

    :param dev:
        Reference to pch_udc_regs structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_set_disconnect`:

pch_udc_set_disconnect
======================

.. c:function:: void pch_udc_set_disconnect(struct pch_udc_dev *dev)

    Set the disconnect status.

    :param dev:
        Reference to pch_udc_regs structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_clear_disconnect`:

pch_udc_clear_disconnect
========================

.. c:function:: void pch_udc_clear_disconnect(struct pch_udc_dev *dev)

    Clear the disconnect status.

    :param dev:
        Reference to pch_udc_regs structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_init`:

pch_udc_init
============

.. c:function:: void pch_udc_init(struct pch_udc_dev *dev)

    This API initializes usb device controller, and clear the disconnect status.

    :param dev:
        Reference to pch_udc_regs structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_vbus_session`:

pch_udc_vbus_session
====================

.. c:function:: void pch_udc_vbus_session(struct pch_udc_dev *dev, int is_active)

    set or clearr the disconnect status.

    :param dev:
        Reference to pch_udc_regs structure
    :type dev: struct pch_udc_dev \*

    :param is_active:
        Parameter specifying the action
        0:   indicating VBUS power is ending
        !0:  indicating VBUS power is starting
    :type is_active: int

.. _`pch_udc_ep_set_stall`:

pch_udc_ep_set_stall
====================

.. c:function:: void pch_udc_ep_set_stall(struct pch_udc_ep *ep)

    Set the stall of endpoint

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_ep_clear_stall`:

pch_udc_ep_clear_stall
======================

.. c:function:: void pch_udc_ep_clear_stall(struct pch_udc_ep *ep)

    Clear the stall of endpoint

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_ep_set_trfr_type`:

pch_udc_ep_set_trfr_type
========================

.. c:function:: void pch_udc_ep_set_trfr_type(struct pch_udc_ep *ep, u8 type)

    Set the transfer type of endpoint

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

    :param type:
        Type of endpoint
    :type type: u8

.. _`pch_udc_ep_set_bufsz`:

pch_udc_ep_set_bufsz
====================

.. c:function:: void pch_udc_ep_set_bufsz(struct pch_udc_ep *ep, u32 buf_size, u32 ep_in)

    Set the maximum packet size for the endpoint

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

    :param buf_size:
        The buffer word size
    :type buf_size: u32

    :param ep_in:
        *undescribed*
    :type ep_in: u32

.. _`pch_udc_ep_set_maxpkt`:

pch_udc_ep_set_maxpkt
=====================

.. c:function:: void pch_udc_ep_set_maxpkt(struct pch_udc_ep *ep, u32 pkt_size)

    Set the Max packet size for the endpoint

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

    :param pkt_size:
        The packet byte size
    :type pkt_size: u32

.. _`pch_udc_ep_set_subptr`:

pch_udc_ep_set_subptr
=====================

.. c:function:: void pch_udc_ep_set_subptr(struct pch_udc_ep *ep, u32 addr)

    Set the Setup buffer pointer for the endpoint

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

    :param addr:
        Address of the register
    :type addr: u32

.. _`pch_udc_ep_set_ddptr`:

pch_udc_ep_set_ddptr
====================

.. c:function:: void pch_udc_ep_set_ddptr(struct pch_udc_ep *ep, u32 addr)

    Set the Data descriptor pointer for the endpoint

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

    :param addr:
        Address of the register
    :type addr: u32

.. _`pch_udc_ep_set_pd`:

pch_udc_ep_set_pd
=================

.. c:function:: void pch_udc_ep_set_pd(struct pch_udc_ep *ep)

    Set the poll demand bit for the endpoint

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_ep_set_rrdy`:

pch_udc_ep_set_rrdy
===================

.. c:function:: void pch_udc_ep_set_rrdy(struct pch_udc_ep *ep)

    Set the receive ready bit for the endpoint

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_ep_clear_rrdy`:

pch_udc_ep_clear_rrdy
=====================

.. c:function:: void pch_udc_ep_clear_rrdy(struct pch_udc_ep *ep)

    Clear the receive ready bit for the endpoint

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_set_dma`:

pch_udc_set_dma
===============

.. c:function:: void pch_udc_set_dma(struct pch_udc_dev *dev, int dir)

    Set the 'TDE' or RDE bit of device control register depending on the direction specified

    :param dev:
        Reference to structure of type pch_udc_regs
    :type dev: struct pch_udc_dev \*

    :param dir:
        whether Tx or Rx
        DMA_DIR_RX: Receive
        DMA_DIR_TX: Transmit
    :type dir: int

.. _`pch_udc_clear_dma`:

pch_udc_clear_dma
=================

.. c:function:: void pch_udc_clear_dma(struct pch_udc_dev *dev, int dir)

    Clear the 'TDE' or RDE bit of device control register depending on the direction specified

    :param dev:
        Reference to structure of type pch_udc_regs
    :type dev: struct pch_udc_dev \*

    :param dir:
        Whether Tx or Rx
        DMA_DIR_RX: Receive
        DMA_DIR_TX: Transmit
    :type dir: int

.. _`pch_udc_set_csr_done`:

pch_udc_set_csr_done
====================

.. c:function:: void pch_udc_set_csr_done(struct pch_udc_dev *dev)

    Set the device control register CSR done field (bit 13)

    :param dev:
        reference to structure of type pch_udc_regs
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_disable_interrupts`:

pch_udc_disable_interrupts
==========================

.. c:function:: void pch_udc_disable_interrupts(struct pch_udc_dev *dev, u32 mask)

    Disables the specified interrupts

    :param dev:
        Reference to structure of type pch_udc_regs
    :type dev: struct pch_udc_dev \*

    :param mask:
        Mask to disable interrupts
    :type mask: u32

.. _`pch_udc_enable_interrupts`:

pch_udc_enable_interrupts
=========================

.. c:function:: void pch_udc_enable_interrupts(struct pch_udc_dev *dev, u32 mask)

    Enable the specified interrupts

    :param dev:
        Reference to structure of type pch_udc_regs
    :type dev: struct pch_udc_dev \*

    :param mask:
        Mask to enable interrupts
    :type mask: u32

.. _`pch_udc_disable_ep_interrupts`:

pch_udc_disable_ep_interrupts
=============================

.. c:function:: void pch_udc_disable_ep_interrupts(struct pch_udc_dev *dev, u32 mask)

    Disable endpoint interrupts

    :param dev:
        Reference to structure of type pch_udc_regs
    :type dev: struct pch_udc_dev \*

    :param mask:
        Mask to disable interrupts
    :type mask: u32

.. _`pch_udc_enable_ep_interrupts`:

pch_udc_enable_ep_interrupts
============================

.. c:function:: void pch_udc_enable_ep_interrupts(struct pch_udc_dev *dev, u32 mask)

    Enable endpoint interrupts

    :param dev:
        Reference to structure of type pch_udc_regs
    :type dev: struct pch_udc_dev \*

    :param mask:
        Mask to enable interrupts
    :type mask: u32

.. _`pch_udc_read_device_interrupts`:

pch_udc_read_device_interrupts
==============================

.. c:function:: u32 pch_udc_read_device_interrupts(struct pch_udc_dev *dev)

    Read the device interrupts

    :param dev:
        Reference to structure of type pch_udc_regs
        Retern       The device interrupts
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_write_device_interrupts`:

pch_udc_write_device_interrupts
===============================

.. c:function:: void pch_udc_write_device_interrupts(struct pch_udc_dev *dev, u32 val)

    Write device interrupts

    :param dev:
        Reference to structure of type pch_udc_regs
    :type dev: struct pch_udc_dev \*

    :param val:
        The value to be written to interrupt register
    :type val: u32

.. _`pch_udc_read_ep_interrupts`:

pch_udc_read_ep_interrupts
==========================

.. c:function:: u32 pch_udc_read_ep_interrupts(struct pch_udc_dev *dev)

    Read the endpoint interrupts

    :param dev:
        Reference to structure of type pch_udc_regs
        Retern       The endpoint interrupt
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_write_ep_interrupts`:

pch_udc_write_ep_interrupts
===========================

.. c:function:: void pch_udc_write_ep_interrupts(struct pch_udc_dev *dev, u32 val)

    Clear endpoint interupts

    :param dev:
        Reference to structure of type pch_udc_regs
    :type dev: struct pch_udc_dev \*

    :param val:
        The value to be written to interrupt register
    :type val: u32

.. _`pch_udc_read_device_status`:

pch_udc_read_device_status
==========================

.. c:function:: u32 pch_udc_read_device_status(struct pch_udc_dev *dev)

    Read the device status

    :param dev:
        Reference to structure of type pch_udc_regs
        Retern       The device status
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_read_ep_control`:

pch_udc_read_ep_control
=======================

.. c:function:: u32 pch_udc_read_ep_control(struct pch_udc_ep *ep)

    Read the endpoint control

    :param ep:
        Reference to structure of type pch_udc_ep_regs
        Retern       The endpoint control register value
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_clear_ep_control`:

pch_udc_clear_ep_control
========================

.. c:function:: void pch_udc_clear_ep_control(struct pch_udc_ep *ep)

    Clear the endpoint control register

    :param ep:
        Reference to structure of type pch_udc_ep_regs
        Retern       The endpoint control register value
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_read_ep_status`:

pch_udc_read_ep_status
======================

.. c:function:: u32 pch_udc_read_ep_status(struct pch_udc_ep *ep)

    Read the endpoint status

    :param ep:
        Reference to structure of type pch_udc_ep_regs
        Retern       The endpoint status
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_clear_ep_status`:

pch_udc_clear_ep_status
=======================

.. c:function:: void pch_udc_clear_ep_status(struct pch_udc_ep *ep, u32 stat)

    Clear the endpoint status

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

    :param stat:
        Endpoint status
    :type stat: u32

.. _`pch_udc_ep_set_nak`:

pch_udc_ep_set_nak
==================

.. c:function:: void pch_udc_ep_set_nak(struct pch_udc_ep *ep)

    Set the bit 7 (SNAK field) of the endpoint control register

    :param ep:
        Reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_ep_clear_nak`:

pch_udc_ep_clear_nak
====================

.. c:function:: void pch_udc_ep_clear_nak(struct pch_udc_ep *ep)

    Set the bit 8 (CNAK field) of the endpoint control register

    :param ep:
        reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_ep_fifo_flush`:

pch_udc_ep_fifo_flush
=====================

.. c:function:: void pch_udc_ep_fifo_flush(struct pch_udc_ep *ep, int dir)

    Flush the endpoint fifo

    :param ep:
        reference to structure of type pch_udc_ep_regs
    :type ep: struct pch_udc_ep \*

    :param dir:
        direction of endpoint
        0:  endpoint is OUT
        !0: endpoint is IN
    :type dir: int

.. _`pch_udc_ep_enable`:

pch_udc_ep_enable
=================

.. c:function:: void pch_udc_ep_enable(struct pch_udc_ep *ep, struct pch_udc_cfg_data *cfg, const struct usb_endpoint_descriptor *desc)

    This api enables endpoint

    :param ep:
        *undescribed*
    :type ep: struct pch_udc_ep \*

    :param cfg:
        *undescribed*
    :type cfg: struct pch_udc_cfg_data \*

    :param desc:
        endpoint descriptor
    :type desc: const struct usb_endpoint_descriptor \*

.. _`pch_udc_ep_disable`:

pch_udc_ep_disable
==================

.. c:function:: void pch_udc_ep_disable(struct pch_udc_ep *ep)

    This api disables endpoint

    :param ep:
        *undescribed*
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_wait_ep_stall`:

pch_udc_wait_ep_stall
=====================

.. c:function:: void pch_udc_wait_ep_stall(struct pch_udc_ep *ep)

    Wait EP stall.

    :param ep:
        *undescribed*
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_init`:

pch_udc_init
============

.. c:function:: void pch_udc_init(struct pch_udc_dev *dev)

    This API initializes usb device controller

    :param dev:
        Rreference to pch_udc_regs structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_exit`:

pch_udc_exit
============

.. c:function:: void pch_udc_exit(struct pch_udc_dev *dev)

    This API exit usb device controller

    :param dev:
        Reference to pch_udc_regs structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_pcd_get_frame`:

pch_udc_pcd_get_frame
=====================

.. c:function:: int pch_udc_pcd_get_frame(struct usb_gadget *gadget)

    This API is invoked to get the current frame number

    :param gadget:
        Reference to the gadget driver
    :type gadget: struct usb_gadget \*

.. _`pch_udc_pcd_get_frame.return-codes`:

Return codes
------------

0:              Success
-EINVAL:        If the gadget passed is NULL

.. _`pch_udc_pcd_wakeup`:

pch_udc_pcd_wakeup
==================

.. c:function:: int pch_udc_pcd_wakeup(struct usb_gadget *gadget)

    This API is invoked to initiate a remote wakeup

    :param gadget:
        Reference to the gadget driver
    :type gadget: struct usb_gadget \*

.. _`pch_udc_pcd_wakeup.return-codes`:

Return codes
------------

0:              Success
-EINVAL:        If the gadget passed is NULL

.. _`pch_udc_pcd_selfpowered`:

pch_udc_pcd_selfpowered
=======================

.. c:function:: int pch_udc_pcd_selfpowered(struct usb_gadget *gadget, int value)

    This API is invoked to specify whether the device is self powered or not

    :param gadget:
        Reference to the gadget driver
    :type gadget: struct usb_gadget \*

    :param value:
        Specifies self powered or not
    :type value: int

.. _`pch_udc_pcd_selfpowered.return-codes`:

Return codes
------------

0:              Success
-EINVAL:        If the gadget passed is NULL

.. _`pch_udc_pcd_pullup`:

pch_udc_pcd_pullup
==================

.. c:function:: int pch_udc_pcd_pullup(struct usb_gadget *gadget, int is_on)

    This API is invoked to make the device visible/invisible to the host

    :param gadget:
        Reference to the gadget driver
    :type gadget: struct usb_gadget \*

    :param is_on:
        Specifies whether the pull up is made active or inactive
    :type is_on: int

.. _`pch_udc_pcd_pullup.return-codes`:

Return codes
------------

0:              Success
-EINVAL:        If the gadget passed is NULL

.. _`pch_udc_pcd_vbus_session`:

pch_udc_pcd_vbus_session
========================

.. c:function:: int pch_udc_pcd_vbus_session(struct usb_gadget *gadget, int is_active)

    This API is used by a driver for an external transceiver (or GPIO) that detects a VBUS power session starting/ending

    :param gadget:
        Reference to the gadget driver
    :type gadget: struct usb_gadget \*

    :param is_active:
        specifies whether the session is starting or ending
    :type is_active: int

.. _`pch_udc_pcd_vbus_session.return-codes`:

Return codes
------------

0:              Success
-EINVAL:        If the gadget passed is NULL

.. _`pch_udc_pcd_vbus_draw`:

pch_udc_pcd_vbus_draw
=====================

.. c:function:: int pch_udc_pcd_vbus_draw(struct usb_gadget *gadget, unsigned int mA)

    This API is used by gadget drivers during SET_CONFIGURATION calls to specify how much power the device can consume

    :param gadget:
        Reference to the gadget driver
    :type gadget: struct usb_gadget \*

    :param mA:
        specifies the current limit in 2mA unit
    :type mA: unsigned int

.. _`pch_udc_pcd_vbus_draw.return-codes`:

Return codes
------------

-EINVAL:        If the gadget passed is NULL
-EOPNOTSUPP:

.. _`pch_vbus_gpio_get_value`:

pch_vbus_gpio_get_value
=======================

.. c:function:: int pch_vbus_gpio_get_value(struct pch_udc_dev *dev)

    This API gets value of GPIO port as VBUS status.

    :param dev:
        Reference to the driver structure
    :type dev: struct pch_udc_dev \*

.. _`pch_vbus_gpio_get_value.return-value`:

Return value
------------

1: VBUS is high
0: VBUS is low
-1: It is not enable to detect VBUS using GPIO

.. _`pch_vbus_gpio_work_fall`:

pch_vbus_gpio_work_fall
=======================

.. c:function:: void pch_vbus_gpio_work_fall(struct work_struct *irq_work)

    This API keeps watch on VBUS becoming Low. If VBUS is Low, disconnect is processed

    :param irq_work:
        Structure for WorkQueue
    :type irq_work: struct work_struct \*

.. _`pch_vbus_gpio_work_rise`:

pch_vbus_gpio_work_rise
=======================

.. c:function:: void pch_vbus_gpio_work_rise(struct work_struct *irq_work)

    This API checks VBUS is High. If VBUS is High, connect is processed

    :param irq_work:
        Structure for WorkQueue
    :type irq_work: struct work_struct \*

.. _`pch_vbus_gpio_irq`:

pch_vbus_gpio_irq
=================

.. c:function:: irqreturn_t pch_vbus_gpio_irq(int irq, void *data)

    IRQ handler for GPIO intrerrupt for changing VBUS

    :param irq:
        Interrupt request number
    :type irq: int

    :param data:
        *undescribed*
    :type data: void \*

.. _`pch_vbus_gpio_irq.return-codes`:

Return codes
------------

0: Success
-EINVAL: GPIO port is invalid or can't be initialized.

.. _`pch_vbus_gpio_init`:

pch_vbus_gpio_init
==================

.. c:function:: int pch_vbus_gpio_init(struct pch_udc_dev *dev, int vbus_gpio_port)

    This API initializes GPIO port detecting VBUS.

    :param dev:
        Reference to the driver structure
        \ ``vbus_gpio``\    Number of GPIO port to detect gpio
    :type dev: struct pch_udc_dev \*

    :param vbus_gpio_port:
        *undescribed*
    :type vbus_gpio_port: int

.. _`pch_vbus_gpio_init.return-codes`:

Return codes
------------

0: Success
-EINVAL: GPIO port is invalid or can't be initialized.

.. _`pch_vbus_gpio_free`:

pch_vbus_gpio_free
==================

.. c:function:: void pch_vbus_gpio_free(struct pch_udc_dev *dev)

    This API frees resources of GPIO port

    :param dev:
        Reference to the driver structure
    :type dev: struct pch_udc_dev \*

.. _`complete_req`:

complete_req
============

.. c:function:: void complete_req(struct pch_udc_ep *ep, struct pch_udc_request *req, int status)

    This API is invoked from the driver when processing of a request is complete

    :param ep:
        Reference to the endpoint structure
    :type ep: struct pch_udc_ep \*

    :param req:
        Reference to the request structure
    :type req: struct pch_udc_request \*

    :param status:
        Indicates the success/failure of completion
    :type status: int

.. _`empty_req_queue`:

empty_req_queue
===============

.. c:function:: void empty_req_queue(struct pch_udc_ep *ep)

    This API empties the request queue of an endpoint

    :param ep:
        Reference to the endpoint structure
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_free_dma_chain`:

pch_udc_free_dma_chain
======================

.. c:function:: void pch_udc_free_dma_chain(struct pch_udc_dev *dev, struct pch_udc_request *req)

    This function frees the DMA chain created for the request \ ``dev``\          Reference to the driver structure \ ``req``\          Reference to the request to be freed

    :param dev:
        *undescribed*
    :type dev: struct pch_udc_dev \*

    :param req:
        *undescribed*
    :type req: struct pch_udc_request \*

.. _`pch_udc_free_dma_chain.return-codes`:

Return codes
------------

0: Success

.. _`pch_udc_create_dma_chain`:

pch_udc_create_dma_chain
========================

.. c:function:: int pch_udc_create_dma_chain(struct pch_udc_ep *ep, struct pch_udc_request *req, unsigned long buf_len, gfp_t gfp_flags)

    This function creates or reinitializes a DMA chain

    :param ep:
        Reference to the endpoint structure
    :type ep: struct pch_udc_ep \*

    :param req:
        Reference to the request
    :type req: struct pch_udc_request \*

    :param buf_len:
        The buffer length
    :type buf_len: unsigned long

    :param gfp_flags:
        Flags to be used while mapping the data buffer
    :type gfp_flags: gfp_t

.. _`pch_udc_create_dma_chain.return-codes`:

Return codes
------------

0:              success,
-ENOMEM:        dma_pool_alloc invocation fails

.. _`prepare_dma`:

prepare_dma
===========

.. c:function:: int prepare_dma(struct pch_udc_ep *ep, struct pch_udc_request *req, gfp_t gfp)

    This function creates and initializes the DMA chain for the request

    :param ep:
        Reference to the endpoint structure
    :type ep: struct pch_udc_ep \*

    :param req:
        Reference to the request
    :type req: struct pch_udc_request \*

    :param gfp:
        Flag to be used while mapping the data buffer
    :type gfp: gfp_t

.. _`prepare_dma.return-codes`:

Return codes
------------

0:              Success

.. _`prepare_dma.other-0`:

Other 0
-------

linux error number on failure

.. _`process_zlp`:

process_zlp
===========

.. c:function:: void process_zlp(struct pch_udc_ep *ep, struct pch_udc_request *req)

    This function process zero length packets from the gadget driver

    :param ep:
        Reference to the endpoint structure
    :type ep: struct pch_udc_ep \*

    :param req:
        Reference to the request
    :type req: struct pch_udc_request \*

.. _`pch_udc_start_rxrequest`:

pch_udc_start_rxrequest
=======================

.. c:function:: void pch_udc_start_rxrequest(struct pch_udc_ep *ep, struct pch_udc_request *req)

    This function starts the receive requirement.

    :param ep:
        Reference to the endpoint structure
    :type ep: struct pch_udc_ep \*

    :param req:
        Reference to the request structure
    :type req: struct pch_udc_request \*

.. _`pch_udc_pcd_ep_enable`:

pch_udc_pcd_ep_enable
=====================

.. c:function:: int pch_udc_pcd_ep_enable(struct usb_ep *usbep, const struct usb_endpoint_descriptor *desc)

    This API enables the endpoint. It is called from gadget driver

    :param usbep:
        Reference to the USB endpoint structure
    :type usbep: struct usb_ep \*

    :param desc:
        Reference to the USB endpoint descriptor structure
    :type desc: const struct usb_endpoint_descriptor \*

.. _`pch_udc_pcd_ep_enable.return-codes`:

Return codes
------------

0:              Success
-EINVAL:
-ESHUTDOWN:

.. _`pch_udc_pcd_ep_disable`:

pch_udc_pcd_ep_disable
======================

.. c:function:: int pch_udc_pcd_ep_disable(struct usb_ep *usbep)

    This API disables endpoint and is called from gadget driver \ ``usbep``\        Reference to the USB endpoint structure

    :param usbep:
        *undescribed*
    :type usbep: struct usb_ep \*

.. _`pch_udc_pcd_ep_disable.return-codes`:

Return codes
------------

0:              Success
-EINVAL:

.. _`pch_udc_alloc_request`:

pch_udc_alloc_request
=====================

.. c:function:: struct usb_request *pch_udc_alloc_request(struct usb_ep *usbep, gfp_t gfp)

    This function allocates request structure. It is called by gadget driver

    :param usbep:
        Reference to the USB endpoint structure
    :type usbep: struct usb_ep \*

    :param gfp:
        Flag to be used while allocating memory
    :type gfp: gfp_t

.. _`pch_udc_alloc_request.null`:

NULL
----

Failure

.. _`pch_udc_alloc_request.allocated-address`:

Allocated address
-----------------

Success

.. _`pch_udc_free_request`:

pch_udc_free_request
====================

.. c:function:: void pch_udc_free_request(struct usb_ep *usbep, struct usb_request *usbreq)

    This function frees request structure. It is called by gadget driver

    :param usbep:
        Reference to the USB endpoint structure
    :type usbep: struct usb_ep \*

    :param usbreq:
        Reference to the USB request
    :type usbreq: struct usb_request \*

.. _`pch_udc_pcd_queue`:

pch_udc_pcd_queue
=================

.. c:function:: int pch_udc_pcd_queue(struct usb_ep *usbep, struct usb_request *usbreq, gfp_t gfp)

    This function queues a request packet. It is called by gadget driver

    :param usbep:
        Reference to the USB endpoint structure
    :type usbep: struct usb_ep \*

    :param usbreq:
        Reference to the USB request
    :type usbreq: struct usb_request \*

    :param gfp:
        Flag to be used while mapping the data buffer
    :type gfp: gfp_t

.. _`pch_udc_pcd_queue.return-codes`:

Return codes
------------

0:                      Success

.. _`pch_udc_pcd_queue.linux-error-number`:

linux error number
------------------

Failure

.. _`pch_udc_pcd_dequeue`:

pch_udc_pcd_dequeue
===================

.. c:function:: int pch_udc_pcd_dequeue(struct usb_ep *usbep, struct usb_request *usbreq)

    This function de-queues a request packet. It is called by gadget driver

    :param usbep:
        Reference to the USB endpoint structure
    :type usbep: struct usb_ep \*

    :param usbreq:
        Reference to the USB request
    :type usbreq: struct usb_request \*

.. _`pch_udc_pcd_dequeue.return-codes`:

Return codes
------------

0:                      Success

.. _`pch_udc_pcd_dequeue.linux-error-number`:

linux error number
------------------

Failure

.. _`pch_udc_pcd_set_halt`:

pch_udc_pcd_set_halt
====================

.. c:function:: int pch_udc_pcd_set_halt(struct usb_ep *usbep, int halt)

    This function Sets or clear the endpoint halt feature

    :param usbep:
        Reference to the USB endpoint structure
    :type usbep: struct usb_ep \*

    :param halt:
        Specifies whether to set or clear the feature
    :type halt: int

.. _`pch_udc_pcd_set_halt.return-codes`:

Return codes
------------

0:                      Success

.. _`pch_udc_pcd_set_halt.linux-error-number`:

linux error number
------------------

Failure

.. _`pch_udc_pcd_set_wedge`:

pch_udc_pcd_set_wedge
=====================

.. c:function:: int pch_udc_pcd_set_wedge(struct usb_ep *usbep)

    This function Sets or clear the endpoint halt feature

    :param usbep:
        Reference to the USB endpoint structure
    :type usbep: struct usb_ep \*

.. _`pch_udc_pcd_set_wedge.return-codes`:

Return codes
------------

0:                      Success

.. _`pch_udc_pcd_set_wedge.linux-error-number`:

linux error number
------------------

Failure

.. _`pch_udc_pcd_fifo_flush`:

pch_udc_pcd_fifo_flush
======================

.. c:function:: void pch_udc_pcd_fifo_flush(struct usb_ep *usbep)

    This function Flush the FIFO of specified endpoint

    :param usbep:
        Reference to the USB endpoint structure
    :type usbep: struct usb_ep \*

.. _`pch_udc_init_setup_buff`:

pch_udc_init_setup_buff
=======================

.. c:function:: void pch_udc_init_setup_buff(struct pch_udc_stp_dma_desc *td_stp)

    This function initializes the SETUP buffer

    :param td_stp:
        Reference to the SETP buffer structure
    :type td_stp: struct pch_udc_stp_dma_desc \*

.. _`pch_udc_start_next_txrequest`:

pch_udc_start_next_txrequest
============================

.. c:function:: void pch_udc_start_next_txrequest(struct pch_udc_ep *ep)

    This function starts the next transmission requirement

    :param ep:
        Reference to the endpoint structure
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_complete_transfer`:

pch_udc_complete_transfer
=========================

.. c:function:: void pch_udc_complete_transfer(struct pch_udc_ep *ep)

    This function completes a transfer

    :param ep:
        Reference to the endpoint structure
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_complete_receiver`:

pch_udc_complete_receiver
=========================

.. c:function:: void pch_udc_complete_receiver(struct pch_udc_ep *ep)

    This function completes a receiver

    :param ep:
        Reference to the endpoint structure
    :type ep: struct pch_udc_ep \*

.. _`pch_udc_svc_data_in`:

pch_udc_svc_data_in
===================

.. c:function:: void pch_udc_svc_data_in(struct pch_udc_dev *dev, int ep_num)

    This function process endpoint interrupts for IN endpoints

    :param dev:
        Reference to the device structure
    :type dev: struct pch_udc_dev \*

    :param ep_num:
        Endpoint that generated the interrupt
    :type ep_num: int

.. _`pch_udc_svc_data_out`:

pch_udc_svc_data_out
====================

.. c:function:: void pch_udc_svc_data_out(struct pch_udc_dev *dev, int ep_num)

    Handles interrupts from OUT endpoint

    :param dev:
        Reference to the device structure
    :type dev: struct pch_udc_dev \*

    :param ep_num:
        Endpoint that generated the interrupt
    :type ep_num: int

.. _`pch_udc_svc_control_in`:

pch_udc_svc_control_in
======================

.. c:function:: void pch_udc_svc_control_in(struct pch_udc_dev *dev)

    Handle Control IN endpoint interrupts

    :param dev:
        Reference to the device structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_svc_control_out`:

pch_udc_svc_control_out
=======================

.. c:function:: void pch_udc_svc_control_out(struct pch_udc_dev *dev)

    Routine that handle Control OUT endpoint interrupts

    :param dev:
        Reference to the device structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_postsvc_epinters`:

pch_udc_postsvc_epinters
========================

.. c:function:: void pch_udc_postsvc_epinters(struct pch_udc_dev *dev, int ep_num)

    This function enables end point interrupts and clears NAK status

    :param dev:
        Reference to the device structure
    :type dev: struct pch_udc_dev \*

    :param ep_num:
        End point number
    :type ep_num: int

.. _`pch_udc_read_all_epstatus`:

pch_udc_read_all_epstatus
=========================

.. c:function:: void pch_udc_read_all_epstatus(struct pch_udc_dev *dev, u32 ep_intr)

    This function read all endpoint status

    :param dev:
        Reference to the device structure
    :type dev: struct pch_udc_dev \*

    :param ep_intr:
        Status of endpoint interrupt
    :type ep_intr: u32

.. _`pch_udc_activate_control_ep`:

pch_udc_activate_control_ep
===========================

.. c:function:: void pch_udc_activate_control_ep(struct pch_udc_dev *dev)

    This function enables the control endpoints for traffic after a reset

    :param dev:
        Reference to the device structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_svc_ur_interrupt`:

pch_udc_svc_ur_interrupt
========================

.. c:function:: void pch_udc_svc_ur_interrupt(struct pch_udc_dev *dev)

    This function handles a USB reset interrupt

    :param dev:
        Reference to driver structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_svc_enum_interrupt`:

pch_udc_svc_enum_interrupt
==========================

.. c:function:: void pch_udc_svc_enum_interrupt(struct pch_udc_dev *dev)

    This function handles a USB speed enumeration done interrupt

    :param dev:
        Reference to driver structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_svc_intf_interrupt`:

pch_udc_svc_intf_interrupt
==========================

.. c:function:: void pch_udc_svc_intf_interrupt(struct pch_udc_dev *dev)

    This function handles a set interface interrupt

    :param dev:
        Reference to driver structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_svc_cfg_interrupt`:

pch_udc_svc_cfg_interrupt
=========================

.. c:function:: void pch_udc_svc_cfg_interrupt(struct pch_udc_dev *dev)

    This function handles a set configuration interrupt

    :param dev:
        Reference to driver structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_dev_isr`:

pch_udc_dev_isr
===============

.. c:function:: void pch_udc_dev_isr(struct pch_udc_dev *dev, u32 dev_intr)

    This function services device interrupts by invoking appropriate routines.

    :param dev:
        Reference to the device structure
    :type dev: struct pch_udc_dev \*

    :param dev_intr:
        The Device interrupt status.
    :type dev_intr: u32

.. _`pch_udc_isr`:

pch_udc_isr
===========

.. c:function:: irqreturn_t pch_udc_isr(int irq, void *pdev)

    This function handles interrupts from the PCH USB Device

    :param irq:
        Interrupt request number
    :type irq: int

    :param pdev:
        *undescribed*
    :type pdev: void \*

.. _`pch_udc_setup_ep0`:

pch_udc_setup_ep0
=================

.. c:function:: void pch_udc_setup_ep0(struct pch_udc_dev *dev)

    This function enables control endpoint for traffic

    :param dev:
        Reference to the device structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_pcd_reinit`:

pch_udc_pcd_reinit
==================

.. c:function:: void pch_udc_pcd_reinit(struct pch_udc_dev *dev)

    This API initializes the endpoint structures

    :param dev:
        Reference to the driver structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_pcd_init`:

pch_udc_pcd_init
================

.. c:function:: int pch_udc_pcd_init(struct pch_udc_dev *dev)

    This API initializes the driver structure

    :param dev:
        Reference to the driver structure
    :type dev: struct pch_udc_dev \*

.. _`pch_udc_pcd_init.return-codes`:

Return codes
------------

0: Success

.. _`init_dma_pools`:

init_dma_pools
==============

.. c:function:: int init_dma_pools(struct pch_udc_dev *dev)

    create dma pools during initialization

    :param dev:
        *undescribed*
    :type dev: struct pch_udc_dev \*

.. This file was automatic generated / don't edit.

