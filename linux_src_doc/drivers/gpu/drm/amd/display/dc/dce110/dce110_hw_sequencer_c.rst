.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/dce110/dce110_hw_sequencer.c

.. _`dce110_enable_accelerated_mode`:

dce110_enable_accelerated_mode
==============================

.. c:function:: void dce110_enable_accelerated_mode(struct dc *dc)

    1. Power down all DC HW blocks 2. Disable VGA engine on all controllers 3. Enable power gating for controller 4. Set acc_mode_change bit (VBIOS will clear this bit when going to FSDOS)

    :param struct dc \*dc:
        *undescribed*

.. _`set_plane_config`:

set_plane_config
================

.. c:function:: void set_plane_config(const struct dc *dc, struct pipe_ctx *pipe_ctx, struct resource_context *res_ctx)

    :param const struct dc \*dc:
        *undescribed*

    :param struct pipe_ctx \*pipe_ctx:
        *undescribed*

    :param struct resource_context \*res_ctx:
        *undescribed*

.. This file was automatic generated / don't edit.

