.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/ehci_pdriver.h

.. _`usb_ehci_pdata`:

struct usb_ehci_pdata
=====================

.. c:type:: struct usb_ehci_pdata

    platform_data for generic ehci driver

.. _`usb_ehci_pdata.definition`:

Definition
----------

.. code-block:: c

    struct usb_ehci_pdata {
        int caps_offset;
        unsigned has_tt:1;
        unsigned has_synopsys_hc_bug:1;
        unsigned big_endian_desc:1;
        unsigned big_endian_mmio:1;
        unsigned no_io_watchdog:1;
        unsigned reset_on_resume:1;
        unsigned dma_mask_64:1;
        int (* power_on) (struct platform_device *pdev);
        void (* power_off) (struct platform_device *pdev);
        void (* power_suspend) (struct platform_device *pdev);
        int (* pre_setup) (struct usb_hcd *hcd);
    }

.. _`usb_ehci_pdata.members`:

Members
-------

caps_offset
    offset of the EHCI Capability Registers to the start of
    the io memory region provided to the driver.

has_tt
    set to 1 if TT is integrated in root hub.

has_synopsys_hc_bug
    *undescribed*

big_endian_desc
    *undescribed*

big_endian_mmio
    *undescribed*

no_io_watchdog
    set to 1 if the controller does not need the I/O
    watchdog to run.

reset_on_resume
    set to 1 if the controller needs to be reset after
    a suspend / resume cycle (but can't detect that itself).

dma_mask_64
    *undescribed*

power_on
    *undescribed*

power_off
    *undescribed*

power_suspend
    *undescribed*

pre_setup
    *undescribed*

.. _`usb_ehci_pdata.description`:

Description
-----------

These are general configuration options for the EHCI controller. All of
these options are activating more or less workarounds for some hardware.

.. This file was automatic generated / don't edit.

