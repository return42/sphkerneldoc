.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/spufs/fault.c

.. _`spufs_handle_event`:

spufs_handle_event
==================

.. c:function:: void spufs_handle_event(struct spu_context *ctx, unsigned long ea, int type)

    :param struct spu_context \*ctx:
        *undescribed*

    :param unsigned long ea:
        *undescribed*

    :param int type:
        *undescribed*

.. _`spufs_handle_event.description`:

Description
-----------

If the context was created with events, we just set the return event.
Otherwise, send an appropriate signal to the process.

.. This file was automatic generated / don't edit.

