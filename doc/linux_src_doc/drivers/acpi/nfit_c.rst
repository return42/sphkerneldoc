.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/nfit.c

.. _`nfit_spa_map`:

nfit_spa_map
============

.. c:function:: void __iomem *nfit_spa_map(struct acpi_nfit_desc *acpi_desc, struct acpi_nfit_system_address *spa, enum spa_map_type type)

    interleave-aware managed-mappings of acpi_nfit_system_address ranges

    :param struct acpi_nfit_desc \*acpi_desc:
        *undescribed*

    :param struct acpi_nfit_system_address \*spa:
        *undescribed*

    :param enum spa_map_type type:
        aperture or control region

.. _`nfit_spa_map.description`:

Description
-----------

In the case where block-data-window apertures and
dimm-control-regions are interleaved they will end up sharing a
single \ :c:func:`request_mem_region`\  + \ :c:func:`ioremap`\  for the address range.  In
the style of devm \ :c:func:`nfit_spa_map`\  mappings are automatically dropped
when all region devices referencing the same mapping are disabled /
unbound.

.. This file was automatic generated / don't edit.

