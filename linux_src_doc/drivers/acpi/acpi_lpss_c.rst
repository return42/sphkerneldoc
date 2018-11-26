.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/acpi_lpss.c

.. _`acpi_lpss_save_ctx`:

acpi_lpss_save_ctx
==================

.. c:function:: void acpi_lpss_save_ctx(struct device *dev, struct lpss_private_data *pdata)

    Save the private registers of LPSS device

    :param dev:
        LPSS device
    :type dev: struct device \*

    :param pdata:
        pointer to the private data of the LPSS device
    :type pdata: struct lpss_private_data \*

.. _`acpi_lpss_save_ctx.description`:

Description
-----------

Most LPSS devices have private registers which may loose their context when
the device is powered down. \ :c:func:`acpi_lpss_save_ctx`\  saves those registers into
prv_reg_ctx array.

.. _`acpi_lpss_restore_ctx`:

acpi_lpss_restore_ctx
=====================

.. c:function:: void acpi_lpss_restore_ctx(struct device *dev, struct lpss_private_data *pdata)

    Restore the private registers of LPSS device

    :param dev:
        LPSS device
    :type dev: struct device \*

    :param pdata:
        pointer to the private data of the LPSS device
    :type pdata: struct lpss_private_data \*

.. _`acpi_lpss_restore_ctx.description`:

Description
-----------

Restores the registers that were previously stored with \ :c:func:`acpi_lpss_save_ctx`\ .

.. This file was automatic generated / don't edit.

