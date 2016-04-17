.. -*- coding: utf-8; mode: rst -*-

============
pxa27x_udc.h
============


.. _`udc_usb_ep`:

struct udc_usb_ep
=================

.. c:type:: udc_usb_ep

    container of each usb_ep structure


.. _`udc_usb_ep.definition`:

Definition
----------

.. code-block:: c

  struct udc_usb_ep {
    struct usb_ep usb_ep;
    struct usb_endpoint_descriptor desc;
    struct pxa_udc * dev;
    struct pxa_ep * pxa_ep;
  };


.. _`udc_usb_ep.members`:

Members
-------

:``usb_ep``:
    usb endpoint

:``desc``:
    usb descriptor, especially type and address

:``dev``:
    udc managing this endpoint

:``pxa_ep``:
    matching pxa_ep (cache of :c:func:`find_pxa_ep` call)




.. _`pxa_ep`:

struct pxa_ep
=============

.. c:type:: pxa_ep

    pxa endpoint


.. _`pxa_ep.definition`:

Definition
----------

.. code-block:: c

  struct pxa_ep {
    struct pxa_udc * dev;
    struct list_head queue;
    spinlock_t lock;
    unsigned enabled:1;
    unsigned in_handle_ep:1;
    unsigned idx:5;
    char * name;
    unsigned dir_in:1;
    unsigned addr:4;
    unsigned config:2;
    unsigned interface:3;
    unsigned alternate:3;
    unsigned fifo_size;
    unsigned type;
    #ifdef CONFIG_PM
    u32 udccsr_value;
    u32 udccr_value;
    #endif
    struct stats stats;
  };


.. _`pxa_ep.members`:

Members
-------

:``dev``:
    udc device

:``queue``:
    requests queue

:``lock``:
    lock to pxa_ep data (queues and stats)

:``enabled``:
    true when endpoint enabled (not stopped by gadget layer)

:``in_handle_ep``:
    number of recursions of :c:func:`handle_ep` function

:``idx``:
    endpoint index (1 => epA, 2 => epB, ..., 24 => epX)

:``name``:
    endpoint name (for trace/debug purpose)

:``dir_in``:
    1 if IN endpoint, 0 if OUT endpoint

:``addr``:
    usb endpoint number

:``config``:
    configuration in which this endpoint is active

:``interface``:
    interface in which this endpoint is active

:``alternate``:
    altsetting in which this endpoitn is active

:``fifo_size``:
    max packet size in the endpoint fifo

:``type``:
    endpoint type (bulk, iso, int, ...)

:``udccsr_value``:
    save register of UDCCSR0 for suspend/resume

:``udccr_value``:
    save register of UDCCR for suspend/resume

:``stats``:
    endpoint statistics




.. _`pxa_ep.prevents-deadlocks-or-infinite-recursions-of-types`:

Prevents deadlocks or infinite recursions of types 
---------------------------------------------------

irq->:c:func:`handle_ep`->:c:func:`req_done`->req.:c:func:`complete`->:c:func:`pxa_ep_queue`->:c:func:`handle_ep`
or
:c:func:`pxa_ep_queue`->:c:func:`handle_ep`->:c:func:`req_done`->req.:c:func:`complete`->:c:func:`pxa_ep_queue`



.. _`pxa_ep.description`:

Description
-----------

The \*PROBLEM\* is that pxa's endpoint configuration scheme is both misdesigned
(cares about config/interface/altsetting, thus placing needless limits on
device capability) and full of implementation bugs forcing it to be set up
for use more or less like a pxa255.

As we define the pxa_ep statically, we must guess all needed pxa_ep for all
gadget which may work with this udc driver.



.. _`pxa27x_request`:

struct pxa27x_request
=====================

.. c:type:: pxa27x_request

    container of each usb_request structure


.. _`pxa27x_request.definition`:

Definition
----------

.. code-block:: c

  struct pxa27x_request {
    struct usb_request req;
    struct udc_usb_ep * udc_usb_ep;
    unsigned in_use:1;
    struct list_head queue;
  };


.. _`pxa27x_request.members`:

Members
-------

:``req``:
    usb request

:``udc_usb_ep``:
    usb endpoint the request was submitted on

:``in_use``:
    sanity check if request already queued on an pxa_ep

:``queue``:
    linked list of requests, linked on pxa_ep->queue




.. _`pxa_udc`:

struct pxa_udc
==============

.. c:type:: pxa_udc

    udc structure


.. _`pxa_udc.definition`:

Definition
----------

.. code-block:: c

  struct pxa_udc {
    void __iomem * regs;
    int irq;
    struct clk * clk;
    struct usb_gadget_driver * driver;
    struct device * dev;
    void (* udc_command) (int);
    struct gpio_desc * gpiod;
    struct usb_phy * transceiver;
    enum ep0_state ep0state;
    struct udc_stats stats;
    struct udc_usb_ep udc_usb_ep[NR_USB_ENDPOINTS];
    struct pxa_ep pxa_ep[NR_PXA_ENDPOINTS];
    unsigned enabled:1;
    unsigned pullup_on:1;
    unsigned pullup_resume:1;
    unsigned config:2;
    unsigned last_interface:3;
    unsigned last_alternate:3;
    #ifdef CONFIG_PM
    unsigned udccsr0;
    #endif
    #ifdef CONFIG_USB_GADGET_DEBUG_FS
    struct dentry * debugfs_root;
    struct dentry * debugfs_state;
    struct dentry * debugfs_queues;
    struct dentry * debugfs_eps;
    #endif
  };


.. _`pxa_udc.members`:

Members
-------

:``regs``:
    mapped IO space

:``irq``:
    udc irq

:``clk``:
    udc clock

:``driver``:
    bound gadget (zero, g_ether, g_mass_storage, ...)

:``dev``:
    device

:``udc_command``:
    machine specific function to activate D+ pullup

:``gpiod``:
    gpio descriptor of gpio for D+ pullup (or NULL if none)

:``transceiver``:
    external transceiver to handle vbus sense and D+ pullup

:``ep0state``:
    control endpoint state machine state

:``stats``:
    statistics on udc usage

:``udc_usb_ep[NR_USB_ENDPOINTS]``:
    array of usb endpoints offered by the gadget

:``pxa_ep[NR_PXA_ENDPOINTS]``:
    array of pxa available endpoints

:``enabled``:
    UDC was enabled by a previous :c:func:`udc_enable`

:``pullup_on``:
    if pullup resistor connected to D+ pin

:``pullup_resume``:
    if pullup resistor should be connected to D+ pin on resume

:``config``:
    UDC active configuration

:``last_interface``:
    UDC interface of the last SET_INTERFACE host request

:``last_alternate``:
    UDC altsetting of the last SET_INTERFACE host request

:``udccsr0``:
    save of udccsr0 in case of suspend

:``debugfs_root``:
    root entry of debug filesystem

:``debugfs_state``:
    debugfs entry for "udcstate"

:``debugfs_queues``:
    debugfs entry for "queues"

:``debugfs_eps``:
    debugfs entry for "epstate"


