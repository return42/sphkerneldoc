.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_lm.h

.. _`to_dpu_hw_mixer`:

to_dpu_hw_mixer
===============

.. c:function:: struct dpu_hw_mixer *to_dpu_hw_mixer(struct dpu_hw_blk *hw)

    convert base object dpu_hw_base to container

    :param hw:
        Pointer to base hardware block
    :type hw: struct dpu_hw_blk \*

.. _`to_dpu_hw_mixer.return`:

Return
------

Pointer to hardware block container

.. _`dpu_hw_lm_init`:

dpu_hw_lm_init
==============

.. c:function:: struct dpu_hw_mixer *dpu_hw_lm_init(enum dpu_lm idx, void __iomem *addr, struct dpu_mdss_cfg *m)

    Initializes the mixer hw driver object. should be called once before accessing every mixer.

    :param idx:
        mixer index for which driver object is required
    :type idx: enum dpu_lm

    :param addr:
        mapped register io address of MDP
    :type addr: void __iomem \*

    :param m:
        pointer to mdss catalog data
    :type m: struct dpu_mdss_cfg \*

.. _`dpu_hw_lm_destroy`:

dpu_hw_lm_destroy
=================

.. c:function:: void dpu_hw_lm_destroy(struct dpu_hw_mixer *lm)

    Destroys layer mixer driver context

    :param lm:
        Pointer to LM driver context
    :type lm: struct dpu_hw_mixer \*

.. This file was automatic generated / don't edit.

