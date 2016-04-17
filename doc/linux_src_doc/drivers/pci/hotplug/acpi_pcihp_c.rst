.. -*- coding: utf-8; mode: rst -*-

============
acpi_pcihp.c
============


.. _`acpi_get_hp_hw_control_from_firmware`:

acpi_get_hp_hw_control_from_firmware
====================================

.. c:function:: int acpi_get_hp_hw_control_from_firmware (struct pci_dev *pdev, u32 flags)

    :param struct pci_dev \*pdev:

        *undescribed*

    :param u32 flags:
        requested control bits for _OSC



.. _`acpi_get_hp_hw_control_from_firmware.description`:

Description
-----------

Attempt to take hotplug control from firmware.



.. _`acpi_pci_check_ejectable`:

acpi_pci_check_ejectable
========================

.. c:function:: int acpi_pci_check_ejectable (struct pci_bus *pbus, acpi_handle handle)

    check if handle is ejectable ACPI PCI slot

    :param struct pci_bus \*pbus:
        the PCI bus of the PCI slot corresponding to 'handle'

    :param acpi_handle handle:
        ACPI handle to check



.. _`acpi_pci_check_ejectable.description`:

Description
-----------

Return 1 if handle is ejectable PCI slot, 0 otherwise.



.. _`acpi_pci_detect_ejectable`:

acpi_pci_detect_ejectable
=========================

.. c:function:: int acpi_pci_detect_ejectable (acpi_handle handle)

    check if the PCI bus has ejectable slots @handle - handle of the PCI bus to scan

    :param acpi_handle handle:

        *undescribed*



.. _`acpi_pci_detect_ejectable.description`:

Description
-----------


Returns 1 if the PCI bus has ACPI based ejectable slots, 0 otherwise.

