.. -*- coding: utf-8; mode: rst -*-

==========
xhci-dbg.c
==========


.. _`xhci_debug_trb`:

xhci_debug_trb
==============

.. c:function:: void xhci_debug_trb (struct xhci_hcd *xhci, union xhci_trb *trb)

    :param struct xhci_hcd \*xhci:

        *undescribed*

    :param union xhci_trb \*trb:

        *undescribed*



.. _`xhci_debug_segment`:

xhci_debug_segment
==================

.. c:function:: void xhci_debug_segment (struct xhci_hcd *xhci, struct xhci_segment *seg)

    :param struct xhci_hcd \*xhci:

        *undescribed*

    :param struct xhci_segment \*seg:

        *undescribed*



.. _`xhci_debug_segment.description`:

Description
-----------


``return`` The Link TRB of the segment, or NULL if there is no Link TRB
(which is a bug, since all segments must have a Link TRB).

Prints out all TRBs in the segment, even those after the Link TRB.



.. _`xhci_debug_segment.xxx`:

XXX
---

should we print out TRBs that the HC owns?  As long as we don't
write, that should be fine...  We shouldn't expect that the memory pointed to
by the TRB is valid at all.  Do we care about ones the HC owns?  Probably,
for HC debugging.



.. _`xhci_debug_ring`:

xhci_debug_ring
===============

.. c:function:: void xhci_debug_ring (struct xhci_hcd *xhci, struct xhci_ring *ring)

    :param struct xhci_hcd \*xhci:

        *undescribed*

    :param struct xhci_ring \*ring:

        *undescribed*



.. _`xhci_debug_ring.description`:

Description
-----------


Print out each segment in the ring.  Check that the DMA address in
each link segment actually matches the segment's stored DMA address.
Check that the link end bit is only set at the end of the ring.
Check that the dequeue and enqueue pointers point to real data in this ring
(not some other ring).

