.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/acpi_pcihp.c

.. _`acpi_get_hp_hw_control_from_firmware`:

acpi_get_hp_hw_control_from_firmware
====================================

.. c:function:: int acpi_get_hp_hw_control_from_firmware(struct pci_dev *pdev)

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. _`acpi_get_hp_hw_control_from_firmware.description`:

Description
-----------

Attempt to take hotplug control from firmware.

.. _`acpi_pci_check_ejectable`:

acpi_pci_check_ejectable
========================

.. c:function:: int acpi_pci_check_ejectable(struct pci_bus *pbus, acpi_handle handle)

    check if handle is ejectable ACPI PCI slot

    :param pbus:
        the PCI bus of the PCI slot corresponding to 'handle'
    :type pbus: struct pci_bus \*

    :param handle:
        ACPI handle to check
    :type handle: acpi_handle

.. _`acpi_pci_check_ejectable.description`:

Description
-----------

Return 1 if handle is ejectable PCI slot, 0 otherwise.

.. _`acpi_pci_detect_ejectable`:

acpi_pci_detect_ejectable
=========================

.. c:function:: int acpi_pci_detect_ejectable(acpi_handle handle)

    check if the PCI bus has ejectable slots \ ``handle``\  - handle of the PCI bus to scan

    :param handle:
        *undescribed*
    :type handle: acpi_handle

.. _`acpi_pci_detect_ejectable.description`:

Description
-----------

Returns 1 if the PCI bus has ACPI based ejectable slots, 0 otherwise.

.. This file was automatic generated / don't edit.

