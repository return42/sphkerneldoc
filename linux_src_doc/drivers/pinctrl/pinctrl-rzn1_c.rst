.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-rzn1.c

.. _`rzn1_pmx_func`:

struct rzn1_pmx_func
====================

.. c:type:: struct rzn1_pmx_func

    describes rzn1 pinmux functions

.. _`rzn1_pmx_func.definition`:

Definition
----------

.. code-block:: c

    struct rzn1_pmx_func {
        const char *name;
        const char **groups;
        unsigned int num_groups;
    }

.. _`rzn1_pmx_func.members`:

Members
-------

name
    the name of this specific function

groups
    corresponding pin groups

num_groups
    the number of groups

.. _`rzn1_pin_group`:

struct rzn1_pin_group
=====================

.. c:type:: struct rzn1_pin_group

    describes an rzn1 pin group

.. _`rzn1_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct rzn1_pin_group {
        const char *name;
        const char *func;
        unsigned int npins;
        unsigned int *pins;
        u8 *pin_ids;
    }

.. _`rzn1_pin_group.members`:

Members
-------

name
    the name of this specific pin group

func
    the name of the function selected by this group

npins
    the number of pins in this group array, i.e. the number of
    elements in .pins so we can iterate over that array

pins
    array of pins. Needed due to pinctrl_ops.get_group_pins()

pin_ids
    array of pin_ids, i.e. the value used to select the mux

.. This file was automatic generated / don't edit.

