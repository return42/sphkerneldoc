.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/spufs/file.c

.. _`spu_switch_log_notify`:

spu_switch_log_notify
=====================

.. c:function:: void spu_switch_log_notify(struct spu *spu, struct spu_context *ctx, u32 type, u32 val)

    :param spu:
        *undescribed*
    :type spu: struct spu \*

    :param ctx:
        *undescribed*
    :type ctx: struct spu_context \*

    :param type:
        *undescribed*
    :type type: u32

    :param val:
        *undescribed*
    :type val: u32

.. _`spu_switch_log_notify.description`:

Description
-----------

Must be called with ctx->state_mutex held.

.. This file was automatic generated / don't edit.

