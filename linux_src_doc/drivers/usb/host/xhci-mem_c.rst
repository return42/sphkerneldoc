.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/xhci-mem.c

.. _`xhci_ring_alloc`:

xhci_ring_alloc
===============

.. c:function:: struct xhci_ring *xhci_ring_alloc(struct xhci_hcd *xhci, unsigned int num_segs, unsigned int cycle_state, enum xhci_ring_type type, unsigned int max_packet, gfp_t flags)

    :param struct xhci_hcd \*xhci:
        *undescribed*

    :param unsigned int num_segs:
        *undescribed*

    :param unsigned int cycle_state:
        *undescribed*

    :param enum xhci_ring_type type:
        *undescribed*

    :param unsigned int max_packet:
        *undescribed*

    :param gfp_t flags:
        *undescribed*

.. _`xhci_ring_alloc.description`:

Description
-----------

Link each segment together into a ring.
Set the end flag and the cycle toggle bit on the last segment.
See section 4.9.1 and figures 15 and 16.

.. This file was automatic generated / don't edit.

