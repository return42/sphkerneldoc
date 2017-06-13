.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/spear/pinctrl-spear.h

.. _`spear_pmx_mode`:

struct spear_pmx_mode
=====================

.. c:type:: struct spear_pmx_mode

    SPEAr pmx mode

.. _`spear_pmx_mode.definition`:

Definition
----------

.. code-block:: c

    struct spear_pmx_mode {
        const char *const name;
        u16 mode;
        u16 reg;
        u16 mask;
        u32 val;
    }

.. _`spear_pmx_mode.members`:

Members
-------

name
    name of pmx mode

mode
    mode id

reg
    register for configuring this mode

mask
    mask of this mode in reg

val
    val to be configured at reg after doing (val & mask)

.. _`spear_muxreg`:

struct spear_muxreg
===================

.. c:type:: struct spear_muxreg

    SPEAr mux reg configuration

.. _`spear_muxreg.definition`:

Definition
----------

.. code-block:: c

    struct spear_muxreg {
        u16 reg;
        u32 mask;
        u32 val;
    }

.. _`spear_muxreg.members`:

Members
-------

reg
    register offset

mask
    mask bits

val
    val to be written on mask bits

.. _`spear_modemux`:

struct spear_modemux
====================

.. c:type:: struct spear_modemux

    SPEAr mode mux configuration

.. _`spear_modemux.definition`:

Definition
----------

.. code-block:: c

    struct spear_modemux {
        u16 modes;
        u8 nmuxregs;
        struct spear_muxreg *muxregs;
    }

.. _`spear_modemux.members`:

Members
-------

modes
    mode ids supported by this group of muxregs

nmuxregs
    number of muxreg configurations to be done for modes

muxregs
    array of muxreg configurations to be done for modes

.. _`spear_pingroup`:

struct spear_pingroup
=====================

.. c:type:: struct spear_pingroup

    SPEAr pin group configurations

.. _`spear_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct spear_pingroup {
        const char *name;
        const unsigned *pins;
        unsigned npins;
        struct spear_modemux *modemuxs;
        unsigned nmodemuxs;
    }

.. _`spear_pingroup.members`:

Members
-------

name
    name of pin group

pins
    array containing pin numbers

npins
    size of pins array

modemuxs
    array of modemux configurations for this pin group

nmodemuxs
    size of array modemuxs

.. _`spear_pingroup.description`:

Description
-----------

A representation of a group of pins in the SPEAr pin controller. Each group
allows some parameter or parameters to be configured.

.. _`spear_function`:

struct spear_function
=====================

.. c:type:: struct spear_function

    SPEAr pinctrl mux function

.. _`spear_function.definition`:

Definition
----------

.. code-block:: c

    struct spear_function {
        const char *name;
        const char *const *groups;
        unsigned ngroups;
    }

.. _`spear_function.members`:

Members
-------

name
    The name of the function, exported to pinctrl core.

groups
    An array of pin groups that may select this function.

ngroups
    The number of entries in \ ``groups``\ .

.. _`spear_pinctrl_machdata`:

struct spear_pinctrl_machdata
=============================

.. c:type:: struct spear_pinctrl_machdata

    SPEAr pin controller machine driver configuration

.. _`spear_pinctrl_machdata.definition`:

Definition
----------

.. code-block:: c

    struct spear_pinctrl_machdata {
        const struct pinctrl_pin_desc *pins;
        unsigned npins;
        struct spear_function **functions;
        unsigned nfunctions;
        struct spear_pingroup **groups;
        unsigned ngroups;
        struct spear_gpio_pingroup *gpio_pingroups;
        void (*gpio_request_endisable)(struct spear_pmx *pmx, int offset, bool enable);
        unsigned ngpio_pingroups;
        bool modes_supported;
        u16 mode;
        struct spear_pmx_mode **pmx_modes;
        unsigned npmx_modes;
    }

.. _`spear_pinctrl_machdata.members`:

Members
-------

pins
    An array describing all pins the pin controller affects.
    All pins which are also GPIOs must be listed first within the \*array,
    and be numbered identically to the GPIO controller's \*numbering.

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

gpio_pingroups
    gpio pingroups

gpio_request_endisable
    *undescribed*

ngpio_pingroups
    gpio pingroups count

modes_supported
    Does SoC support modes

mode
    mode configured from probe

pmx_modes
    array of modes supported by SoC

npmx_modes
    number of entries in pmx_modes.

.. _`spear_pmx`:

struct spear_pmx
================

.. c:type:: struct spear_pmx

    SPEAr pinctrl mux

.. _`spear_pmx.definition`:

Definition
----------

.. code-block:: c

    struct spear_pmx {
        struct device *dev;
        struct pinctrl_dev *pctl;
        struct spear_pinctrl_machdata *machdata;
        void __iomem *vbase;
    }

.. _`spear_pmx.members`:

Members
-------

dev
    pointer to struct dev of platform_device registered

pctl
    pointer to struct pinctrl_dev

machdata
    pointer to SoC or machine specific structure

vbase
    virtual base address of pinmux controller

.. This file was automatic generated / don't edit.

