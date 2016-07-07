.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-tz1090-pdc.c

.. _`tz1090_pdc_function`:

struct tz1090_pdc_function
==========================

.. c:type:: struct tz1090_pdc_function

    TZ1090 PDC pinctrl mux function

.. _`tz1090_pdc_function.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_pdc_function {
        const char *name;
        const char * const *groups;
        unsigned int ngroups;
    }

.. _`tz1090_pdc_function.members`:

Members
-------

name
    The name of the function, exported to pinctrl core.

groups
    An array of pin groups that may select this function.

ngroups
    The number of entries in \ ``groups``\ .

.. _`tz1090_pdc_pingroup`:

struct tz1090_pdc_pingroup
==========================

.. c:type:: struct tz1090_pdc_pingroup

    TZ1090 PDC pin group

.. _`tz1090_pdc_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_pdc_pingroup {
        const char *name;
        const unsigned int *pins;
        unsigned int npins;
        int func;
        u16 reg;
        u8 bit;
        bool drv;
    }

.. _`tz1090_pdc_pingroup.members`:

Members
-------

name
    Name of pin group.

pins
    Array of pin numbers in this pin group.

npins
    Number of pins in this pin group.

func
    Function enabled by the mux.

reg
    Mux register offset.

bit
    Mux register bit.

drv
    Drive control supported, otherwise it's a mux.
    This means Schmitt, Slew, and Drive strength.

.. _`tz1090_pdc_pingroup.description`:

Description
-----------

A representation of a group of pins (possibly just one pin) in the TZ1090
PDC pin controller. Each group allows some parameter or parameters to be
configured. The most common is mux function selection.

.. _`mux_pg`:

MUX_PG
======

.. c:function::  MUX_PG( pg_name,  f0,  mux_r,  mux_b)

    Initialise a pin group with mux control

    :param  pg_name:
        Pin group name (stringified, \_pins appended to get pins array)

    :param  f0:
        Function 0 (TZ1090_PDC_MUX\_ is prepended)

    :param  mux_r:
        Mux register (REG_PINCTRL\_ is prepended)

    :param  mux_b:
        Bit number in register of mux field

.. _`drv_pg`:

DRV_PG
======

.. c:function::  DRV_PG( pg_name)

    Initialise a pin group with drive control

    :param  pg_name:
        Pin group name (stringified, \_pins appended to get pins array)

.. _`tz1090_pdc_pmx`:

struct tz1090_pdc_pmx
=====================

.. c:type:: struct tz1090_pdc_pmx

    Private pinctrl data

.. _`tz1090_pdc_pmx.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_pdc_pmx {
        struct device *dev;
        struct pinctrl_dev *pctl;
        void __iomem *regs;
        spinlock_t lock;
        u32 mux_en;
        u32 gpio_en;
    }

.. _`tz1090_pdc_pmx.members`:

Members
-------

dev
    Platform device

pctl
    Pin control device

regs
    Register region

lock
    Lock protecting coherency of mux_en and gpio_en

mux_en
    Muxes that have been enabled

gpio_en
    Muxable GPIOs that have been enabled

.. _`get_group_selector`:

get_group_selector
==================

.. c:function:: int get_group_selector(const char *pin_group)

    returns the group selector for a group

    :param const char \*pin_group:
        the pin group to look up

.. _`get_group_selector.description`:

Description
-----------

This is the same as pinctrl_get_group_selector except it doesn't produce an
error message if the group isn't found or debug messages.

.. _`tz1090_pdc_pinctrl_mux`:

tz1090_pdc_pinctrl_mux
======================

.. c:function:: void tz1090_pdc_pinctrl_mux(struct tz1090_pdc_pmx *pmx, const struct tz1090_pdc_pingroup *grp)

    update mux bit

    :param struct tz1090_pdc_pmx \*pmx:
        Pinmux data

    :param const struct tz1090_pdc_pingroup \*grp:
        Pin mux group

.. This file was automatic generated / don't edit.

