.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/xhci-mem.c

.. _`xhci_ring_alloc`:

xhci_ring_alloc
===============

.. c:function:: struct xhci_ring *xhci_ring_alloc(struct xhci_hcd *xhci, unsigned int num_segs, unsigned int cycle_state, enum xhci_ring_type type, unsigned int max_packet, gfp_t flags)

    :param xhci:
        *undescribed*
    :type xhci: struct xhci_hcd \*

    :param num_segs:
        *undescribed*
    :type num_segs: unsigned int

    :param cycle_state:
        *undescribed*
    :type cycle_state: unsigned int

    :param type:
        *undescribed*
    :type type: enum xhci_ring_type

    :param max_packet:
        *undescribed*
    :type max_packet: unsigned int

    :param flags:
        *undescribed*
    :type flags: gfp_t

.. _`xhci_ring_alloc.description`:

Description
-----------

Link each segment together into a ring.
Set the end flag and the cycle toggle bit on the last segment.
See section 4.9.1 and figures 15 and 16.

.. This file was automatic generated / don't edit.

