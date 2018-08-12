.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/keystone/sci-clk.c

.. _`sci_clk_provider`:

struct sci_clk_provider
=======================

.. c:type:: struct sci_clk_provider

    TI SCI clock provider representation

.. _`sci_clk_provider.definition`:

Definition
----------

.. code-block:: c

    struct sci_clk_provider {
        const struct ti_sci_handle *sci;
        const struct ti_sci_clk_ops *ops;
        struct device *dev;
        struct sci_clk **clocks;
        int num_clocks;
    }

.. _`sci_clk_provider.members`:

Members
-------

sci
    Handle to the System Control Interface protocol handler

ops
    Pointer to the SCI ops to be used by the clocks

dev
    Device pointer for the clock provider

clocks
    Clocks array for this device

num_clocks
    Total number of clocks for this provider

.. _`sci_clk`:

struct sci_clk
==============

.. c:type:: struct sci_clk

    TI SCI clock representation

.. _`sci_clk.definition`:

Definition
----------

.. code-block:: c

    struct sci_clk {
        struct clk_hw hw;
        u16 dev_id;
        u8 clk_id;
        u8 num_parents;
        struct sci_clk_provider *provider;
        u8 flags;
    }

.. _`sci_clk.members`:

Members
-------

hw
    Hardware clock cookie for common clock framework

dev_id
    Device index

clk_id
    Clock index

num_parents
    Number of parents for this clock

provider
    Master clock provider

flags
    Flags for the clock

.. _`sci_clk_prepare`:

sci_clk_prepare
===============

.. c:function:: int sci_clk_prepare(struct clk_hw *hw)

    Prepare (enable) a TI SCI clock

    :param struct clk_hw \*hw:
        clock to prepare

.. _`sci_clk_prepare.description`:

Description
-----------

Prepares a clock to be actively used. Returns the SCI protocol status.

.. _`sci_clk_unprepare`:

sci_clk_unprepare
=================

.. c:function:: void sci_clk_unprepare(struct clk_hw *hw)

    Un-prepares (disables) a TI SCI clock

    :param struct clk_hw \*hw:
        clock to unprepare

.. _`sci_clk_unprepare.description`:

Description
-----------

Un-prepares a clock from active state.

.. _`sci_clk_is_prepared`:

sci_clk_is_prepared
===================

.. c:function:: int sci_clk_is_prepared(struct clk_hw *hw)

    Check if a TI SCI clock is prepared or not

    :param struct clk_hw \*hw:
        clock to check status for

.. _`sci_clk_is_prepared.description`:

Description
-----------

Checks if a clock is prepared (enabled) in hardware. Returns non-zero
value if clock is enabled, zero otherwise.

.. _`sci_clk_recalc_rate`:

sci_clk_recalc_rate
===================

.. c:function:: unsigned long sci_clk_recalc_rate(struct clk_hw *hw, unsigned long parent_rate)

    Get clock rate for a TI SCI clock

    :param struct clk_hw \*hw:
        clock to get rate for

    :param unsigned long parent_rate:
        parent rate provided by common clock framework, not used

.. _`sci_clk_recalc_rate.description`:

Description
-----------

Gets the current clock rate of a TI SCI clock. Returns the current
clock rate, or zero in failure.

.. _`sci_clk_determine_rate`:

sci_clk_determine_rate
======================

.. c:function:: int sci_clk_determine_rate(struct clk_hw *hw, struct clk_rate_request *req)

    Determines a clock rate a clock can be set to

    :param struct clk_hw \*hw:
        clock to change rate for

    :param struct clk_rate_request \*req:
        requested rate configuration for the clock

.. _`sci_clk_determine_rate.description`:

Description
-----------

Determines a suitable clock rate and parent for a TI SCI clock.
The parent handling is un-used, as generally the parent clock rates
are not known by the kernel; instead these are internally handled
by the firmware. Returns 0 on success, negative error value on failure.

.. _`sci_clk_set_rate`:

sci_clk_set_rate
================

.. c:function:: int sci_clk_set_rate(struct clk_hw *hw, unsigned long rate, unsigned long parent_rate)

    Set rate for a TI SCI clock

    :param struct clk_hw \*hw:
        clock to change rate for

    :param unsigned long rate:
        target rate for the clock

    :param unsigned long parent_rate:
        rate of the clock parent, not used for TI SCI clocks

.. _`sci_clk_set_rate.description`:

Description
-----------

Sets a clock frequency for a TI SCI clock. Returns the TI SCI
protocol status.

.. _`sci_clk_get_parent`:

sci_clk_get_parent
==================

.. c:function:: u8 sci_clk_get_parent(struct clk_hw *hw)

    Get the current parent of a TI SCI clock

    :param struct clk_hw \*hw:
        clock to get parent for

.. _`sci_clk_get_parent.description`:

Description
-----------

Returns the index of the currently selected parent for a TI SCI clock.

.. _`sci_clk_set_parent`:

sci_clk_set_parent
==================

.. c:function:: int sci_clk_set_parent(struct clk_hw *hw, u8 index)

    Set the parent of a TI SCI clock

    :param struct clk_hw \*hw:
        clock to set parent for

    :param u8 index:
        new parent index for the clock

.. _`sci_clk_set_parent.description`:

Description
-----------

Sets the parent of a TI SCI clock. Return TI SCI protocol status.

.. _`_sci_clk_build`:

\_sci_clk_build
===============

.. c:function:: int _sci_clk_build(struct sci_clk_provider *provider, struct sci_clk *sci_clk)

    Gets a handle for an SCI clock

    :param struct sci_clk_provider \*provider:
        Handle to SCI clock provider

    :param struct sci_clk \*sci_clk:
        Handle to the SCI clock to populate

.. _`_sci_clk_build.description`:

Description
-----------

Gets a handle to an existing TI SCI hw clock, or builds a new clock
entry and registers it with the common clock framework. Called from
the common clock framework, when a corresponding of_clk_get call is
executed, or recursively from itself when parsing parent clocks.
Returns 0 on success, negative error code on failure.

.. _`sci_clk_get`:

sci_clk_get
===========

.. c:function:: struct clk_hw *sci_clk_get(struct of_phandle_args *clkspec, void *data)

    Xlate function for getting clock handles

    :param struct of_phandle_args \*clkspec:
        device tree clock specifier

    :param void \*data:
        pointer to the clock provider

.. _`sci_clk_get.description`:

Description
-----------

Xlate function for retrieving clock TI SCI hw clock handles based on
device tree clock specifier. Called from the common clock framework,
when a corresponding of_clk_get call is executed. Returns a pointer
to the TI SCI hw clock struct, or ERR_PTR value in failure.

.. _`ti_sci_clk_probe`:

ti_sci_clk_probe
================

.. c:function:: int ti_sci_clk_probe(struct platform_device *pdev)

    Probe function for the TI SCI clock driver

    :param struct platform_device \*pdev:
        platform device pointer to be probed

.. _`ti_sci_clk_probe.description`:

Description
-----------

Probes the TI SCI clock device. Allocates a new clock provider
and registers this to the common clock framework. Also applies
any required flags to the identified clocks via clock lists
supplied from DT. Returns 0 for success, negative error value
for failure.

.. _`ti_sci_clk_remove`:

ti_sci_clk_remove
=================

.. c:function:: int ti_sci_clk_remove(struct platform_device *pdev)

    Remove TI SCI clock device

    :param struct platform_device \*pdev:
        platform device pointer for the device to be removed

.. _`ti_sci_clk_remove.description`:

Description
-----------

Removes the TI SCI device. Unregisters the clock provider registered
via common clock framework. Any memory allocated for the device will
be free'd silently via the devm framework. Returns 0 always.

.. This file was automatic generated / don't edit.

