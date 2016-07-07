.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/sti/bdisp/bdisp-hw.c

.. _`bdisp_hw_reset`:

bdisp_hw_reset
==============

.. c:function:: int bdisp_hw_reset(struct bdisp_dev *bdisp)

    :param struct bdisp_dev \*bdisp:
        bdisp entity

.. _`bdisp_hw_reset.description`:

Description
-----------

Resets HW

.. _`bdisp_hw_reset.return`:

Return
------

0 on success.

.. _`bdisp_hw_get_and_clear_irq`:

bdisp_hw_get_and_clear_irq
==========================

.. c:function:: int bdisp_hw_get_and_clear_irq(struct bdisp_dev *bdisp)

    :param struct bdisp_dev \*bdisp:
        bdisp entity

.. _`bdisp_hw_get_and_clear_irq.description`:

Description
-----------

Read then reset interrupt status

.. _`bdisp_hw_get_and_clear_irq.return`:

Return
------

0 if expected interrupt was raised.

.. _`bdisp_hw_free_nodes`:

bdisp_hw_free_nodes
===================

.. c:function:: void bdisp_hw_free_nodes(struct bdisp_ctx *ctx)

    :param struct bdisp_ctx \*ctx:
        bdisp context

.. _`bdisp_hw_free_nodes.description`:

Description
-----------

Free node memory

.. _`bdisp_hw_free_nodes.return`:

Return
------

None

.. _`bdisp_hw_alloc_nodes`:

bdisp_hw_alloc_nodes
====================

.. c:function:: int bdisp_hw_alloc_nodes(struct bdisp_ctx *ctx)

    :param struct bdisp_ctx \*ctx:
        bdisp context

.. _`bdisp_hw_alloc_nodes.description`:

Description
-----------

Allocate dma memory for nodes

.. _`bdisp_hw_alloc_nodes.return`:

Return
------

0 on success

.. _`bdisp_hw_free_filters`:

bdisp_hw_free_filters
=====================

.. c:function:: void bdisp_hw_free_filters(struct device *dev)

    :param struct device \*dev:
        device

.. _`bdisp_hw_free_filters.description`:

Description
-----------

Free filters memory

.. _`bdisp_hw_free_filters.return`:

Return
------

None

.. _`bdisp_hw_alloc_filters`:

bdisp_hw_alloc_filters
======================

.. c:function:: int bdisp_hw_alloc_filters(struct device *dev)

    :param struct device \*dev:
        device

.. _`bdisp_hw_alloc_filters.description`:

Description
-----------

Allocate dma memory for filters

.. _`bdisp_hw_alloc_filters.return`:

Return
------

0 on success

.. _`bdisp_hw_get_hf_addr`:

bdisp_hw_get_hf_addr
====================

.. c:function:: dma_addr_t bdisp_hw_get_hf_addr(u16 inc)

    :param u16 inc:
        resize increment

.. _`bdisp_hw_get_hf_addr.description`:

Description
-----------

Find the horizontal filter table that fits the resize increment

.. _`bdisp_hw_get_hf_addr.return`:

Return
------

table physical address

.. _`bdisp_hw_get_vf_addr`:

bdisp_hw_get_vf_addr
====================

.. c:function:: dma_addr_t bdisp_hw_get_vf_addr(u16 inc)

    :param u16 inc:
        resize increment

.. _`bdisp_hw_get_vf_addr.description`:

Description
-----------

Find the vertical filter table that fits the resize increment

.. _`bdisp_hw_get_vf_addr.return`:

Return
------

table physical address

.. _`bdisp_hw_get_inc`:

bdisp_hw_get_inc
================

.. c:function:: int bdisp_hw_get_inc(u32 from, u32 to, u16 *inc)

    :param u32 from:
        input size

    :param u32 to:
        output size

    :param u16 \*inc:
        resize increment in 6.10 format

.. _`bdisp_hw_get_inc.description`:

Description
-----------

Computes the increment (inverse of scale) in 6.10 format

.. _`bdisp_hw_get_inc.return`:

Return
------

0 on success

.. _`bdisp_hw_get_hv_inc`:

bdisp_hw_get_hv_inc
===================

.. c:function:: int bdisp_hw_get_hv_inc(struct bdisp_ctx *ctx, u16 *h_inc, u16 *v_inc)

    :param struct bdisp_ctx \*ctx:
        device context

    :param u16 \*h_inc:
        horizontal increment

    :param u16 \*v_inc:
        vertical increment

.. _`bdisp_hw_get_hv_inc.description`:

Description
-----------

Computes the horizontal & vertical increments (inverse of scale)

.. _`bdisp_hw_get_hv_inc.return`:

Return
------

0 on success

.. _`bdisp_hw_get_op_cfg`:

bdisp_hw_get_op_cfg
===================

.. c:function:: int bdisp_hw_get_op_cfg(struct bdisp_ctx *ctx, struct bdisp_op_cfg *c)

    :param struct bdisp_ctx \*ctx:
        device context

    :param struct bdisp_op_cfg \*c:
        operation configuration

.. _`bdisp_hw_get_op_cfg.description`:

Description
-----------

Check which blitter operations are expected and sets the scaling increments

.. _`bdisp_hw_get_op_cfg.return`:

Return
------

0 on success

.. _`bdisp_hw_color_format`:

bdisp_hw_color_format
=====================

.. c:function:: u32 bdisp_hw_color_format(u32 pixelformat)

    :param u32 pixelformat:
        v4l2 pixel format

.. _`bdisp_hw_color_format.description`:

Description
-----------

v4l2 to bdisp pixel format convert

.. _`bdisp_hw_color_format.return`:

Return
------

bdisp pixel format

.. _`bdisp_hw_build_node`:

bdisp_hw_build_node
===================

.. c:function:: void bdisp_hw_build_node(struct bdisp_ctx *ctx, struct bdisp_op_cfg *cfg, struct bdisp_node *node, enum bdisp_target_plan t_plan, int src_x_offset)

    :param struct bdisp_ctx \*ctx:
        device context

    :param struct bdisp_op_cfg \*cfg:
        operation configuration

    :param struct bdisp_node \*node:
        node to be set

    :param enum bdisp_target_plan t_plan:
        whether the node refers to a RGB/Y or a CbCr plane

    :param int src_x_offset:
        x offset in the source image

.. _`bdisp_hw_build_node.description`:

Description
-----------

Build a node

.. _`bdisp_hw_build_node.return`:

Return
------

None

.. _`bdisp_hw_build_all_nodes`:

bdisp_hw_build_all_nodes
========================

.. c:function:: int bdisp_hw_build_all_nodes(struct bdisp_ctx *ctx)

    :param struct bdisp_ctx \*ctx:
        device context

.. _`bdisp_hw_build_all_nodes.description`:

Description
-----------

Build all the nodes for the blitter operation

.. _`bdisp_hw_build_all_nodes.return`:

Return
------

0 on success

.. _`bdisp_hw_save_request`:

bdisp_hw_save_request
=====================

.. c:function:: void bdisp_hw_save_request(struct bdisp_ctx *ctx)

    :param struct bdisp_ctx \*ctx:
        device context

.. _`bdisp_hw_save_request.description`:

Description
-----------

Save a copy of the request and of the built nodes

.. _`bdisp_hw_save_request.return`:

Return
------

None

.. _`bdisp_hw_update`:

bdisp_hw_update
===============

.. c:function:: int bdisp_hw_update(struct bdisp_ctx *ctx)

    :param struct bdisp_ctx \*ctx:
        device context

.. _`bdisp_hw_update.description`:

Description
-----------

Send the request to the HW

.. _`bdisp_hw_update.return`:

Return
------

0 on success

.. This file was automatic generated / don't edit.

