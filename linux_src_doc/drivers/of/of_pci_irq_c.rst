.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/of_pci_irq.c

.. _`of_irq_parse_pci`:

of_irq_parse_pci
================

.. c:function:: int of_irq_parse_pci(const struct pci_dev *pdev, struct of_phandle_args *out_irq)

    Resolve the interrupt for a PCI device

    :param const struct pci_dev \*pdev:
        the device whose interrupt is to be resolved

    :param struct of_phandle_args \*out_irq:
        structure of_irq filled by this function

.. _`of_irq_parse_pci.description`:

Description
-----------

This function resolves the PCI interrupt for a given PCI device. If a
device-node exists for a given pci_dev, it will use normal OF tree
walking. If not, it will implement standard swizzling and walk up the
PCI tree until an device-node is found, at which point it will finish
resolving using the OF tree walking.

.. _`of_irq_parse_and_map_pci`:

of_irq_parse_and_map_pci
========================

.. c:function:: int of_irq_parse_and_map_pci(const struct pci_dev *dev, u8 slot, u8 pin)

    Decode a PCI irq from the device tree and map to a virq

    :param const struct pci_dev \*dev:
        The pci device needing an irq

    :param u8 slot:
        PCI slot number; passed when used as map_irq callback. Unused

    :param u8 pin:
        PCI irq pin number; passed when used as map_irq callback. Unused

.. _`of_irq_parse_and_map_pci.description`:

Description
-----------

@slot and \ ``pin``\  are unused, but included in the function so that this
function can be used directly as the map_irq callback to \ :c:func:`pci_fixup_irqs`\ .

.. This file was automatic generated / don't edit.

