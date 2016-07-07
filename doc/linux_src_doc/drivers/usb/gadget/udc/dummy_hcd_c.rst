.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/udc/dummy_hcd.c

.. _`set_link_state_by_speed`:

set_link_state_by_speed
=======================

.. c:function:: void set_link_state_by_speed(struct dummy_hcd *dum_hcd)

    Sets the current state of the link according to the hcd speed

    :param struct dummy_hcd \*dum_hcd:
        pointer to the dummy_hcd structure to update the link state for

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

    :param struct dummy_hcd \*dum_hcd:
        *undescribed*

    :param struct urb \*urb:
        the urb request to handle

    :param struct usb_ctrlrequest \*setup:
        pointer to the setup data for a USB device control
        request

    :param int \*status:
        pointer to request handling status

.. _`handle_control_request.description`:

Description
-----------

Return 0 - if the request was handled
1 - if the request wasn't handles
error code on error

.. This file was automatic generated / don't edit.

