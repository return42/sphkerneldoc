.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/platform.c

.. _`dwc2_lowlevel_hw_enable`:

dwc2_lowlevel_hw_enable
=======================

.. c:function:: int dwc2_lowlevel_hw_enable(struct dwc2_hsotg *hsotg)

    enable platform lowlevel hw resources

    :param hsotg:
        The driver state
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_lowlevel_hw_enable.description`:

Description
-----------

A wrapper for platform code responsible for controlling
low-level USB platform resources (phy, clock, regulators)

.. _`dwc2_lowlevel_hw_disable`:

dwc2_lowlevel_hw_disable
========================

.. c:function:: int dwc2_lowlevel_hw_disable(struct dwc2_hsotg *hsotg)

    disable platform lowlevel hw resources

    :param hsotg:
        The driver state
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_lowlevel_hw_disable.description`:

Description
-----------

A wrapper for platform code responsible for controlling
low-level USB platform resources (phy, clock, regulators)

.. _`dwc2_driver_remove`:

dwc2_driver_remove
==================

.. c:function:: int dwc2_driver_remove(struct platform_device *dev)

    Called when the DWC_otg core is unregistered with the DWC_otg driver

    :param dev:
        Platform device
    :type dev: struct platform_device \*

.. _`dwc2_driver_remove.description`:

Description
-----------

This routine is called, for example, when the rmmod command is executed. The
device may or may not be electrically present. If it is present, the driver
stops device processing. Any resources used on behalf of this device are
freed.

.. _`dwc2_driver_shutdown`:

dwc2_driver_shutdown
====================

.. c:function:: void dwc2_driver_shutdown(struct platform_device *dev)

    Called on device shutdown

    :param dev:
        Platform device
    :type dev: struct platform_device \*

.. _`dwc2_driver_shutdown.description`:

Description
-----------

In specific conditions (involving usb hubs) dwc2 devices can create a
lot of interrupts, even to the point of overwhelming devices running
at low frequencies. Some devices need to do special clock handling
at shutdown-time which may bring the system clock below the threshold
of being able to handle the dwc2 interrupts. Disabling dwc2-irqs
prevents reboots/poweroffs from getting stuck in such cases.

.. _`dwc2_check_core_endianness`:

dwc2_check_core_endianness
==========================

.. c:function:: bool dwc2_check_core_endianness(struct dwc2_hsotg *hsotg)

    Returns true if core and AHB have opposite endianness.

    :param hsotg:
        Programming view of the DWC_otg controller.
    :type hsotg: struct dwc2_hsotg \*

.. _`dwc2_driver_probe`:

dwc2_driver_probe
=================

.. c:function:: int dwc2_driver_probe(struct platform_device *dev)

    Called when the DWC_otg core is bound to the DWC_otg driver

    :param dev:
        Platform device
    :type dev: struct platform_device \*

.. _`dwc2_driver_probe.description`:

Description
-----------

This routine creates the driver components required to control the device
(core, HCD, and PCD) and initializes the device. The driver components are
stored in a dwc2_hsotg structure. A reference to the dwc2_hsotg is saved
in the device private data. This allows the driver to access the dwc2_hsotg
structure on subsequent calls to driver methods for this device.

.. This file was automatic generated / don't edit.

