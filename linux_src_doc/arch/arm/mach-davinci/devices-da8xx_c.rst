.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-davinci/devices-da8xx.c

.. _`da8xx_get_cfgchip`:

da8xx_get_cfgchip
=================

.. c:function:: struct regmap *da8xx_get_cfgchip( void)

    Lazy gets CFGCHIP as regmap

    :param  void:
        no arguments

.. _`da8xx_get_cfgchip.description`:

Description
-----------

This is for use on non-DT boards only. For DT boards, use
syscon_regmap_lookup_by_compatible("ti,da830-cfgchip")

.. _`da8xx_get_cfgchip.return`:

Return
------

Pointer to the CFGCHIP regmap or negative error code.

.. This file was automatic generated / don't edit.

