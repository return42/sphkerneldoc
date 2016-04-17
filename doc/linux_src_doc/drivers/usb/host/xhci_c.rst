.. -*- coding: utf-8; mode: rst -*-

======
xhci.c
======


.. _`xhci_get_endpoint_index`:

xhci_get_endpoint_index
=======================

.. c:function:: unsigned int xhci_get_endpoint_index (struct usb_endpoint_descriptor *desc)

    Used for passing endpoint bitmasks between the core and HCDs. Find the index for an endpoint given its descriptor. Use the return value to right shift 1 for the bitmask.

    :param struct usb_endpoint_descriptor \*desc:

        *undescribed*



.. _`xhci_get_endpoint_index.description`:

Description
-----------


Index  = (epnum * 2) + direction - 1,
where direction = 0 for OUT, 1 for IN.
For control endpoints, the IN index is used (OUT index is unused), so
index = (epnum * 2) + direction - 1 = (epnum * 2) + 1 - 1 = (epnum * 2)

