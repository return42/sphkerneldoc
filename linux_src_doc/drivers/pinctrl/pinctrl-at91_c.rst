.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-at91.c

.. _`drive_strength_default`:

DRIVE_STRENGTH_DEFAULT
======================

.. c:function::  DRIVE_STRENGTH_DEFAULT()

    settings. They are not necessarily the same value as the register setting. The actual drive strength current of low, medium and high must be looked up from the corresponding device datasheet. This value is different for pins that are even in the same banks. It is also dependent on VCC. DRIVE_STRENGTH_DEFAULT is just a placeholder to avoid changing the drive strength when there is no dt config for it.

.. _`at91_pmx_func`:

struct at91_pmx_func
====================

.. c:type:: struct at91_pmx_func

    describes AT91 pinmux functions

.. _`at91_pmx_func.definition`:

Definition
----------

.. code-block:: c

    struct at91_pmx_func {
        const char *name;
        const char **groups;
        unsigned ngroups;
    }

.. _`at91_pmx_func.members`:

Members
-------

name
    the name of this specific function

groups
    corresponding pin groups

ngroups
    the number of groups

.. _`at91_pmx_pin`:

struct at91_pmx_pin
===================

.. c:type:: struct at91_pmx_pin

    describes an At91 pin mux

.. _`at91_pmx_pin.definition`:

Definition
----------

.. code-block:: c

    struct at91_pmx_pin {
        uint32_t bank;
        uint32_t pin;
        enum at91_mux mux;
        unsigned long conf;
    }

.. _`at91_pmx_pin.members`:

Members
-------

bank
    the bank of the pin

pin
    the pin number in the \ ``bank``\ 

mux
    the mux mode : gpio or periph_x of the pin i.e. alternate function.

conf
    the configuration of the pin: PULL_UP, MULTIDRIVE etc...

.. _`at91_pin_group`:

struct at91_pin_group
=====================

.. c:type:: struct at91_pin_group

    describes an At91 pin group

.. _`at91_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct at91_pin_group {
        const char *name;
        struct at91_pmx_pin *pins_conf;
        unsigned int *pins;
        unsigned npins;
    }

.. _`at91_pin_group.members`:

Members
-------

name
    the name of this specific pin group

pins_conf
    the mux mode for each pin in this group. The size of this
    array is the same as pins.

pins
    an array of discrete physical pins used in this group, taken
    from the driver-local pin enumeration space

npins
    the number of pins in this group array, i.e. the number of
    elements in .pins so we can iterate over that array

.. _`at91_pinctrl_mux_ops`:

struct at91_pinctrl_mux_ops
===========================

.. c:type:: struct at91_pinctrl_mux_ops

    describes an AT91 mux ops group on new IP with support for periph C and D the way to mux in periph A and B has changed So provide the right call back if not present means the IP does not support it

.. _`at91_pinctrl_mux_ops.definition`:

Definition
----------

.. code-block:: c

    struct at91_pinctrl_mux_ops {
        enum at91_mux (*get_periph)(void __iomem *pio, unsigned mask);
        void (*mux_A_periph)(void __iomem *pio, unsigned mask);
        void (*mux_B_periph)(void __iomem *pio, unsigned mask);
        void (*mux_C_periph)(void __iomem *pio, unsigned mask);
        void (*mux_D_periph)(void __iomem *pio, unsigned mask);
        bool (*get_deglitch)(void __iomem *pio, unsigned pin);
        void (*set_deglitch)(void __iomem *pio, unsigned mask, bool is_on);
        bool (*get_debounce)(void __iomem *pio, unsigned pin, u32 *div);
        void (*set_debounce)(void __iomem *pio, unsigned mask, bool is_on, u32 div);
        bool (*get_pulldown)(void __iomem *pio, unsigned pin);
        void (*set_pulldown)(void __iomem *pio, unsigned mask, bool is_on);
        bool (*get_schmitt_trig)(void __iomem *pio, unsigned pin);
        void (*disable_schmitt_trig)(void __iomem *pio, unsigned mask);
        unsigned (*get_drivestrength)(void __iomem *pio, unsigned pin);
        void (*set_drivestrength)(void __iomem *pio, unsigned pin,u32 strength);
        int (*irq_type)(struct irq_data *d, unsigned type);
    }

.. _`at91_pinctrl_mux_ops.members`:

Members
-------

get_periph
    return the periph mode configured

mux_A_periph
    mux as periph A

mux_B_periph
    mux as periph B

mux_C_periph
    mux as periph C

mux_D_periph
    mux as periph D

get_deglitch
    get deglitch status

set_deglitch
    enable/disable deglitch

get_debounce
    get debounce status

set_debounce
    enable/disable debounce

get_pulldown
    get pulldown status

set_pulldown
    enable/disable pulldown

get_schmitt_trig
    get schmitt trigger status

disable_schmitt_trig
    disable schmitt trigger

get_drivestrength
    *undescribed*

set_drivestrength
    *undescribed*

irq_type
    return irq type

.. This file was automatic generated / don't edit.

