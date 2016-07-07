.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-exynos5.c

.. _`hsi2c_ctl`:

HSI2C_CTL
=========

.. c:function::  HSI2C_CTL()

    exynos5.c - Samsung Exynos5 I2C Controller Driver

.. _`hsi2c_ctl.description`:

Description
-----------

Copyright (C) 2013 Samsung Electronics Co., Ltd.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

.. _`exynos_hsi2c_variant`:

struct exynos_hsi2c_variant
===========================

.. c:type:: struct exynos_hsi2c_variant

    platform specific HSI2C driver data

.. _`exynos_hsi2c_variant.definition`:

Definition
----------

.. code-block:: c

    struct exynos_hsi2c_variant {
        unsigned int fifo_depth;
        unsigned int hw;
    }

.. _`exynos_hsi2c_variant.members`:

Members
-------

fifo_depth
    the fifo depth supported by the HSI2C module

hw
    *undescribed*

.. _`exynos_hsi2c_variant.description`:

Description
-----------

Specifies platform specific configuration of HSI2C module.

.. _`exynos_hsi2c_variant.note`:

Note
----

A structure for driver specific platform data is used for future
expansion of its usage.

.. This file was automatic generated / don't edit.

