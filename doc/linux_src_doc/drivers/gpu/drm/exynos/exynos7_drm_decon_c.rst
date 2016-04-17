.. -*- coding: utf-8; mode: rst -*-

===================
exynos7_drm_decon.c
===================


.. _`decon_shadow_protect_win`:

decon_shadow_protect_win
========================

.. c:function:: void decon_shadow_protect_win (struct decon_context *ctx, unsigned int win, bool protect)

    disable updating values from shadow registers at vsync

    :param struct decon_context \*ctx:

        *undescribed*

    :param unsigned int win:
        window to protect registers for

    :param bool protect:
        1 to protect (disable updates)

