.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/dwc3-pci.c

.. _`pci_device_id_synopsys_hapsusb3`:

PCI_DEVICE_ID_SYNOPSYS_HAPSUSB3
===============================

.. c:function::  PCI_DEVICE_ID_SYNOPSYS_HAPSUSB3()

    pci.c - PCI Specific glue layer

.. _`pci_device_id_synopsys_hapsusb3.description`:

Description
-----------

Copyright (C) 2010-2011 Texas Instruments Incorporated - http://www.ti.com

.. _`pci_device_id_synopsys_hapsusb3.authors`:

Authors
-------

Felipe Balbi <balbi@ti.com>,
Sebastian Andrzej Siewior <bigeasy@linutronix.de>

.. _`dwc3_pci`:

struct dwc3_pci
===============

.. c:type:: struct dwc3_pci

    Driver private structure

.. _`dwc3_pci.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_pci {
        struct platform_device *dwc3;
        struct pci_dev *pci;
        guid_t guid;
        unsigned int has_dsm_for_pm:1;
        struct work_struct wakeup_work;
    }

.. _`dwc3_pci.members`:

Members
-------

dwc3
    child dwc3 platform_device

pci
    our link to PCI bus

guid
    \_DSM GUID

has_dsm_for_pm
    true for devices which need to run \_DSM on runtime PM

wakeup_work
    *undescribed*

.. This file was automatic generated / don't edit.

