.. -*- coding: utf-8; mode: rst -*-

==========
hcd_ddma.c
==========


.. _`dwc2_hcd_qh_init_ddma`:

dwc2_hcd_qh_init_ddma
=====================

.. c:function:: int dwc2_hcd_qh_init_ddma (struct dwc2_hsotg *hsotg, struct dwc2_qh *qh, gfp_t mem_flags)

    Initializes a QH structure's Descriptor DMA related members

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        The QH to init

    :param gfp_t mem_flags:

        *undescribed*



.. _`dwc2_hcd_qh_init_ddma.return`:

Return
------

0 if successful, negative error code otherwise

Allocates memory for the descriptor list. For the first periodic QH,
allocates memory for the FrameList and enables periodic scheduling.



.. _`dwc2_hcd_qh_free_ddma`:

dwc2_hcd_qh_free_ddma
=====================

.. c:function:: void dwc2_hcd_qh_free_ddma (struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Frees a QH structure's Descriptor DMA related members

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        The QH to free



.. _`dwc2_hcd_qh_free_ddma.description`:

Description
-----------

Frees descriptor list memory associated with the QH. If QH is periodic and
the last, frees FrameList memory and disables periodic scheduling.



.. _`dwc2_hcd_start_xfer_ddma`:

dwc2_hcd_start_xfer_ddma
========================

.. c:function:: void dwc2_hcd_start_xfer_ddma (struct dwc2_hsotg *hsotg, struct dwc2_qh *qh)

    Starts a transfer in Descriptor DMA mode

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_qh \*qh:
        The QH to init



.. _`dwc2_hcd_start_xfer_ddma.return`:

Return
------

0 if successful, negative error code otherwise

For Control and Bulk endpoints, initializes descriptor list and starts the
transfer. For Interrupt and Isochronous endpoints, initializes descriptor
list then updates FrameList, marking appropriate entries as active.

For Isochronous endpoints the starting descriptor index is calculated based
on the scheduled frame, but only on the first transfer descriptor within a
session. Then the transfer is started via enabling the channel.

For Isochronous endpoints the channel is not halted on XferComplete
interrupt so remains assigned to the endpoint(QH) until session is done.



.. _`dwc2_hcd_complete_xfer_ddma`:

dwc2_hcd_complete_xfer_ddma
===========================

.. c:function:: void dwc2_hcd_complete_xfer_ddma (struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan, int chnum, enum dwc2_halt_status halt_status)

    Scans the descriptor list, updates URB's status and calls completion routine for the URB if it's done. Called from interrupt handlers.

    :param struct dwc2_hsotg \*hsotg:
        The HCD state structure for the DWC OTG controller

    :param struct dwc2_host_chan \*chan:
        Host channel the transfer is completed on

    :param int chnum:
        Index of Host channel registers

    :param enum dwc2_halt_status halt_status:
        Reason the channel is being halted or just XferComplete
        for isochronous transfers



.. _`dwc2_hcd_complete_xfer_ddma.description`:

Description
-----------

Releases the channel to be used by other transfers.
In case of Isochronous endpoint the channel is not halted until the end of
the session, i.e. QTD list is empty.
If periodic channel released the FrameList is updated accordingly.
Calls transaction selection routines to activate pending transfers.

