.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-gemini.c

.. _`gemini_pin_conf`:

struct gemini_pin_conf
======================

.. c:type:: struct gemini_pin_conf

    information about configuring a pin

.. _`gemini_pin_conf.definition`:

Definition
----------

.. code-block:: c

    struct gemini_pin_conf {
        unsigned int pin;
        u32 reg;
        u32 mask;
    }

.. _`gemini_pin_conf.members`:

Members
-------

pin
    the pin number

reg
    config register

mask
    the bits affecting the configuration of the pin

.. _`gemini_pmx`:

struct gemini_pmx
=================

.. c:type:: struct gemini_pmx

    state holder for the gemini pin controller

.. _`gemini_pmx.definition`:

Definition
----------

.. code-block:: c

    struct gemini_pmx {
        struct device *dev;
        struct pinctrl_dev *pctl;
        struct regmap *map;
        bool is_3512;
        bool is_3516;
        bool flash_pin;
        const struct gemini_pin_conf *confs;
        unsigned int nconfs;
    }

.. _`gemini_pmx.members`:

Members
-------

dev
    a pointer back to containing device

pctl
    *undescribed*

map
    regmap to access registers

is_3512
    whether the SoC/package is the 3512 variant

is_3516
    whether the SoC/package is the 3516 variant

flash_pin
    whether the flash pin (extended pins for parallel
    flash) is set

confs
    pin config information

nconfs
    number of pin config information items

.. _`gemini_pin_group`:

struct gemini_pin_group
=======================

.. c:type:: struct gemini_pin_group

    describes a Gemini pin group

.. _`gemini_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct gemini_pin_group {
        const char *name;
        const unsigned int *pins;
        const unsigned int num_pins;
        u32 mask;
        u32 value;
    }

.. _`gemini_pin_group.members`:

Members
-------

name
    the name of this specific pin group

pins
    an array of discrete physical pins used in this group, taken
    from the driver-local pin enumeration space

num_pins
    the number of pins in this group array, i.e. the number of
    elements in .pins so we can iterate over that array

mask
    bits to clear to enable this when doing pin muxing

value
    bits to set to enable this when doing pin muxing

.. _`gemini_pmx_func`:

struct gemini_pmx_func
======================

.. c:type:: struct gemini_pmx_func

    describes Gemini pinmux functions

.. _`gemini_pmx_func.definition`:

Definition
----------

.. code-block:: c

    struct gemini_pmx_func {
        const char *name;
        const char * const *groups;
        const unsigned int num_groups;
    }

.. _`gemini_pmx_func.members`:

Members
-------

name
    the name of this specific function

groups
    corresponding pin groups

num_groups
    *undescribed*

.. This file was automatic generated / don't edit.

