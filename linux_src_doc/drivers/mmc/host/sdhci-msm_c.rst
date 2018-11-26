.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/sdhci-msm.c

.. _`__sdhci_msm_set_clock`:

\__sdhci_msm_set_clock
======================

.. c:function:: void __sdhci_msm_set_clock(struct sdhci_host *host, unsigned int clock)

    sdhci_msm clock control.

    :param host:
        *undescribed*
    :type host: struct sdhci_host \*

    :param clock:
        *undescribed*
    :type clock: unsigned int

.. _`__sdhci_msm_set_clock.description`:

Description
-----------

MSM controller does not use internal divider and
instead directly control the GCC clock as per
HW recommendation.

.. This file was automatic generated / don't edit.

