.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/meson/pinctrl-meson.c

.. _`meson_get_bank`:

meson_get_bank
==============

.. c:function:: int meson_get_bank(struct meson_pinctrl *pc, unsigned int pin, struct meson_bank **bank)

    find the bank containing a given pin

    :param pc:
        the pinctrl instance
    :type pc: struct meson_pinctrl \*

    :param pin:
        the pin number
    :type pin: unsigned int

    :param bank:
        the found bank
    :type bank: struct meson_bank \*\*

.. _`meson_get_bank.return`:

Return
------

0 on success, a negative value on error

.. _`meson_calc_reg_and_bit`:

meson_calc_reg_and_bit
======================

.. c:function:: void meson_calc_reg_and_bit(struct meson_bank *bank, unsigned int pin, enum meson_reg_type reg_type, unsigned int *reg, unsigned int *bit)

    calculate register and bit for a pin

    :param bank:
        the bank containing the pin
    :type bank: struct meson_bank \*

    :param pin:
        the pin number
    :type pin: unsigned int

    :param reg_type:
        the type of register needed (pull-enable, pull, etc...)
    :type reg_type: enum meson_reg_type

    :param reg:
        the computed register offset
    :type reg: unsigned int \*

    :param bit:
        the computed bit
    :type bit: unsigned int \*

.. This file was automatic generated / don't edit.

