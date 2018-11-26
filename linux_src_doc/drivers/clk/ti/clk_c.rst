.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/clk.c

.. _`ti_clk_setup_ll_ops`:

ti_clk_setup_ll_ops
===================

.. c:function:: int ti_clk_setup_ll_ops(struct ti_clk_ll_ops *ops)

    setup low level clock operations

    :param ops:
        low level clock ops descriptor
    :type ops: struct ti_clk_ll_ops \*

.. _`ti_clk_setup_ll_ops.description`:

Description
-----------

Sets up low level clock operations for TI clock driver. This is used
to provide various callbacks for the clock driver towards platform
specific code. Returns 0 on success, -EBUSY if ll_ops have been
registered already.

.. _`ti_dt_clocks_register`:

ti_dt_clocks_register
=====================

.. c:function:: void ti_dt_clocks_register(struct ti_dt_clk oclks)

    register DT alias clocks during boot

    :param oclks:
        list of clocks to register
    :type oclks: struct ti_dt_clk

.. _`ti_dt_clocks_register.description`:

Description
-----------

Register alias or non-standard DT clock entries during boot. By
default, DT clocks are found based on their node name. If any
additional con-id / dev-id -> clock mapping is required, use this
function to list these.

.. _`ti_clk_retry_init`:

ti_clk_retry_init
=================

.. c:function:: int ti_clk_retry_init(struct device_node *node, void *user, ti_of_clk_init_cb_t func)

    retries a failed clock init at later phase

    :param node:
        device not for the clock
    :type node: struct device_node \*

    :param user:
        user data pointer
    :type user: void \*

    :param func:
        init function to be called for the clock
    :type func: ti_of_clk_init_cb_t

.. _`ti_clk_retry_init.description`:

Description
-----------

Adds a failed clock init to the retry list. The retry list is parsed
once all the other clocks have been initialized.

.. _`ti_clk_get_reg_addr`:

ti_clk_get_reg_addr
===================

.. c:function:: int ti_clk_get_reg_addr(struct device_node *node, int index, struct clk_omap_reg *reg)

    get register address for a clock register

    :param node:
        device node for the clock
    :type node: struct device_node \*

    :param index:
        register index from the clock node
    :type index: int

    :param reg:
        pointer to target register struct
    :type reg: struct clk_omap_reg \*

.. _`ti_clk_get_reg_addr.description`:

Description
-----------

Builds clock register address from device tree information, and returns
the data via the provided output pointer \ ``reg``\ . Returns 0 on success,
negative error value on failure.

.. _`omap2_clk_provider_init`:

omap2_clk_provider_init
=======================

.. c:function:: int omap2_clk_provider_init(struct device_node *parent, int index, struct regmap *syscon, void __iomem *mem)

    init master clock provider

    :param parent:
        master node
    :type parent: struct device_node \*

    :param index:
        internal index for clk_reg_ops
    :type index: int

    :param syscon:
        syscon regmap pointer for accessing clock registers
    :type syscon: struct regmap \*

    :param mem:
        iomem pointer for the clock provider memory area, only used if
        syscon is not provided
    :type mem: void __iomem \*

.. _`omap2_clk_provider_init.description`:

Description
-----------

Initializes a master clock IP block. This basically sets up the
mapping from clocks node to the memory map index. All the clocks
are then initialized through the common of_clk_init call, and the
clocks will access their memory maps based on the node layout.
Returns 0 in success.

.. _`omap2_clk_legacy_provider_init`:

omap2_clk_legacy_provider_init
==============================

.. c:function:: void omap2_clk_legacy_provider_init(int index, void __iomem *mem)

    initialize a legacy clock provider

    :param index:
        index for the clock provider
    :type index: int

    :param mem:
        iomem pointer for the clock provider memory area
    :type mem: void __iomem \*

.. _`omap2_clk_legacy_provider_init.description`:

Description
-----------

Initializes a legacy clock provider memory mapping.

.. _`ti_dt_clk_init_retry_clks`:

ti_dt_clk_init_retry_clks
=========================

.. c:function:: void ti_dt_clk_init_retry_clks( void)

    init clocks from the retry list

    :param void:
        no arguments
    :type void: 

.. _`ti_dt_clk_init_retry_clks.description`:

Description
-----------

Initializes any clocks that have failed to initialize before,
reasons being missing parent node(s) during earlier init. This
typically happens only for DPLLs which need to have both of their
parent clocks ready during init.

.. _`ti_clk_add_aliases`:

ti_clk_add_aliases
==================

.. c:function:: void ti_clk_add_aliases( void)

    setup clock aliases

    :param void:
        no arguments
    :type void: 

.. _`ti_clk_add_aliases.description`:

Description
-----------

Sets up any missing clock aliases. No return value.

.. _`ti_clk_setup_features`:

ti_clk_setup_features
=====================

.. c:function:: void ti_clk_setup_features(struct ti_clk_features *features)

    setup clock features flags

    :param features:
        features definition to use
    :type features: struct ti_clk_features \*

.. _`ti_clk_setup_features.description`:

Description
-----------

Initializes the clock driver features flags based on platform
provided data. No return value.

.. _`ti_clk_get_features`:

ti_clk_get_features
===================

.. c:function:: const struct ti_clk_features *ti_clk_get_features( void)

    get clock driver features flags

    :param void:
        no arguments
    :type void: 

.. _`ti_clk_get_features.description`:

Description
-----------

Get TI clock driver features description. Returns a pointer
to the current feature setup.

.. _`omap2_clk_enable_init_clocks`:

omap2_clk_enable_init_clocks
============================

.. c:function:: void omap2_clk_enable_init_clocks(const char **clk_names, u8 num_clocks)

    prepare & enable a list of clocks

    :param clk_names:
        ptr to an array of strings of clock names to enable
    :type clk_names: const char \*\*

    :param num_clocks:
        number of clock names in \ ``clk_names``\ 
    :type num_clocks: u8

.. _`omap2_clk_enable_init_clocks.description`:

Description
-----------

Prepare and enable a list of clocks, named by \ ``clk_names``\ .  No
return value. XXX Deprecated; only needed until these clocks are
properly claimed and enabled by the drivers or core code that uses
them.  XXX What code disables & calls clk_put on these clocks?

.. _`ti_clk_add_alias`:

ti_clk_add_alias
================

.. c:function:: int ti_clk_add_alias(struct device *dev, struct clk *clk, const char *con)

    add a clock alias for a TI clock

    :param dev:
        device alias for this clock
    :type dev: struct device \*

    :param clk:
        clock handle to create alias for
    :type clk: struct clk \*

    :param con:
        connection ID for this clock
    :type con: const char \*

.. _`ti_clk_add_alias.description`:

Description
-----------

Creates a clock alias for a TI clock. Allocates the clock lookup entry
and assigns the data to it. Returns 0 if successful, negative error
value otherwise.

.. _`ti_clk_register`:

ti_clk_register
===============

.. c:function:: struct clk *ti_clk_register(struct device *dev, struct clk_hw *hw, const char *con)

    register a TI clock to the common clock framework

    :param dev:
        device for this clock
    :type dev: struct device \*

    :param hw:
        hardware clock handle
    :type hw: struct clk_hw \*

    :param con:
        connection ID for this clock
    :type con: const char \*

.. _`ti_clk_register.description`:

Description
-----------

Registers a TI clock to the common clock framework, and adds a clock
alias for it. Returns a handle to the registered clock if successful,
ERR_PTR value in failure.

.. This file was automatic generated / don't edit.

