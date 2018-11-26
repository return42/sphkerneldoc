.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/gadget.h

.. _`next_request`:

next_request
============

.. c:function:: struct dwc3_request *next_request(struct list_head *list)

    gets the next request on the given list

    :param list:
        the request list to operate on
    :type list: struct list_head \*

.. _`next_request.description`:

Description
-----------

Caller should take care of locking. This function return \ ``NULL``\  or the first
request available on \ ``list``\ .

.. _`dwc3_gadget_move_started_request`:

dwc3_gadget_move_started_request
================================

.. c:function:: void dwc3_gadget_move_started_request(struct dwc3_request *req)

    move \ ``req``\  to the started_list

    :param req:
        the request to be moved
    :type req: struct dwc3_request \*

.. _`dwc3_gadget_move_started_request.description`:

Description
-----------

Caller should take care of locking. This function will move \ ``req``\  from its
current list to the endpoint's started_list.

.. _`dwc3_gadget_ep_get_transfer_index`:

dwc3_gadget_ep_get_transfer_index
=================================

.. c:function:: void dwc3_gadget_ep_get_transfer_index(struct dwc3_ep *dep)

    Gets transfer index from HW

    :param dep:
        dwc3 endpoint
    :type dep: struct dwc3_ep \*

.. _`dwc3_gadget_ep_get_transfer_index.description`:

Description
-----------

Caller should take care of locking. Returns the transfer resource
index for a given endpoint.

.. This file was automatic generated / don't edit.

