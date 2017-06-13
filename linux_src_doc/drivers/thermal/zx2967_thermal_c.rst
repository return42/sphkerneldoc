.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/zx2967_thermal.c

.. _`zx2967_thermal_priv`:

struct zx2967_thermal_priv
==========================

.. c:type:: struct zx2967_thermal_priv

    zx2967 thermal sensor private structure

.. _`zx2967_thermal_priv.definition`:

Definition
----------

.. code-block:: c

    struct zx2967_thermal_priv {
        struct thermal_zone_device *tzd;
        struct mutex lock;
        struct clk *clk_topcrm;
        struct clk *clk_apb;
        void __iomem *regs;
        struct device *dev;
    }

.. _`zx2967_thermal_priv.members`:

Members
-------

tzd
    struct thermal_zone_device where the sensor is registered

lock
    prevents read sensor in parallel

clk_topcrm
    topcrm clk structure

clk_apb
    apb clk structure

regs
    pointer to base address of the thermal sensor

dev
    *undescribed*

.. This file was automatic generated / don't edit.

