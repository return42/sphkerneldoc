.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/udc/pxa27x_udc.c

.. _`is_match_usb_pxa`:

is_match_usb_pxa
================

.. c:function:: int is_match_usb_pxa(struct udc_usb_ep *udc_usb_ep, struct pxa_ep *ep, int config, int interface, int altsetting)

    check if usb_ep and pxa_ep match

    :param struct udc_usb_ep \*udc_usb_ep:
        usb endpoint

    :param struct pxa_ep \*ep:
        pxa endpoint

    :param int config:
        configuration required in pxa_ep

    :param int interface:
        interface required in pxa_ep

    :param int altsetting:
        altsetting required in pxa_ep

.. _`is_match_usb_pxa.description`:

Description
-----------

Returns 1 if all criteria match between pxa and usb endpoint, 0 otherwise

.. _`find_pxa_ep`:

find_pxa_ep
===========

.. c:function:: struct pxa_ep *find_pxa_ep(struct pxa_udc *udc, struct udc_usb_ep *udc_usb_ep)

    find pxa_ep structure matching udc_usb_ep

    :param struct pxa_udc \*udc:
        pxa udc

    :param struct udc_usb_ep \*udc_usb_ep:
        udc_usb_ep structure

.. _`find_pxa_ep.description`:

Description
-----------

Match udc_usb_ep and all pxa_ep available, to see if one matches.
This is necessary because of the strong pxa hardware restriction requiring
that once pxa endpoints are initialized, their configuration is freezed, and
no change can be made to their address, direction, or in which configuration,
interface or altsetting they are active ... which differs from more usual
models which have endpoints be roughly just addressable fifos, and leave
configuration events up to gadget drivers (like all control messages).

Note that there is still a blurred point here :
- we rely on UDCCR register "active interface" and "active altsetting".
This is a nonsense in regard of USB spec, where multiple interfaces are
active at the same time.
- if we knew for sure that the pxa can handle multiple interface at the
same time, assuming Intel's Developer Guide is wrong, this function
should be reviewed, and a cache of couples (iface, altsetting) should
be kept in the pxa_udc structure. In this case this function would match
against the cache of couples instead of the "last altsetting" set up.

Returns the matched pxa_ep structure or NULL if none found

.. _`update_pxa_ep_matches`:

update_pxa_ep_matches
=====================

.. c:function:: void update_pxa_ep_matches(struct pxa_udc *udc)

    update pxa_ep cached values in all udc_usb_ep

    :param struct pxa_udc \*udc:
        pxa udc

.. _`update_pxa_ep_matches.context`:

Context
-------

in_interrupt()

.. _`update_pxa_ep_matches.description`:

Description
-----------

Updates all pxa_ep fields in udc_usb_ep structures, if this field was
previously set up (and is not NULL). The update is necessary is a
configuration change or altsetting change was issued by the USB host.

.. _`pio_irq_enable`:

pio_irq_enable
==============

.. c:function:: void pio_irq_enable(struct pxa_ep *ep)

    Enables irq generation for one endpoint

    :param struct pxa_ep \*ep:
        udc endpoint

.. _`pio_irq_disable`:

pio_irq_disable
===============

.. c:function:: void pio_irq_disable(struct pxa_ep *ep)

    Disables irq generation for one endpoint

    :param struct pxa_ep \*ep:
        udc endpoint

.. _`udc_set_mask_udccr`:

udc_set_mask_UDCCR
==================

.. c:function:: void udc_set_mask_UDCCR(struct pxa_udc *udc, int mask)

    set bits in UDCCR

    :param struct pxa_udc \*udc:
        udc device

    :param int mask:
        bits to set in UDCCR

.. _`udc_set_mask_udccr.description`:

Description
-----------

Sets bits in UDCCR, leaving DME and FST bits as they were.

.. _`udc_clear_mask_udccr`:

udc_clear_mask_UDCCR
====================

.. c:function:: void udc_clear_mask_UDCCR(struct pxa_udc *udc, int mask)

    clears bits in UDCCR

    :param struct pxa_udc \*udc:
        udc device

    :param int mask:
        bit to clear in UDCCR

.. _`udc_clear_mask_udccr.description`:

Description
-----------

Clears bits in UDCCR, leaving DME and FST bits as they were.

.. _`ep_write_udccsr`:

ep_write_UDCCSR
===============

.. c:function:: void ep_write_UDCCSR(struct pxa_ep *ep, int mask)

    set bits in UDCCSR

    :param struct pxa_ep \*ep:
        *undescribed*

    :param int mask:
        bits to set in UDCCR

.. _`ep_write_udccsr.description`:

Description
-----------

Sets bits in UDCCSR (UDCCSR0 and UDCCSR\*).

A specific case is applied to ep0 : the ACM bit is always set to 1, for
SET_INTERFACE and SET_CONFIGURATION.

.. _`ep_count_bytes_remain`:

ep_count_bytes_remain
=====================

.. c:function:: int ep_count_bytes_remain(struct pxa_ep *ep)

    get how many bytes in udc endpoint

    :param struct pxa_ep \*ep:
        udc endpoint

.. _`ep_count_bytes_remain.description`:

Description
-----------

Returns number of bytes in OUT fifos. Broken for IN fifos (-EOPNOTSUPP)

.. _`ep_is_empty`:

ep_is_empty
===========

.. c:function:: int ep_is_empty(struct pxa_ep *ep)

    checks if ep has byte ready for reading

    :param struct pxa_ep \*ep:
        udc endpoint

.. _`ep_is_empty.description`:

Description
-----------

If endpoint is the control endpoint, checks if there are bytes in the
control endpoint fifo. If endpoint is a data endpoint, checks if bytes
are ready for reading on OUT endpoint.

Returns 0 if ep not empty, 1 if ep empty, -EOPNOTSUPP if IN endpoint

.. _`ep_is_full`:

ep_is_full
==========

.. c:function:: int ep_is_full(struct pxa_ep *ep)

    checks if ep has place to write bytes

    :param struct pxa_ep \*ep:
        udc endpoint

.. _`ep_is_full.description`:

Description
-----------

If endpoint is not the control endpoint and is an IN endpoint, checks if
there is place to write bytes into the endpoint.

Returns 0 if ep not full, 1 if ep full, -EOPNOTSUPP if OUT endpoint

.. _`epout_has_pkt`:

epout_has_pkt
=============

.. c:function:: int epout_has_pkt(struct pxa_ep *ep)

    checks if OUT endpoint fifo has a packet available

    :param struct pxa_ep \*ep:
        pxa endpoint

.. _`epout_has_pkt.description`:

Description
-----------

Returns 1 if a complete packet is available, 0 if not, -EOPNOTSUPP for IN ep.

.. _`set_ep0state`:

set_ep0state
============

.. c:function:: void set_ep0state(struct pxa_udc *udc, int state)

    Set ep0 automata state

    :param struct pxa_udc \*udc:
        *undescribed*

    :param int state:
        state

.. _`ep0_idle`:

ep0_idle
========

.. c:function:: void ep0_idle(struct pxa_udc *dev)

    Put control endpoint into idle state

    :param struct pxa_udc \*dev:
        udc device

.. _`inc_ep_stats_reqs`:

inc_ep_stats_reqs
=================

.. c:function:: void inc_ep_stats_reqs(struct pxa_ep *ep, int is_in)

    Update ep stats counts

    :param struct pxa_ep \*ep:
        physical endpoint

    :param int is_in:
        ep direction (USB_DIR_IN or 0)

.. _`inc_ep_stats_bytes`:

inc_ep_stats_bytes
==================

.. c:function:: void inc_ep_stats_bytes(struct pxa_ep *ep, int count, int is_in)

    Update ep stats counts

    :param struct pxa_ep \*ep:
        physical endpoint

    :param int count:
        bytes transferred on endpoint

    :param int is_in:
        ep direction (USB_DIR_IN or 0)

.. _`pxa_ep_setup`:

pxa_ep_setup
============

.. c:function:: void pxa_ep_setup(struct pxa_ep *ep)

    Sets up an usb physical endpoint

    :param struct pxa_ep \*ep:
        pxa27x physical endpoint

.. _`pxa_ep_setup.description`:

Description
-----------

Find the physical pxa27x ep, and setup its UDCCR

.. _`pxa_eps_setup`:

pxa_eps_setup
=============

.. c:function:: void pxa_eps_setup(struct pxa_udc *dev)

    Sets up all usb physical endpoints

    :param struct pxa_udc \*dev:
        udc device

.. _`pxa_eps_setup.description`:

Description
-----------

Setup all pxa physical endpoints, except ep0

.. _`pxa_ep_alloc_request`:

pxa_ep_alloc_request
====================

.. c:function:: struct usb_request *pxa_ep_alloc_request(struct usb_ep *_ep, gfp_t gfp_flags)

    Allocate usb request

    :param struct usb_ep \*_ep:
        usb endpoint

    :param gfp_t gfp_flags:
        *undescribed*

.. _`pxa_ep_alloc_request.description`:

Description
-----------

For the pxa27x, these can just wrap kmalloc/kfree.  gadget drivers
must still pass correctly initialized endpoints, since other controller
drivers may care about how it's currently set up (dma issues etc).

.. _`pxa_ep_free_request`:

pxa_ep_free_request
===================

.. c:function:: void pxa_ep_free_request(struct usb_ep *_ep, struct usb_request *_req)

    Free usb request

    :param struct usb_ep \*_ep:
        usb endpoint

    :param struct usb_request \*_req:
        usb request

.. _`pxa_ep_free_request.description`:

Description
-----------

Wrapper around kfree to free \_req

.. _`ep_add_request`:

ep_add_request
==============

.. c:function:: void ep_add_request(struct pxa_ep *ep, struct pxa27x_request *req)

    add a request to the endpoint's queue

    :param struct pxa_ep \*ep:
        usb endpoint

    :param struct pxa27x_request \*req:
        usb request

.. _`ep_add_request.context`:

Context
-------

ep->lock held

.. _`ep_add_request.description`:

Description
-----------

Queues the request in the endpoint's queue, and enables the interrupts
on the endpoint.

.. _`ep_del_request`:

ep_del_request
==============

.. c:function:: void ep_del_request(struct pxa_ep *ep, struct pxa27x_request *req)

    removes a request from the endpoint's queue

    :param struct pxa_ep \*ep:
        usb endpoint

    :param struct pxa27x_request \*req:
        usb request

.. _`ep_del_request.context`:

Context
-------

ep->lock held

.. _`ep_del_request.description`:

Description
-----------

Unqueue the request from the endpoint's queue. If there are no more requests
on the endpoint, and if it's not the control endpoint, interrupts are
disabled on the endpoint.

.. _`req_done`:

req_done
========

.. c:function:: void req_done(struct pxa_ep *ep, struct pxa27x_request *req, int status, unsigned long *pflags)

    Complete an usb request

    :param struct pxa_ep \*ep:
        pxa physical endpoint

    :param struct pxa27x_request \*req:
        pxa request

    :param int status:
        usb request status sent to gadget API

    :param unsigned long \*pflags:
        flags of previous \ :c:func:`spinlock_irq_save`\  or NULL if no lock held

.. _`req_done.context`:

Context
-------

ep->lock held if flags not NULL, else ep->lock released

.. _`req_done.description`:

Description
-----------

Retire a pxa27x usb request. Endpoint must be locked.

.. _`ep_end_out_req`:

ep_end_out_req
==============

.. c:function:: void ep_end_out_req(struct pxa_ep *ep, struct pxa27x_request *req, unsigned long *pflags)

    Ends endpoint OUT request

    :param struct pxa_ep \*ep:
        physical endpoint

    :param struct pxa27x_request \*req:
        pxa request

    :param unsigned long \*pflags:
        flags of previous \ :c:func:`spinlock_irq_save`\  or NULL if no lock held

.. _`ep_end_out_req.context`:

Context
-------

ep->lock held or released (see \ :c:func:`req_done`\ )

.. _`ep_end_out_req.description`:

Description
-----------

Ends endpoint OUT request (completes usb request).

.. _`ep0_end_out_req`:

ep0_end_out_req
===============

.. c:function:: void ep0_end_out_req(struct pxa_ep *ep, struct pxa27x_request *req, unsigned long *pflags)

    Ends control endpoint OUT request (ends data stage)

    :param struct pxa_ep \*ep:
        physical endpoint

    :param struct pxa27x_request \*req:
        pxa request

    :param unsigned long \*pflags:
        flags of previous \ :c:func:`spinlock_irq_save`\  or NULL if no lock held

.. _`ep0_end_out_req.context`:

Context
-------

ep->lock held or released (see \ :c:func:`req_done`\ )

.. _`ep0_end_out_req.description`:

Description
-----------

Ends control endpoint OUT request (completes usb request), and puts
control endpoint into idle state

.. _`ep_end_in_req`:

ep_end_in_req
=============

.. c:function:: void ep_end_in_req(struct pxa_ep *ep, struct pxa27x_request *req, unsigned long *pflags)

    Ends endpoint IN request

    :param struct pxa_ep \*ep:
        physical endpoint

    :param struct pxa27x_request \*req:
        pxa request

    :param unsigned long \*pflags:
        flags of previous \ :c:func:`spinlock_irq_save`\  or NULL if no lock held

.. _`ep_end_in_req.context`:

Context
-------

ep->lock held or released (see \ :c:func:`req_done`\ )

.. _`ep_end_in_req.description`:

Description
-----------

Ends endpoint IN request (completes usb request).

.. _`ep0_end_in_req`:

ep0_end_in_req
==============

.. c:function:: void ep0_end_in_req(struct pxa_ep *ep, struct pxa27x_request *req, unsigned long *pflags)

    Ends control endpoint IN request (ends data stage)

    :param struct pxa_ep \*ep:
        physical endpoint

    :param struct pxa27x_request \*req:
        pxa request

    :param unsigned long \*pflags:
        flags of previous \ :c:func:`spinlock_irq_save`\  or NULL if no lock held

.. _`ep0_end_in_req.context`:

Context
-------

ep->lock held or released (see \ :c:func:`req_done`\ )

.. _`ep0_end_in_req.description`:

Description
-----------

Ends control endpoint IN request (completes usb request), and puts
control endpoint into status state

.. _`nuke`:

nuke
====

.. c:function:: void nuke(struct pxa_ep *ep, int status)

    Dequeue all requests

    :param struct pxa_ep \*ep:
        pxa endpoint

    :param int status:
        usb request status

.. _`nuke.context`:

Context
-------

ep->lock released

.. _`nuke.description`:

Description
-----------

Dequeues all requests on an endpoint. As a side effect, interrupts will be
disabled on that endpoint (because no more requests).

.. _`read_packet`:

read_packet
===========

.. c:function:: int read_packet(struct pxa_ep *ep, struct pxa27x_request *req)

    transfer 1 packet from an OUT endpoint into request

    :param struct pxa_ep \*ep:
        pxa physical endpoint

    :param struct pxa27x_request \*req:
        usb request

.. _`read_packet.description`:

Description
-----------

Takes bytes from OUT endpoint and transfers them info the usb request.
If there is less space in request than bytes received in OUT endpoint,
bytes are left in the OUT endpoint.

Returns how many bytes were actually transferred

.. _`write_packet`:

write_packet
============

.. c:function:: int write_packet(struct pxa_ep *ep, struct pxa27x_request *req, unsigned int max)

    transfer 1 packet from request into an IN endpoint

    :param struct pxa_ep \*ep:
        pxa physical endpoint

    :param struct pxa27x_request \*req:
        usb request

    :param unsigned int max:
        max bytes that fit into endpoint

.. _`write_packet.description`:

Description
-----------

Takes bytes from usb request, and transfers them into the physical
endpoint. If there are no bytes to transfer, doesn't write anything
to physical endpoint.

Returns how many bytes were actually transferred.

.. _`read_fifo`:

read_fifo
=========

.. c:function:: int read_fifo(struct pxa_ep *ep, struct pxa27x_request *req)

    Transfer packets from OUT endpoint into usb request

    :param struct pxa_ep \*ep:
        pxa physical endpoint

    :param struct pxa27x_request \*req:
        usb request

.. _`read_fifo.context`:

Context
-------

callable when \ :c:func:`in_interrupt`\ 

.. _`read_fifo.description`:

Description
-----------

Unload as many packets as possible from the fifo we use for usb OUT
transfers and put them into the request. Caller should have made sure
there's at least one packet ready.
Doesn't complete the request, that's the caller's job

Returns 1 if the request completed, 0 otherwise

.. _`write_fifo`:

write_fifo
==========

.. c:function:: int write_fifo(struct pxa_ep *ep, struct pxa27x_request *req)

    transfer packets from usb request into an IN endpoint

    :param struct pxa_ep \*ep:
        pxa physical endpoint

    :param struct pxa27x_request \*req:
        pxa usb request

.. _`write_fifo.description`:

Description
-----------

Write to an IN endpoint fifo, as many packets as possible.
irqs will use this to write the rest later.
caller guarantees at least one packet buffer is ready (or a zlp).
Doesn't complete the request, that's the caller's job

Returns 1 if request fully transferred, 0 if partial transfer

.. _`read_ep0_fifo`:

read_ep0_fifo
=============

.. c:function:: int read_ep0_fifo(struct pxa_ep *ep, struct pxa27x_request *req)

    Transfer packets from control endpoint into usb request

    :param struct pxa_ep \*ep:
        control endpoint

    :param struct pxa27x_request \*req:
        pxa usb request

.. _`read_ep0_fifo.description`:

Description
-----------

Special ep0 version of the above read_fifo. Reads as many bytes from control
endpoint as can be read, and stores them into usb request (limited by request
maximum length).

Returns 0 if usb request only partially filled, 1 if fully filled

.. _`write_ep0_fifo`:

write_ep0_fifo
==============

.. c:function:: int write_ep0_fifo(struct pxa_ep *ep, struct pxa27x_request *req)

    Send a request to control endpoint (ep0 in)

    :param struct pxa_ep \*ep:
        control endpoint

    :param struct pxa27x_request \*req:
        request

.. _`write_ep0_fifo.context`:

Context
-------

callable when \ :c:func:`in_interrupt`\ 

.. _`write_ep0_fifo.description`:

Description
-----------

Sends a request (or a part of the request) to the control endpoint (ep0 in).
If the request doesn't fit, the remaining part will be sent from irq.
The request is considered fully written only if either :
- last write transferred all remaining bytes, but fifo was not fully filled
- last write was a 0 length write

Returns 1 if request fully written, 0 if request only partially sent

.. _`pxa_ep_queue`:

pxa_ep_queue
============

.. c:function:: int pxa_ep_queue(struct usb_ep *_ep, struct usb_request *_req, gfp_t gfp_flags)

    Queue a request into an IN endpoint

    :param struct usb_ep \*_ep:
        usb endpoint

    :param struct usb_request \*_req:
        usb request

    :param gfp_t gfp_flags:
        flags

.. _`pxa_ep_queue.context`:

Context
-------

normally called when !in_interrupt, but callable when \ :c:func:`in_interrupt`\ 
in the special case of ep0 setup :
(irq->handle_ep0_ctrl_req->gadget_setup->pxa_ep_queue)

.. _`pxa_ep_queue.description`:

Description
-----------

Returns 0 if succedeed, error otherwise

.. _`pxa_ep_dequeue`:

pxa_ep_dequeue
==============

.. c:function:: int pxa_ep_dequeue(struct usb_ep *_ep, struct usb_request *_req)

    Dequeue one request

    :param struct usb_ep \*_ep:
        usb endpoint

    :param struct usb_request \*_req:
        usb request

.. _`pxa_ep_dequeue.description`:

Description
-----------

Return 0 if no error, -EINVAL or -ECONNRESET otherwise

.. _`pxa_ep_set_halt`:

pxa_ep_set_halt
===============

.. c:function:: int pxa_ep_set_halt(struct usb_ep *_ep, int value)

    Halts operations on one endpoint

    :param struct usb_ep \*_ep:
        usb endpoint

    :param int value:
        *undescribed*

.. _`pxa_ep_set_halt.description`:

Description
-----------

Returns 0 if no error, -EINVAL, -EROFS, -EAGAIN otherwise

.. _`pxa_ep_fifo_status`:

pxa_ep_fifo_status
==================

.. c:function:: int pxa_ep_fifo_status(struct usb_ep *_ep)

    Get how many bytes in physical endpoint

    :param struct usb_ep \*_ep:
        usb endpoint

.. _`pxa_ep_fifo_status.description`:

Description
-----------

Returns number of bytes in OUT fifos. Broken for IN fifos.

.. _`pxa_ep_fifo_flush`:

pxa_ep_fifo_flush
=================

.. c:function:: void pxa_ep_fifo_flush(struct usb_ep *_ep)

    Flushes one endpoint

    :param struct usb_ep \*_ep:
        usb endpoint

.. _`pxa_ep_fifo_flush.description`:

Description
-----------

Discards all data in one endpoint(IN or OUT), except control endpoint.

.. _`pxa_ep_enable`:

pxa_ep_enable
=============

.. c:function:: int pxa_ep_enable(struct usb_ep *_ep, const struct usb_endpoint_descriptor *desc)

    Enables usb endpoint

    :param struct usb_ep \*_ep:
        usb endpoint

    :param const struct usb_endpoint_descriptor \*desc:
        usb endpoint descriptor

.. _`pxa_ep_enable.description`:

Description
-----------

Nothing much to do here, as ep configuration is done once and for all
before udc is enabled. After udc enable, no physical endpoint configuration
can be changed.
Function makes sanity checks and flushes the endpoint.

.. _`pxa_ep_disable`:

pxa_ep_disable
==============

.. c:function:: int pxa_ep_disable(struct usb_ep *_ep)

    Disable usb endpoint

    :param struct usb_ep \*_ep:
        usb endpoint

.. _`pxa_ep_disable.description`:

Description
-----------

Same as for pxa_ep_enable, no physical endpoint configuration can be
changed.
Function flushes the endpoint and related requests.

.. _`dplus_pullup`:

dplus_pullup
============

.. c:function:: void dplus_pullup(struct pxa_udc *udc, int on)

    Connect or disconnect pullup resistor to D+ pin

    :param struct pxa_udc \*udc:
        udc device

    :param int on:
        0 if disconnect pullup resistor, 1 otherwise

.. _`dplus_pullup.context`:

Context
-------

any

.. _`dplus_pullup.description`:

Description
-----------

Handle D+ pullup resistor, make the device visible to the usb bus, and
declare it as a full speed usb device

.. _`pxa_udc_get_frame`:

pxa_udc_get_frame
=================

.. c:function:: int pxa_udc_get_frame(struct usb_gadget *_gadget)

    Returns usb frame number

    :param struct usb_gadget \*_gadget:
        usb gadget

.. _`pxa_udc_wakeup`:

pxa_udc_wakeup
==============

.. c:function:: int pxa_udc_wakeup(struct usb_gadget *_gadget)

    Force udc device out of suspend

    :param struct usb_gadget \*_gadget:
        usb gadget

.. _`pxa_udc_wakeup.description`:

Description
-----------

Returns 0 if successful, error code otherwise

.. _`should_enable_udc`:

should_enable_udc
=================

.. c:function:: int should_enable_udc(struct pxa_udc *udc)

    Tells if UDC should be enabled

    :param struct pxa_udc \*udc:
        udc device

.. _`should_enable_udc.context`:

Context
-------

any

.. _`should_enable_udc.description`:

Description
-----------

The UDC should be enabled if :
- the pullup resistor is connected
- and a gadget driver is bound
- and vbus is sensed (or no vbus sense is available)

Returns 1 if UDC should be enabled, 0 otherwise

.. _`should_disable_udc`:

should_disable_udc
==================

.. c:function:: int should_disable_udc(struct pxa_udc *udc)

    Tells if UDC should be disabled

    :param struct pxa_udc \*udc:
        udc device

.. _`should_disable_udc.context`:

Context
-------

any

.. _`should_disable_udc.description`:

Description
-----------

The UDC should be disabled if :
- the pullup resistor is not connected
- or no gadget driver is bound
- or no vbus is sensed (when vbus sesing is available)

Returns 1 if UDC should be disabled

.. _`pxa_udc_pullup`:

pxa_udc_pullup
==============

.. c:function:: int pxa_udc_pullup(struct usb_gadget *_gadget, int is_active)

    Offer manual D+ pullup control

    :param struct usb_gadget \*_gadget:
        usb gadget using the control

    :param int is_active:
        0 if disconnect, else connect D+ pullup resistor

.. _`pxa_udc_pullup.context`:

Context
-------

!in_interrupt()

.. _`pxa_udc_pullup.description`:

Description
-----------

Returns 0 if OK, -EOPNOTSUPP if udc driver doesn't handle D+ pullup

.. _`pxa_udc_vbus_session`:

pxa_udc_vbus_session
====================

.. c:function:: int pxa_udc_vbus_session(struct usb_gadget *_gadget, int is_active)

    Called by external transceiver to enable/disable udc

    :param struct usb_gadget \*_gadget:
        usb gadget

    :param int is_active:
        0 if should disable the udc, 1 if should enable

.. _`pxa_udc_vbus_session.description`:

Description
-----------

Enables the udc, and optionnaly activates D+ pullup resistor. Or disables the
udc, and deactivates D+ pullup resistor.

Returns 0

.. _`pxa_udc_vbus_draw`:

pxa_udc_vbus_draw
=================

.. c:function:: int pxa_udc_vbus_draw(struct usb_gadget *_gadget, unsigned mA)

    Called by gadget driver after SET_CONFIGURATION completed

    :param struct usb_gadget \*_gadget:
        usb gadget

    :param unsigned mA:
        current drawn

.. _`pxa_udc_vbus_draw.context`:

Context
-------

!in_interrupt()

.. _`pxa_udc_vbus_draw.description`:

Description
-----------

Called after a configuration was chosen by a USB host, to inform how much
current can be drawn by the device from VBus line.

Returns 0 or -EOPNOTSUPP if no transceiver is handling the udc

.. _`pxa_udc_phy_event`:

pxa_udc_phy_event
=================

.. c:function:: int pxa_udc_phy_event(struct notifier_block *nb, unsigned long action, void *data)

    Called by phy upon VBus event

    :param struct notifier_block \*nb:
        notifier block

    :param unsigned long action:
        phy action, is vbus connect or disconnect

    :param void \*data:
        the usb_gadget structure in pxa_udc

.. _`pxa_udc_phy_event.description`:

Description
-----------

Called by the USB Phy when a cable connect or disconnect is sensed.

Returns 0

.. _`udc_disable`:

udc_disable
===========

.. c:function:: void udc_disable(struct pxa_udc *udc)

    disable udc device controller

    :param struct pxa_udc \*udc:
        udc device

.. _`udc_disable.context`:

Context
-------

any

.. _`udc_disable.description`:

Description
-----------

Disables the udc device : disables clocks, udc interrupts, control endpoint
interrupts.

.. _`udc_init_data`:

udc_init_data
=============

.. c:function:: void udc_init_data(struct pxa_udc *dev)

    Initialize udc device data structures

    :param struct pxa_udc \*dev:
        udc device

.. _`udc_init_data.description`:

Description
-----------

Initializes gadget endpoint list, endpoints locks. No action is taken
on the hardware.

.. _`udc_enable`:

udc_enable
==========

.. c:function:: void udc_enable(struct pxa_udc *udc)

    Enables the udc device

    :param struct pxa_udc \*udc:
        *undescribed*

.. _`udc_enable.description`:

Description
-----------

Enables the udc device : enables clocks, udc interrupts, control endpoint
interrupts, sets usb as UDC client and setups endpoints.

.. _`pxa27x_udc_start`:

pxa27x_udc_start
================

.. c:function:: int pxa27x_udc_start(struct usb_gadget *g, struct usb_gadget_driver *driver)

    Register gadget driver

    :param struct usb_gadget \*g:
        *undescribed*

    :param struct usb_gadget_driver \*driver:
        gadget driver

.. _`pxa27x_udc_start.description`:

Description
-----------

When a driver is successfully registered, it will receive control requests
including \ :c:func:`set_configuration`\ , which enables non-control requests.  Then
usb traffic follows until a disconnect is reported.  Then a host may connect
again, or the driver might get unbound.

Note that the udc is not automatically enabled. Check function
\ :c:func:`should_enable_udc`\ .

Returns 0 if no error, -EINVAL, -ENODEV, -EBUSY otherwise

.. _`stop_activity`:

stop_activity
=============

.. c:function:: void stop_activity(struct pxa_udc *udc)

    Stops udc endpoints

    :param struct pxa_udc \*udc:
        udc device

.. _`stop_activity.description`:

Description
-----------

Disables all udc endpoints (even control endpoint), report disconnect to
the gadget user.

.. _`pxa27x_udc_stop`:

pxa27x_udc_stop
===============

.. c:function:: int pxa27x_udc_stop(struct usb_gadget *g)

    Unregister the gadget driver

    :param struct usb_gadget \*g:
        *undescribed*

.. _`pxa27x_udc_stop.description`:

Description
-----------

Returns 0 if no error, -ENODEV, -EINVAL otherwise

.. _`handle_ep0_ctrl_req`:

handle_ep0_ctrl_req
===================

.. c:function:: void handle_ep0_ctrl_req(struct pxa_udc *udc, struct pxa27x_request *req)

    handle control endpoint control request

    :param struct pxa_udc \*udc:
        udc device

    :param struct pxa27x_request \*req:
        control request

.. _`handle_ep0`:

handle_ep0
==========

.. c:function:: void handle_ep0(struct pxa_udc *udc, int fifo_irq, int opc_irq)

    Handle control endpoint data transfers

    :param struct pxa_udc \*udc:
        udc device

    :param int fifo_irq:
        1 if triggered by fifo service type irq

    :param int opc_irq:
        1 if triggered by output packet complete type irq

.. _`handle_ep0.description`:

Description
-----------

Context : when \ :c:func:`in_interrupt`\  or with ep->lock held

Tries to transfer all pending request data into the endpoint and/or
transfer all pending data in the endpoint into usb requests.
Handles states of ep0 automata.

PXA27x hardware handles several standard usb control requests without
driver notification.  The requests fully handled by hardware are :
SET_ADDRESS, SET_FEATURE, CLEAR_FEATURE, GET_CONFIGURATION, GET_INTERFACE,
GET_STATUS
The requests handled by hardware, but with irq notification are :
SYNCH_FRAME, SET_CONFIGURATION, SET_INTERFACE
The remaining standard requests really handled by handle_ep0 are :
GET_DESCRIPTOR, SET_DESCRIPTOR, specific requests.
Requests standardized outside of USB 2.0 chapter 9 are handled more
uniformly, by gadget drivers.

The control endpoint state machine is \_not\_ USB spec compliant, it's even
hardly compliant with Intel PXA270 developers guide.
The key points which inferred this state machine are :
- on every setup token, bit UDCCSR0_SA is raised and held until cleared by
software.
- on every OUT packet received, UDCCSR0_OPC is raised and held until
cleared by software.
- clearing UDCCSR0_OPC always flushes ep0. If in setup stage, never do it
before reading ep0.
This is true only for PXA27x. This is not true anymore for PXA3xx family
(check Back-to-Back setup packet in developers guide).
- irq can be called on a "packet complete" event (opc_irq=1), while
UDCCSR0_OPC is not yet raised (delta can be as big as 100ms
from experimentation).
- as UDCCSR0_SA can be activated while in irq handling, and clearing
UDCCSR0_OPC would flush the setup data, we almost never clear UDCCSR0_OPC
=> we never actually read the "status stage" packet of an IN data stage
=> this is not documented in Intel documentation
- hardware as no idea of STATUS STAGE, it only handle SETUP STAGE and DATA
STAGE. The driver add STATUS STAGE to send last zero length packet in
OUT_STATUS_STAGE.
- special attention was needed for IN_STATUS_STAGE. If a packet complete
event is detected, we terminate the status stage without ackowledging the
packet (not to risk to loose a potential SETUP packet)

.. _`handle_ep`:

handle_ep
=========

.. c:function:: void handle_ep(struct pxa_ep *ep)

    Handle endpoint data tranfers

    :param struct pxa_ep \*ep:
        pxa physical endpoint

.. _`handle_ep.description`:

Description
-----------

Tries to transfer all pending request data into the endpoint and/or
transfer all pending data in the endpoint into usb requests.

Is always called when \ :c:func:`in_interrupt`\  and with ep->lock released.

.. _`pxa27x_change_configuration`:

pxa27x_change_configuration
===========================

.. c:function:: void pxa27x_change_configuration(struct pxa_udc *udc, int config)

    Handle SET_CONF usb request notification

    :param struct pxa_udc \*udc:
        udc device

    :param int config:
        usb configuration

.. _`pxa27x_change_configuration.description`:

Description
-----------

Post the request to upper level.
Don't use any pxa specific harware configuration capabilities

.. _`pxa27x_change_interface`:

pxa27x_change_interface
=======================

.. c:function:: void pxa27x_change_interface(struct pxa_udc *udc, int iface, int alt)

    Handle SET_INTERF usb request notification

    :param struct pxa_udc \*udc:
        udc device

    :param int iface:
        interface number

    :param int alt:
        alternate setting number

.. _`pxa27x_change_interface.description`:

Description
-----------

Post the request to upper level.
Don't use any pxa specific harware configuration capabilities

.. _`irq_udc_suspend`:

irq_udc_suspend
===============

.. c:function:: void irq_udc_suspend(struct pxa_udc *udc)

    Handle IRQ "UDC Suspend"

    :param struct pxa_udc \*udc:
        udc device

.. _`irq_udc_resume`:

irq_udc_resume
==============

.. c:function:: void irq_udc_resume(struct pxa_udc *udc)

    Handle IRQ "UDC Resume"

    :param struct pxa_udc \*udc:
        udc device

.. _`irq_udc_reconfig`:

irq_udc_reconfig
================

.. c:function:: void irq_udc_reconfig(struct pxa_udc *udc)

    Handle IRQ "UDC Change Configuration"

    :param struct pxa_udc \*udc:
        udc device

.. _`irq_udc_reset`:

irq_udc_reset
=============

.. c:function:: void irq_udc_reset(struct pxa_udc *udc)

    Handle IRQ "UDC Reset"

    :param struct pxa_udc \*udc:
        udc device

.. _`pxa_udc_irq`:

pxa_udc_irq
===========

.. c:function:: irqreturn_t pxa_udc_irq(int irq, void *_dev)

    Main irq handler

    :param int irq:
        irq number

    :param void \*_dev:
        udc device

.. _`pxa_udc_irq.description`:

Description
-----------

Handles all udc interrupts

.. _`pxa_udc_probe`:

pxa_udc_probe
=============

.. c:function:: int pxa_udc_probe(struct platform_device *pdev)

    probes the udc device

    :param struct platform_device \*pdev:
        *undescribed*

.. _`pxa_udc_probe.description`:

Description
-----------

Perform basic init : allocates udc clock, creates sysfs files, requests
irq.

.. _`pxa_udc_remove`:

pxa_udc_remove
==============

.. c:function:: int pxa_udc_remove(struct platform_device *_dev)

    removes the udc device driver

    :param struct platform_device \*_dev:
        platform device

.. _`pxa_udc_suspend`:

pxa_udc_suspend
===============

.. c:function:: int pxa_udc_suspend(struct platform_device *_dev, pm_message_t state)

    Suspend udc device

    :param struct platform_device \*_dev:
        platform device

    :param pm_message_t state:
        suspend state

.. _`pxa_udc_suspend.description`:

Description
-----------

Suspends udc : saves configuration registers (UDCCR\*), then disables the udc
device.

.. _`pxa_udc_resume`:

pxa_udc_resume
==============

.. c:function:: int pxa_udc_resume(struct platform_device *_dev)

    Resume udc device

    :param struct platform_device \*_dev:
        platform device

.. _`pxa_udc_resume.description`:

Description
-----------

Resumes udc : restores configuration registers (UDCCR\*), then enables the udc
device.

.. This file was automatic generated / don't edit.

