.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/exynos/exynos7_drm_decon.c

.. _`decon_shadow_protect_win`:

decon_shadow_protect_win
========================

.. c:function:: void decon_shadow_protect_win(struct decon_context *ctx, unsigned int win, bool protect)

    disable updating values from shadow registers at vsync

    :param ctx:
        *undescribed*
    :type ctx: struct decon_context \*

    :param win:
        window to protect registers for
    :type win: unsigned int

    :param protect:
        1 to protect (disable updates)
    :type protect: bool

.. This file was automatic generated / don't edit.

