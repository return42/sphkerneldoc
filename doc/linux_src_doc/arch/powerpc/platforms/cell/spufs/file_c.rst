.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/spufs/file.c

.. _`spu_switch_log_notify`:

spu_switch_log_notify
=====================

.. c:function:: void spu_switch_log_notify(struct spu *spu, struct spu_context *ctx, u32 type, u32 val)

    :param struct spu \*spu:
        *undescribed*

    :param struct spu_context \*ctx:
        *undescribed*

    :param u32 type:
        *undescribed*

    :param u32 val:
        *undescribed*

.. _`spu_switch_log_notify.description`:

Description
-----------

Must be called with ctx->state_mutex held.

.. This file was automatic generated / don't edit.

