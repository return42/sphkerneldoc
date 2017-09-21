.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/mvebu/pinctrl-mvebu.h

.. _`mvebu_mpp_ctrl_data`:

struct mvebu_mpp_ctrl_data
==========================

.. c:type:: struct mvebu_mpp_ctrl_data

    private data for the mpp ctrl operations

.. _`mvebu_mpp_ctrl_data.definition`:

Definition
----------

.. code-block:: c

    struct mvebu_mpp_ctrl_data {
        union regmap;
         };
    }

.. _`mvebu_mpp_ctrl_data.members`:

Members
-------

regmap
    *undescribed*

regmap.map
    regmap structure

regmap.offset
    regmap offset

}
    *undescribed*

.. _`mvebu_mpp_ctrl`:

struct mvebu_mpp_ctrl
=====================

.. c:type:: struct mvebu_mpp_ctrl

    describe a mpp control

.. _`mvebu_mpp_ctrl.definition`:

Definition
----------

.. code-block:: c

    struct mvebu_mpp_ctrl {
        const char *name;
        u8 pid;
        u8 npins;
        unsigned *pins;
        int (*mpp_get)(struct mvebu_mpp_ctrl_data *data, unsigned pid, unsigned long *config);
        int (*mpp_set)(struct mvebu_mpp_ctrl_data *data, unsigned pid, unsigned long config);
        int (*mpp_gpio_req)(struct mvebu_mpp_ctrl_data *data, unsigned pid);
        int (*mpp_gpio_dir)(struct mvebu_mpp_ctrl_data *data, unsigned pid, bool input);
    }

.. _`mvebu_mpp_ctrl.members`:

Members
-------

name
    name of the control group

pid
    first pin id handled by this control

npins
    number of pins controlled by this control

pins
    *undescribed*

mpp_get
    (optional) special function to get mpp setting

mpp_set
    (optional) special function to set mpp setting

mpp_gpio_req
    (optional) special function to request gpio

mpp_gpio_dir
    (optional) special function to set gpio direction

.. _`mvebu_mpp_ctrl.description`:

Description
-----------

A mpp_ctrl describes a muxable unit, e.g. pin, group of pins, or
internal function, inside the SoC. Each muxable unit can be switched
between two or more different settings, e.g. assign mpp pin 13 to
uart1 or sata.

The mpp_get/_set functions are mandatory and are used to get/set a
specific mode. The optional mpp_gpio_req/_dir functions can be used
to allow pin settings with varying gpio pins.

.. _`mvebu_mpp_ctrl_setting`:

struct mvebu_mpp_ctrl_setting
=============================

.. c:type:: struct mvebu_mpp_ctrl_setting

    describe a mpp ctrl setting

.. _`mvebu_mpp_ctrl_setting.definition`:

Definition
----------

.. code-block:: c

    struct mvebu_mpp_ctrl_setting {
        u8 val;
        const char *name;
        const char *subname;
        u8 variant;
        u8 flags;
    #define MVEBU_SETTING_GPO (1 << 0)
    #define MVEBU_SETTING_GPI (1 << 1)
    }

.. _`mvebu_mpp_ctrl_setting.members`:

Members
-------

val
    ctrl setting value

name
    ctrl setting name, e.g. uart2, spi0 - unique per mpp_mode

subname
    (optional) additional ctrl setting name, e.g. rts, cts

variant
    (optional) variant identifier mask

flags
    (private) flags to store gpi/gpo/gpio capabilities

.. _`mvebu_mpp_ctrl_setting.description`:

Description
-----------

A ctrl_setting describes a specific internal mux function that a mpp pin
can be switched to. The value (val) will be written in the corresponding
register for common mpp pin configuration registers on MVEBU. SoC specific
mpp_get/_set function may use val to distinguish between different settings.

The name will be used to switch to this setting in DT description, e.g.
marvell,function = "uart2". subname is only for debugging purposes.

If name is one of "gpi", "gpo", "gpio" gpio capabilities are
parsed during initialization and stored in flags.

The variant can be used to combine different revisions of one SoC to a
common pinctrl driver. It is matched (AND) with variant of soc_info to
determine if a setting is available on the current SoC revision.

.. _`mvebu_mpp_mode`:

struct mvebu_mpp_mode
=====================

.. c:type:: struct mvebu_mpp_mode

    link ctrl and settings

.. _`mvebu_mpp_mode.definition`:

Definition
----------

.. code-block:: c

    struct mvebu_mpp_mode {
        u8 pid;
        struct mvebu_mpp_ctrl_setting *settings;
    }

.. _`mvebu_mpp_mode.members`:

Members
-------

pid
    first pin id handled by this mode

settings
    list of settings available for this mode

.. _`mvebu_mpp_mode.description`:

Description
-----------

A mode connects all available settings with the corresponding mpp_ctrl
given by pid.

.. _`mvebu_pinctrl_soc_info`:

struct mvebu_pinctrl_soc_info
=============================

.. c:type:: struct mvebu_pinctrl_soc_info

    SoC specific info passed to pinctrl-mvebu

.. _`mvebu_pinctrl_soc_info.definition`:

Definition
----------

.. code-block:: c

    struct mvebu_pinctrl_soc_info {
        u8 variant;
        const struct mvebu_mpp_ctrl *controls;
        struct mvebu_mpp_ctrl_data *control_data;
        int ncontrols;
        struct mvebu_mpp_mode *modes;
        int nmodes;
        struct pinctrl_gpio_range *gpioranges;
        int ngpioranges;
    }

.. _`mvebu_pinctrl_soc_info.members`:

Members
-------

variant
    variant mask of soc_info

controls
    list of available mvebu_mpp_ctrls

control_data
    optional array, one entry for each control

ncontrols
    number of available mvebu_mpp_ctrls

modes
    list of available mvebu_mpp_modes

nmodes
    number of available mvebu_mpp_modes

gpioranges
    list of pinctrl_gpio_ranges

ngpioranges
    number of available pinctrl_gpio_ranges

.. _`mvebu_pinctrl_soc_info.description`:

Description
-----------

This struct describes all pinctrl related information for a specific SoC.
If variant is unequal 0 it will be matched (AND) with variant of each
setting and allows to distinguish between different revisions of one SoC.

.. This file was automatic generated / don't edit.

