.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/udc/dummy_hcd.c

.. _`set_link_state_by_speed`:

set_link_state_by_speed
=======================

.. c:function:: void set_link_state_by_speed(struct dummy_hcd *dum_hcd)

    Sets the current state of the link according to the hcd speed

    :param dum_hcd:
        pointer to the dummy_hcd structure to update the link state for
    :type dum_hcd: struct dummy_hcd \*

.. _`set_link_state_by_speed.description`:

Description
-----------

This function updates the port_status according to the link state and the
speed of the hcd.

.. _`handle_control_request`:

handle_control_request
======================

.. c:function:: int handle_control_request(struct dummy_hcd *dum_hcd, struct urb *urb, struct usb_ctrlrequest *setup, int *status)

    handles all control transfers

    :param dum_hcd:
        *undescribed*
    :type dum_hcd: struct dummy_hcd \*

    :param urb:
        the urb request to handle
    :type urb: struct urb \*

    :param setup:
        pointer to the setup data for a USB device control
        request
    :type setup: struct usb_ctrlrequest \*

    :param status:
        pointer to request handling status
    :type status: int \*

.. _`handle_control_request.description`:

Description
-----------

Return 0 - if the request was handled
1 - if the request wasn't handles
error code on error

.. This file was automatic generated / don't edit.

