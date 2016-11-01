.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/meson/pinctrl-meson.c

.. _`meson_get_bank`:

meson_get_bank
==============

.. c:function:: int meson_get_bank(struct meson_pinctrl *pc, unsigned int pin, struct meson_bank **bank)

    find the bank containing a given pin

    :param struct meson_pinctrl \*pc:
        the pinctrl instance

    :param unsigned int pin:
        the pin number

    :param struct meson_bank \*\*bank:
        the found bank

.. _`meson_get_bank.return`:

Return
------

0 on success, a negative value on error

.. _`meson_calc_reg_and_bit`:

meson_calc_reg_and_bit
======================

.. c:function:: void meson_calc_reg_and_bit(struct meson_bank *bank, unsigned int pin, enum meson_reg_type reg_type, unsigned int *reg, unsigned int *bit)

    calculate register and bit for a pin

    :param struct meson_bank \*bank:
        the bank containing the pin

    :param unsigned int pin:
        the pin number

    :param enum meson_reg_type reg_type:
        the type of register needed (pull-enable, pull, etc...)

    :param unsigned int \*reg:
        the computed register offset

    :param unsigned int \*bit:
        the computed bit

.. _`meson_pmx_disable_other_groups`:

meson_pmx_disable_other_groups
==============================

.. c:function:: void meson_pmx_disable_other_groups(struct meson_pinctrl *pc, unsigned int pin, int sel_group)

    disable other groups using a given pin

    :param struct meson_pinctrl \*pc:
        meson pin controller device

    :param unsigned int pin:
        number of the pin

    :param int sel_group:
        index of the selected group, or -1 if none

.. _`meson_pmx_disable_other_groups.description`:

Description
-----------

The function disables all pinmux groups using a pin except the
selected one. If \ ``sel_group``\  is -1 all groups are disabled, leaving
the pin in GPIO mode.

.. This file was automatic generated / don't edit.

