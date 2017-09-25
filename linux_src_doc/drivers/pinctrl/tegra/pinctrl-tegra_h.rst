.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/tegra/pinctrl-tegra.h

.. _`tegra_function`:

struct tegra_function
=====================

.. c:type:: struct tegra_function

    Tegra pinctrl mux function

.. _`tegra_function.definition`:

Definition
----------

.. code-block:: c

    struct tegra_function {
        const char *name;
        const char **groups;
        unsigned ngroups;
    }

.. _`tegra_function.members`:

Members
-------

name
    The name of the function, exported to pinctrl core.

groups
    An array of pin groups that may select this function.

ngroups
    The number of entries in \ ``groups``\ .

.. _`tegra_pingroup`:

struct tegra_pingroup
=====================

.. c:type:: struct tegra_pingroup

    Tegra pin group \ ``name``\                 The name of the pin group. \ ``pins``\                 An array of pin IDs included in this pin group. \ ``npins``\                The number of entries in \ ``pins``\ . \ ``funcs``\                The mux functions which can be muxed onto this group.

.. _`tegra_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct tegra_pingroup {
        const char *name;
        const unsigned *pins;
        u8 npins;
        u8 funcs[4];
        s16 mux_reg;
        s16 pupd_reg;
        s16 tri_reg;
        s16 drv_reg;
        u32 mux_bank:2;
        u32 pupd_bank:2;
        u32 tri_bank:2;
        u32 drv_bank:2;
        s32 mux_bit:6;
        s32 pupd_bit:6;
        s32 tri_bit:6;
        s32 parked_bit:6;
        s32 einput_bit:6;
        s32 odrain_bit:6;
        s32 lock_bit:6;
        s32 ioreset_bit:6;
        s32 rcv_sel_bit:6;
        s32 hsm_bit:6;
        s32 schmitt_bit:6;
        s32 lpmd_bit:6;
        s32 drvdn_bit:6;
        s32 drvup_bit:6;
        s32 slwr_bit:6;
        s32 slwf_bit:6;
        s32 drvtype_bit:6;
        s32 drvdn_width:6;
        s32 drvup_width:6;
        s32 slwr_width:6;
        s32 slwf_width:6;
    }

.. _`tegra_pingroup.members`:

Members
-------

name
    *undescribed*

pins
    *undescribed*

npins
    *undescribed*

funcs
    *undescribed*

mux_reg
    Mux register offset.
    This register contains the mux, einput, odrain, lock,
    ioreset, rcv_sel parameters.

pupd_reg
    Pull-up/down register offset.

tri_reg
    Tri-state register offset.

drv_reg
    Drive fields register offset.
    This register contains hsm, schmitt, lpmd, drvdn,
    drvup, slwr, slwf, and drvtype parameters.

mux_bank
    Mux register bank.

pupd_bank
    Pull-up/down register bank.

tri_bank
    Tri-state register bank.

drv_bank
    Drive fields register bank.

mux_bit
    Mux register bit.

pupd_bit
    Pull-up/down register bit.

tri_bit
    Tri-state register bit.

parked_bit
    Parked register bit. -1 if unsupported.

einput_bit
    Enable-input register bit.

odrain_bit
    Open-drain register bit.

lock_bit
    Lock register bit.

ioreset_bit
    IO reset register bit.

rcv_sel_bit
    Receiver select bit.

hsm_bit
    High Speed Mode register bit.

schmitt_bit
    Scmitt register bit.

lpmd_bit
    Low Power Mode register bit.

drvdn_bit
    Drive Down register bit.

drvup_bit
    Drive Up register bit.

slwr_bit
    Slew Rising register bit.

slwf_bit
    Slew Falling register bit.

drvtype_bit
    Drive type register bit.

drvdn_width
    Drive Down field width.

drvup_width
    Drive Up field width.

slwr_width
    Slew Rising field width.

slwf_width
    Slew Falling field width.

.. _`tegra_pingroup.description`:

Description
-----------

-1 in a \*\_reg field means that feature is unsupported for this group.
\*\_bank and \*\_reg values are irrelevant when \*\_reg is -1.
When \*\_reg is valid, \*\_bit may be -1 to indicate an unsupported feature.

A representation of a group of pins (possibly just one pin) in the Tegra
pin controller. Each group allows some parameter or parameters to be
configured. The most common is mux function selection. Many others exist
such as pull-up/down, tri-state, etc. Tegra's pin controller is complex;
certain groups may only support configuring certain parameters, hence
each parameter is optional.

.. _`tegra_pinctrl_soc_data`:

struct tegra_pinctrl_soc_data
=============================

.. c:type:: struct tegra_pinctrl_soc_data

    Tegra pin controller driver configuration

.. _`tegra_pinctrl_soc_data.definition`:

Definition
----------

.. code-block:: c

    struct tegra_pinctrl_soc_data {
        unsigned ngpios;
        const struct pinctrl_pin_desc *pins;
        unsigned npins;
        struct tegra_function *functions;
        unsigned nfunctions;
        const struct tegra_pingroup *groups;
        unsigned ngroups;
        bool hsm_in_mux;
        bool schmitt_in_mux;
        bool drvtype_in_mux;
    }

.. _`tegra_pinctrl_soc_data.members`:

Members
-------

ngpios
    The number of GPIO pins the pin controller HW affects.

pins
    An array describing all pins the pin controller affects.
    All pins which are also GPIOs must be listed first within the
    array, and be numbered identically to the GPIO controller's
    numbering.

npins
    The numbmer of entries in \ ``pins``\ .

functions
    An array describing all mux functions the SoC supports.

nfunctions
    The numbmer of entries in \ ``functions``\ .

groups
    An array describing all pin groups the pin SoC supports.

ngroups
    The numbmer of entries in \ ``groups``\ .

hsm_in_mux
    *undescribed*

schmitt_in_mux
    *undescribed*

drvtype_in_mux
    *undescribed*

.. This file was automatic generated / don't edit.

