.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/acpi.h

.. _`iwl_acpi_get_mcc`:

iwl_acpi_get_mcc
================

.. c:function:: int iwl_acpi_get_mcc(struct device *dev, char *mcc)

    read MCC from ACPI, if available

    :param struct device \*dev:
        the struct device

    :param char \*mcc:
        output buffer (3 bytes) that will get the MCC

.. _`iwl_acpi_get_mcc.description`:

Description
-----------

This function tries to read the current MCC from ACPI if available.

.. This file was automatic generated / don't edit.

