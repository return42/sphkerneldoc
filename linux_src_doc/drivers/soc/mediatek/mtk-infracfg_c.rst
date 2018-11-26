.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/mediatek/mtk-infracfg.c

.. _`mtk_infracfg_set_bus_protection`:

mtk_infracfg_set_bus_protection
===============================

.. c:function:: int mtk_infracfg_set_bus_protection(struct regmap *infracfg, u32 mask, bool reg_update)

    enable bus protection

    :param infracfg:
        *undescribed*
    :type infracfg: struct regmap \*

    :param mask:
        The mask containing the protection bits to be enabled.
    :type mask: u32

    :param reg_update:
        The boolean flag determines to set the protection bits
        by regmap_update_bits with enable register(PROTECTEN) or
        by regmap_write with set register(PROTECTEN_SET).
    :type reg_update: bool

.. _`mtk_infracfg_set_bus_protection.description`:

Description
-----------

This function enables the bus protection bits for disabled power
domains so that the system does not hang when some unit accesses the
bus while in power down.

.. _`mtk_infracfg_clear_bus_protection`:

mtk_infracfg_clear_bus_protection
=================================

.. c:function:: int mtk_infracfg_clear_bus_protection(struct regmap *infracfg, u32 mask, bool reg_update)

    disable bus protection

    :param infracfg:
        *undescribed*
    :type infracfg: struct regmap \*

    :param mask:
        The mask containing the protection bits to be disabled.
    :type mask: u32

    :param reg_update:
        The boolean flag determines to clear the protection bits
        by regmap_update_bits with enable register(PROTECTEN) or
        by regmap_write with clear register(PROTECTEN_CLR).
    :type reg_update: bool

.. _`mtk_infracfg_clear_bus_protection.description`:

Description
-----------

This function disables the bus protection bits previously enabled with
mtk_infracfg_set_bus_protection.

.. This file was automatic generated / don't edit.

