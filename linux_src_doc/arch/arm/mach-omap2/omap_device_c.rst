.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap_device.c

.. _`_add_hwmod_clocks_clkdev`:

\_add_hwmod_clocks_clkdev
=========================

.. c:function:: void _add_hwmod_clocks_clkdev(struct omap_device *od, struct omap_hwmod *oh)

    Add clkdev entry for hwmod optional clocks and main clock

    :param od:
        struct omap_device \*od
    :type od: struct omap_device \*

    :param oh:
        struct omap_hwmod \*oh
    :type oh: struct omap_hwmod \*

.. _`_add_hwmod_clocks_clkdev.description`:

Description
-----------

For the main clock and every optional clock present per hwmod per
omap_device, this function adds an entry in the clkdev table of the
form <dev-id=dev_name, con-id=role> if it does not exist already.

The function is called from inside \ :c:func:`omap_device_build_ss`\ , after
omap_device_register.

This allows drivers to get a pointer to its optional clocks based on its role
by calling clk_get(<dev\*>, <role>).
In the case of the main clock, a "fck" alias is used.

No return value.

.. _`omap_device_build_from_dt`:

omap_device_build_from_dt
=========================

.. c:function:: int omap_device_build_from_dt(struct platform_device *pdev)

    build an omap_device with multiple hwmods

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`omap_device_build_from_dt.description`:

Description
-----------

Function for building an omap_device already registered from device-tree

Returns 0 or \ :c:func:`PTR_ERR`\  on error.

.. _`_omap_device_enable_hwmods`:

\_omap_device_enable_hwmods
===========================

.. c:function:: int _omap_device_enable_hwmods(struct omap_device *od)

    call \ :c:func:`omap_hwmod_enable`\  on all hwmods

    :param od:
        struct omap_device \*od
    :type od: struct omap_device \*

.. _`_omap_device_enable_hwmods.description`:

Description
-----------

Enable all underlying hwmods.  Returns 0.

.. _`_omap_device_idle_hwmods`:

\_omap_device_idle_hwmods
=========================

.. c:function:: int _omap_device_idle_hwmods(struct omap_device *od)

    call \ :c:func:`omap_hwmod_idle`\  on all hwmods

    :param od:
        struct omap_device \*od
    :type od: struct omap_device \*

.. _`_omap_device_idle_hwmods.description`:

Description
-----------

Idle all underlying hwmods.  Returns 0.

.. _`omap_device_get_context_loss_count`:

omap_device_get_context_loss_count
==================================

.. c:function:: int omap_device_get_context_loss_count(struct platform_device *pdev)

    get lost context count

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`omap_device_get_context_loss_count.description`:

Description
-----------

Using the primary hwmod, query the context loss count for this
device.

Callers should consider context for this device lost any time this
function returns a value different than the value the caller got
the last time it called this function.

If any hwmods exist for the omap_device associated with \ ``pdev``\ ,
return the context loss counter for that hwmod, otherwise return
zero.

.. _`omap_device_alloc`:

omap_device_alloc
=================

.. c:function:: struct omap_device *omap_device_alloc(struct platform_device *pdev, struct omap_hwmod **ohs, int oh_cnt)

    allocate an omap_device

    :param pdev:
        platform_device that will be included in this omap_device
    :type pdev: struct platform_device \*

    :param ohs:
        *undescribed*
    :type ohs: struct omap_hwmod \*\*

    :param oh_cnt:
        *undescribed*
    :type oh_cnt: int

.. _`omap_device_alloc.description`:

Description
-----------

Convenience function for allocating an omap_device structure and filling
hwmods, and resources.

Returns an struct omap_device pointer or \ :c:func:`ERR_PTR`\  on error;

.. _`omap_device_copy_resources`:

omap_device_copy_resources
==========================

.. c:function:: int omap_device_copy_resources(struct omap_hwmod *oh, struct platform_device *pdev)

    Add legacy IO and IRQ resources

    :param oh:
        interconnect target module
    :type oh: struct omap_hwmod \*

    :param pdev:
        platform device to copy resources to
    :type pdev: struct platform_device \*

.. _`omap_device_copy_resources.description`:

Description
-----------

We still have legacy DMA and smartreflex needing resources.
Let's populate what they need until we can eventually just
remove this function. Note that there should be no need to
call this from \ :c:func:`omap_device_build_from_dt`\ , nor should there
be any need to call it for other devices.

.. _`omap_device_build`:

omap_device_build
=================

.. c:function:: struct platform_device *omap_device_build(const char *pdev_name, int pdev_id, struct omap_hwmod *oh, void *pdata, int pdata_len)

    build and register an omap_device with one omap_hwmod

    :param pdev_name:
        name of the platform_device driver to use
    :type pdev_name: const char \*

    :param pdev_id:
        this platform_device's connection ID
    :type pdev_id: int

    :param oh:
        ptr to the single omap_hwmod that backs this omap_device
    :type oh: struct omap_hwmod \*

    :param pdata:
        platform_data ptr to associate with the platform_device
    :type pdata: void \*

    :param pdata_len:
        amount of memory pointed to by \ ``pdata``\ 
    :type pdata_len: int

.. _`omap_device_build.description`:

Description
-----------

Convenience function for building and registering a single
omap_device record, which in turn builds and registers a
platform_device record.  See \ :c:func:`omap_device_build_ss`\  for more
information.  Returns ERR_PTR(-EINVAL) if \ ``oh``\  is NULL; otherwise,
passes along the return value of \ :c:func:`omap_device_build_ss`\ .

.. _`omap_device_register`:

omap_device_register
====================

.. c:function:: int omap_device_register(struct platform_device *pdev)

    register an omap_device with one omap_hwmod

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`omap_device_register.description`:

Description
-----------

Register the omap_device structure.  This currently just calls
\ :c:func:`platform_device_register`\  on the underlying platform_device.
Returns the return value of \ :c:func:`platform_device_register`\ .

.. _`omap_device_enable`:

omap_device_enable
==================

.. c:function:: int omap_device_enable(struct platform_device *pdev)

    fully activate an omap_device

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`omap_device_enable.description`:

Description
-----------

Do whatever is necessary for the hwmods underlying omap_device \ ``od``\ 
to be accessible and ready to operate.  This generally involves
enabling clocks, setting SYSCONFIG registers; and in the future may
involve remuxing pins.  Device drivers should call this function
indirectly via pm_runtime_get\*().  Returns -EINVAL if called when
the omap_device is already enabled, or passes along the return
value of \_omap_device_enable_hwmods().

.. _`omap_device_idle`:

omap_device_idle
================

.. c:function:: int omap_device_idle(struct platform_device *pdev)

    idle an omap_device

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`omap_device_idle.description`:

Description
-----------

Idle omap_device \ ``od``\ .  Device drivers call this function indirectly
via pm_runtime_put\*().  Returns -EINVAL if the omap_device is not
currently enabled, or passes along the return value of
\_omap_device_idle_hwmods().

.. _`omap_device_assert_hardreset`:

omap_device_assert_hardreset
============================

.. c:function:: int omap_device_assert_hardreset(struct platform_device *pdev, const char *name)

    set a device's hardreset line

    :param pdev:
        struct platform_device \* to reset
    :type pdev: struct platform_device \*

    :param name:
        const char \* name of the reset line
    :type name: const char \*

.. _`omap_device_assert_hardreset.description`:

Description
-----------

Set the hardreset line identified by \ ``name``\  on the IP blocks
associated with the hwmods backing the platform_device \ ``pdev``\ .  All
of the hwmods associated with \ ``pdev``\  must have the same hardreset
line linked to them for this to work.  Passes along the return value
of \ :c:func:`omap_hwmod_assert_hardreset`\  in the event of any failure, or
returns 0 upon success.

.. _`omap_device_deassert_hardreset`:

omap_device_deassert_hardreset
==============================

.. c:function:: int omap_device_deassert_hardreset(struct platform_device *pdev, const char *name)

    release a device's hardreset line

    :param pdev:
        struct platform_device \* to reset
    :type pdev: struct platform_device \*

    :param name:
        const char \* name of the reset line
    :type name: const char \*

.. _`omap_device_deassert_hardreset.description`:

Description
-----------

Release the hardreset line identified by \ ``name``\  on the IP blocks
associated with the hwmods backing the platform_device \ ``pdev``\ .  All
of the hwmods associated with \ ``pdev``\  must have the same hardreset
line linked to them for this to work.  Passes along the return
value of \ :c:func:`omap_hwmod_deassert_hardreset`\  in the event of any
failure, or returns 0 upon success.

.. _`omap_device_get_by_hwmod_name`:

omap_device_get_by_hwmod_name
=============================

.. c:function:: struct device *omap_device_get_by_hwmod_name(const char *oh_name)

    convert a hwmod name to device pointer.

    :param oh_name:
        name of the hwmod device
    :type oh_name: const char \*

.. _`omap_device_get_by_hwmod_name.description`:

Description
-----------

Returns back a struct device \* pointer associated with a hwmod
device represented by a hwmod_name

.. _`omap_device_late_idle`:

omap_device_late_idle
=====================

.. c:function:: int omap_device_late_idle(struct device *dev, void *data)

    idle devices without drivers

    :param dev:
        struct device \* associated with omap_device
    :type dev: struct device \*

    :param data:
        unused
    :type data: void \*

.. _`omap_device_late_idle.description`:

Description
-----------

Check the driver bound status of this device, and idle it
if there is no driver attached.

.. This file was automatic generated / don't edit.

