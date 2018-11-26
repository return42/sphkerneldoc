.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/gadget.c

.. _`dwc3_gadget_set_test_mode`:

dwc3_gadget_set_test_mode
=========================

.. c:function:: int dwc3_gadget_set_test_mode(struct dwc3 *dwc, int mode)

    enables usb2 test modes

    :param dwc:
        pointer to our context structure
    :type dwc: struct dwc3 \*

    :param mode:
        the mode to set (J, K SE0 NAK, Force Enable)
    :type mode: int

.. _`dwc3_gadget_set_test_mode.description`:

Description
-----------

Caller should take care of locking. This function will return 0 on
success or -EINVAL if wrong Test Selector is passed.

.. _`dwc3_gadget_get_link_state`:

dwc3_gadget_get_link_state
==========================

.. c:function:: int dwc3_gadget_get_link_state(struct dwc3 *dwc)

    gets current state of usb link

    :param dwc:
        pointer to our context structure
    :type dwc: struct dwc3 \*

.. _`dwc3_gadget_get_link_state.description`:

Description
-----------

Caller should take care of locking. This function will
return the link state on success (>= 0) or -ETIMEDOUT.

.. _`dwc3_gadget_set_link_state`:

dwc3_gadget_set_link_state
==========================

.. c:function:: int dwc3_gadget_set_link_state(struct dwc3 *dwc, enum dwc3_link_state state)

    sets usb link to a particular state

    :param dwc:
        pointer to our context structure
    :type dwc: struct dwc3 \*

    :param state:
        the state to put link into
    :type state: enum dwc3_link_state

.. _`dwc3_gadget_set_link_state.description`:

Description
-----------

Caller should take care of locking. This function will
return 0 on success or -ETIMEDOUT.

.. _`dwc3_ep_inc_trb`:

dwc3_ep_inc_trb
===============

.. c:function:: void dwc3_ep_inc_trb(u8 *index)

    increment a trb index.

    :param index:
        Pointer to the TRB index to increment.
    :type index: u8 \*

.. _`dwc3_ep_inc_trb.description`:

Description
-----------

The index should never point to the link TRB. After incrementing,
if it is point to the link TRB, wrap around to the beginning. The
link TRB is always at the last TRB entry.

.. _`dwc3_ep_inc_enq`:

dwc3_ep_inc_enq
===============

.. c:function:: void dwc3_ep_inc_enq(struct dwc3_ep *dep)

    increment endpoint's enqueue pointer

    :param dep:
        The endpoint whose enqueue pointer we're incrementing
    :type dep: struct dwc3_ep \*

.. _`dwc3_ep_inc_deq`:

dwc3_ep_inc_deq
===============

.. c:function:: void dwc3_ep_inc_deq(struct dwc3_ep *dep)

    increment endpoint's dequeue pointer

    :param dep:
        The endpoint whose enqueue pointer we're incrementing
    :type dep: struct dwc3_ep \*

.. _`dwc3_gadget_giveback`:

dwc3_gadget_giveback
====================

.. c:function:: void dwc3_gadget_giveback(struct dwc3_ep *dep, struct dwc3_request *req, int status)

    call struct usb_request's ->complete callback

    :param dep:
        The endpoint to whom the request belongs to
    :type dep: struct dwc3_ep \*

    :param req:
        The request we're giving back
    :type req: struct dwc3_request \*

    :param status:
        completion code for the request
    :type status: int

.. _`dwc3_gadget_giveback.description`:

Description
-----------

Must be called with controller's lock held and interrupts disabled. This
function will unmap \ ``req``\  and call its ->complete() callback to notify upper
layers that it has completed.

.. _`dwc3_send_gadget_generic_command`:

dwc3_send_gadget_generic_command
================================

.. c:function:: int dwc3_send_gadget_generic_command(struct dwc3 *dwc, unsigned cmd, u32 param)

    issue a generic command for the controller

    :param dwc:
        pointer to the controller context
    :type dwc: struct dwc3 \*

    :param cmd:
        the command to be issued
    :type cmd: unsigned

    :param param:
        command parameter
    :type param: u32

.. _`dwc3_send_gadget_generic_command.description`:

Description
-----------

Caller should take care of locking. Issue \ ``cmd``\  with a given \ ``param``\  to \ ``dwc``\ 
and wait for its completion.

.. _`dwc3_send_gadget_ep_cmd`:

dwc3_send_gadget_ep_cmd
=======================

.. c:function:: int dwc3_send_gadget_ep_cmd(struct dwc3_ep *dep, unsigned cmd, struct dwc3_gadget_ep_cmd_params *params)

    issue an endpoint command

    :param dep:
        the endpoint to which the command is going to be issued
    :type dep: struct dwc3_ep \*

    :param cmd:
        the command to be issued
    :type cmd: unsigned

    :param params:
        parameters to the command
    :type params: struct dwc3_gadget_ep_cmd_params \*

.. _`dwc3_send_gadget_ep_cmd.description`:

Description
-----------

Caller should handle locking. This function will issue \ ``cmd``\  with given
\ ``params``\  to \ ``dep``\  and wait for its completion.

.. _`dwc3_gadget_start_config`:

dwc3_gadget_start_config
========================

.. c:function:: int dwc3_gadget_start_config(struct dwc3_ep *dep)

    configure ep resources

    :param dep:
        endpoint that is being enabled
    :type dep: struct dwc3_ep \*

.. _`dwc3_gadget_start_config.description`:

Description
-----------

Issue a \ ``DWC3_DEPCMD_DEPSTARTCFG``\  command to \ ``dep``\ . After the command's
completion, it will set Transfer Resource for all available endpoints.

The assignment of transfer resources cannot perfectly follow the data book
due to the fact that the controller driver does not have all knowledge of the
configuration in advance. It is given this information piecemeal by the
composite gadget framework after every SET_CONFIGURATION and
SET_INTERFACE. Trying to follow the databook programming model in this
scenario can cause errors. For two reasons:

1) The databook says to do \ ``DWC3_DEPCMD_DEPSTARTCFG``\  for every
\ ``USB_REQ_SET_CONFIGURATION``\  and \ ``USB_REQ_SET_INTERFACE``\  (8.1.5). This is
incorrect in the scenario of multiple interfaces.

2) The databook does not mention doing more \ ``DWC3_DEPCMD_DEPXFERCFG``\  for new
endpoint on alt setting (8.1.6).

.. _`dwc3_gadget_start_config.the-following-simplified-method-is-used-instead`:

The following simplified method is used instead
-----------------------------------------------


All hardware endpoints can be assigned a transfer resource and this setting
will stay persistent until either a core reset or hibernation. So whenever we
do a \ ``DWC3_DEPCMD_DEPSTARTCFG``\ (0) we can go ahead and do
\ ``DWC3_DEPCMD_DEPXFERCFG``\  for every hardware endpoint as well. We are
guaranteed that there are as many transfer resources as endpoints.

This function is called for each endpoint when it is being enabled but is
triggered only when called for EP0-out, which always happens first, and which
should only happen in one of the above conditions.

.. _`__dwc3_gadget_ep_enable`:

__dwc3_gadget_ep_enable
=======================

.. c:function:: int __dwc3_gadget_ep_enable(struct dwc3_ep *dep, unsigned int action)

    initializes a hw endpoint

    :param dep:
        endpoint to be initialized
    :type dep: struct dwc3_ep \*

    :param action:
        one of INIT, MODIFY or RESTORE
    :type action: unsigned int

.. _`__dwc3_gadget_ep_enable.description`:

Description
-----------

Caller should take care of locking. Execute all necessary commands to
initialize a HW endpoint so it can be used by a gadget driver.

.. _`__dwc3_gadget_ep_disable`:

__dwc3_gadget_ep_disable
========================

.. c:function:: int __dwc3_gadget_ep_disable(struct dwc3_ep *dep)

    disables a hw endpoint

    :param dep:
        the endpoint to disable
    :type dep: struct dwc3_ep \*

.. _`__dwc3_gadget_ep_disable.description`:

Description
-----------

This function undoes what __dwc3_gadget_ep_enable did and also removes
requests which are currently being processed by the hardware and those which
are not yet scheduled.

Caller should take care of locking.

.. _`dwc3_ep_prev_trb`:

dwc3_ep_prev_trb
================

.. c:function:: struct dwc3_trb *dwc3_ep_prev_trb(struct dwc3_ep *dep, u8 index)

    returns the previous TRB in the ring

    :param dep:
        The endpoint with the TRB ring
    :type dep: struct dwc3_ep \*

    :param index:
        The index of the current TRB in the ring
    :type index: u8

.. _`dwc3_ep_prev_trb.description`:

Description
-----------

Returns the TRB prior to the one pointed to by the index. If the
index is 0, we will wrap backwards, skip the link TRB, and return
the one just before that.

.. _`dwc3_prepare_one_trb`:

dwc3_prepare_one_trb
====================

.. c:function:: void dwc3_prepare_one_trb(struct dwc3_ep *dep, struct dwc3_request *req, unsigned chain, unsigned node)

    setup one TRB from one request

    :param dep:
        endpoint for which this request is prepared
    :type dep: struct dwc3_ep \*

    :param req:
        dwc3_request pointer
    :type req: struct dwc3_request \*

    :param chain:
        should this TRB be chained to the next?
    :type chain: unsigned

    :param node:
        only for isochronous endpoints. First TRB needs different type.
    :type node: unsigned

.. _`dwc3_gadget_setup_nump`:

dwc3_gadget_setup_nump
======================

.. c:function:: void dwc3_gadget_setup_nump(struct dwc3 *dwc)

    calculate and initialize NUMP field of \ ``DWC3_DCFG``\ 

    :param dwc:
        pointer to our context structure
    :type dwc: struct dwc3 \*

.. _`dwc3_gadget_setup_nump.description`:

Description
-----------

The following looks like complex but it's actually very simple. In order to
calculate the number of packets we can burst at once on OUT transfers, we're
gonna use RxFIFO size.

.. _`dwc3_gadget_setup_nump.to-calculate-rxfifo-size-we-need-two-numbers`:

To calculate RxFIFO size we need two numbers
--------------------------------------------

MDWIDTH = size, in bits, of the internal memory bus
RAM2_DEPTH = depth, in MDWIDTH, of internal RAM2 (where RxFIFO sits)

Given these two numbers, the formula is simple:

RxFIFO Size = (RAM2_DEPTH * MDWIDTH / 8) - 24 - 16;

24 bytes is for 3x SETUP packets
16 bytes is a clock domain crossing tolerance

Given RxFIFO Size, NUMP = RxFIFOSize / 1024;

.. _`dwc3_gadget_init`:

dwc3_gadget_init
================

.. c:function:: int dwc3_gadget_init(struct dwc3 *dwc)

    initializes gadget related registers

    :param dwc:
        pointer to our controller context structure
    :type dwc: struct dwc3 \*

.. _`dwc3_gadget_init.description`:

Description
-----------

Returns 0 on success otherwise negative errno.

.. This file was automatic generated / don't edit.

