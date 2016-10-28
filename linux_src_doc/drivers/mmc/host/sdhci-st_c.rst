.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/sdhci-st.c

.. _`st_mmcss_cconfig`:

st_mmcss_cconfig
================

.. c:function:: void st_mmcss_cconfig(struct device_node *np, struct sdhci_host *host)

    configure the Arasan HC inside the flashSS.

    :param struct device_node \*np:
        dt device node.

    :param struct sdhci_host \*host:
        sdhci host

.. _`st_mmcss_cconfig.description`:

Description
-----------

this function is to configure the Arasan host controller.
On some ST SoCs, i.e. STiH407 family, the MMC devices inside a dedicated
flashSS sub-system which needs to be configured to be compliant to eMMC 4.5
or eMMC4.3.  This has to be done before registering the sdhci host.

.. This file was automatic generated / don't edit.

