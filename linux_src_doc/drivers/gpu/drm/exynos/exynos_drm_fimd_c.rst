.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/exynos/exynos_drm_fimd.c

.. _`fimd_shadow_protect_win`:

fimd_shadow_protect_win
=======================

.. c:function:: void fimd_shadow_protect_win(struct fimd_context *ctx, unsigned int win, bool protect)

    disable updating values from shadow registers at vsync

    :param ctx:
        *undescribed*
    :type ctx: struct fimd_context \*

    :param win:
        window to protect registers for
    :type win: unsigned int

    :param protect:
        1 to protect (disable updates)
    :type protect: bool

.. This file was automatic generated / don't edit.

