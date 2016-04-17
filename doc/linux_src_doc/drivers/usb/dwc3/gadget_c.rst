.. -*- coding: utf-8; mode: rst -*-

========
gadget.c
========


.. _`dwc3_gadget_set_test_mode`:

dwc3_gadget_set_test_mode
=========================

.. c:function:: int dwc3_gadget_set_test_mode (struct dwc3 *dwc, int mode)

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

Felipe Balbi <balbi\ ``ti``\ .com>,
Sebastian Andrzej Siewior <bigeasy\ ``linutronix``\ .de>



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

.. c:function:: int dwc3_gadget_get_link_state (struct dwc3 *dwc)

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

.. c:function:: int dwc3_gadget_set_link_state (struct dwc3 *dwc, enum dwc3_link_state state)

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



.. _`dwc3_gadget_resize_tx_fifos`:

dwc3_gadget_resize_tx_fifos
===========================

.. c:function:: int dwc3_gadget_resize_tx_fifos (struct dwc3 *dwc)

    reallocate fifo spaces for current use-case

    :param struct dwc3 \*dwc:
        pointer to our context structure



.. _`dwc3_gadget_resize_tx_fifos.description`:

Description
-----------

This function will a best effort FIFO allocation in order
to improve FIFO usage and throughput, while still allowing
us to enable as many endpoints as possible.

Keep in mind that this operation will be highly dependent
on the configured size for RAM1 - which contains TxFifo -,
the amount of endpoints enabled on coreConsultant tool, and
the width of the Master Bus.

In the ideal world, we would always be able to satisfy the



.. _`dwc3_gadget_resize_tx_fifos.following-equation`:

following equation
------------------


((512 + 2 * MDWIDTH-Bytes) + (Number of IN Endpoints - 1) *  * (3 * (1024 + MDWIDTH-Bytes) + MDWIDTH-Bytes)) / MDWIDTH-Bytes

Unfortunately, due to many variables that's not always the case.



.. _`dwc3_gadget_start_config`:

dwc3_gadget_start_config
========================

.. c:function:: int dwc3_gadget_start_config (struct dwc3 *dwc, struct dwc3_ep *dep)

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

.. c:function:: int __dwc3_gadget_ep_enable (struct dwc3_ep *dep, const struct usb_endpoint_descriptor *desc, const struct usb_ss_ep_comp_descriptor *comp_desc, bool ignore, bool restore)

    Initializes a HW endpoint

    :param struct dwc3_ep \*dep:
        endpoint to be initialized

    :param const struct usb_endpoint_descriptor \*desc:
        USB Endpoint Descriptor

    :param const struct usb_ss_ep_comp_descriptor \*comp_desc:

        *undescribed*

    :param bool ignore:

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

.. c:function:: int __dwc3_gadget_ep_disable (struct dwc3_ep *dep)

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

.. c:function:: void dwc3_prepare_one_trb (struct dwc3_ep *dep, struct dwc3_request *req, dma_addr_t dma, unsigned length, unsigned last, unsigned chain, unsigned node)

    setup one TRB from one request

    :param struct dwc3_ep \*dep:
        endpoint for which this request is prepared

    :param struct dwc3_request \*req:
        dwc3_request pointer

    :param dma_addr_t dma:

        *undescribed*

    :param unsigned length:

        *undescribed*

    :param unsigned last:

        *undescribed*

    :param unsigned chain:

        *undescribed*

    :param unsigned node:

        *undescribed*



.. _`dwc3_gadget_init`:

dwc3_gadget_init
================

.. c:function:: int dwc3_gadget_init (struct dwc3 *dwc)

    Initializes gadget related registers

    :param struct dwc3 \*dwc:
        pointer to our controller context structure



.. _`dwc3_gadget_init.description`:

Description
-----------

Returns 0 on success otherwise negative errno.

