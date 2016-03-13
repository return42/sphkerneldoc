.. -*- coding: utf-8; mode: rst -*-

==========
bdisp-hw.c
==========



.. _xref_bdisp_hw_reset:

bdisp_hw_reset
==============

.. c:function:: int bdisp_hw_reset (struct bdisp_dev * bdisp)

    

    :param struct bdisp_dev * bdisp:
        bdisp entity



Description
-----------

Resets HW



RETURNS
-------

0 on success.




.. _xref_bdisp_hw_get_and_clear_irq:

bdisp_hw_get_and_clear_irq
==========================

.. c:function:: int bdisp_hw_get_and_clear_irq (struct bdisp_dev * bdisp)

    

    :param struct bdisp_dev * bdisp:
        bdisp entity



Description
-----------

Read then reset interrupt status



RETURNS
-------

0 if expected interrupt was raised.




.. _xref_bdisp_hw_free_nodes:

bdisp_hw_free_nodes
===================

.. c:function:: void bdisp_hw_free_nodes (struct bdisp_ctx * ctx)

    

    :param struct bdisp_ctx * ctx:
        bdisp context



Description
-----------

Free node memory



RETURNS
-------

None




.. _xref_bdisp_hw_alloc_nodes:

bdisp_hw_alloc_nodes
====================

.. c:function:: int bdisp_hw_alloc_nodes (struct bdisp_ctx * ctx)

    

    :param struct bdisp_ctx * ctx:
        bdisp context



Description
-----------

Allocate dma memory for nodes



RETURNS
-------

0 on success




.. _xref_bdisp_hw_free_filters:

bdisp_hw_free_filters
=====================

.. c:function:: void bdisp_hw_free_filters (struct device * dev)

    

    :param struct device * dev:
        device



Description
-----------

Free filters memory



RETURNS
-------

None




.. _xref_bdisp_hw_alloc_filters:

bdisp_hw_alloc_filters
======================

.. c:function:: int bdisp_hw_alloc_filters (struct device * dev)

    

    :param struct device * dev:
        device



Description
-----------

Allocate dma memory for filters



RETURNS
-------

0 on success




.. _xref_bdisp_hw_get_hf_addr:

bdisp_hw_get_hf_addr
====================

.. c:function:: dma_addr_t bdisp_hw_get_hf_addr (u16 inc)

    

    :param u16 inc:
        resize increment



Description
-----------

Find the horizontal filter table that fits the resize increment



RETURNS
-------

table physical address




.. _xref_bdisp_hw_get_vf_addr:

bdisp_hw_get_vf_addr
====================

.. c:function:: dma_addr_t bdisp_hw_get_vf_addr (u16 inc)

    

    :param u16 inc:
        resize increment



Description
-----------

Find the vertical filter table that fits the resize increment



RETURNS
-------

table physical address




.. _xref_bdisp_hw_get_inc:

bdisp_hw_get_inc
================

.. c:function:: int bdisp_hw_get_inc (u32 from, u32 to, u16 * inc)

    

    :param u32 from:
        input size

    :param u32 to:
        output size

    :param u16 * inc:
        resize increment in 6.10 format



Description
-----------

Computes the increment (inverse of scale) in 6.10 format



RETURNS
-------

0 on success




.. _xref_bdisp_hw_get_hv_inc:

bdisp_hw_get_hv_inc
===================

.. c:function:: int bdisp_hw_get_hv_inc (struct bdisp_ctx * ctx, u16 * h_inc, u16 * v_inc)

    

    :param struct bdisp_ctx * ctx:
        device context

    :param u16 * h_inc:
        horizontal increment

    :param u16 * v_inc:
        vertical increment



Description
-----------

Computes the horizontal & vertical increments (inverse of scale)



RETURNS
-------

0 on success




.. _xref_bdisp_hw_get_op_cfg:

bdisp_hw_get_op_cfg
===================

.. c:function:: int bdisp_hw_get_op_cfg (struct bdisp_ctx * ctx, struct bdisp_op_cfg * c)

    

    :param struct bdisp_ctx * ctx:
        device context

    :param struct bdisp_op_cfg * c:
        operation configuration



Description
-----------

Check which blitter operations are expected and sets the scaling increments



RETURNS
-------

0 on success




.. _xref_bdisp_hw_color_format:

bdisp_hw_color_format
=====================

.. c:function:: u32 bdisp_hw_color_format (u32 pixelformat)

    

    :param u32 pixelformat:
        v4l2 pixel format



Description
-----------

v4l2 to bdisp pixel format convert



RETURNS
-------

bdisp pixel format




.. _xref_bdisp_hw_build_node:

bdisp_hw_build_node
===================

.. c:function:: void bdisp_hw_build_node (struct bdisp_ctx * ctx, struct bdisp_op_cfg * cfg, struct bdisp_node * node, enum bdisp_target_plan t_plan, int src_x_offset)

    

    :param struct bdisp_ctx * ctx:
        device context

    :param struct bdisp_op_cfg * cfg:
        operation configuration

    :param struct bdisp_node * node:
        node to be set

    :param enum bdisp_target_plan t_plan:
        whether the node refers to a RGB/Y or a CbCr plane

    :param int src_x_offset:
        x offset in the source image



Description
-----------

Build a node



RETURNS
-------

None




.. _xref_bdisp_hw_build_all_nodes:

bdisp_hw_build_all_nodes
========================

.. c:function:: int bdisp_hw_build_all_nodes (struct bdisp_ctx * ctx)

    

    :param struct bdisp_ctx * ctx:
        device context



Description
-----------

Build all the nodes for the blitter operation



RETURNS
-------

0 on success




.. _xref_bdisp_hw_save_request:

bdisp_hw_save_request
=====================

.. c:function:: void bdisp_hw_save_request (struct bdisp_ctx * ctx)

    

    :param struct bdisp_ctx * ctx:
        device context



Description
-----------

Save a copy of the request and of the built nodes



RETURNS
-------

None




.. _xref_bdisp_hw_update:

bdisp_hw_update
===============

.. c:function:: int bdisp_hw_update (struct bdisp_ctx * ctx)

    

    :param struct bdisp_ctx * ctx:
        device context



Description
-----------

Send the request to the HW



RETURNS
-------

0 on success


