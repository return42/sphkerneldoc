.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/msm_iommu.h

.. _`msm_iommu_dev`:

struct msm_iommu_dev
====================

.. c:type:: struct msm_iommu_dev

    a single IOMMU hardware instance ncb          Number of context banks present on this IOMMU HW instance

.. _`msm_iommu_dev.definition`:

Definition
----------

.. code-block:: c

    struct msm_iommu_dev {
        void __iomem *base;
        int ncb;
        struct device *dev;
        int irq;
        struct clk *clk;
        struct clk *pclk;
        struct list_head dev_node;
        struct list_head dom_node;
        struct list_head ctx_list;
        DECLARE_BITMAP(context_map, IOMMU_MAX_CBS);
        struct iommu_device iommu;
    }

.. _`msm_iommu_dev.members`:

Members
-------

base
    *undescribed*

ncb
    *undescribed*

dev
    *undescribed*

irq
    *undescribed*

clk
    *undescribed*

pclk
    *undescribed*

dev_node
    *undescribed*

dom_node
    *undescribed*

ctx_list
    *undescribed*

context_map
    *undescribed*

iommu
    *undescribed*

.. _`msm_iommu_dev.dev`:

dev
---

IOMMU device

.. _`msm_iommu_dev.irq`:

irq
---

Interrupt number

.. _`msm_iommu_dev.clk`:

clk
---

The bus clock for this IOMMU hardware instance

.. _`msm_iommu_dev.pclk`:

pclk
----

The clock for the IOMMU bus interconnect

.. _`msm_iommu_dev.dev_node`:

dev_node
--------

list head in qcom_iommu_device_list

.. _`msm_iommu_dev.dom_node`:

dom_node
--------

list head for domain

.. _`msm_iommu_dev.ctx_list`:

ctx_list
--------

list of 'struct msm_iommu_ctx_dev'

.. _`msm_iommu_dev.context_map`:

context_map
-----------

Bitmap to track allocated context banks

.. _`msm_iommu_ctx_dev`:

struct msm_iommu_ctx_dev
========================

.. c:type:: struct msm_iommu_ctx_dev

    an IOMMU context bank instance of_node      node ptr of client device num          Index of this context bank within the hardware mids         List of Machine IDs that are to be mapped into this context bank, terminated by -1. The MID is a set of signals on the AXI bus that identifies the function associated with a specific memory request. (See ARM spec). num_mids     Total number of mids node         list head in ctx_list

.. _`msm_iommu_ctx_dev.definition`:

Definition
----------

.. code-block:: c

    struct msm_iommu_ctx_dev {
        struct device_node *of_node;
        int num;
        int mids[MAX_NUM_MIDS];
        int num_mids;
        struct list_head list;
    }

.. _`msm_iommu_ctx_dev.members`:

Members
-------

of_node
    *undescribed*

num
    *undescribed*

mids
    *undescribed*

num_mids
    *undescribed*

list
    *undescribed*

.. This file was automatic generated / don't edit.

