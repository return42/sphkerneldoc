.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/hcd_intr.c

.. _`dwc2_update_urb_state`:

dwc2_update_urb_state
=====================

.. c:function:: int dwc2_update_urb_state(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan, int chnum, struct dwc2_hcd_urb *urb, struct dwc2_qtd *qtd)

    Updates the state of the URB after a Transfer Complete interrupt on the host channel. Updates the actual_length field of the URB based on the number of bytes transferred via the host channel. Sets the URB status if the data transfer is finished.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

    :param chan:
        Programming view of host channel
    :type chan: struct dwc2_host_chan \*

    :param chnum:
        Channel number
    :type chnum: int

    :param urb:
        Processing URB
    :type urb: struct dwc2_hcd_urb \*

    :param qtd:
        Queue transfer descriptor
    :type qtd: struct dwc2_qtd \*

.. _`dwc2_update_urb_state.return`:

Return
------

1 if the data transfer specified by the URB is completely finished,
0 otherwise

.. _`dwc2_update_isoc_urb_state`:

dwc2_update_isoc_urb_state
==========================

.. c:function:: enum dwc2_halt_status dwc2_update_isoc_urb_state(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan, int chnum, struct dwc2_qtd *qtd, enum dwc2_halt_status halt_status)

    Updates the state of an Isochronous URB when the transfer is stopped for any reason. The fields of the current entry in the frame descriptor array are set based on the transfer state and the input halt_status. Completes the Isochronous URB if all the URB frames have been completed.

    :param hsotg:
        Programming view of the DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

    :param chan:
        Programming view of host channel
    :type chan: struct dwc2_host_chan \*

    :param chnum:
        Channel number
    :type chnum: int

    :param qtd:
        Queue transfer descriptor
    :type qtd: struct dwc2_qtd \*

    :param halt_status:
        Reason for halting a host channel
    :type halt_status: enum dwc2_halt_status

.. _`dwc2_update_isoc_urb_state.return`:

Return
------

DWC2_HC_XFER_COMPLETE if there are more frames remaining to be
transferred in the URB. Otherwise return DWC2_HC_XFER_URB_COMPLETE.

.. _`dwc2_release_channel`:

dwc2_release_channel
====================

.. c:function:: void dwc2_release_channel(struct dwc2_hsotg *hsotg, struct dwc2_host_chan *chan, struct dwc2_qtd *qtd, enum dwc2_halt_status halt_status)

    Releases a host channel for use by other transfers

    :param hsotg:
        The HCD state structure
    :type hsotg: struct dwc2_hsotg \*

    :param chan:
        The host channel to release
    :type chan: struct dwc2_host_chan \*

    :param qtd:
        The QTD associated with the host channel. This QTD may be
        freed if the transfer is complete or an error has occurred.
    :type qtd: struct dwc2_qtd \*

    :param halt_status:
        Reason the channel is being released. This status
        determines the actions taken by this function.
    :type halt_status: enum dwc2_halt_status

.. _`dwc2_release_channel.description`:

Description
-----------

Also attempts to select and queue more transactions since at least one host
channel is available.

.. This file was automatic generated / don't edit.

