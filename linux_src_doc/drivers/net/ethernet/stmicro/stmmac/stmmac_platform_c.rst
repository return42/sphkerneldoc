.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/stmicro/stmmac/stmmac_platform.c

.. _`dwmac1000_validate_mcast_bins`:

dwmac1000_validate_mcast_bins
=============================

.. c:function:: int dwmac1000_validate_mcast_bins(int mcast_bins)

    validates the number of Multicast filter bins

    :param mcast_bins:
        Multicast filtering bins
    :type mcast_bins: int

.. _`dwmac1000_validate_mcast_bins.description`:

Description
-----------

this function validates the number of Multicast filtering bins specified
by the configuration through the device tree. The Synopsys GMAC supports
64 bins, 128 bins, or 256 bins. "bins" refer to the division of CRC
number space. 64 bins correspond to 6 bits of the CRC, 128 corresponds
to 7 bits, and 256 refers to 8 bits of the CRC. Any other setting is
invalid and will cause the filtering algorithm to use Multicast
promiscuous mode.

.. _`dwmac1000_validate_ucast_entries`:

dwmac1000_validate_ucast_entries
================================

.. c:function:: int dwmac1000_validate_ucast_entries(int ucast_entries)

    validate the Unicast address entries

    :param ucast_entries:
        number of Unicast address entries
    :type ucast_entries: int

.. _`dwmac1000_validate_ucast_entries.description`:

Description
-----------

This function validates the number of Unicast address entries supported
by a particular Synopsys 10/100/1000 controller. The Synopsys controller
supports 1..32, 64, or 128 Unicast filter entries for it's Unicast filter
logic. This function validates a valid, supported configuration is
selected, and defaults to 1 Unicast address if an unsupported
configuration is selected.

.. _`stmmac_axi_setup`:

stmmac_axi_setup
================

.. c:function:: struct stmmac_axi *stmmac_axi_setup(struct platform_device *pdev)

    parse DT parameters for programming the AXI register

    :param pdev:
        platform device
    :type pdev: struct platform_device \*

.. _`stmmac_axi_setup.description`:

Description
-----------

if required, from device-tree the AXI internal register can be tuned
by using platform parameters.

.. _`stmmac_mtl_setup`:

stmmac_mtl_setup
================

.. c:function:: int stmmac_mtl_setup(struct platform_device *pdev, struct plat_stmmacenet_data *plat)

    parse DT parameters for multiple queues configuration

    :param pdev:
        platform device
    :type pdev: struct platform_device \*

    :param plat:
        *undescribed*
    :type plat: struct plat_stmmacenet_data \*

.. _`stmmac_dt_phy`:

stmmac_dt_phy
=============

.. c:function:: int stmmac_dt_phy(struct plat_stmmacenet_data *plat, struct device_node *np, struct device *dev)

    parse device-tree driver parameters to allocate PHY resources

    :param plat:
        driver data platform structure
    :type plat: struct plat_stmmacenet_data \*

    :param np:
        device tree node
    :type np: struct device_node \*

    :param dev:
        device pointer
    :type dev: struct device \*

.. _`stmmac_dt_phy.description`:

Description
-----------

The mdio bus will be allocated in case of a phy transceiver is on board;
it will be NULL if the fixed-link is configured.
If there is the "snps,dwmac-mdio" sub-node the mdio will be allocated
in any case (for DSA, mdio must be registered even if fixed-link).

.. _`stmmac_dt_phy.the-table-below-sums-the-supported-configurations`:

The table below sums the supported configurations
-------------------------------------------------

-------------------------------
snps,phy-addr   \|     Y
-------------------------------
phy-handle      \|     Y
-------------------------------
fixed-link      \|     N
-------------------------------
snps,dwmac-mdio \|
even if       \|     Y
fixed-link      \|
-------------------------------

It returns 0 in case of success otherwise -ENODEV.

.. _`stmmac_probe_config_dt`:

stmmac_probe_config_dt
======================

.. c:function:: struct plat_stmmacenet_data *stmmac_probe_config_dt(struct platform_device *pdev, const char **mac)

    parse device-tree driver parameters

    :param pdev:
        platform_device structure
    :type pdev: struct platform_device \*

    :param mac:
        MAC address to use
    :type mac: const char \*\*

.. _`stmmac_probe_config_dt.description`:

Description
-----------

this function is to read the driver parameters from device-tree and
set some private fields that will be used by the main at runtime.

.. _`stmmac_remove_config_dt`:

stmmac_remove_config_dt
=======================

.. c:function:: void stmmac_remove_config_dt(struct platform_device *pdev, struct plat_stmmacenet_data *plat)

    undo the effects of \ :c:func:`stmmac_probe_config_dt`\ 

    :param pdev:
        platform_device structure
    :type pdev: struct platform_device \*

    :param plat:
        driver data platform structure
    :type plat: struct plat_stmmacenet_data \*

.. _`stmmac_remove_config_dt.description`:

Description
-----------

Release resources claimed by \ :c:func:`stmmac_probe_config_dt`\ .

.. _`stmmac_pltfr_remove`:

stmmac_pltfr_remove
===================

.. c:function:: int stmmac_pltfr_remove(struct platform_device *pdev)

    :param pdev:
        platform device pointer
    :type pdev: struct platform_device \*

.. _`stmmac_pltfr_remove.description`:

Description
-----------

this function calls the main to free the net resources
and calls the platforms hook and release the resources (e.g. mem).

.. _`stmmac_pltfr_suspend`:

stmmac_pltfr_suspend
====================

.. c:function:: int stmmac_pltfr_suspend(struct device *dev)

    :param dev:
        device pointer
    :type dev: struct device \*

.. _`stmmac_pltfr_suspend.description`:

Description
-----------

this function is invoked when suspend the driver and it direcly
call the main suspend function and then, if required, on some platform, it
can call an exit helper.

.. _`stmmac_pltfr_resume`:

stmmac_pltfr_resume
===================

.. c:function:: int stmmac_pltfr_resume(struct device *dev)

    :param dev:
        device pointer
    :type dev: struct device \*

.. _`stmmac_pltfr_resume.description`:

Description
-----------

this function is invoked when resume the driver before calling
the main resume function, on some platforms, it can call own init helper
if required.

.. This file was automatic generated / don't edit.

