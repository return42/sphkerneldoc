.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/mvebu/pinctrl-armada-37xx.c

.. _`armada_37xx_pin_group`:

struct armada_37xx_pin_group
============================

.. c:type:: struct armada_37xx_pin_group

    represents group of pins of a pinmux function. The pins of a pinmux groups are composed of one or two groups of contiguous pins.

.. _`armada_37xx_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct armada_37xx_pin_group {
        const char *name;
        unsigned int start_pin;
        unsigned int npins;
        u32 reg_mask;
        u32 val[NB_FUNCS];
        unsigned int extra_pin;
        unsigned int extra_npins;
        const char *funcs[NB_FUNCS];
        unsigned int *pins;
    }

.. _`armada_37xx_pin_group.members`:

Members
-------

name
    Name of the pin group, used to lookup the group.

start_pin
    *undescribed*

npins
    Number of pins included in the second optional range

reg_mask
    Bit mask matching the group in the selection register

val
    *undescribed*

extra_pin
    *undescribed*

extra_npins
    *undescribed*

funcs
    A list of pinmux functions that can be selected for this group.

pins
    List of the pins included in the group

.. _`armada_37xx_add_function`:

armada_37xx_add_function
========================

.. c:function:: int armada_37xx_add_function(struct armada_37xx_pmx_func *funcs, int *funcsize, const char *name)

    Add a new function to the list

    :param struct armada_37xx_pmx_func \*funcs:
        array of function to add the new one

    :param int \*funcsize:
        size of the remaining space for the function

    :param const char \*name:
        name of the function to add

.. _`armada_37xx_add_function.description`:

Description
-----------

If it is a new function then create it by adding its name else
increment the number of group associated to this function.

.. _`armada_37xx_fill_group`:

armada_37xx_fill_group
======================

.. c:function:: int armada_37xx_fill_group(struct armada_37xx_pinctrl *info)

    complete the group array

    :param struct armada_37xx_pinctrl \*info:
        info driver instance

.. _`armada_37xx_fill_group.description`:

Description
-----------

Based on the data available from the armada_37xx_pin_group array

.. _`armada_37xx_fill_group.completes-the-last-member-of-the-struct-for-each-function`:

completes the last member of the struct for each function
---------------------------------------------------------

the list
of the groups associated to this function.

.. _`armada_37xx_fill_func`:

armada_37xx_fill_func
=====================

.. c:function:: int armada_37xx_fill_func(struct armada_37xx_pinctrl *info)

    complete the funcs array

    :param struct armada_37xx_pinctrl \*info:
        info driver instance

.. _`armada_37xx_fill_func.description`:

Description
-----------

Based on the data available from the armada_37xx_pin_group array

.. _`armada_37xx_fill_func.completes-the-last-two-member-of-the-struct-for-each-group`:

completes the last two member of the struct for each group
----------------------------------------------------------

- the list of the pins included in the group
- the list of pinmux functions that can be selected for this group

.. This file was automatic generated / don't edit.

