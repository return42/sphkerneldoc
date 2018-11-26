.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/isp1760/isp1760-udc.c

.. _`isp1760_udc_select_ep`:

isp1760_udc_select_ep
=====================

.. c:function:: void isp1760_udc_select_ep(struct isp1760_ep *ep)

    Select an endpoint for register access

    :param ep:
        The endpoint
    :type ep: struct isp1760_ep \*

.. _`isp1760_udc_select_ep.description`:

Description
-----------

The ISP1761 endpoint registers are banked. This function selects the target
endpoint for banked register access. The selection remains valid until the
next call to this function, the next direct access to the EPINDEX register
or the next reset, whichever comes first.

Called with the UDC spinlock held.

.. This file was automatic generated / don't edit.

