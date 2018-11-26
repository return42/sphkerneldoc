.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/sdhci-of-esdhc.c

.. _`esdhc_readl_fixup`:

esdhc_readl_fixup
=================

.. c:function:: u32 esdhc_readl_fixup(struct sdhci_host *host, int spec_reg, u32 value)

    Fixup the value read from incompatible eSDHC register to make it compatible with SD spec.

    :param host:
        pointer to sdhci_host
    :type host: struct sdhci_host \*

    :param spec_reg:
        SD spec register address
    :type spec_reg: int

    :param value:
        32bit eSDHC register value on spec_reg address
    :type value: u32

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

    :param host:
        pointer to sdhci_host
    :type host: struct sdhci_host \*

    :param spec_reg:
        SD spec register address
    :type spec_reg: int

    :param value:
        8/16/32bit SD spec register value that would be written
    :type value: u32

    :param old_value:
        32bit eSDHC register value on spec_reg address
    :type old_value: u32

.. _`esdhc_writel_fixup.description`:

Description
-----------

In SD spec, there are 8/16/32/64 bits registers, while all of eSDHC
registers are 32 bits. There are differences in register size, register
address, register function, bit position and function between eSDHC spec
and SD spec.

Return a fixed up register value

.. This file was automatic generated / don't edit.

