.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-mdp/mtk_mdp_vpu.h

.. _`mtk_mdp_vpu`:

struct mtk_mdp_vpu
==================

.. c:type:: struct mtk_mdp_vpu

    VPU instance for MDP

.. _`mtk_mdp_vpu.definition`:

Definition
----------

.. code-block:: c

    struct mtk_mdp_vpu {
        struct platform_device *pdev;
        uint32_t inst_addr;
        int32_t failure;
        struct mdp_process_vsi *vsi;
    }

.. _`mtk_mdp_vpu.members`:

Members
-------

pdev
    pointer to the VPU platform device

inst_addr
    VPU MDP instance address

failure
    VPU execution result status

vsi
    VPU shared information

.. This file was automatic generated / don't edit.

