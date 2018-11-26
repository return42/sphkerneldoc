.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_blk.c

.. _`dpu_hw_blk_init`:

dpu_hw_blk_init
===============

.. c:function:: int dpu_hw_blk_init(struct dpu_hw_blk *hw_blk, u32 type, int id, struct dpu_hw_blk_ops *ops)

    initialize hw block object

    :param hw_blk:
        *undescribed*
    :type hw_blk: struct dpu_hw_blk \*

    :param type:
        hw block type - enum dpu_hw_blk_type
    :type type: u32

    :param id:
        instance id of the hw block
    :type id: int

    :param ops:
        Pointer to block operations
    :type ops: struct dpu_hw_blk_ops \*

.. _`dpu_hw_blk_init.return`:

Return
------

0 if success; error code otherwise

.. _`dpu_hw_blk_destroy`:

dpu_hw_blk_destroy
==================

.. c:function:: void dpu_hw_blk_destroy(struct dpu_hw_blk *hw_blk)

    destroy hw block object.

    :param hw_blk:
        pointer to hw block object
    :type hw_blk: struct dpu_hw_blk \*

.. _`dpu_hw_blk_destroy.return`:

Return
------

none

.. _`dpu_hw_blk_get`:

dpu_hw_blk_get
==============

.. c:function:: struct dpu_hw_blk *dpu_hw_blk_get(struct dpu_hw_blk *hw_blk, u32 type, int id)

    get hw_blk from free pool

    :param hw_blk:
        if specified, increment reference count only
    :type hw_blk: struct dpu_hw_blk \*

    :param type:
        if hw_blk is not specified, allocate the next available of this type
    :type type: u32

    :param id:
        if specified (>= 0), allocate the given instance of the above type
    :type id: int

.. _`dpu_hw_blk_get.return`:

Return
------

pointer to hw block object

.. _`dpu_hw_blk_put`:

dpu_hw_blk_put
==============

.. c:function:: void dpu_hw_blk_put(struct dpu_hw_blk *hw_blk)

    put hw_blk to free pool if decremented refcount is zero

    :param hw_blk:
        hw block to be freed
    :type hw_blk: struct dpu_hw_blk \*

.. This file was automatic generated / don't edit.

