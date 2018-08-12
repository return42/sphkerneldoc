.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/davinci/psc.c

.. _`davinci_lpsc_clk`:

struct davinci_lpsc_clk
=======================

.. c:type:: struct davinci_lpsc_clk

    LPSC clock structure

.. _`davinci_lpsc_clk.definition`:

Definition
----------

.. code-block:: c

    struct davinci_lpsc_clk {
        struct device *dev;
        struct clk_hw hw;
        struct generic_pm_domain pm_domain;
        struct clk *genpd_clk;
        struct regmap *regmap;
        u32 md;
        u32 pd;
        u32 flags;
    }

.. _`davinci_lpsc_clk.members`:

Members
-------

dev
    the device that provides this LPSC or NULL

hw
    clk_hw for the LPSC

pm_domain
    power domain for the LPSC

genpd_clk
    clock reference owned by \ ``pm_domain``\ 

regmap
    PSC MMIO region

md
    Module domain (LPSC module id)

pd
    Power domain

flags
    LPSC\_\* quirk flags

.. _`best_dev_name`:

best_dev_name
=============

.. c:function:: const char *best_dev_name(struct device *dev)

    get the "best" device name.

    :param struct device \*dev:
        the device

.. _`best_dev_name.description`:

Description
-----------

Returns the device tree compatible name if the device has a DT node,
otherwise return the device name. This is mainly needed because clkdev
lookups are limited to 20 chars for dev_id and when using device tree,
dev_name(dev) is much longer than that.

.. _`davinci_lpsc_clk_register`:

davinci_lpsc_clk_register
=========================

.. c:function:: struct davinci_lpsc_clk *davinci_lpsc_clk_register(struct device *dev, const char *name, const char *parent_name, struct regmap *regmap, u32 md, u32 pd, u32 flags)

    register LPSC clock

    :param struct device \*dev:
        the clocks's device or NULL

    :param const char \*name:
        name of this clock

    :param const char \*parent_name:
        name of clock's parent

    :param struct regmap \*regmap:
        PSC MMIO region

    :param u32 md:
        local PSC number

    :param u32 pd:
        power domain

    :param u32 flags:
        LPSC\_\* flags

.. This file was automatic generated / don't edit.

