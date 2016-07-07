.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/mediatek/mtk-infracfg.c

.. _`mtk_infracfg_set_bus_protection`:

mtk_infracfg_set_bus_protection
===============================

.. c:function:: int mtk_infracfg_set_bus_protection(struct regmap *infracfg, u32 mask)

    enable bus protection

    :param struct regmap \*infracfg:
        *undescribed*

    :param u32 mask:
        The mask containing the protection bits to be enabled.

.. _`mtk_infracfg_set_bus_protection.description`:

Description
-----------

This function enables the bus protection bits for disabled power
domains so that the system does not hang when some unit accesses the
bus while in power down.

.. _`mtk_infracfg_clear_bus_protection`:

mtk_infracfg_clear_bus_protection
=================================

.. c:function:: int mtk_infracfg_clear_bus_protection(struct regmap *infracfg, u32 mask)

    disable bus protection

    :param struct regmap \*infracfg:
        *undescribed*

    :param u32 mask:
        The mask containing the protection bits to be disabled.

.. _`mtk_infracfg_clear_bus_protection.description`:

Description
-----------

This function disables the bus protection bits previously enabled with
mtk_infracfg_set_bus_protection.

.. This file was automatic generated / don't edit.

