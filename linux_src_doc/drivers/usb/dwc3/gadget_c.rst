.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/gadget.c

.. _`dwc3_gadget_set_test_mode`:

dwc3_gadget_set_test_mode
=========================

.. c:function:: int dwc3_gadget_set_test_mode(struct dwc3 *dwc, int mode)

    DesignWare USB3 DRD Controller Gadget Framework Link

    :param struct dwc3 \*dwc:
        *undescribed*

    :param int mode:
        *undescribed*

.. _`dwc3_gadget_set_test_mode.description`:

Description
-----------

Copyright (C) 2010-2011 Texas Instruments Incorporated - http://www.ti.com

.. _`dwc3_gadget_set_test_mode.authors`:

Authors
-------

Felipe Balbi <balbi@ti.com>,
Sebastian Andrzej Siewior <bigeasy@linutronix.de>

.. _`dwc3_gadget_set_test_mode.this-program-is-free-software`:

This program is free software
-----------------------------

you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2  of
the License as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

.. _`dwc3_gadget_get_link_state`:

dwc3_gadget_get_link_state
==========================

.. c:function:: int dwc3_gadget_get_link_state(struct dwc3 *dwc)

    Gets current state of USB Link

    :param struct dwc3 \*dwc:
        pointer to our context structure

.. _`dwc3_gadget_get_link_state.description`:

Description
-----------

Caller should take care of locking. This function will
return the link state on success (>= 0) or -ETIMEDOUT.

.. _`dwc3_gadget_set_link_state`:

dwc3_gadget_set_link_state
==========================

.. c:function:: int dwc3_gadget_set_link_state(struct dwc3 *dwc, enum dwc3_link_state state)

    Sets USB Link to a particular State

    :param struct dwc3 \*dwc:
        pointer to our context structure

    :param enum dwc3_link_state state:
        the state to put link into

.. _`dwc3_gadget_set_link_state.description`:

Description
-----------

Caller should take care of locking. This function will
return 0 on success or -ETIMEDOUT.

.. _`dwc3_ep_inc_trb`:

dwc3_ep_inc_trb
===============

.. c:function:: void dwc3_ep_inc_trb(u8 *index)

    Increment a TRB index. \ ``index``\  - Pointer to the TRB index to increment.

    :param u8 \*index:
        *undescribed*

.. _`dwc3_ep_inc_trb.description`:

Description
-----------

The index should never point to the link TRB. After incrementing,
if it is point to the link TRB, wrap around to the beginning. The
link TRB is always at the last TRB entry.

.. _`dwc3_gadget_start_config`:

dwc3_gadget_start_config
========================

.. c:function:: int dwc3_gadget_start_config(struct dwc3 *dwc, struct dwc3_ep *dep)

    Configure EP resources

    :param struct dwc3 \*dwc:
        pointer to our controller context structure

    :param struct dwc3_ep \*dep:
        endpoint that is being enabled

.. _`dwc3_gadget_start_config.description`:

Description
-----------

The assignment of transfer resources cannot perfectly follow the
data book due to the fact that the controller driver does not have
all knowledge of the configuration in advance. It is given this
information piecemeal by the composite gadget framework after every
SET_CONFIGURATION and SET_INTERFACE. Trying to follow the databook
programming model in this scenario can cause errors. For two

.. _`dwc3_gadget_start_config.reasons`:

reasons
-------


1) The databook says to do DEPSTARTCFG for every SET_CONFIGURATION
and SET_INTERFACE (8.1.5). This is incorrect in the scenario of
multiple interfaces.

2) The databook does not mention doing more DEPXFERCFG for new
endpoint on alt setting (8.1.6).

.. _`dwc3_gadget_start_config.the-following-simplified-method-is-used-instead`:

The following simplified method is used instead
-----------------------------------------------


All hardware endpoints can be assigned a transfer resource and this
setting will stay persistent until either a core reset or
hibernation. So whenever we do a DEPSTARTCFG(0) we can go ahead and
do DEPXFERCFG for every hardware endpoint as well. We are
guaranteed that there are as many transfer resources as endpoints.

This function is called for each endpoint when it is being enabled
but is triggered only when called for EP0-out, which always happens
first, and which should only happen in one of the above conditions.

.. _`__dwc3_gadget_ep_enable`:

__dwc3_gadget_ep_enable
=======================

.. c:function:: int __dwc3_gadget_ep_enable(struct dwc3_ep *dep, const struct usb_endpoint_descriptor *desc, const struct usb_ss_ep_comp_descriptor *comp_desc, bool modify, bool restore)

    Initializes a HW endpoint

    :param struct dwc3_ep \*dep:
        endpoint to be initialized

    :param const struct usb_endpoint_descriptor \*desc:
        USB Endpoint Descriptor

    :param const struct usb_ss_ep_comp_descriptor \*comp_desc:
        *undescribed*

    :param bool modify:
        *undescribed*

    :param bool restore:
        *undescribed*

.. _`__dwc3_gadget_ep_enable.description`:

Description
-----------

Caller should take care of locking

.. _`__dwc3_gadget_ep_disable`:

__dwc3_gadget_ep_disable
========================

.. c:function:: int __dwc3_gadget_ep_disable(struct dwc3_ep *dep)

    Disables a HW endpoint

    :param struct dwc3_ep \*dep:
        the endpoint to disable

.. _`__dwc3_gadget_ep_disable.description`:

Description
-----------

This function also removes requests which are currently processed ny the
hardware and those which are not yet scheduled.
Caller should take care of locking.

.. _`dwc3_prepare_one_trb`:

dwc3_prepare_one_trb
====================

.. c:function:: void dwc3_prepare_one_trb(struct dwc3_ep *dep, struct dwc3_request *req, dma_addr_t dma, unsigned length, unsigned chain, unsigned node)

    setup one TRB from one request

    :param struct dwc3_ep \*dep:
        endpoint for which this request is prepared

    :param struct dwc3_request \*req:
        dwc3_request pointer

    :param dma_addr_t dma:
        *undescribed*

    :param unsigned length:
        *undescribed*

    :param unsigned chain:
        *undescribed*

    :param unsigned node:
        *undescribed*

.. _`dwc3_ep_prev_trb`:

dwc3_ep_prev_trb
================

.. c:function:: struct dwc3_trb *dwc3_ep_prev_trb(struct dwc3_ep *dep, u8 index)

    Returns the previous TRB in the ring

    :param struct dwc3_ep \*dep:
        The endpoint with the TRB ring

    :param u8 index:
        The index of the current TRB in the ring

.. _`dwc3_ep_prev_trb.description`:

Description
-----------

Returns the TRB prior to the one pointed to by the index. If the
index is 0, we will wrap backwards, skip the link TRB, and return
the one just before that.

.. _`dwc3_gadget_setup_nump`:

dwc3_gadget_setup_nump
======================

.. c:function:: void dwc3_gadget_setup_nump(struct dwc3 *dwc)

    Calculate and initialize NUMP field of DCFG

    :param struct dwc3 \*dwc:
        *undescribed*

.. _`dwc3_gadget_setup_nump.dwc`:

dwc
---

pointer to our context structure

The following looks like complex but it's actually very simple. In order to
calculate the number of packets we can burst at once on OUT transfers, we're
gonna use RxFIFO size.

.. _`dwc3_gadget_setup_nump.to-calculate-rxfifo-size-we-need-two-numbers`:

To calculate RxFIFO size we need two numbers
--------------------------------------------

MDWIDTH = size, in bits, of the internal memory bus
RAM2_DEPTH = depth, in MDWIDTH, of internal RAM2 (where RxFIFO sits)

Given these two numbers, the formula is simple:

RxFIFO Size = (RAM2_DEPTH \* MDWIDTH / 8) - 24 - 16;

24 bytes is for 3x SETUP packets
16 bytes is a clock domain crossing tolerance

Given RxFIFO Size, NUMP = RxFIFOSize / 1024;

.. _`dwc3_gadget_init`:

dwc3_gadget_init
================

.. c:function:: int dwc3_gadget_init(struct dwc3 *dwc)

    Initializes gadget related registers

    :param struct dwc3 \*dwc:
        pointer to our controller context structure

.. _`dwc3_gadget_init.description`:

Description
-----------

Returns 0 on success otherwise negative errno.

.. This file was automatic generated / don't edit.

