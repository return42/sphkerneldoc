.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_blk.h

.. _`dpu_hw_blk_ops`:

struct dpu_hw_blk_ops
=====================

.. c:type:: struct dpu_hw_blk_ops

    common hardware block operations

.. _`dpu_hw_blk_ops.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_blk_ops {
        int (*start)(struct dpu_hw_blk *);
        void (*stop)(struct dpu_hw_blk *);
    }

.. _`dpu_hw_blk_ops.members`:

Members
-------

start
    start operation on first get

stop
    stop operation on last put

.. _`dpu_hw_blk`:

struct dpu_hw_blk
=================

.. c:type:: struct dpu_hw_blk

    definition of hardware block object

.. _`dpu_hw_blk.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_blk {
        struct list_head list;
        u32 type;
        int id;
        atomic_t refcount;
        struct dpu_hw_blk_ops ops;
    }

.. _`dpu_hw_blk.members`:

Members
-------

list
    list of hardware blocks

type
    hardware block type

id
    instance id

refcount
    reference/usage count

ops
    *undescribed*

.. This file was automatic generated / don't edit.

