.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/freescale/pinctrl-imx1.h

.. _`imx1_pin`:

struct imx1_pin
===============

.. c:type:: struct imx1_pin

    describes an IMX1/21/27 pin.

.. _`imx1_pin.definition`:

Definition
----------

.. code-block:: c

    struct imx1_pin {
        unsigned int pin_id;
        unsigned int mux_id;
        unsigned long config;
    }

.. _`imx1_pin.members`:

Members
-------

pin_id
    ID of the described pin.

mux_id
    ID of the mux setup.

config
    Configuration of the pin (currently only pullup-enable).

.. _`imx1_pin_group`:

struct imx1_pin_group
=====================

.. c:type:: struct imx1_pin_group

    describes an IMX pin group

.. _`imx1_pin_group.definition`:

Definition
----------

.. code-block:: c

    struct imx1_pin_group {
        const char *name;
        unsigned int *pin_ids;
        struct imx1_pin *pins;
        unsigned npins;
    }

.. _`imx1_pin_group.members`:

Members
-------

name
    the name of this specific pin group

pin_ids
    *undescribed*

pins
    an array of imx1_pin structs used in this group

npins
    the number of pins in this group array, i.e. the number of
    elements in .pins so we can iterate over that array

.. _`imx1_pmx_func`:

struct imx1_pmx_func
====================

.. c:type:: struct imx1_pmx_func

    describes IMX pinmux functions

.. _`imx1_pmx_func.definition`:

Definition
----------

.. code-block:: c

    struct imx1_pmx_func {
        const char *name;
        const char **groups;
        unsigned num_groups;
    }

.. _`imx1_pmx_func.members`:

Members
-------

name
    the name of this specific function

groups
    corresponding pin groups

num_groups
    the number of groups

.. This file was automatic generated / don't edit.

