.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_pingpong.h

.. _`to_dpu_hw_pingpong`:

to_dpu_hw_pingpong
==================

.. c:function:: struct dpu_hw_pingpong *to_dpu_hw_pingpong(struct dpu_hw_blk *hw)

    convert base object dpu_hw_base to container

    :param hw:
        Pointer to base hardware block
    :type hw: struct dpu_hw_blk \*

.. _`to_dpu_hw_pingpong.return`:

Return
------

Pointer to hardware block container

.. _`dpu_hw_pingpong_init`:

dpu_hw_pingpong_init
====================

.. c:function:: struct dpu_hw_pingpong *dpu_hw_pingpong_init(enum dpu_pingpong idx, void __iomem *addr, struct dpu_mdss_cfg *m)

    initializes the pingpong driver for the passed pingpong idx.

    :param idx:
        Pingpong index for which driver object is required
    :type idx: enum dpu_pingpong

    :param addr:
        Mapped register io address of MDP
    :type addr: void __iomem \*

    :param m:
        Pointer to mdss catalog data
    :type m: struct dpu_mdss_cfg \*

.. _`dpu_hw_pingpong_init.return`:

Return
------

Error code or allocated dpu_hw_pingpong context

.. _`dpu_hw_pingpong_destroy`:

dpu_hw_pingpong_destroy
=======================

.. c:function:: void dpu_hw_pingpong_destroy(struct dpu_hw_pingpong *pp)

    destroys pingpong driver context should be called to free the context

    :param pp:
        Pointer to PP driver context returned by dpu_hw_pingpong_init
    :type pp: struct dpu_hw_pingpong \*

.. This file was automatic generated / don't edit.

