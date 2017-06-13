.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/ti/pinctrl-ti-iodelay.c

.. _`ti_iodelay_reg_data`:

struct ti_iodelay_reg_data
==========================

.. c:type:: struct ti_iodelay_reg_data

    Describes the registers for the iodelay instance

.. _`ti_iodelay_reg_data.definition`:

Definition
----------

.. code-block:: c

    struct ti_iodelay_reg_data {
        u32 signature_mask;
        u32 signature_value;
        u32 lock_mask;
        u32 lock_val;
        u32 unlock_val;
        u32 binary_data_coarse_mask;
        u32 binary_data_fine_mask;
        u32 reg_refclk_offset;
        u32 refclk_period_mask;
        u32 reg_coarse_offset;
        u32 coarse_delay_count_mask;
        u32 coarse_ref_count_mask;
        u32 reg_fine_offset;
        u32 fine_delay_count_mask;
        u32 fine_ref_count_mask;
        u32 reg_global_lock_offset;
        u32 global_lock_mask;
        u32 global_unlock_val;
        u32 global_lock_val;
        u32 reg_start_offset;
        u32 reg_nr_per_pin;
        struct regmap_config *regmap_config;
    }

.. _`ti_iodelay_reg_data.members`:

Members
-------

signature_mask
    CONFIG_REG mask for the signature bits (see TRM)

signature_value
    CONFIG_REG signature value to be written (see TRM)

lock_mask
    CONFIG_REG mask for the lock bits (see TRM)

lock_val
    CONFIG_REG lock value for the lock bits (see TRM)

unlock_val
    CONFIG_REG unlock value for the lock bits (see TRM)

binary_data_coarse_mask
    CONFIG_REG coarse mask (see TRM)

binary_data_fine_mask
    CONFIG_REG fine mask (see TRM)

reg_refclk_offset
    Refclk register offset

refclk_period_mask
    Refclk mask

reg_coarse_offset
    Coarse register configuration offset

coarse_delay_count_mask
    Coarse delay count mask

coarse_ref_count_mask
    Coarse ref count mask

reg_fine_offset
    Fine register configuration offset

fine_delay_count_mask
    Fine delay count mask

fine_ref_count_mask
    Fine ref count mask

reg_global_lock_offset
    Global iodelay module lock register offset

global_lock_mask
    Lock mask

global_unlock_val
    Unlock value

global_lock_val
    Lock value

reg_start_offset
    Offset to iodelay registers after the CONFIG_REG_0 to 8

reg_nr_per_pin
    Number of iodelay registers for each pin

regmap_config
    Regmap configuration for the IODelay region

.. _`ti_iodelay_reg_values`:

struct ti_iodelay_reg_values
============================

.. c:type:: struct ti_iodelay_reg_values

    Computed io_reg configuration values (see TRM)

.. _`ti_iodelay_reg_values.definition`:

Definition
----------

.. code-block:: c

    struct ti_iodelay_reg_values {
        u16 coarse_ref_count;
        u16 coarse_delay_count;
        u16 fine_ref_count;
        u16 fine_delay_count;
        u16 ref_clk_period;
        u32 cdpe;
        u32 fdpe;
    }

.. _`ti_iodelay_reg_values.members`:

Members
-------

coarse_ref_count
    Coarse reference count

coarse_delay_count
    Coarse delay count

fine_ref_count
    Fine reference count

fine_delay_count
    Fine Delay count

ref_clk_period
    Reference Clock period

cdpe
    Coarse delay parameter

fdpe
    Fine delay parameter

.. _`ti_iodelay_cfg`:

struct ti_iodelay_cfg
=====================

.. c:type:: struct ti_iodelay_cfg

    Description of each configuration parameters

.. _`ti_iodelay_cfg.definition`:

Definition
----------

.. code-block:: c

    struct ti_iodelay_cfg {
        u16 offset;
        u16 a_delay;
        u16 g_delay;
    }

.. _`ti_iodelay_cfg.members`:

Members
-------

offset
    Configuration register offset

a_delay
    Agnostic Delay (in ps)

g_delay
    Gnostic Delay (in ps)

.. _`ti_iodelay_pingroup`:

struct ti_iodelay_pingroup
==========================

.. c:type:: struct ti_iodelay_pingroup

    Structure that describes one group

.. _`ti_iodelay_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct ti_iodelay_pingroup {
        struct ti_iodelay_cfg *cfg;
        int ncfg;
        unsigned long config;
    }

.. _`ti_iodelay_pingroup.members`:

Members
-------

cfg
    configuration array for the pin (from dt)

ncfg
    number of configuration values allocated

config
    pinconf "Config" - currently a dummy value

.. _`ti_iodelay_device`:

struct ti_iodelay_device
========================

.. c:type:: struct ti_iodelay_device

    Represents information for a iodelay instance

.. _`ti_iodelay_device.definition`:

Definition
----------

.. code-block:: c

    struct ti_iodelay_device {
        struct device *dev;
        unsigned long phys_base;
        void __iomem *reg_base;
        struct regmap *regmap;
        struct pinctrl_dev *pctl;
        struct pinctrl_desc desc;
        struct pinctrl_pin_desc *pa;
        const struct ti_iodelay_reg_data *reg_data;
        struct ti_iodelay_reg_values reg_init_conf_values;
    }

.. _`ti_iodelay_device.members`:

Members
-------

dev
    Device pointer

phys_base
    Physical address base of the iodelay device

reg_base
    Virtual address base of the iodelay device

regmap
    Regmap for this iodelay instance

pctl
    Pinctrl device

desc
    pinctrl descriptor for pctl

pa
    pinctrl pin wise description

reg_data
    Register definition data for the IODelay instance

reg_init_conf_values
    Initial configuration values.

.. _`ti_iodelay_extract`:

ti_iodelay_extract
==================

.. c:function:: u32 ti_iodelay_extract(u32 val, u32 mask)

    extract bits for a field

    :param u32 val:
        Register value

    :param u32 mask:
        Mask

.. _`ti_iodelay_extract.return`:

Return
------

extracted value which is appropriately shifted

.. _`ti_iodelay_compute_dpe`:

ti_iodelay_compute_dpe
======================

.. c:function:: u32 ti_iodelay_compute_dpe(u16 period, u16 ref, u16 delay, u16 delay_m)

    Compute equation for delay parameter

    :param u16 period:
        Period to use

    :param u16 ref:
        Reference Count

    :param u16 delay:
        Delay count

    :param u16 delay_m:
        Delay multiplier

.. _`ti_iodelay_compute_dpe.return`:

Return
------

Computed delay parameter

.. _`ti_iodelay_pinconf_set`:

ti_iodelay_pinconf_set
======================

.. c:function:: int ti_iodelay_pinconf_set(struct ti_iodelay_device *iod, struct ti_iodelay_cfg *cfg)

    Configure the pin configuration

    :param struct ti_iodelay_device \*iod:
        iodelay device

    :param struct ti_iodelay_cfg \*cfg:
        Configuration

.. _`ti_iodelay_pinconf_set.description`:

Description
-----------

Update the configuration register as per TRM and lockup once done.
\*IMPORTANT NOTE\* SoC TRM does recommend doing iodelay programmation only
while in Isolation. But, then, isolation also implies that every pin
on the SoC (including DDR) will be isolated out. The only benefit being
a glitchless configuration, However, the intent of this driver is purely
to support a "glitchy" configuration where applicable.

.. _`ti_iodelay_pinconf_set.return`:

Return
------

0 in case of success, else appropriate error value

.. _`ti_iodelay_pinconf_init_dev`:

ti_iodelay_pinconf_init_dev
===========================

.. c:function:: int ti_iodelay_pinconf_init_dev(struct ti_iodelay_device *iod)

    Initialize IODelay device

    :param struct ti_iodelay_device \*iod:
        iodelay device

.. _`ti_iodelay_pinconf_init_dev.description`:

Description
-----------

Unlocks the iodelay region, computes the common parameters

.. _`ti_iodelay_pinconf_init_dev.return`:

Return
------

0 in case of success, else appropriate error value

.. _`ti_iodelay_pinconf_deinit_dev`:

ti_iodelay_pinconf_deinit_dev
=============================

.. c:function:: void ti_iodelay_pinconf_deinit_dev(struct ti_iodelay_device *iod)

    deinit the iodelay device

    :param struct ti_iodelay_device \*iod:
        IODelay device

.. _`ti_iodelay_pinconf_deinit_dev.description`:

Description
-----------

Deinitialize the IODelay device (basically just lock the region back up.

.. _`ti_iodelay_get_pingroup`:

ti_iodelay_get_pingroup
=======================

.. c:function:: struct ti_iodelay_pingroup *ti_iodelay_get_pingroup(struct ti_iodelay_device *iod, unsigned int selector)

    Find the group mapped by a group selector

    :param struct ti_iodelay_device \*iod:
        iodelay device

    :param unsigned int selector:
        Group Selector

.. _`ti_iodelay_get_pingroup.return`:

Return
------

Corresponding group representing group selector

.. _`ti_iodelay_offset_to_pin`:

ti_iodelay_offset_to_pin
========================

.. c:function:: int ti_iodelay_offset_to_pin(struct ti_iodelay_device *iod, unsigned int offset)

    get a pin index based on the register offset

    :param struct ti_iodelay_device \*iod:
        iodelay driver instance

    :param unsigned int offset:
        register offset from the base

.. _`ti_iodelay_node_iterator`:

ti_iodelay_node_iterator
========================

.. c:function:: int ti_iodelay_node_iterator(struct pinctrl_dev *pctldev, struct device_node *np, const struct of_phandle_args *pinctrl_spec, int *pins, int pin_index, void *data)

    Iterate iodelay node

    :param struct pinctrl_dev \*pctldev:
        Pin controller driver

    :param struct device_node \*np:
        Device node

    :param const struct of_phandle_args \*pinctrl_spec:
        Parsed arguments from device tree

    :param int \*pins:
        Array of pins in the pin group

    :param int pin_index:
        Pin index in the pin array

    :param void \*data:
        Pin controller driver specific data

.. _`ti_iodelay_dt_node_to_map`:

ti_iodelay_dt_node_to_map
=========================

.. c:function:: int ti_iodelay_dt_node_to_map(struct pinctrl_dev *pctldev, struct device_node *np, struct pinctrl_map **map, unsigned int *num_maps)

    Map a device tree node to appropriate group

    :param struct pinctrl_dev \*pctldev:
        pinctrl device representing IODelay device

    :param struct device_node \*np:
        Node Pointer (device tree)

    :param struct pinctrl_map \*\*map:
        Pinctrl Map returned back to pinctrl framework

    :param unsigned int \*num_maps:
        Number of maps (1)

.. _`ti_iodelay_dt_node_to_map.description`:

Description
-----------

Maps the device tree description into a group of configuration parameters
for iodelay block entry.

.. _`ti_iodelay_dt_node_to_map.return`:

Return
------

0 in case of success, else appropriate error value

.. _`ti_iodelay_pinconf_group_get`:

ti_iodelay_pinconf_group_get
============================

.. c:function:: int ti_iodelay_pinconf_group_get(struct pinctrl_dev *pctldev, unsigned int selector, unsigned long *config)

    Get the group configuration

    :param struct pinctrl_dev \*pctldev:
        pinctrl device representing IODelay device

    :param unsigned int selector:
        Group selector

    :param unsigned long \*config:
        Configuration returned

.. _`ti_iodelay_pinconf_group_get.return`:

Return
------

The configuration if the group is valid, else returns -EINVAL

.. _`ti_iodelay_pinconf_group_set`:

ti_iodelay_pinconf_group_set
============================

.. c:function:: int ti_iodelay_pinconf_group_set(struct pinctrl_dev *pctldev, unsigned int selector, unsigned long *configs, unsigned int num_configs)

    Configure the groups of pins

    :param struct pinctrl_dev \*pctldev:
        pinctrl device representing IODelay device

    :param unsigned int selector:
        Group selector

    :param unsigned long \*configs:
        Configurations

    :param unsigned int num_configs:
        Number of configurations

.. _`ti_iodelay_pinconf_group_set.return`:

Return
------

0 if all went fine, else appropriate error value.

.. _`ti_iodelay_pin_to_offset`:

ti_iodelay_pin_to_offset
========================

.. c:function:: unsigned int ti_iodelay_pin_to_offset(struct ti_iodelay_device *iod, unsigned int selector)

    get pin register offset based on the pin index

    :param struct ti_iodelay_device \*iod:
        iodelay driver instance

    :param unsigned int selector:
        Pin index

.. _`ti_iodelay_pinconf_group_dbg_show`:

ti_iodelay_pinconf_group_dbg_show
=================================

.. c:function:: void ti_iodelay_pinconf_group_dbg_show(struct pinctrl_dev *pctldev, struct seq_file *s, unsigned int selector)

    show the group information

    :param struct pinctrl_dev \*pctldev:
        Show the group information

    :param struct seq_file \*s:
        Sequence file

    :param unsigned int selector:
        Group selector

.. _`ti_iodelay_pinconf_group_dbg_show.description`:

Description
-----------

Provide the configuration information of the selected group

.. _`ti_iodelay_alloc_pins`:

ti_iodelay_alloc_pins
=====================

.. c:function:: int ti_iodelay_alloc_pins(struct device *dev, struct ti_iodelay_device *iod, u32 base_phy)

    Allocate structures needed for pins for iodelay

    :param struct device \*dev:
        Device pointer

    :param struct ti_iodelay_device \*iod:
        iodelay device

    :param u32 base_phy:
        Base Physical Address

.. _`ti_iodelay_alloc_pins.return`:

Return
------

0 if all went fine, else appropriate error value.

.. _`ti_iodelay_probe`:

ti_iodelay_probe
================

.. c:function:: int ti_iodelay_probe(struct platform_device *pdev)

    Standard probe

    :param struct platform_device \*pdev:
        platform device

.. _`ti_iodelay_probe.return`:

Return
------

0 if all went fine, else appropriate error value.

.. _`ti_iodelay_remove`:

ti_iodelay_remove
=================

.. c:function:: int ti_iodelay_remove(struct platform_device *pdev)

    standard remove

    :param struct platform_device \*pdev:
        platform device

.. _`ti_iodelay_remove.return`:

Return
------

0 if all went fine, else appropriate error value.

.. This file was automatic generated / don't edit.

