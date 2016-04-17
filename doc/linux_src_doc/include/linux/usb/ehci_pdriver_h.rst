.. -*- coding: utf-8; mode: rst -*-

==============
ehci_pdriver.h
==============


.. _`usb_ehci_pdata`:

struct usb_ehci_pdata
=====================

.. c:type:: usb_ehci_pdata

    platform_data for generic ehci driver


.. _`usb_ehci_pdata.definition`:

Definition
----------

.. code-block:: c

  struct usb_ehci_pdata {
    int caps_offset;
    unsigned has_tt:1;
    unsigned no_io_watchdog:1;
    unsigned reset_on_resume:1;
  };


.. _`usb_ehci_pdata.members`:

Members
-------

:``caps_offset``:
    offset of the EHCI Capability Registers to the start of
    the io memory region provided to the driver.

:``has_tt``:
    set to 1 if TT is integrated in root hub.

:``no_io_watchdog``:
    set to 1 if the controller does not need the I/O
    watchdog to run.

:``reset_on_resume``:
    set to 1 if the controller needs to be reset after
    a suspend / resume cycle (but can't detect that itself).




.. _`usb_ehci_pdata.description`:

Description
-----------

These are general configuration options for the EHCI controller. All of
these options are activating more or less workarounds for some hardware.

