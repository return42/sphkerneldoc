.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/actions/pinctrl-owl.h

.. _`owl_pullctl`:

struct owl_pullctl
==================

.. c:type:: struct owl_pullctl

    Actions pad pull control register

.. _`owl_pullctl.definition`:

Definition
----------

.. code-block:: c

    struct owl_pullctl {
        int reg;
        unsigned int shift;
        unsigned int width;
    }

.. _`owl_pullctl.members`:

Members
-------

reg
    offset to the pull control register

shift
    shift value of the register

width
    width of the register

.. _`owl_st`:

struct owl_st
=============

.. c:type:: struct owl_st

    Actions pad schmitt trigger enable register

.. _`owl_st.definition`:

Definition
----------

.. code-block:: c

    struct owl_st {
        int reg;
        unsigned int shift;
        unsigned int width;
    }

.. _`owl_st.members`:

Members
-------

reg
    offset to the schmitt trigger enable register

shift
    shift value of the register

width
    width of the register

.. _`owl_pingroup`:

struct owl_pingroup
===================

.. c:type:: struct owl_pingroup

    Actions pingroup definition

.. _`owl_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct owl_pingroup {
        const char *name;
        unsigned int *pads;
        unsigned int npads;
        unsigned int *funcs;
        unsigned int nfuncs;
        int mfpctl_reg;
        unsigned int mfpctl_shift;
        unsigned int mfpctl_width;
        int drv_reg;
        unsigned int drv_shift;
        unsigned int drv_width;
        int sr_reg;
        unsigned int sr_shift;
        unsigned int sr_width;
    }

.. _`owl_pingroup.members`:

Members
-------

name
    name of the  pin group

pads
    list of pins assigned to this pingroup

npads
    size of \ ``pads``\  array

funcs
    list of pinmux functions for this pingroup

nfuncs
    size of \ ``funcs``\  array

mfpctl_reg
    multiplexing control register offset

mfpctl_shift
    multiplexing control register bit mask

mfpctl_width
    multiplexing control register width

drv_reg
    drive control register offset

drv_shift
    drive control register bit mask

drv_width
    driver control register width

sr_reg
    slew rate control register offset

sr_shift
    slew rate control register bit mask

sr_width
    slew rate control register width

.. _`owl_padinfo`:

struct owl_padinfo
==================

.. c:type:: struct owl_padinfo

    Actions pinctrl pad info

.. _`owl_padinfo.definition`:

Definition
----------

.. code-block:: c

    struct owl_padinfo {
        int pad;
        struct owl_pullctl *pullctl;
        struct owl_st *st;
    }

.. _`owl_padinfo.members`:

Members
-------

pad
    pad name of the SoC

pullctl
    pull control register info

st
    schmitt trigger register info

.. _`owl_pinmux_func`:

struct owl_pinmux_func
======================

.. c:type:: struct owl_pinmux_func

    Actions pinctrl mux functions

.. _`owl_pinmux_func.definition`:

Definition
----------

.. code-block:: c

    struct owl_pinmux_func {
        const char *name;
        const char * const *groups;
        unsigned int ngroups;
    }

.. _`owl_pinmux_func.members`:

Members
-------

name
    name of the pinmux function.

groups
    array of pin groups that may select this function.

ngroups
    number of entries in \ ``groups``\ .

.. _`owl_gpio_port`:

struct owl_gpio_port
====================

.. c:type:: struct owl_gpio_port

    Actions GPIO port info

.. _`owl_gpio_port.definition`:

Definition
----------

.. code-block:: c

    struct owl_gpio_port {
        unsigned int offset;
        unsigned int pins;
        unsigned int outen;
        unsigned int inen;
        unsigned int dat;
    }

.. _`owl_gpio_port.members`:

Members
-------

offset
    offset of the GPIO port.

pins
    number of pins belongs to the GPIO port.

outen
    offset of the output enable register.

inen
    offset of the input enable register.

dat
    offset of the data register.

.. _`owl_pinctrl_soc_data`:

struct owl_pinctrl_soc_data
===========================

.. c:type:: struct owl_pinctrl_soc_data

    Actions pin controller driver configuration

.. _`owl_pinctrl_soc_data.definition`:

Definition
----------

.. code-block:: c

    struct owl_pinctrl_soc_data {
        const struct pinctrl_pin_desc *pins;
        unsigned int npins;
        const struct owl_pinmux_func *functions;
        unsigned int nfunctions;
        const struct owl_pingroup *groups;
        unsigned int ngroups;
        const struct owl_padinfo *padinfo;
        unsigned int ngpios;
        const struct owl_gpio_port *ports;
        unsigned int nports;
    }

.. _`owl_pinctrl_soc_data.members`:

Members
-------

pins
    array describing all pins of the pin controller.

npins
    number of entries in \ ``pins``\ .

functions
    array describing all mux functions of this SoC.

nfunctions
    *undescribed*

groups
    array describing all pin groups of this SoC.

ngroups
    number of entries in \ ``groups``\ .

padinfo
    array describing the pad info of this SoC.

ngpios
    number of pingroups the driver should expose as GPIOs.

ports
    *undescribed*

nports
    number of GPIO ports in this SoC.

.. This file was automatic generated / don't edit.

