.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-u300.c

.. _`u300_pin_group`:

struct u300_pin_group
=====================

.. c:type:: struct u300_pin_group

    describes a U300 pin group

.. _`u300_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct u300_pin_group {
        const char *name;
        const unsigned int *pins;
        const unsigned num_pins;
    }

.. _`u300_pin_group.members`:

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

.. _`u300_pmx_mask`:

struct u300_pmx_mask
====================

.. c:type:: struct u300_pmx_mask

    mask bits to enable/disable padmux

.. _`u300_pmx_mask.definition`:

Definition
----------

.. code-block:: c

    struct u300_pmx_mask {
        u16 mask;
        u16 bits;
    }

.. _`u300_pmx_mask.members`:

Members
-------

mask
    mask bits to disable

bits
    *undescribed*

.. _`u300_pmx_mask.onmask-lazy-dog`:

onmask lazy dog
---------------

onmask = {
{"PMC1LR" mask, "PMC1LR" value},
{"PMC1HR" mask, "PMC1HR" value},
{"PMC2R"  mask, "PMC2R"  value},
{"PMC3R"  mask, "PMC3R"  value},
{"PMC4R"  mask, "PMC4R"  value}
}

.. _`u300_pmx_func`:

struct u300_pmx_func
====================

.. c:type:: struct u300_pmx_func

    describes U300 pinmux functions

.. _`u300_pmx_func.definition`:

Definition
----------

.. code-block:: c

    struct u300_pmx_func {
        const char *name;
        const char * const *groups;
        const unsigned num_groups;
        const struct u300_pmx_mask *mask;
    }

.. _`u300_pmx_func.members`:

Members
-------

name
    the name of this specific function

groups
    corresponding pin groups

num_groups
    *undescribed*

mask
    *undescribed*

.. This file was automatic generated / don't edit.

