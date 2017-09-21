.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/sprd/pinctrl-sprd.c

.. _`sprd_pin`:

struct sprd_pin
===============

.. c:type:: struct sprd_pin

    represent one pin's description

.. _`sprd_pin.definition`:

Definition
----------

.. code-block:: c

    struct sprd_pin {
        const char *name;
        unsigned int number;
        enum pin_type type;
        unsigned long reg;
        unsigned long bit_offset;
        unsigned long bit_width;
    }

.. _`sprd_pin.members`:

Members
-------

name
    pin name

number
    pin number

type
    pin type, can be GLOBAL_CTRL_PIN/COMMON_PIN/MISC_PIN

reg
    pin register address

bit_offset
    bit offset in pin register

bit_width
    bit width in pin register

.. _`sprd_pin_group`:

struct sprd_pin_group
=====================

.. c:type:: struct sprd_pin_group

    represent one group's description

.. _`sprd_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct sprd_pin_group {
        const char *name;
        unsigned int npins;
        unsigned int *pins;
    }

.. _`sprd_pin_group.members`:

Members
-------

name
    group name

npins
    pin numbers of this group

pins
    pointer to pins array

.. _`sprd_pinctrl_soc_info`:

struct sprd_pinctrl_soc_info
============================

.. c:type:: struct sprd_pinctrl_soc_info

    represent the SoC's pins description

.. _`sprd_pinctrl_soc_info.definition`:

Definition
----------

.. code-block:: c

    struct sprd_pinctrl_soc_info {
        struct sprd_pin_group *groups;
        unsigned int ngroups;
        struct sprd_pin *pins;
        unsigned int npins;
        const char **grp_names;
    }

.. _`sprd_pinctrl_soc_info.members`:

Members
-------

groups
    pointer to groups of pins

ngroups
    group numbers of the whole SoC

pins
    pointer to pins description

npins
    pin numbers of the whole SoC

grp_names
    pointer to group names array

.. _`sprd_pinctrl`:

struct sprd_pinctrl
===================

.. c:type:: struct sprd_pinctrl

    represent the pin controller device

.. _`sprd_pinctrl.definition`:

Definition
----------

.. code-block:: c

    struct sprd_pinctrl {
        struct device *dev;
        struct pinctrl_dev *pctl;
        void __iomem *base;
        struct sprd_pinctrl_soc_info *info;
    }

.. _`sprd_pinctrl.members`:

Members
-------

dev
    pointer to the device structure

pctl
    pointer to the pinctrl handle

base
    base address of the controller

info
    pointer to SoC's pins description information

.. This file was automatic generated / don't edit.

