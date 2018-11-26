.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/qcom/pinctrl-msm.h

.. _`msm_function`:

struct msm_function
===================

.. c:type:: struct msm_function

    a pinmux function

.. _`msm_function.definition`:

Definition
----------

.. code-block:: c

    struct msm_function {
        const char *name;
        const char * const *groups;
        unsigned ngroups;
    }

.. _`msm_function.members`:

Members
-------

name
    Name of the pinmux function.

groups
    List of pingroups for this function.

ngroups
    Number of entries in \ ``groups``\ .

.. _`msm_pingroup`:

struct msm_pingroup
===================

.. c:type:: struct msm_pingroup

    Qualcomm pingroup definition

.. _`msm_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct msm_pingroup {
        const char *name;
        const unsigned *pins;
        unsigned npins;
        unsigned *funcs;
        unsigned nfuncs;
        u32 ctl_reg;
        u32 io_reg;
        u32 intr_cfg_reg;
        u32 intr_status_reg;
        u32 intr_target_reg;
        unsigned int tile:2;
        unsigned mux_bit:5;
        unsigned pull_bit:5;
        unsigned drv_bit:5;
        unsigned oe_bit:5;
        unsigned in_bit:5;
        unsigned out_bit:5;
        unsigned intr_enable_bit:5;
        unsigned intr_status_bit:5;
        unsigned intr_ack_high:1;
        unsigned intr_target_bit:5;
        unsigned intr_target_kpss_val:5;
        unsigned intr_raw_status_bit:5;
        unsigned intr_polarity_bit:5;
        unsigned intr_detection_bit:5;
        unsigned intr_detection_width:5;
    }

.. _`msm_pingroup.members`:

Members
-------

name
    Name of the pingroup.

pins
    A list of pins assigned to this pingroup.

npins
    Number of entries in \ ``pins``\ .

funcs
    A list of pinmux functions that can be selected for
    this group. The index of the selected function is used
    for programming the function selector.
    Entries should be indices into the groups list of the
    struct msm_pinctrl_soc_data.

nfuncs
    *undescribed*

ctl_reg
    Offset of the register holding control bits for this group.

io_reg
    Offset of the register holding input/output bits for this group.

intr_cfg_reg
    Offset of the register holding interrupt configuration bits.

intr_status_reg
    Offset of the register holding the status bits for this group.

intr_target_reg
    Offset of the register specifying routing of the interrupts
    from this group.

tile
    *undescribed*

mux_bit
    Offset in \ ``ctl_reg``\  for the pinmux function selection.

pull_bit
    Offset in \ ``ctl_reg``\  for the bias configuration.

drv_bit
    Offset in \ ``ctl_reg``\  for the drive strength configuration.

oe_bit
    Offset in \ ``ctl_reg``\  for controlling output enable.

in_bit
    Offset in \ ``io_reg``\  for the input bit value.

out_bit
    Offset in \ ``io_reg``\  for the output bit value.

intr_enable_bit
    Offset in \ ``intr_cfg_reg``\  for enabling the interrupt for this group.

intr_status_bit
    Offset in \ ``intr_status_reg``\  for reading and acking the interrupt
    status.

intr_ack_high
    *undescribed*

intr_target_bit
    Offset in \ ``intr_target_reg``\  for configuring the interrupt routing.

intr_target_kpss_val
    Value in \ ``intr_target_bit``\  for specifying that the interrupt from
    this gpio should get routed to the KPSS processor.

intr_raw_status_bit
    Offset in \ ``intr_cfg_reg``\  for the raw status bit.

intr_polarity_bit
    Offset in \ ``intr_cfg_reg``\  for specifying polarity of the interrupt.

intr_detection_bit
    Offset in \ ``intr_cfg_reg``\  for specifying interrupt type.

intr_detection_width
    Number of bits used for specifying interrupt type,
    Should be 2 for SoCs that can detect both edges in hardware,
    otherwise 1.

.. _`msm_pinctrl_soc_data`:

struct msm_pinctrl_soc_data
===========================

.. c:type:: struct msm_pinctrl_soc_data

    Qualcomm pin controller driver configuration

.. _`msm_pinctrl_soc_data.definition`:

Definition
----------

.. code-block:: c

    struct msm_pinctrl_soc_data {
        const struct pinctrl_pin_desc *pins;
        unsigned npins;
        const struct msm_function *functions;
        unsigned nfunctions;
        const struct msm_pingroup *groups;
        unsigned ngroups;
        unsigned ngpios;
        bool pull_no_keeper;
        const char *const *tiles;
        unsigned int ntiles;
    }

.. _`msm_pinctrl_soc_data.members`:

Members
-------

pins
    An array describing all pins the pin controller affects.

npins
    The number of entries in \ ``pins``\ .

functions
    An array describing all mux functions the SoC supports.

nfunctions
    The number of entries in \ ``functions``\ .

groups
    An array describing all pin groups the pin SoC supports.

ngroups
    The numbmer of entries in \ ``groups``\ .

ngpios
    *undescribed*

pull_no_keeper
    The SoC does not support keeper bias.

tiles
    *undescribed*

ntiles
    *undescribed*

.. This file was automatic generated / don't edit.

