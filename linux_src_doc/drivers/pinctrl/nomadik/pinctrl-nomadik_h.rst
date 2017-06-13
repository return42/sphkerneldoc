.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/nomadik/pinctrl-nomadik.h

.. _`prcm_gpiocr_reg_index`:

enum prcm_gpiocr_reg_index
==========================

.. c:type:: enum prcm_gpiocr_reg_index

    Used to reference an PRCM GPIOCR register address.

.. _`prcm_gpiocr_reg_index.definition`:

Definition
----------

.. code-block:: c

    enum prcm_gpiocr_reg_index {
        PRCM_IDX_GPIOCR1,
        PRCM_IDX_GPIOCR2,
        PRCM_IDX_GPIOCR3
    };

.. _`prcm_gpiocr_reg_index.constants`:

Constants
---------

PRCM_IDX_GPIOCR1
    *undescribed*

PRCM_IDX_GPIOCR2
    *undescribed*

PRCM_IDX_GPIOCR3
    *undescribed*

.. _`prcm_gpiocr_altcx_index`:

enum prcm_gpiocr_altcx_index
============================

.. c:type:: enum prcm_gpiocr_altcx_index

    Used to reference an Other alternate-C function.

.. _`prcm_gpiocr_altcx_index.definition`:

Definition
----------

.. code-block:: c

    enum prcm_gpiocr_altcx_index {
        PRCM_IDX_GPIOCR_ALTC1,
        PRCM_IDX_GPIOCR_ALTC2,
        PRCM_IDX_GPIOCR_ALTC3,
        PRCM_IDX_GPIOCR_ALTC4,
        PRCM_IDX_GPIOCR_ALTC_MAX
    };

.. _`prcm_gpiocr_altcx_index.constants`:

Constants
---------

PRCM_IDX_GPIOCR_ALTC1
    *undescribed*

PRCM_IDX_GPIOCR_ALTC2
    *undescribed*

PRCM_IDX_GPIOCR_ALTC3
    *undescribed*

PRCM_IDX_GPIOCR_ALTC4
    *undescribed*

PRCM_IDX_GPIOCR_ALTC_MAX
    *undescribed*

.. _`prcm_gpiocr_altcx`:

struct prcm_gpiocr_altcx
========================

.. c:type:: struct prcm_gpiocr_altcx

    Other alternate-C function

.. _`prcm_gpiocr_altcx.definition`:

Definition
----------

.. code-block:: c

    struct prcm_gpiocr_altcx {
        bool used:1;
        u8 reg_index:2;
        u8 control_bit:5;
    }

.. _`prcm_gpiocr_altcx.members`:

Members
-------

used
    other alternate-C function availability

reg_index
    PRCM GPIOCR register index used to control the function

control_bit
    PRCM GPIOCR bit used to control the function

.. _`prcm_gpiocr_altcx_pin_desc`:

struct prcm_gpiocr_altcx_pin_desc
=================================

.. c:type:: struct prcm_gpiocr_altcx_pin_desc

    Other alternate-C pin

.. _`prcm_gpiocr_altcx_pin_desc.definition`:

Definition
----------

.. code-block:: c

    struct prcm_gpiocr_altcx_pin_desc {
        unsigned short pin;
        struct prcm_gpiocr_altcx altcx;
    }

.. _`prcm_gpiocr_altcx_pin_desc.members`:

Members
-------

pin
    The pin number

altcx
    array of other alternate-C[1-4] functions

.. _`nmk_function`:

struct nmk_function
===================

.. c:type:: struct nmk_function

    Nomadik pinctrl mux function

.. _`nmk_function.definition`:

Definition
----------

.. code-block:: c

    struct nmk_function {
        const char *name;
        const char * const *groups;
        unsigned ngroups;
    }

.. _`nmk_function.members`:

Members
-------

name
    The name of the function, exported to pinctrl core.

groups
    An array of pin groups that may select this function.

ngroups
    The number of entries in \ ``groups``\ .

.. _`nmk_pingroup`:

struct nmk_pingroup
===================

.. c:type:: struct nmk_pingroup

    describes a Nomadik pin group

.. _`nmk_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct nmk_pingroup {
        const char *name;
        const unsigned int *pins;
        const unsigned npins;
        int altsetting;
    }

.. _`nmk_pingroup.members`:

Members
-------

name
    the name of this specific pin group

pins
    an array of discrete physical pins used in this group, taken
    from the driver-local pin enumeration space

npins
    *undescribed*

altsetting
    the altsetting to apply to all pins in this group to
    configure them to be used by a function

.. _`nmk_pinctrl_soc_data`:

struct nmk_pinctrl_soc_data
===========================

.. c:type:: struct nmk_pinctrl_soc_data

    Nomadik pin controller per-SoC configuration

.. _`nmk_pinctrl_soc_data.definition`:

Definition
----------

.. code-block:: c

    struct nmk_pinctrl_soc_data {
        const struct pinctrl_pin_desc *pins;
        unsigned npins;
        const struct nmk_function *functions;
        unsigned nfunctions;
        const struct nmk_pingroup *groups;
        unsigned ngroups;
        const struct prcm_gpiocr_altcx_pin_desc *altcx_pins;
        unsigned npins_altcx;
        const u16 *prcm_gpiocr_registers;
    }

.. _`nmk_pinctrl_soc_data.members`:

Members
-------

pins
    An array describing all pins the pin controller affects.
    All pins which are also GPIOs must be listed first within the
    array, and be numbered identically to the GPIO controller's
    numbering.

npins
    The number of entries in \ ``pins``\ .

functions
    The functions supported on this SoC.

nfunctions
    *undescribed*

groups
    An array describing all pin groups the pin SoC supports.

ngroups
    The number of entries in \ ``groups``\ .

altcx_pins
    The pins that support Other alternate-C function on this SoC

npins_altcx
    The number of Other alternate-C pins

prcm_gpiocr_registers
    The array of PRCM GPIOCR registers on this SoC

.. This file was automatic generated / don't edit.

