.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-mdp/mtk_mdp_comp.h

.. _`mtk_mdp_comp_type`:

enum mtk_mdp_comp_type
======================

.. c:type:: enum mtk_mdp_comp_type

    the MDP component

.. _`mtk_mdp_comp_type.definition`:

Definition
----------

.. code-block:: c

    enum mtk_mdp_comp_type {
        MTK_MDP_RDMA,
        MTK_MDP_RSZ,
        MTK_MDP_WDMA,
        MTK_MDP_WROT,
        MTK_MDP_COMP_TYPE_MAX
    };

.. _`mtk_mdp_comp_type.constants`:

Constants
---------

MTK_MDP_RDMA
    Read DMA

MTK_MDP_RSZ
    Riszer

MTK_MDP_WDMA
    Write DMA

MTK_MDP_WROT
    Write DMA with rotation

MTK_MDP_COMP_TYPE_MAX
    *undescribed*

.. _`mtk_mdp_comp`:

struct mtk_mdp_comp
===================

.. c:type:: struct mtk_mdp_comp

    the MDP's function component data

.. _`mtk_mdp_comp.definition`:

Definition
----------

.. code-block:: c

    struct mtk_mdp_comp {
        struct device_node *dev_node;
        struct clk *clk[2];
        void __iomem *regs;
        struct device *larb_dev;
        enum mtk_mdp_comp_type type;
        enum mtk_mdp_comp_id id;
    }

.. _`mtk_mdp_comp.members`:

Members
-------

dev_node
    component device node

clk
    clocks required for component

regs
    Mapped address of component registers.

larb_dev
    SMI device required for component

type
    component type

id
    component ID

.. This file was automatic generated / don't edit.

