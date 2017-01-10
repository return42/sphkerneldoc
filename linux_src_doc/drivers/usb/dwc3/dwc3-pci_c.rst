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

.. _`pci_device_id_synopsys_hapsusb3.this-program-is-free-software`:

This program is free software
-----------------------------

you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2  of
the License as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

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
        u8 uuid[16];
        unsigned int has_dsm_for_pm:1;
    }

.. _`dwc3_pci.members`:

Members
-------

dwc3
    child dwc3 platform_device

pci
    our link to PCI bus

uuid
    _DSM UUID

has_dsm_for_pm
    true for devices which need to run \_DSM on runtime PM

.. This file was automatic generated / don't edit.

