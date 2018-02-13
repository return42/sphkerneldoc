.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/of-fpga-region.c

.. _`of_fpga_region_find`:

of_fpga_region_find
===================

.. c:function:: struct fpga_region *of_fpga_region_find(struct device_node *np)

    find FPGA region

    :param struct device_node \*np:
        device node of FPGA Region

.. _`of_fpga_region_find.description`:

Description
-----------

Caller will need to put_device(&region->dev) when done.

Returns FPGA Region struct or NULL

.. _`of_fpga_region_get_mgr`:

of_fpga_region_get_mgr
======================

.. c:function:: struct fpga_manager *of_fpga_region_get_mgr(struct device_node *np)

    get reference for FPGA manager

    :param struct device_node \*np:
        device node of FPGA region

.. _`of_fpga_region_get_mgr.description`:

Description
-----------

Get FPGA Manager from "fpga-mgr" property or from ancestor region.

Caller should call \ :c:func:`fpga_mgr_put`\  when done with manager.

.. _`of_fpga_region_get_mgr.return`:

Return
------

fpga manager struct or \ :c:func:`IS_ERR`\  condition containing error code.

.. _`of_fpga_region_get_bridges`:

of_fpga_region_get_bridges
==========================

.. c:function:: int of_fpga_region_get_bridges(struct fpga_region *region)

    create a list of bridges

    :param struct fpga_region \*region:
        FPGA region

.. _`of_fpga_region_get_bridges.description`:

Description
-----------

Create a list of bridges including the parent bridge and the bridges
specified by "fpga-bridges" property.  Note that the
fpga_bridges_enable/disable/put functions are all fine with an empty list
if that happens.

Caller should call fpga_bridges_put(&region->bridge_list) when
done with the bridges.

Return 0 for success (even if there are no bridges specified)
or -EBUSY if any of the bridges are in use.

.. _`child_regions_with_firmware`:

child_regions_with_firmware
===========================

.. c:function:: int child_regions_with_firmware(struct device_node *overlay)

    :param struct device_node \*overlay:
        device node of the overlay

.. _`child_regions_with_firmware.description`:

Description
-----------

If the overlay adds child FPGA regions, they are not allowed to have
firmware-name property.

Return 0 for OK or -EINVAL if child FPGA region adds firmware-name.

.. _`of_fpga_region_parse_ov`:

of_fpga_region_parse_ov
=======================

.. c:function:: struct fpga_image_info *of_fpga_region_parse_ov(struct fpga_region *region, struct device_node *overlay)

    parse and check overlay applied to region

    :param struct fpga_region \*region:
        FPGA region

    :param struct device_node \*overlay:
        overlay applied to the FPGA region

.. _`of_fpga_region_parse_ov.description`:

Description
-----------

Given an overlay applied to a FPGA region, parse the FPGA image specific
info in the overlay and do some checking.

.. _`of_fpga_region_parse_ov.return`:

Return
------

NULL if overlay doesn't direct us to program the FPGA.
fpga_image_info struct if there is an image to program.
error code for invalid overlay.

.. _`of_fpga_region_notify_pre_apply`:

of_fpga_region_notify_pre_apply
===============================

.. c:function:: int of_fpga_region_notify_pre_apply(struct fpga_region *region, struct of_overlay_notify_data *nd)

    pre-apply overlay notification

    :param struct fpga_region \*region:
        FPGA region that the overlay was applied to

    :param struct of_overlay_notify_data \*nd:
        overlay notification data

.. _`of_fpga_region_notify_pre_apply.description`:

Description
-----------

Called when an overlay targeted to a FPGA Region is about to be applied.
Parses the overlay for properties that influence how the FPGA will be
programmed and does some checking. If the checks pass, programs the FPGA.
If the checks fail, overlay is rejected and does not get added to the
live tree.

Returns 0 for success or negative error code for failure.

.. _`of_fpga_region_notify_post_remove`:

of_fpga_region_notify_post_remove
=================================

.. c:function:: void of_fpga_region_notify_post_remove(struct fpga_region *region, struct of_overlay_notify_data *nd)

    post-remove overlay notification

    :param struct fpga_region \*region:
        FPGA region that was targeted by the overlay that was removed

    :param struct of_overlay_notify_data \*nd:
        overlay notification data

.. _`of_fpga_region_notify_post_remove.description`:

Description
-----------

Called after an overlay has been removed if the overlay's target was a
FPGA region.

.. _`of_fpga_region_notify`:

of_fpga_region_notify
=====================

.. c:function:: int of_fpga_region_notify(struct notifier_block *nb, unsigned long action, void *arg)

    reconfig notifier for dynamic DT changes

    :param struct notifier_block \*nb:
        notifier block

    :param unsigned long action:
        notifier action

    :param void \*arg:
        reconfig data

.. _`of_fpga_region_notify.description`:

Description
-----------

This notifier handles programming a FPGA when a "firmware-name" property is
added to a fpga-region.

Returns NOTIFY_OK or error if FPGA programming fails.

.. _`of_fpga_region_init`:

of_fpga_region_init
===================

.. c:function:: int of_fpga_region_init( void)

    init function for fpga_region class Creates the fpga_region class and registers a reconfig notifier.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

