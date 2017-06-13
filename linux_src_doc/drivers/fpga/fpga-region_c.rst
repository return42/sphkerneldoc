.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/fpga-region.c

.. _`fpga_region`:

struct fpga_region
==================

.. c:type:: struct fpga_region

    FPGA Region structure

.. _`fpga_region.definition`:

Definition
----------

.. code-block:: c

    struct fpga_region {
        struct device dev;
        struct mutex mutex;
        struct list_head bridge_list;
        struct fpga_image_info *info;
    }

.. _`fpga_region.members`:

Members
-------

dev
    FPGA Region device

mutex
    enforces exclusive reference to region

bridge_list
    list of FPGA bridges specified in region

info
    fpga image specific information

.. _`fpga_region_find`:

fpga_region_find
================

.. c:function:: struct fpga_region *fpga_region_find(struct device_node *np)

    find FPGA region

    :param struct device_node \*np:
        device node of FPGA Region
        Caller will need to put_device(&region->dev) when done.
        Returns FPGA Region struct or NULL

.. _`fpga_region_get`:

fpga_region_get
===============

.. c:function:: struct fpga_region *fpga_region_get(struct fpga_region *region)

    get an exclusive reference to a fpga region

    :param struct fpga_region \*region:
        FPGA Region struct

.. _`fpga_region_get.description`:

Description
-----------

Caller should call \ :c:func:`fpga_region_put`\  when done with region.

Return fpga_region struct if successful.
Return -EBUSY if someone already has a reference to the region.
Return -ENODEV if \ ``np``\  is not a FPGA Region.

.. _`fpga_region_put`:

fpga_region_put
===============

.. c:function:: void fpga_region_put(struct fpga_region *region)

    release a reference to a region

    :param struct fpga_region \*region:
        FPGA region

.. _`fpga_region_get_manager`:

fpga_region_get_manager
=======================

.. c:function:: struct fpga_manager *fpga_region_get_manager(struct fpga_region *region)

    get exclusive reference for FPGA manager

    :param struct fpga_region \*region:
        FPGA region

.. _`fpga_region_get_manager.description`:

Description
-----------

Get FPGA Manager from "fpga-mgr" property or from ancestor region.

Caller should call \ :c:func:`fpga_mgr_put`\  when done with manager.

.. _`fpga_region_get_manager.return`:

Return
------

fpga manager struct or \ :c:func:`IS_ERR`\  condition containing error code.

.. _`fpga_region_get_bridges`:

fpga_region_get_bridges
=======================

.. c:function:: int fpga_region_get_bridges(struct fpga_region *region, struct device_node *overlay)

    create a list of bridges

    :param struct fpga_region \*region:
        FPGA region

    :param struct device_node \*overlay:
        device node of the overlay

.. _`fpga_region_get_bridges.description`:

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

.. _`fpga_region_program_fpga`:

fpga_region_program_fpga
========================

.. c:function:: int fpga_region_program_fpga(struct fpga_region *region, const char *firmware_name, struct device_node *overlay)

    program FPGA

    :param struct fpga_region \*region:
        FPGA region

    :param const char \*firmware_name:
        name of FPGA image firmware file

    :param struct device_node \*overlay:
        device node of the overlay
        Program an FPGA using information in the device tree.
        Function assumes that there is a firmware-name property.
        Return 0 for success or negative error code.

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

.. _`fpga_region_notify_pre_apply`:

fpga_region_notify_pre_apply
============================

.. c:function:: int fpga_region_notify_pre_apply(struct fpga_region *region, struct of_overlay_notify_data *nd)

    pre-apply overlay notification

    :param struct fpga_region \*region:
        FPGA region that the overlay was applied to

    :param struct of_overlay_notify_data \*nd:
        overlay notification data

.. _`fpga_region_notify_pre_apply.description`:

Description
-----------

Called after when an overlay targeted to a FPGA Region is about to be
applied.  Function will check the properties that will be added to the FPGA
region.  If the checks pass, it will program the FPGA.

.. _`fpga_region_notify_pre_apply.the-checks-are`:

The checks are
--------------

The overlay must add either firmware-name or external-fpga-config property
to the FPGA Region.

firmware-name         : program the FPGA
external-fpga-config  : FPGA is already programmed
encrypted-fpga-config : FPGA bitstream is encrypted

The overlay can add other FPGA regions, but child FPGA regions cannot have a
firmware-name property since those regions don't exist yet.

If the overlay that breaks the rules, notifier returns an error and the
overlay is rejected before it goes into the main tree.

Returns 0 for success or negative error code for failure.

.. _`fpga_region_notify_post_remove`:

fpga_region_notify_post_remove
==============================

.. c:function:: void fpga_region_notify_post_remove(struct fpga_region *region, struct of_overlay_notify_data *nd)

    post-remove overlay notification

    :param struct fpga_region \*region:
        FPGA region that was targeted by the overlay that was removed

    :param struct of_overlay_notify_data \*nd:
        overlay notification data

.. _`fpga_region_notify_post_remove.description`:

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

.. _`fpga_region_init`:

fpga_region_init
================

.. c:function:: int fpga_region_init( void)

    init function for fpga_region class Creates the fpga_region class and registers a reconfig notifier.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

