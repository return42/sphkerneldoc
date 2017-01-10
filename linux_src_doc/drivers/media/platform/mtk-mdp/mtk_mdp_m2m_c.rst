.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-mdp/mtk_mdp_m2m.c

.. _`mtk_mdp_pix_limit`:

struct mtk_mdp_pix_limit
========================

.. c:type:: struct mtk_mdp_pix_limit

    image pixel size limits

.. _`mtk_mdp_pix_limit.definition`:

Definition
----------

.. code-block:: c

    struct mtk_mdp_pix_limit {
        u16 org_w;
        u16 org_h;
        u16 target_rot_dis_w;
        u16 target_rot_dis_h;
        u16 target_rot_en_w;
        u16 target_rot_en_h;
    }

.. _`mtk_mdp_pix_limit.members`:

Members
-------

org_w
    source pixel width

org_h
    source pixel height

target_rot_dis_w
    pixel dst scaled width with the rotator is off

target_rot_dis_h
    pixel dst scaled height with the rotator is off

target_rot_en_w
    pixel dst scaled width with the rotator is on

target_rot_en_h
    pixel dst scaled height with the rotator is on

.. This file was automatic generated / don't edit.

