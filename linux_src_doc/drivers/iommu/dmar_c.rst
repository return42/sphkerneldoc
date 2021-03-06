.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/dmar.c

.. _`dmar_parse_one_drhd`:

dmar_parse_one_drhd
===================

.. c:function:: int dmar_parse_one_drhd(struct acpi_dmar_header *header, void *arg)

    parses exactly one DMA remapping hardware definition structure which uniquely represent one DMA remapping hardware unit present in the platform

    :param header:
        *undescribed*
    :type header: struct acpi_dmar_header \*

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`dmar_table_detect`:

dmar_table_detect
=================

.. c:function:: int dmar_table_detect( void)

    checks to see if the platform supports DMAR devices

    :param void:
        no arguments
    :type void: 

.. _`parse_dmar_table`:

parse_dmar_table
================

.. c:function:: int parse_dmar_table( void)

    parses the DMA reporting table

    :param void:
        no arguments
    :type void: 

.. _`map_iommu`:

map_iommu
=========

.. c:function:: int map_iommu(struct intel_iommu *iommu, u64 phys_addr)

    map the iommu's registers

    :param iommu:
        the iommu to map
    :type iommu: struct intel_iommu \*

    :param phys_addr:
        the physical address of the base resgister
    :type phys_addr: u64

.. _`map_iommu.description`:

Description
-----------

Memory map the iommu's registers.  Start w/ a single page, and
possibly expand if that turns out to be insufficent.

.. This file was automatic generated / don't edit.

