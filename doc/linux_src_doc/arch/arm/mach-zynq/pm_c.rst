.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-zynq/pm.c

.. _`zynq_pm_ioremap`:

zynq_pm_ioremap
===============

.. c:function:: void __iomem *zynq_pm_ioremap(const char *comp)

    Create IO mappings

    :param const char \*comp:
        DT compatible string

.. _`zynq_pm_ioremap.return`:

Return
------

Pointer to the mapped memory or NULL.

Remap the memory region for a compatible DT node.

.. _`zynq_pm_late_init`:

zynq_pm_late_init
=================

.. c:function:: void zynq_pm_late_init( void)

    Power management init

    :param  void:
        no arguments

.. _`zynq_pm_late_init.description`:

Description
-----------

Initialization of power management related features and infrastructure.

.. This file was automatic generated / don't edit.

