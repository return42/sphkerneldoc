.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/msm_iommu.h

.. _`msm_iommu_dev`:

struct msm_iommu_dev
====================

.. c:type:: struct msm_iommu_dev

    a single IOMMU hardware instance name         Human-readable name given to this IOMMU HW instance ncb          Number of context banks present on this IOMMU HW instance

.. _`msm_iommu_dev.definition`:

Definition
----------

.. code-block:: c

    struct msm_iommu_dev {
        const char *name;
        int ncb;
    }

.. _`msm_iommu_dev.members`:

Members
-------

name
    *undescribed*

ncb
    *undescribed*

.. _`msm_iommu_ctx_dev`:

struct msm_iommu_ctx_dev
========================

.. c:type:: struct msm_iommu_ctx_dev

    an IOMMU context bank instance name         Human-readable name given to this context bank num          Index of this context bank within the hardware mids         List of Machine IDs that are to be mapped into this context bank, terminated by -1. The MID is a set of signals on the AXI bus that identifies the function associated with a specific memory request. (See ARM spec).

.. _`msm_iommu_ctx_dev.definition`:

Definition
----------

.. code-block:: c

    struct msm_iommu_ctx_dev {
        const char *name;
        int num;
        int mids[MAX_NUM_MIDS];
    }

.. _`msm_iommu_ctx_dev.members`:

Members
-------

name
    *undescribed*

num
    *undescribed*

.. _`msm_iommu_drvdata`:

struct msm_iommu_drvdata
========================

.. c:type:: struct msm_iommu_drvdata

    A single IOMMU hardware instance

.. _`msm_iommu_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct msm_iommu_drvdata {
        void __iomem *base;
        int irq;
        int ncb;
        struct clk *clk;
        struct clk *pclk;
    }

.. _`msm_iommu_drvdata.members`:

Members
-------

base
    IOMMU config port base address (VA)
    \ ``ncb``\          The number of contexts on this IOMMU

irq
    Interrupt number

ncb
    *undescribed*

clk
    The bus clock for this IOMMU hardware instance

pclk
    The clock for the IOMMU bus interconnect

.. _`msm_iommu_drvdata.description`:

Description
-----------

A msm_iommu_drvdata holds the global driver data about a single piece
of an IOMMU hardware instance.

.. _`msm_iommu_ctx_drvdata`:

struct msm_iommu_ctx_drvdata
============================

.. c:type:: struct msm_iommu_ctx_drvdata

    an IOMMU context bank instance

.. _`msm_iommu_ctx_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct msm_iommu_ctx_drvdata {
        int num;
        struct platform_device *pdev;
        struct list_head attached_elm;
    }

.. _`msm_iommu_ctx_drvdata.members`:

Members
-------

num
    Hardware context number of this context

pdev
    Platform device associated wit this HW instance

attached_elm
    List element for domains to track which devices are
    attached to them

.. _`msm_iommu_ctx_drvdata.description`:

Description
-----------

A msm_iommu_ctx_drvdata holds the driver data for a single context bank
within each IOMMU hardware instance

.. This file was automatic generated / don't edit.

