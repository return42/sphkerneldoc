.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/libahci_platform.c

.. _`ahci_platform_enable_phys`:

ahci_platform_enable_phys
=========================

.. c:function:: int ahci_platform_enable_phys(struct ahci_host_priv *hpriv)

    Enable PHYs

    :param hpriv:
        host private area to store config values
    :type hpriv: struct ahci_host_priv \*

.. _`ahci_platform_enable_phys.description`:

Description
-----------

This function enables all the PHYs found in hpriv->phys, if any.
If a PHY fails to be enabled, it disables all the PHYs already
enabled in reverse order and returns an error.

.. _`ahci_platform_enable_phys.return`:

Return
------

0 on success otherwise a negative error code

.. _`ahci_platform_disable_phys`:

ahci_platform_disable_phys
==========================

.. c:function:: void ahci_platform_disable_phys(struct ahci_host_priv *hpriv)

    Disable PHYs

    :param hpriv:
        host private area to store config values
    :type hpriv: struct ahci_host_priv \*

.. _`ahci_platform_disable_phys.description`:

Description
-----------

This function disables all PHYs found in hpriv->phys.

.. _`ahci_platform_enable_clks`:

ahci_platform_enable_clks
=========================

.. c:function:: int ahci_platform_enable_clks(struct ahci_host_priv *hpriv)

    Enable platform clocks

    :param hpriv:
        host private area to store config values
    :type hpriv: struct ahci_host_priv \*

.. _`ahci_platform_enable_clks.description`:

Description
-----------

This function enables all the clks found in hpriv->clks, starting at
index 0. If any clk fails to enable it disables all the clks already
enabled in reverse order, and then returns an error.

.. _`ahci_platform_enable_clks.return`:

Return
------

0 on success otherwise a negative error code

.. _`ahci_platform_disable_clks`:

ahci_platform_disable_clks
==========================

.. c:function:: void ahci_platform_disable_clks(struct ahci_host_priv *hpriv)

    Disable platform clocks

    :param hpriv:
        host private area to store config values
    :type hpriv: struct ahci_host_priv \*

.. _`ahci_platform_disable_clks.description`:

Description
-----------

This function disables all the clks found in hpriv->clks, in reverse
order of ahci_platform_enable_clks (starting at the end of the array).

.. _`ahci_platform_enable_regulators`:

ahci_platform_enable_regulators
===============================

.. c:function:: int ahci_platform_enable_regulators(struct ahci_host_priv *hpriv)

    Enable regulators

    :param hpriv:
        host private area to store config values
    :type hpriv: struct ahci_host_priv \*

.. _`ahci_platform_enable_regulators.description`:

Description
-----------

This function enables all the regulators found in controller and
hpriv->target_pwrs, if any.  If a regulator fails to be enabled, it
disables all the regulators already enabled in reverse order and
returns an error.

.. _`ahci_platform_enable_regulators.return`:

Return
------

0 on success otherwise a negative error code

.. _`ahci_platform_disable_regulators`:

ahci_platform_disable_regulators
================================

.. c:function:: void ahci_platform_disable_regulators(struct ahci_host_priv *hpriv)

    Disable regulators

    :param hpriv:
        host private area to store config values
    :type hpriv: struct ahci_host_priv \*

.. _`ahci_platform_disable_regulators.description`:

Description
-----------

This function disables all regulators found in hpriv->target_pwrs and
AHCI controller.

.. _`ahci_platform_enable_resources`:

ahci_platform_enable_resources
==============================

.. c:function:: int ahci_platform_enable_resources(struct ahci_host_priv *hpriv)

    Enable platform resources

    :param hpriv:
        host private area to store config values
    :type hpriv: struct ahci_host_priv \*

.. _`ahci_platform_enable_resources.description`:

Description
-----------

This function enables all ahci_platform managed resources in the

.. _`ahci_platform_enable_resources.following-order`:

following order
---------------

1) Regulator
2) Clocks (through ahci_platform_enable_clks)
3) Resets
4) Phys

If resource enabling fails at any point the previous enabled resources
are disabled in reverse order.

.. _`ahci_platform_enable_resources.return`:

Return
------

0 on success otherwise a negative error code

.. _`ahci_platform_disable_resources`:

ahci_platform_disable_resources
===============================

.. c:function:: void ahci_platform_disable_resources(struct ahci_host_priv *hpriv)

    Disable platform resources

    :param hpriv:
        host private area to store config values
    :type hpriv: struct ahci_host_priv \*

.. _`ahci_platform_disable_resources.description`:

Description
-----------

This function disables all ahci_platform managed resources in the

.. _`ahci_platform_disable_resources.following-order`:

following order
---------------

1) Phys
2) Resets
3) Clocks (through ahci_platform_disable_clks)
4) Regulator

.. _`ahci_platform_get_resources`:

ahci_platform_get_resources
===========================

.. c:function:: struct ahci_host_priv *ahci_platform_get_resources(struct platform_device *pdev, unsigned int flags)

    Get platform resources

    :param pdev:
        platform device to get resources for
    :type pdev: struct platform_device \*

    :param flags:
        bitmap representing the resource to get
    :type flags: unsigned int

.. _`ahci_platform_get_resources.description`:

Description
-----------

This function allocates an ahci_host_priv struct, and gets the following
resources, storing a reference to them inside the returned struct:

1) mmio registers (IORESOURCE_MEM 0, mandatory)
2) regulator for controlling the targets power (optional)
regulator for controlling the AHCI controller (optional)
3) 0 - AHCI_MAX_CLKS clocks, as specified in the devs devicetree node,
or for non devicetree enabled platforms a single clock
4) resets, if flags has AHCI_PLATFORM_GET_RESETS (optional)
5) phys (optional)

.. _`ahci_platform_get_resources.return`:

Return
------

The allocated ahci_host_priv on success, otherwise an ERR_PTR value

.. _`ahci_platform_init_host`:

ahci_platform_init_host
=======================

.. c:function:: int ahci_platform_init_host(struct platform_device *pdev, struct ahci_host_priv *hpriv, const struct ata_port_info *pi_template, struct scsi_host_template *sht)

    Bring up an ahci-platform host

    :param pdev:
        platform device pointer for the host
    :type pdev: struct platform_device \*

    :param hpriv:
        ahci-host private data for the host
    :type hpriv: struct ahci_host_priv \*

    :param pi_template:
        template for the ata_port_info to use
    :type pi_template: const struct ata_port_info \*

    :param sht:
        scsi_host_template to use when registering
    :type sht: struct scsi_host_template \*

.. _`ahci_platform_init_host.description`:

Description
-----------

This function does all the usual steps needed to bring up an
ahci-platform host, note any necessary resources (ie clks, phys, etc.)
must be initialized / enabled before calling this.

.. _`ahci_platform_init_host.return`:

Return
------

0 on success otherwise a negative error code

.. _`ahci_platform_shutdown`:

ahci_platform_shutdown
======================

.. c:function:: void ahci_platform_shutdown(struct platform_device *pdev)

    Disable interrupts and stop DMA for host ports

    :param pdev:
        platform device pointer for the host
    :type pdev: struct platform_device \*

.. _`ahci_platform_shutdown.description`:

Description
-----------

This function is called during system shutdown and performs the minimal
deconfiguration required to ensure that an ahci_platform host cannot
corrupt or otherwise interfere with a new kernel being started with kexec.

.. _`ahci_platform_suspend_host`:

ahci_platform_suspend_host
==========================

.. c:function:: int ahci_platform_suspend_host(struct device *dev)

    Suspend an ahci-platform host

    :param dev:
        device pointer for the host
    :type dev: struct device \*

.. _`ahci_platform_suspend_host.description`:

Description
-----------

This function does all the usual steps needed to suspend an
ahci-platform host, note any necessary resources (ie clks, phys, etc.)
must be disabled after calling this.

.. _`ahci_platform_suspend_host.return`:

Return
------

0 on success otherwise a negative error code

.. _`ahci_platform_resume_host`:

ahci_platform_resume_host
=========================

.. c:function:: int ahci_platform_resume_host(struct device *dev)

    Resume an ahci-platform host

    :param dev:
        device pointer for the host
    :type dev: struct device \*

.. _`ahci_platform_resume_host.description`:

Description
-----------

This function does all the usual steps needed to resume an ahci-platform
host, note any necessary resources (ie clks, phys, etc.)  must be
initialized / enabled before calling this.

.. _`ahci_platform_resume_host.return`:

Return
------

0 on success otherwise a negative error code

.. _`ahci_platform_suspend`:

ahci_platform_suspend
=====================

.. c:function:: int ahci_platform_suspend(struct device *dev)

    Suspend an ahci-platform device

    :param dev:
        the platform device to suspend
    :type dev: struct device \*

.. _`ahci_platform_suspend.description`:

Description
-----------

This function suspends the host associated with the device, followed by
disabling all the resources of the device.

.. _`ahci_platform_suspend.return`:

Return
------

0 on success otherwise a negative error code

.. _`ahci_platform_resume`:

ahci_platform_resume
====================

.. c:function:: int ahci_platform_resume(struct device *dev)

    Resume an ahci-platform device

    :param dev:
        the platform device to resume
    :type dev: struct device \*

.. _`ahci_platform_resume.description`:

Description
-----------

This function enables all the resources of the device followed by
resuming the host associated with the device.

.. _`ahci_platform_resume.return`:

Return
------

0 on success otherwise a negative error code

.. This file was automatic generated / don't edit.

