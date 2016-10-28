.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/memory/samsung/exynos-srom.c

.. _`exynos_srom_reg_dump`:

struct exynos_srom_reg_dump
===========================

.. c:type:: struct exynos_srom_reg_dump

    register dump of SROM Controller registers.

.. _`exynos_srom_reg_dump.definition`:

Definition
----------

.. code-block:: c

    struct exynos_srom_reg_dump {
        u32 offset;
        u32 value;
    }

.. _`exynos_srom_reg_dump.members`:

Members
-------

offset
    srom register offset from the controller base address.

value
    the value of register under the offset.

.. _`exynos_srom`:

struct exynos_srom
==================

.. c:type:: struct exynos_srom

    platform data for exynos srom controller driver.

.. _`exynos_srom.definition`:

Definition
----------

.. code-block:: c

    struct exynos_srom {
        struct device *dev;
        void __iomem *reg_base;
        struct exynos_srom_reg_dump *reg_offset;
    }

.. _`exynos_srom.members`:

Members
-------

dev
    platform device pointer

reg_base
    srom base address

reg_offset
    exynos_srom_reg_dump pointer to hold offset and its value.

.. This file was automatic generated / don't edit.

