.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/meson/pinctrl-meson8-pmx.c

.. _`meson8_pmx_disable_other_groups`:

meson8_pmx_disable_other_groups
===============================

.. c:function:: void meson8_pmx_disable_other_groups(struct meson_pinctrl *pc, unsigned int pin, int sel_group)

    disable other groups using a given pin

    :param pc:
        meson pin controller device
    :type pc: struct meson_pinctrl \*

    :param pin:
        number of the pin
    :type pin: unsigned int

    :param sel_group:
        index of the selected group, or -1 if none
    :type sel_group: int

.. _`meson8_pmx_disable_other_groups.description`:

Description
-----------

The function disables all pinmux groups using a pin except the
selected one. If \ ``sel_group``\  is -1 all groups are disabled, leaving
the pin in GPIO mode.

.. This file was automatic generated / don't edit.

