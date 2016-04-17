.. -*- coding: utf-8; mode: rst -*-

==================
libahci_platform.c
==================


.. _`ahci_platform_enable_phys`:

ahci_platform_enable_phys
=========================

.. c:function:: int ahci_platform_enable_phys (struct ahci_host_priv *hpriv)

    Enable PHYs

    :param struct ahci_host_priv \*hpriv:
        host private area to store config values



.. _`ahci_platform_enable_phys.description`:

Description
-----------

This function enables all the PHYs found in hpriv->phys, if any.
If a PHY fails to be enabled, it disables all the PHYs already
enabled in reverse order and returns an error.



.. _`ahci_platform_enable_phys.returns`:

RETURNS
-------

0 on success otherwise a negative error code



.. _`ahci_platform_disable_phys`:

ahci_platform_disable_phys
==========================

.. c:function:: void ahci_platform_disable_phys (struct ahci_host_priv *hpriv)

    Disable PHYs

    :param struct ahci_host_priv \*hpriv:
        host private area to store config values



.. _`ahci_platform_disable_phys.description`:

Description
-----------

This function disables all PHYs found in hpriv->phys.



.. _`ahci_platform_enable_clks`:

ahci_platform_enable_clks
=========================

.. c:function:: int ahci_platform_enable_clks (struct ahci_host_priv *hpriv)

    Enable platform clocks

    :param struct ahci_host_priv \*hpriv:
        host private area to store config values



.. _`ahci_platform_enable_clks.description`:

Description
-----------

This function enables all the clks found in hpriv->clks, starting at
index 0. If any clk fails to enable it disables all the clks already
enabled in reverse order, and then returns an error.



.. _`ahci_platform_enable_clks.returns`:

RETURNS
-------

0 on success otherwise a negative error code



.. _`ahci_platform_disable_clks`:

ahci_platform_disable_clks
==========================

.. c:function:: void ahci_platform_disable_clks (struct ahci_host_priv *hpriv)

    Disable platform clocks

    :param struct ahci_host_priv \*hpriv:
        host private area to store config values



.. _`ahci_platform_disable_clks.description`:

Description
-----------

This function disables all the clks found in hpriv->clks, in reverse
order of ahci_platform_enable_clks (starting at the end of the array).



.. _`ahci_platform_enable_regulators`:

ahci_platform_enable_regulators
===============================

.. c:function:: int ahci_platform_enable_regulators (struct ahci_host_priv *hpriv)

    Enable regulators

    :param struct ahci_host_priv \*hpriv:
        host private area to store config values



.. _`ahci_platform_enable_regulators.description`:

Description
-----------

This function enables all the regulators found in
hpriv->target_pwrs, if any.  If a regulator fails to be enabled, it
disables all the regulators already enabled in reverse order and
returns an error.



.. _`ahci_platform_enable_regulators.returns`:

RETURNS
-------

0 on success otherwise a negative error code



.. _`ahci_platform_disable_regulators`:

ahci_platform_disable_regulators
================================

.. c:function:: void ahci_platform_disable_regulators (struct ahci_host_priv *hpriv)

    Disable regulators

    :param struct ahci_host_priv \*hpriv:
        host private area to store config values



.. _`ahci_platform_disable_regulators.description`:

Description
-----------

This function disables all regulators found in hpriv->target_pwrs.



.. _`ahci_platform_enable_resources`:

ahci_platform_enable_resources
==============================

.. c:function:: int ahci_platform_enable_resources (struct ahci_host_priv *hpriv)

    Enable platform resources

    :param struct ahci_host_priv \*hpriv:
        host private area to store config values



.. _`ahci_platform_enable_resources.description`:

Description
-----------

This function enables all ahci_platform managed resources in the



.. _`ahci_platform_enable_resources.following-order`:

following order
---------------

1) Regulator
2) Clocks (through ahci_platform_enable_clks)
3) Phys

If resource enabling fails at any point the previous enabled resources
are disabled in reverse order.



.. _`ahci_platform_enable_resources.returns`:

RETURNS
-------

0 on success otherwise a negative error code



.. _`ahci_platform_disable_resources`:

ahci_platform_disable_resources
===============================

.. c:function:: void ahci_platform_disable_resources (struct ahci_host_priv *hpriv)

    Disable platform resources

    :param struct ahci_host_priv \*hpriv:
        host private area to store config values



.. _`ahci_platform_disable_resources.description`:

Description
-----------

This function disables all ahci_platform managed resources in the



.. _`ahci_platform_disable_resources.following-order`:

following order
---------------

1) Phys
2) Clocks (through ahci_platform_disable_clks)
3) Regulator



.. _`ahci_platform_get_resources`:

ahci_platform_get_resources
===========================

.. c:function:: struct ahci_host_priv *ahci_platform_get_resources (struct platform_device *pdev)

    Get platform resources

    :param struct platform_device \*pdev:
        platform device to get resources for



.. _`ahci_platform_get_resources.description`:

Description
-----------

This function allocates an ahci_host_priv struct, and gets the following
resources, storing a reference to them inside the returned struct:

1) mmio registers (IORESOURCE_MEM 0, mandatory)
2) regulator for controlling the targets power (optional)
3) 0 - AHCI_MAX_CLKS clocks, as specified in the devs devicetree node,

   or for non devicetree enabled platforms a single clock
        4) phys (optional)



.. _`ahci_platform_get_resources.returns`:

RETURNS
-------

The allocated ahci_host_priv on success, otherwise an ERR_PTR value



.. _`ahci_platform_init_host`:

ahci_platform_init_host
=======================

.. c:function:: int ahci_platform_init_host (struct platform_device *pdev, struct ahci_host_priv *hpriv, const struct ata_port_info *pi_template, struct scsi_host_template *sht)

    Bring up an ahci-platform host

    :param struct platform_device \*pdev:
        platform device pointer for the host

    :param struct ahci_host_priv \*hpriv:
        ahci-host private data for the host

    :param const struct ata_port_info \*pi_template:
        template for the ata_port_info to use

    :param struct scsi_host_template \*sht:
        scsi_host_template to use when registering



.. _`ahci_platform_init_host.description`:

Description
-----------

This function does all the usual steps needed to bring up an
ahci-platform host, note any necessary resources (ie clks, phys, etc.)
must be initialized / enabled before calling this.



.. _`ahci_platform_init_host.returns`:

RETURNS
-------

0 on success otherwise a negative error code



.. _`ahci_platform_suspend_host`:

ahci_platform_suspend_host
==========================

.. c:function:: int ahci_platform_suspend_host (struct device *dev)

    Suspend an ahci-platform host

    :param struct device \*dev:
        device pointer for the host



.. _`ahci_platform_suspend_host.description`:

Description
-----------

This function does all the usual steps needed to suspend an
ahci-platform host, note any necessary resources (ie clks, phys, etc.)
must be disabled after calling this.



.. _`ahci_platform_suspend_host.returns`:

RETURNS
-------

0 on success otherwise a negative error code



.. _`ahci_platform_resume_host`:

ahci_platform_resume_host
=========================

.. c:function:: int ahci_platform_resume_host (struct device *dev)

    Resume an ahci-platform host

    :param struct device \*dev:
        device pointer for the host



.. _`ahci_platform_resume_host.description`:

Description
-----------

This function does all the usual steps needed to resume an ahci-platform
host, note any necessary resources (ie clks, phys, etc.)  must be
initialized / enabled before calling this.



.. _`ahci_platform_resume_host.returns`:

RETURNS
-------

0 on success otherwise a negative error code



.. _`ahci_platform_suspend`:

ahci_platform_suspend
=====================

.. c:function:: int ahci_platform_suspend (struct device *dev)

    Suspend an ahci-platform device

    :param struct device \*dev:
        the platform device to suspend



.. _`ahci_platform_suspend.description`:

Description
-----------

This function suspends the host associated with the device, followed by
disabling all the resources of the device.



.. _`ahci_platform_suspend.returns`:

RETURNS
-------

0 on success otherwise a negative error code



.. _`ahci_platform_resume`:

ahci_platform_resume
====================

.. c:function:: int ahci_platform_resume (struct device *dev)

    Resume an ahci-platform device

    :param struct device \*dev:
        the platform device to resume



.. _`ahci_platform_resume.description`:

Description
-----------

This function enables all the resources of the device followed by
resuming the host associated with the device.



.. _`ahci_platform_resume.returns`:

RETURNS
-------

0 on success otherwise a negative error code

