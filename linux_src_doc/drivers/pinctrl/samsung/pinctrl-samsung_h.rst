.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/samsung/pinctrl-samsung.h

.. _`pincfg_type`:

enum pincfg_type
================

.. c:type:: enum pincfg_type

    possible pin configuration types supported.

.. _`pincfg_type.definition`:

Definition
----------

.. code-block:: c

    enum pincfg_type {
        PINCFG_TYPE_FUNC,
        PINCFG_TYPE_DAT,
        PINCFG_TYPE_PUD,
        PINCFG_TYPE_DRV,
        PINCFG_TYPE_CON_PDN,
        PINCFG_TYPE_PUD_PDN,
        PINCFG_TYPE_NUM
    };

.. _`pincfg_type.constants`:

Constants
---------

PINCFG_TYPE_FUNC
    Function configuration.

PINCFG_TYPE_DAT
    Pin value configuration.

PINCFG_TYPE_PUD
    Pull up/down configuration.

PINCFG_TYPE_DRV
    Drive strength configuration.

PINCFG_TYPE_CON_PDN
    Pin function in power down mode.

PINCFG_TYPE_PUD_PDN
    Pull up/down configuration in power down mode.

PINCFG_TYPE_NUM
    *undescribed*

.. _`eint_type`:

enum eint_type
==============

.. c:type:: enum eint_type

    possible external interrupt types.

.. _`eint_type.definition`:

Definition
----------

.. code-block:: c

    enum eint_type {
        EINT_TYPE_NONE,
        EINT_TYPE_GPIO,
        EINT_TYPE_WKUP,
        EINT_TYPE_WKUP_MUX
    };

.. _`eint_type.constants`:

Constants
---------

EINT_TYPE_NONE
    bank does not support external interrupts

EINT_TYPE_GPIO
    bank supportes external gpio interrupts

EINT_TYPE_WKUP
    bank supportes external wakeup interrupts

EINT_TYPE_WKUP_MUX
    bank supports multiplexed external wakeup interrupts

.. _`eint_type.description`:

Description
-----------

Samsung GPIO controller groups all the available pins into banks. The pins
in a pin bank can support external gpio interrupts or external wakeup
interrupts or no interrupts at all. From a software perspective, the only
difference between external gpio and external wakeup interrupts is that
the wakeup interrupts can additionally wakeup the system if it is in
suspended state.

.. _`samsung_pin_bank_type`:

struct samsung_pin_bank_type
============================

.. c:type:: struct samsung_pin_bank_type

    pin bank type description

.. _`samsung_pin_bank_type.definition`:

Definition
----------

.. code-block:: c

    struct samsung_pin_bank_type {
        u8 fld_width[PINCFG_TYPE_NUM];
        u8 reg_offset[PINCFG_TYPE_NUM];
    }

.. _`samsung_pin_bank_type.members`:

Members
-------

fld_width
    widths of configuration bitfields (0 if unavailable)

reg_offset
    offsets of configuration registers (don't care of width is 0)

.. _`samsung_pin_bank_data`:

struct samsung_pin_bank_data
============================

.. c:type:: struct samsung_pin_bank_data

    represent a controller pin-bank (init data).

.. _`samsung_pin_bank_data.definition`:

Definition
----------

.. code-block:: c

    struct samsung_pin_bank_data {
        const struct samsung_pin_bank_type *type;
        u32 pctl_offset;
        u8 nr_pins;
        u8 eint_func;
        enum eint_type eint_type;
        u32 eint_mask;
        u32 eint_offset;
        const char *name;
    }

.. _`samsung_pin_bank_data.members`:

Members
-------

type
    type of the bank (register offsets and bitfield widths)

pctl_offset
    starting offset of the pin-bank registers.

nr_pins
    number of pins included in this bank.

eint_func
    function to set in CON register to configure pin as EINT.

eint_type
    type of the external interrupt supported by the bank.

eint_mask
    bit mask of pins which support EINT function.

eint_offset
    SoC-specific EINT register or interrupt offset of bank.

name
    name to be prefixed for each pin in this pin bank.

.. _`samsung_pin_bank`:

struct samsung_pin_bank
=======================

.. c:type:: struct samsung_pin_bank

    represent a controller pin-bank.

.. _`samsung_pin_bank.definition`:

Definition
----------

.. code-block:: c

    struct samsung_pin_bank {
        const struct samsung_pin_bank_type *type;
        u32 pctl_offset;
        u8 nr_pins;
        u8 eint_func;
        enum eint_type eint_type;
        u32 eint_mask;
        u32 eint_offset;
        const char *name;
        u32 pin_base;
        void *soc_priv;
        struct device_node *of_node;
        struct samsung_pinctrl_drv_data *drvdata;
        struct irq_domain *irq_domain;
        struct gpio_chip gpio_chip;
        struct pinctrl_gpio_range grange;
        struct exynos_irq_chip *irq_chip;
        spinlock_t slock;
        u32 pm_save[PINCFG_TYPE_NUM + 1];
    }

.. _`samsung_pin_bank.members`:

Members
-------

type
    type of the bank (register offsets and bitfield widths)

pctl_offset
    starting offset of the pin-bank registers.

nr_pins
    number of pins included in this bank.

eint_func
    function to set in CON register to configure pin as EINT.

eint_type
    type of the external interrupt supported by the bank.

eint_mask
    bit mask of pins which support EINT function.

eint_offset
    SoC-specific EINT register or interrupt offset of bank.

name
    name to be prefixed for each pin in this pin bank.

pin_base
    starting pin number of the bank.

soc_priv
    per-bank private data for SoC-specific code.

of_node
    OF node of the bank.

drvdata
    link to controller driver data

irq_domain
    IRQ domain of the bank.

gpio_chip
    GPIO chip of the bank.

grange
    linux gpio pin range supported by this bank.

irq_chip
    link to irq chip for external gpio and wakeup interrupts.

slock
    spinlock protecting bank registers

pm_save
    saved register values during suspend

.. _`samsung_pin_ctrl`:

struct samsung_pin_ctrl
=======================

.. c:type:: struct samsung_pin_ctrl

    represent a pin controller.

.. _`samsung_pin_ctrl.definition`:

Definition
----------

.. code-block:: c

    struct samsung_pin_ctrl {
        const struct samsung_pin_bank_data *pin_banks;
        u32 nr_banks;
        int (*eint_gpio_init)(struct samsung_pinctrl_drv_data *);
        int (*eint_wkup_init)(struct samsung_pinctrl_drv_data *);
        void (*suspend)(struct samsung_pinctrl_drv_data *);
        void (*resume)(struct samsung_pinctrl_drv_data *);
    }

.. _`samsung_pin_ctrl.members`:

Members
-------

pin_banks
    list of pin banks included in this controller.

nr_banks
    number of pin banks.

eint_gpio_init
    platform specific callback to setup the external gpio
    interrupts for the controller.

eint_wkup_init
    platform specific callback to setup the external wakeup
    interrupts for the controller.

suspend
    *undescribed*

resume
    *undescribed*

.. _`samsung_pinctrl_drv_data`:

struct samsung_pinctrl_drv_data
===============================

.. c:type:: struct samsung_pinctrl_drv_data

    wrapper for holding driver data together.

.. _`samsung_pinctrl_drv_data.definition`:

Definition
----------

.. code-block:: c

    struct samsung_pinctrl_drv_data {
        struct list_head node;
        void __iomem *virt_base;
        struct device *dev;
        int irq;
        struct pinctrl_desc pctl;
        struct pinctrl_dev *pctl_dev;
        const struct samsung_pin_group *pin_groups;
        unsigned int nr_groups;
        const struct samsung_pmx_func *pmx_functions;
        unsigned int nr_functions;
        struct samsung_pin_bank *pin_banks;
        u32 nr_banks;
        unsigned int pin_base;
        unsigned int nr_pins;
        void (*suspend)(struct samsung_pinctrl_drv_data *);
        void (*resume)(struct samsung_pinctrl_drv_data *);
    }

.. _`samsung_pinctrl_drv_data.members`:

Members
-------

node
    global list node

virt_base
    register base address of the controller.

dev
    device instance representing the controller.

irq
    interrpt number used by the controller to notify gpio interrupts.

pctl
    pin controller descriptor registered with the pinctrl subsystem.

pctl_dev
    cookie representing pinctrl device instance.

pin_groups
    list of pin groups available to the driver.

nr_groups
    number of such pin groups.

pmx_functions
    list of pin functions available to the driver.

nr_functions
    *undescribed*

pin_banks
    *undescribed*

nr_banks
    *undescribed*

pin_base
    starting system wide pin number.

nr_pins
    number of pins supported by the controller.

suspend
    *undescribed*

resume
    *undescribed*

.. _`samsung_pin_group`:

struct samsung_pin_group
========================

.. c:type:: struct samsung_pin_group

    represent group of pins of a pinmux function.

.. _`samsung_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct samsung_pin_group {
        const char *name;
        const unsigned int *pins;
        u8 num_pins;
        u8 func;
    }

.. _`samsung_pin_group.members`:

Members
-------

name
    name of the pin group, used to lookup the group.

pins
    the pins included in this group.

num_pins
    number of pins included in this group.

func
    the function number to be programmed when selected.

.. _`samsung_pmx_func`:

struct samsung_pmx_func
=======================

.. c:type:: struct samsung_pmx_func

    represent a pin function.

.. _`samsung_pmx_func.definition`:

Definition
----------

.. code-block:: c

    struct samsung_pmx_func {
        const char *name;
        const char **groups;
        u8 num_groups;
        u32 val;
    }

.. _`samsung_pmx_func.members`:

Members
-------

name
    name of the pin function, used to lookup the function.

groups
    one or more names of pin groups that provide this function.

num_groups
    number of groups included in \ ``groups``\ .

val
    *undescribed*

.. This file was automatic generated / don't edit.
