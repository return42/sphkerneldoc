.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-adi2.h

.. _`adi_pinctrl_soc_data`:

struct adi_pinctrl_soc_data
===========================

.. c:type:: struct adi_pinctrl_soc_data

    ADI pin controller per-SoC configuration

.. _`adi_pinctrl_soc_data.definition`:

Definition
----------

.. code-block:: c

    struct adi_pinctrl_soc_data {
        const struct adi_pmx_func *functions;
        int nfunctions;
        const struct adi_pin_group *groups;
        int ngroups;
        const struct pinctrl_pin_desc *pins;
        int npins;
    }

.. _`adi_pinctrl_soc_data.members`:

Members
-------

functions
    The functions supported on this SoC.

nfunctions
    *undescribed*

groups
    An array describing all pin groups the pin SoC supports.

ngroups
    The number of entries in \ ``groups``\ .

pins
    An array describing all pins the pin controller affects.

npins
    The number of entries in \ ``pins``\ .

.. This file was automatic generated / don't edit.

