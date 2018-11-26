.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/spufs/context.c

.. _`spu_acquire_saved`:

spu_acquire_saved
=================

.. c:function:: int spu_acquire_saved(struct spu_context *ctx)

    lock spu contex and make sure it is in saved state

    :param ctx:
        spu contex to lock
    :type ctx: struct spu_context \*

.. _`spu_release_saved`:

spu_release_saved
=================

.. c:function:: void spu_release_saved(struct spu_context *ctx)

    unlock spu context and return it to the runqueue

    :param ctx:
        context to unlock
    :type ctx: struct spu_context \*

.. This file was automatic generated / don't edit.

