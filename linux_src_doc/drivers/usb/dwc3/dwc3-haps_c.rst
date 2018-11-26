.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/dwc3-haps.c

.. _`pci_device_id_synopsys_hapsusb3`:

PCI_DEVICE_ID_SYNOPSYS_HAPSUSB3
===============================

.. c:function::  PCI_DEVICE_ID_SYNOPSYS_HAPSUSB3()

    haps.c - Synopsys HAPS PCI Specific glue layer

.. _`pci_device_id_synopsys_hapsusb3.description`:

Description
-----------

Copyright (C) 2018 Synopsys, Inc.

.. _`pci_device_id_synopsys_hapsusb3.authors`:

Authors
-------

Thinh Nguyen <thinhn@synopsys.com>,
John Youn <johnyoun@synopsys.com>

.. _`dwc3_haps`:

struct dwc3_haps
================

.. c:type:: struct dwc3_haps

    Driver private structure

.. _`dwc3_haps.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_haps {
        struct platform_device *dwc3;
        struct pci_dev *pci;
    }

.. _`dwc3_haps.members`:

Members
-------

dwc3
    child dwc3 platform_device

pci
    our link to PCI bus

.. This file was automatic generated / don't edit.

