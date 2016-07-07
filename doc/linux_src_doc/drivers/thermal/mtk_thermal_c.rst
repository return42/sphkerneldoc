.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/mtk_thermal.c

.. _`raw_to_mcelsius`:

raw_to_mcelsius
===============

.. c:function:: int raw_to_mcelsius(struct mtk_thermal *mt, int sensno, s32 raw)

    convert a raw ADC value to mcelsius

    :param struct mtk_thermal \*mt:
        The thermal controller

    :param int sensno:
        *undescribed*

    :param s32 raw:
        raw ADC value

.. _`raw_to_mcelsius.description`:

Description
-----------

This converts the raw ADC value to mcelsius using the SoC specific
calibration constants

.. _`mtk_thermal_get_bank`:

mtk_thermal_get_bank
====================

.. c:function:: void mtk_thermal_get_bank(struct mtk_thermal_bank *bank)

    get bank

    :param struct mtk_thermal_bank \*bank:
        The bank

.. _`mtk_thermal_get_bank.description`:

Description
-----------

The bank registers are banked, we have to select a bank in the
PTPCORESEL register to access it.

.. _`mtk_thermal_put_bank`:

mtk_thermal_put_bank
====================

.. c:function:: void mtk_thermal_put_bank(struct mtk_thermal_bank *bank)

    release bank

    :param struct mtk_thermal_bank \*bank:
        The bank

.. _`mtk_thermal_put_bank.description`:

Description
-----------

release a bank previously taken with mtk_thermal_get_bank,

.. _`mtk_thermal_bank_temperature`:

mtk_thermal_bank_temperature
============================

.. c:function:: int mtk_thermal_bank_temperature(struct mtk_thermal_bank *bank)

    get the temperature of a bank

    :param struct mtk_thermal_bank \*bank:
        The bank

.. _`mtk_thermal_bank_temperature.description`:

Description
-----------

The temperature of a bank is considered the maximum temperature of
the sensors associated to the bank.

.. This file was automatic generated / don't edit.

