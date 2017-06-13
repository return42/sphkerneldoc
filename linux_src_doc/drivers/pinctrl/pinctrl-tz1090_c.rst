.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-tz1090.c

.. _`tz1090_function`:

struct tz1090_function
======================

.. c:type:: struct tz1090_function

    TZ1090 pinctrl mux function

.. _`tz1090_function.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_function {
        const char *name;
        const char * const *groups;
        unsigned int ngroups;
    }

.. _`tz1090_function.members`:

Members
-------

name
    The name of the function, exported to pinctrl core.

groups
    An array of pin groups that may select this function.

ngroups
    The number of entries in \ ``groups``\ .

.. _`tz1090_muxdesc`:

struct tz1090_muxdesc
=====================

.. c:type:: struct tz1090_muxdesc

    TZ1090 individual mux description

.. _`tz1090_muxdesc.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_muxdesc {
        int funcs;
        u16 reg;
        u8 bit;
        u8 width;
    }

.. _`tz1090_muxdesc.members`:

Members
-------

funcs
    Function for each mux value.

reg
    Mux register offset. 0 if unsupported.

bit
    Mux register bit. 0 if unsupported.

width
    Mux field width. 0 if unsupported.

.. _`tz1090_muxdesc.description`:

Description
-----------

A representation of a group of signals (possibly just one signal) in the
TZ1090 which can be muxed to a set of functions or sub muxes.

.. _`tz1090_pingroup`:

struct tz1090_pingroup
======================

.. c:type:: struct tz1090_pingroup

    TZ1090 pin group

.. _`tz1090_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_pingroup {
        const char *name;
        const unsigned int *pins;
        unsigned int npins;
        struct tz1090_muxdesc mux;
        bool drv;
        u8 slw_bit;
        int func;
        unsigned int func_count;
    }

.. _`tz1090_pingroup.members`:

Members
-------

name
    Name of pin group.

pins
    Array of pin numbers in this pin group.

npins
    Number of pins in this pin group.

mux
    Top level mux.

drv
    Drive control supported, 0 if unsupported.
    This means Schmitt, Slew, and Drive strength.

slw_bit
    Slew register bit. 0 if unsupported.
    The same bit is used for Schmitt, and Drive (\*2).

func
    Currently muxed function.

func_count
    Number of pins using current mux function.

.. _`tz1090_pingroup.description`:

Description
-----------

A representation of a group of pins (possibly just one pin) in the TZ1090
pin controller. Each group allows some parameter or parameters to be
configured. The most common is mux function selection.

.. _`mux`:

MUX
===

.. c:function::  MUX( f0,  f1,  f2,  f3,  f4,  mux_r,  mux_b,  mux_w)

    Initialise a mux description.

    :param  f0:
        Function 0 (TZ1090_MUX\_ is prepended, NA for none)

    :param  f1:
        Function 1 (TZ1090_MUX\_ is prepended, NA for none)

    :param  f2:
        Function 2 (TZ1090_MUX\_ is prepended, NA for none)

    :param  f3:
        Function 3 (TZ1090_MUX\_ is prepended, NA for none)

    :param  f4:
        Function 4 (TZ1090_MUX\_ is prepended, NA for none)

    :param  mux_r:
        Mux register (REG_PINCTRL\_ is prepended)

    :param  mux_b:
        Bit number in register that the mux field begins

    :param  mux_w:
        Width of mux field in register

.. _`define_submux`:

DEFINE_SUBMUX
=============

.. c:function::  DEFINE_SUBMUX( mux,  f0,  f1,  f2,  f3,  f4,  mux_r,  mux_b,  mux_w)

    Defines a submux description separate from a pin group.

    :param  mux:
        Mux name (_submux is appended)

    :param  f0:
        Function 0 (TZ1090_MUX\_ is prepended, NA for none)

    :param  f1:
        Function 1 (TZ1090_MUX\_ is prepended, NA for none)

    :param  f2:
        Function 2 (TZ1090_MUX\_ is prepended, NA for none)

    :param  f3:
        Function 3 (TZ1090_MUX\_ is prepended, NA for none)

    :param  f4:
        Function 4 (TZ1090_MUX\_ is prepended, NA for none)

    :param  mux_r:
        Mux register (REG_PINCTRL\_ is prepended)

    :param  mux_b:
        Bit number in register that the mux field begins

    :param  mux_w:
        Width of mux field in register

.. _`define_submux.description`:

Description
-----------

A sub mux is a nested mux that can be bound to a magic function number used
by another mux description. For example value 4 of the top level mux might
correspond to a function which has a submux pointed to in tz1090_submux[].
The outer mux can then take on any function in the top level mux or the
submux, and if a submux function is chosen both muxes are updated to route
the signal from the submux.

The submux can be defined with DEFINE_SUBMUX and pointed to from
tz1090_submux[] using SUBMUX.

.. _`submux`:

SUBMUX
======

.. c:function::  SUBMUX( f,  submux)

    Link a submux to a function number.

    :param  f:
        Function name (TZ1090_MUX\_ is prepended)

    :param  submux:
        Submux name (_submux is appended)

.. _`submux.description`:

Description
-----------

For use in tz1090_submux[] initialisation to link an intermediate function
number to a particular submux description. It indicates that when the
function is chosen the signal is connected to the submux.

.. _`simple_pg`:

SIMPLE_PG
=========

.. c:function::  SIMPLE_PG( pg_name)

    Initialise a simple convenience pin group

    :param  pg_name:
        Pin group name (stringified, \_pins appended to get pins array)

.. _`simple_pg.description`:

Description
-----------

A simple pin group is simply used for binding pins together so they can be
referred to by a single name instead of having to list every pin
individually.

.. _`drv_pg`:

DRV_PG
======

.. c:function::  DRV_PG( pg_name,  slw_b)

    Initialise a pin group with drive control

    :param  pg_name:
        Pin group name (stringified, \_pins appended to get pins array)

    :param  slw_b:
        Slew register bit.
        The same bit is used for Schmitt, and Drive (\*2).

.. _`tz1090_init_mux_pins`:

tz1090_init_mux_pins
====================

.. c:function:: void tz1090_init_mux_pins( void)

    Initialise GPIO pin to mux group mapping.

    :param  void:
        no arguments

.. _`tz1090_init_mux_pins.description`:

Description
-----------

Initialises the tz1090_mux_pins[] array to be the inverse of the pin lists in
each pin mux group in tz1090_mux_groups[].

It is assumed that no pin mux groups overlap (share pins).

.. _`tz1090_pmx`:

struct tz1090_pmx
=================

.. c:type:: struct tz1090_pmx

    Private pinctrl data

.. _`tz1090_pmx.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_pmx {
        struct device *dev;
        struct pinctrl_dev *pctl;
        void __iomem *regs;
        spinlock_t lock;
        u32 pin_en;
        u32 gpio_en;
    }

.. _`tz1090_pmx.members`:

Members
-------

dev
    Platform device

pctl
    Pin control device

regs
    Register region

lock
    Lock protecting coherency of pin_en, gpio_en, and SELECT regs

pin_en
    Pins that have been enabled (32 pins packed into each element)

gpio_en
    GPIOs that have been enabled (32 pins packed into each element)

.. _`tz1090_pinctrl_select`:

tz1090_pinctrl_select
=====================

.. c:function:: void tz1090_pinctrl_select(struct tz1090_pmx *pmx, unsigned int pin)

    update bit in SELECT register

    :param struct tz1090_pmx \*pmx:
        Pinmux data

    :param unsigned int pin:
        Pin number (must be within GPIO range)

.. _`tz1090_pinctrl_gpio_select`:

tz1090_pinctrl_gpio_select
==========================

.. c:function:: void tz1090_pinctrl_gpio_select(struct tz1090_pmx *pmx, unsigned int pin, bool gpio_select)

    enable/disable GPIO usage for a pin

    :param struct tz1090_pmx \*pmx:
        Pinmux data

    :param unsigned int pin:
        Pin number

    :param bool gpio_select:
        true to enable pin as GPIO,
        false to leave control to whatever function is enabled

.. _`tz1090_pinctrl_gpio_select.description`:

Description
-----------

Records that GPIO usage is enabled/disabled so that enabling a function
doesn't override the SELECT register bit.

.. _`tz1090_pinctrl_perip_select`:

tz1090_pinctrl_perip_select
===========================

.. c:function:: void tz1090_pinctrl_perip_select(struct tz1090_pmx *pmx, unsigned int pin, bool perip_select)

    enable/disable peripheral interface for a pin

    :param struct tz1090_pmx \*pmx:
        Pinmux data

    :param unsigned int pin:
        Pin number

    :param bool perip_select:
        true to enable peripheral interface when not GPIO,
        false to leave pin in GPIO mode

.. _`tz1090_pinctrl_perip_select.description`:

Description
-----------

Records that peripheral usage is enabled/disabled so that SELECT register can
be set appropriately when GPIO is disabled.

.. _`tz1090_pinctrl_enable_mux`:

tz1090_pinctrl_enable_mux
=========================

.. c:function:: int tz1090_pinctrl_enable_mux(struct tz1090_pmx *pmx, const struct tz1090_muxdesc *desc, unsigned int function)

    Switch a pin mux group to a function.

    :param struct tz1090_pmx \*pmx:
        Pinmux data

    :param const struct tz1090_muxdesc \*desc:
        Pinmux description

    :param unsigned int function:
        Function to switch to

.. _`tz1090_pinctrl_enable_mux.description`:

Description
-----------

Enable a particular function on a pin mux group. Since pin mux descriptions
are nested this function is recursive.

.. _`tz1090_pinctrl_set_mux`:

tz1090_pinctrl_set_mux
======================

.. c:function:: int tz1090_pinctrl_set_mux(struct pinctrl_dev *pctldev, unsigned int function, unsigned int group)

    Enable a function on a pin group.

    :param struct pinctrl_dev \*pctldev:
        Pin control data

    :param unsigned int function:
        Function index to enable

    :param unsigned int group:
        Group index to enable

.. _`tz1090_pinctrl_set_mux.description`:

Description
-----------

Enable a particular function on a group of pins. The per GPIO pin pseudo pin
groups can be used (in which case the pin will be enabled in peripheral mode
and if it belongs to a pin mux group the mux will be switched if it isn't
already in use. Some convenience pin groups can also be used in which case
the effect is the same as enabling the function on each individual pin in the
group.

.. _`tz1090_pinctrl_gpio_request_enable`:

tz1090_pinctrl_gpio_request_enable
==================================

.. c:function:: int tz1090_pinctrl_gpio_request_enable(struct pinctrl_dev *pctldev, struct pinctrl_gpio_range *range, unsigned int pin)

    Put pin in GPIO mode.

    :param struct pinctrl_dev \*pctldev:
        Pin control data

    :param struct pinctrl_gpio_range \*range:
        GPIO range

    :param unsigned int pin:
        Pin number

.. _`tz1090_pinctrl_gpio_request_enable.description`:

Description
-----------

Puts a particular pin into GPIO mode, disabling peripheral control until it's
disabled again.

.. _`tz1090_pinctrl_gpio_disable_free`:

tz1090_pinctrl_gpio_disable_free
================================

.. c:function:: void tz1090_pinctrl_gpio_disable_free(struct pinctrl_dev *pctldev, struct pinctrl_gpio_range *range, unsigned int pin)

    Take pin out of GPIO mode.

    :param struct pinctrl_dev \*pctldev:
        Pin control data

    :param struct pinctrl_gpio_range \*range:
        GPIO range

    :param unsigned int pin:
        Pin number

.. _`tz1090_pinctrl_gpio_disable_free.description`:

Description
-----------

Take a particular pin out of GPIO mode. If the pin is enabled for a
peripheral it will return to peripheral mode.

.. This file was automatic generated / don't edit.

