.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/wm8400-regulator.c

.. _`wm8400_register_regulator`:

wm8400_register_regulator
=========================

.. c:function:: int wm8400_register_regulator(struct device *dev, int reg, struct regulator_init_data *initdata)

    enable software control of a WM8400 regulator

    :param struct device \*dev:
        *undescribed*

    :param int reg:
        *undescribed*

    :param struct regulator_init_data \*initdata:
        *undescribed*

.. _`wm8400_register_regulator.description`:

Description
-----------

This function enables software control of a WM8400 regulator via
the regulator API.  It is intended to be called from the
\ :c:func:`platform_init`\  callback of the WM8400 MFD driver.

\ ``param``\  dev      The WM8400 device to operate on.
\ ``param``\  reg      The regulator to control.
\ ``param``\  initdata Regulator initdata for the regulator.

.. This file was automatic generated / don't edit.

