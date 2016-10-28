.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/meson/pinctrl-meson.h

.. _`meson_pmx_group`:

struct meson_pmx_group
======================

.. c:type:: struct meson_pmx_group

    a pinmux group

.. _`meson_pmx_group.definition`:

Definition
----------

.. code-block:: c

    struct meson_pmx_group {
        const char *name;
        const unsigned int *pins;
        unsigned int num_pins;
        bool is_gpio;
        unsigned int reg;
        unsigned int bit;
    }

.. _`meson_pmx_group.members`:

Members
-------

name
    group name

pins
    pins in the group

num_pins
    number of pins in the group

is_gpio
    whether the group is a single GPIO group

reg
    register offset for the group in the domain mux registers
    \ ``bit``\          bit index enabling the group

bit
    *undescribed*

.. _`meson_pmx_func`:

struct meson_pmx_func
=====================

.. c:type:: struct meson_pmx_func

    a pinmux function

.. _`meson_pmx_func.definition`:

Definition
----------

.. code-block:: c

    struct meson_pmx_func {
        const char *name;
        const char * const *groups;
        unsigned int num_groups;
    }

.. _`meson_pmx_func.members`:

Members
-------

name
    function name

groups
    groups in the function

num_groups
    number of groups in the function

.. _`meson_reg_desc`:

struct meson_reg_desc
=====================

.. c:type:: struct meson_reg_desc

    a register descriptor

.. _`meson_reg_desc.definition`:

Definition
----------

.. code-block:: c

    struct meson_reg_desc {
        unsigned int reg;
        unsigned int bit;
    }

.. _`meson_reg_desc.members`:

Members
-------

reg
    register offset in the regmap

bit
    bit index in register

.. _`meson_reg_desc.description`:

Description
-----------

The structure describes the information needed to control pull,
pull-enable, direction, etc. for a single pin

.. _`meson_reg_type`:

enum meson_reg_type
===================

.. c:type:: enum meson_reg_type

    type of registers encoded in \ ``meson_reg_desc``\ 

.. _`meson_reg_type.definition`:

Definition
----------

.. code-block:: c

    enum meson_reg_type {
        REG_PULLEN,
        REG_PULL,
        REG_DIR,
        REG_OUT,
        REG_IN,
        NUM_REG
    };

.. _`meson_reg_type.constants`:

Constants
---------

REG_PULLEN
    *undescribed*

REG_PULL
    *undescribed*

REG_DIR
    *undescribed*

REG_OUT
    *undescribed*

REG_IN
    *undescribed*

NUM_REG
    *undescribed*

.. _`meson_bank`:

struct meson_bank
=================

.. c:type:: struct meson_bank


.. _`meson_bank.definition`:

Definition
----------

.. code-block:: c

    struct meson_bank {
        const char *name;
        unsigned int first;
        unsigned int last;
        struct meson_reg_desc regs[NUM_REG];
    }

.. _`meson_bank.members`:

Members
-------

name
    bank name

first
    first pin of the bank

last
    last pin of the bank

regs
    array of register descriptors

.. _`meson_bank.description`:

Description
-----------

A bank represents a set of pins controlled by a contiguous set of
bits in the domain registers. The structure specifies which bits in
the regmap control the different functionalities. Each member of
the \ ``regs``\  array refers to the first pin of the bank.

.. _`meson_domain_data`:

struct meson_domain_data
========================

.. c:type:: struct meson_domain_data

    domain platform data

.. _`meson_domain_data.definition`:

Definition
----------

.. code-block:: c

    struct meson_domain_data {
        const char *name;
        struct meson_bank *banks;
        unsigned int num_banks;
        unsigned int pin_base;
        unsigned int num_pins;
    }

.. _`meson_domain_data.members`:

Members
-------

name
    name of the domain

banks
    set of banks belonging to the domain

num_banks
    number of banks in the domain

pin_base
    *undescribed*

num_pins
    *undescribed*

.. _`meson_domain`:

struct meson_domain
===================

.. c:type:: struct meson_domain


.. _`meson_domain.definition`:

Definition
----------

.. code-block:: c

    struct meson_domain {
        struct regmap *reg_mux;
        struct regmap *reg_pullen;
        struct regmap *reg_pull;
        struct regmap *reg_gpio;
        struct gpio_chip chip;
        struct meson_domain_data *data;
        struct device_node *of_node;
    }

.. _`meson_domain.members`:

Members
-------

reg_mux
    registers for mux settings

reg_pullen
    registers for pull-enable settings

reg_pull
    registers for pull settings

reg_gpio
    registers for gpio settings

chip
    gpio chip associated with the domain
    \ ``data``\ ;       platform data for the domain

data
    *undescribed*

of_node
    *undescribed*

.. _`meson_domain.description`:

Description
-----------

A domain represents a set of banks controlled by the same set of
registers.

.. This file was automatic generated / don't edit.

