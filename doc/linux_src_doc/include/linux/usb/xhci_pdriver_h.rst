.. -*- coding: utf-8; mode: rst -*-

==============
xhci_pdriver.h
==============


.. _`usb_xhci_pdata`:

struct usb_xhci_pdata
=====================

.. c:type:: usb_xhci_pdata

    platform_data for generic xhci platform driver


.. _`usb_xhci_pdata.definition`:

Definition
----------

.. code-block:: c

  struct usb_xhci_pdata {
    unsigned usb3_lpm_capable:1;
  };


.. _`usb_xhci_pdata.members`:

Members
-------

:``usb3_lpm_capable``:
    determines if this xhci platform supports USB3
    LPM capability


