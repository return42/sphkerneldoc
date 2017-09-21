.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-gemini.c

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

