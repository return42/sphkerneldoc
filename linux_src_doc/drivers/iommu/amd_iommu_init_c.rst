.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/amd_iommu_init.c

.. _`get_highest_supported_ivhd_type`:

get_highest_supported_ivhd_type
===============================

.. c:function:: u8 get_highest_supported_ivhd_type(struct acpi_table_header *ivrs)

    Look up the appropriate IVHD type \ ``ivrs``\           Pointer to the IVRS header

    :param struct acpi_table_header \*ivrs:
        *undescribed*

.. _`get_highest_supported_ivhd_type.description`:

Description
-----------

This function search through all IVDB of the maximum supported IVHD

.. This file was automatic generated / don't edit.

