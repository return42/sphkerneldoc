.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/core_intr.c

.. _`dwc2_handle_usb_port_intr`:

dwc2_handle_usb_port_intr
=========================

.. c:function:: void dwc2_handle_usb_port_intr(struct dwc2_hsotg *hsotg)

    handles OTG PRTINT interrupts. When the PRTINT interrupt fires, there are certain status bits in the Host Port that needs to get cleared.

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_handle_mode_mismatch_intr`:

dwc2_handle_mode_mismatch_intr
==============================

.. c:function:: void dwc2_handle_mode_mismatch_intr(struct dwc2_hsotg *hsotg)

    Logs a mode mismatch warning message

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_handle_otg_intr`:

dwc2_handle_otg_intr
====================

.. c:function:: void dwc2_handle_otg_intr(struct dwc2_hsotg *hsotg)

    Handles the OTG Interrupts. It reads the OTG Interrupt Register (GOTGINT) to determine what interrupt has occurred.

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_handle_conn_id_status_change_intr`:

dwc2_handle_conn_id_status_change_intr
======================================

.. c:function:: void dwc2_handle_conn_id_status_change_intr(struct dwc2_hsotg *hsotg)

    Handles the Connector ID Status Change Interrupt

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_handle_conn_id_status_change_intr.description`:

Description
-----------

Reads the OTG Interrupt Register (GOTCTL) to determine whether this is a
Device to Host Mode transition or a Host to Device Mode transition. This only
occurs when the cable is connected/removed from the PHY connector.

.. _`dwc2_handle_session_req_intr`:

dwc2_handle_session_req_intr
============================

.. c:function:: void dwc2_handle_session_req_intr(struct dwc2_hsotg *hsotg)

    This interrupt indicates that a device is initiating the Session Request Protocol to request the host to turn on bus power so a new session can begin

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_handle_session_req_intr.description`:

Description
-----------

This handler responds by turning on bus power. If the DWC_otg controller is
in low power mode, this handler brings the controller out of low power mode
before turning on bus power.

.. _`dwc2_wakeup_from_lpm_l1`:

dwc2_wakeup_from_lpm_l1
=======================

.. c:function:: void dwc2_wakeup_from_lpm_l1(struct dwc2_hsotg *hsotg)

    Exit the device from LPM L1 state

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_handle_lpm_intr`:

dwc2_handle_lpm_intr
====================

.. c:function:: void dwc2_handle_lpm_intr(struct dwc2_hsotg *hsotg)

    GINTSTS_LPMTRANRCVD Interrupt handler

    :param hsotg:
        Programming view of DWC_otg controller
    :type hsotg: struct dwc2_hsotg \*

.. This file was automatic generated / don't edit.

