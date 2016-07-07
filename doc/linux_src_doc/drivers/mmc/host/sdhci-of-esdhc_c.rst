.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/sdhci-of-esdhc.c

.. _`esdhc_readl_fixup`:

esdhc_readl_fixup
=================

.. c:function:: u32 esdhc_readl_fixup(struct sdhci_host *host, int spec_reg, u32 value)

    Fixup the value read from incompatible eSDHC register to make it compatible with SD spec.

    :param struct sdhci_host \*host:
        pointer to sdhci_host

    :param int spec_reg:
        SD spec register address

    :param u32 value:
        32bit eSDHC register value on spec_reg address

.. _`esdhc_readl_fixup.description`:

Description
-----------

In SD spec, there are 8/16/32/64 bits registers, while all of eSDHC
registers are 32 bits. There are differences in register size, register
address, register function, bit position and function between eSDHC spec
and SD spec.

Return a fixed up register value

.. _`esdhc_writel_fixup`:

esdhc_writel_fixup
==================

.. c:function:: u32 esdhc_writel_fixup(struct sdhci_host *host, int spec_reg, u32 value, u32 old_value)

    Fixup the SD spec register value so that it could be written into eSDHC register.

    :param struct sdhci_host \*host:
        pointer to sdhci_host

    :param int spec_reg:
        SD spec register address

    :param u32 value:
        8/16/32bit SD spec register value that would be written

    :param u32 old_value:
        32bit eSDHC register value on spec_reg address

.. _`esdhc_writel_fixup.description`:

Description
-----------

In SD spec, there are 8/16/32/64 bits registers, while all of eSDHC
registers are 32 bits. There are differences in register size, register
address, register function, bit position and function between eSDHC spec
and SD spec.

Return a fixed up register value

.. This file was automatic generated / don't edit.

