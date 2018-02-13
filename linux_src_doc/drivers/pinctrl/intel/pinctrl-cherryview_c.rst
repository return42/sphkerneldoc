.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/intel/pinctrl-cherryview.c

.. _`chv_alternate_function`:

struct chv_alternate_function
=============================

.. c:type:: struct chv_alternate_function

    A per group or per pin alternate function

.. _`chv_alternate_function.definition`:

Definition
----------

.. code-block:: c

    struct chv_alternate_function {
        unsigned pin;
        u8 mode;
        bool invert_oe;
    }

.. _`chv_alternate_function.members`:

Members
-------

pin
    Pin number (only used in per pin configs)

mode
    Mode the pin should be set in

invert_oe
    Invert OE for this pin

.. _`chv_pingroup`:

struct chv_pingroup
===================

.. c:type:: struct chv_pingroup

    describes a CHV pin group

.. _`chv_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct chv_pingroup {
        const char *name;
        const unsigned *pins;
        size_t npins;
        struct chv_alternate_function altfunc;
        const struct chv_alternate_function *overrides;
        size_t noverrides;
    }

.. _`chv_pingroup.members`:

Members
-------

name
    Name of the group

pins
    An array of pins in this group

npins
    Number of pins in this group

altfunc
    Alternate function applied to all pins in this group

overrides
    Alternate function override per pin or \ ``NULL``\  if not used

noverrides
    Number of per pin alternate function overrides if
    \ ``overrides``\  != NULL.

.. _`chv_function`:

struct chv_function
===================

.. c:type:: struct chv_function

    A CHV pinmux function

.. _`chv_function.definition`:

Definition
----------

.. code-block:: c

    struct chv_function {
        const char *name;
        const char * const *groups;
        size_t ngroups;
    }

.. _`chv_function.members`:

Members
-------

name
    Name of the function

groups
    An array of groups for this function

ngroups
    Number of groups in \ ``groups``\ 

.. _`chv_gpio_pinrange`:

struct chv_gpio_pinrange
========================

.. c:type:: struct chv_gpio_pinrange

    A range of pins that can be used as GPIOs

.. _`chv_gpio_pinrange.definition`:

Definition
----------

.. code-block:: c

    struct chv_gpio_pinrange {
        unsigned base;
        unsigned npins;
    }

.. _`chv_gpio_pinrange.members`:

Members
-------

base
    Start pin number

npins
    Number of pins in this range

.. _`chv_community`:

struct chv_community
====================

.. c:type:: struct chv_community

    A community specific configuration

.. _`chv_community.definition`:

Definition
----------

.. code-block:: c

    struct chv_community {
        const char *uid;
        const struct pinctrl_pin_desc *pins;
        size_t npins;
        const struct chv_pingroup *groups;
        size_t ngroups;
        const struct chv_function *functions;
        size_t nfunctions;
        const struct chv_gpio_pinrange *gpio_ranges;
        size_t ngpio_ranges;
        size_t nirqs;
        acpi_adr_space_type acpi_space_id;
    }

.. _`chv_community.members`:

Members
-------

uid
    ACPI \_UID used to match the community

pins
    All pins in this community

npins
    Number of pins

groups
    All groups in this community

ngroups
    Number of groups

functions
    All functions in this community

nfunctions
    Number of functions

gpio_ranges
    An array of GPIO ranges in this community

ngpio_ranges
    Number of GPIO ranges

nirqs
    Total number of IRQs this community can generate

acpi_space_id
    *undescribed*

.. _`chv_pinctrl`:

struct chv_pinctrl
==================

.. c:type:: struct chv_pinctrl

    CHV pinctrl private structure

.. _`chv_pinctrl.definition`:

Definition
----------

.. code-block:: c

    struct chv_pinctrl {
        struct device *dev;
        struct pinctrl_desc pctldesc;
        struct pinctrl_dev *pctldev;
        struct gpio_chip chip;
        void __iomem *regs;
        unsigned intr_lines[16];
        const struct chv_community *community;
        u32 saved_intmask;
        struct chv_pin_context *saved_pin_context;
    }

.. _`chv_pinctrl.members`:

Members
-------

dev
    Pointer to the parent device

pctldesc
    Pin controller description

pctldev
    Pointer to the pin controller device

chip
    GPIO chip in this pin controller

regs
    MMIO registers

intr_lines
    Stores mapping between 16 HW interrupt wires and GPIO
    offset (in GPIO number space)

community
    Community this pinctrl instance represents

saved_intmask
    *undescribed*

saved_pin_context
    *undescribed*

.. _`chv_pinctrl.description`:

Description
-----------

The first group in \ ``groups``\  is expected to contain all pins that can be
used as GPIOs.

.. This file was automatic generated / don't edit.

