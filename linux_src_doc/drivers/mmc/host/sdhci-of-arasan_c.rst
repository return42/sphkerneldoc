.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/sdhci-of-arasan.c

.. _`sdhci_arasan_data`:

struct sdhci_arasan_data
========================

.. c:type:: struct sdhci_arasan_data


.. _`sdhci_arasan_data.definition`:

Definition
----------

.. code-block:: c

    struct sdhci_arasan_data {
        struct clk *clk_ahb;
        struct phy *phy;
    }

.. _`sdhci_arasan_data.members`:

Members
-------

clk_ahb
    Pointer to the AHB clock

phy
    Pointer to the generic phy

.. _`sdhci_arasan_suspend`:

sdhci_arasan_suspend
====================

.. c:function:: int sdhci_arasan_suspend(struct device *dev)

    Suspend method for the driver

    :param struct device \*dev:
        Address of the device structure
        Returns 0 on success and error value on error

.. _`sdhci_arasan_suspend.description`:

Description
-----------

Put the device in a low power state.

.. _`sdhci_arasan_resume`:

sdhci_arasan_resume
===================

.. c:function:: int sdhci_arasan_resume(struct device *dev)

    Resume method for the driver

    :param struct device \*dev:
        Address of the device structure
        Returns 0 on success and error value on error

.. _`sdhci_arasan_resume.description`:

Description
-----------

Resume operation after suspend

.. This file was automatic generated / don't edit.

