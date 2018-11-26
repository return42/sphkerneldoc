.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/fsl-mc/dprc-driver.c

.. _`dprc_remove_devices`:

dprc_remove_devices
===================

.. c:function:: void dprc_remove_devices(struct fsl_mc_device *mc_bus_dev, struct fsl_mc_obj_desc *obj_desc_array, int num_child_objects_in_mc)

    Removes devices for objects removed from a DPRC

    :param mc_bus_dev:
        pointer to the fsl-mc device that represents a DPRC object
    :type mc_bus_dev: struct fsl_mc_device \*

    :param obj_desc_array:
        array of object descriptors for child objects currently
        present in the DPRC in the MC.
    :type obj_desc_array: struct fsl_mc_obj_desc \*

    :param num_child_objects_in_mc:
        number of entries in obj_desc_array
    :type num_child_objects_in_mc: int

.. _`dprc_remove_devices.description`:

Description
-----------

Synchronizes the state of the Linux bus driver with the actual state of
the MC by removing devices that represent MC objects that have
been dynamically removed in the physical DPRC.

.. _`check_plugged_state_change`:

check_plugged_state_change
==========================

.. c:function:: void check_plugged_state_change(struct fsl_mc_device *mc_dev, struct fsl_mc_obj_desc *obj_desc)

    Check change in an MC object's plugged state

    :param mc_dev:
        pointer to the fsl-mc device for a given MC object
    :type mc_dev: struct fsl_mc_device \*

    :param obj_desc:
        pointer to the MC object's descriptor in the MC
    :type obj_desc: struct fsl_mc_obj_desc \*

.. _`check_plugged_state_change.description`:

Description
-----------

If the plugged state has changed from unplugged to plugged, the fsl-mc
device is bound to the corresponding device driver.
If the plugged state has changed from plugged to unplugged, the fsl-mc
device is unbound from the corresponding device driver.

.. _`dprc_add_new_devices`:

dprc_add_new_devices
====================

.. c:function:: void dprc_add_new_devices(struct fsl_mc_device *mc_bus_dev, struct fsl_mc_obj_desc *obj_desc_array, int num_child_objects_in_mc)

    Adds devices to the logical bus for a DPRC

    :param mc_bus_dev:
        pointer to the fsl-mc device that represents a DPRC object
    :type mc_bus_dev: struct fsl_mc_device \*

    :param obj_desc_array:
        array of device descriptors for child devices currently
        present in the physical DPRC.
    :type obj_desc_array: struct fsl_mc_obj_desc \*

    :param num_child_objects_in_mc:
        number of entries in obj_desc_array
    :type num_child_objects_in_mc: int

.. _`dprc_add_new_devices.description`:

Description
-----------

Synchronizes the state of the Linux bus driver with the actual
state of the MC by adding objects that have been newly discovered
in the physical DPRC.

.. _`dprc_scan_objects`:

dprc_scan_objects
=================

.. c:function:: int dprc_scan_objects(struct fsl_mc_device *mc_bus_dev, unsigned int *total_irq_count)

    Discover objects in a DPRC

    :param mc_bus_dev:
        pointer to the fsl-mc device that represents a DPRC object
    :type mc_bus_dev: struct fsl_mc_device \*

    :param total_irq_count:
        If argument is provided the function populates the
        total number of IRQs created by objects in the DPRC.
    :type total_irq_count: unsigned int \*

.. _`dprc_scan_objects.description`:

Description
-----------

Detects objects added and removed from a DPRC and synchronizes the
state of the Linux bus driver, MC by adding and removing
devices accordingly.

.. _`dprc_scan_objects.two-types-of-devices-can-be-found-in-a-dprc`:

Two types of devices can be found in a DPRC
-------------------------------------------

allocatable objects (e.g.,
dpbp, dpmcp) and non-allocatable devices (e.g., dprc, dpni).
All allocatable devices needed to be probed before all non-allocatable
devices, to ensure that device drivers for non-allocatable
devices can allocate any type of allocatable devices.
That is, we need to ensure that the corresponding resource pools are
populated before they can get allocation requests from probe callbacks
of the device drivers for the non-allocatable devices.

.. _`dprc_scan_container`:

dprc_scan_container
===================

.. c:function:: int dprc_scan_container(struct fsl_mc_device *mc_bus_dev)

    Scans a physical DPRC and synchronizes Linux bus state

    :param mc_bus_dev:
        pointer to the fsl-mc device that represents a DPRC object
    :type mc_bus_dev: struct fsl_mc_device \*

.. _`dprc_scan_container.description`:

Description
-----------

Scans the physical DPRC and synchronizes the state of the Linux
bus driver with the actual state of the MC by adding and removing
devices as appropriate.

.. _`dprc_irq0_handler`:

dprc_irq0_handler
=================

.. c:function:: irqreturn_t dprc_irq0_handler(int irq_num, void *arg)

    Regular ISR for DPRC interrupt 0

    :param irq_num:
        *undescribed*
    :type irq_num: int

    :param arg:
        Pointer to device structure
    :type arg: void \*

.. _`dprc_irq0_handler_thread`:

dprc_irq0_handler_thread
========================

.. c:function:: irqreturn_t dprc_irq0_handler_thread(int irq_num, void *arg)

    Handler thread function for DPRC interrupt 0

    :param irq_num:
        *undescribed*
    :type irq_num: int

    :param arg:
        Pointer to device structure
    :type arg: void \*

.. _`dprc_probe`:

dprc_probe
==========

.. c:function:: int dprc_probe(struct fsl_mc_device *mc_dev)

    callback invoked when a DPRC is being bound to this driver

    :param mc_dev:
        Pointer to fsl-mc device representing a DPRC
    :type mc_dev: struct fsl_mc_device \*

.. _`dprc_probe.description`:

Description
-----------

It opens the physical DPRC in the MC.
It scans the DPRC to discover the MC objects contained in it.
It creates the interrupt pool for the MC bus associated with the DPRC.
It configures the interrupts for the DPRC device itself.

.. _`dprc_remove`:

dprc_remove
===========

.. c:function:: int dprc_remove(struct fsl_mc_device *mc_dev)

    callback invoked when a DPRC is being unbound from this driver

    :param mc_dev:
        Pointer to fsl-mc device representing the DPRC
    :type mc_dev: struct fsl_mc_device \*

.. _`dprc_remove.description`:

Description
-----------

It removes the DPRC's child objects from Linux (not from the MC) and
closes the DPRC device in the MC.
It tears down the interrupts that were configured for the DPRC device.
It destroys the interrupt pool associated with this MC bus.

.. This file was automatic generated / don't edit.

