.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/inc/dce_calcs.h

.. _`bw_calcs_init`:

bw_calcs_init
=============

.. c:function:: void bw_calcs_init(struct bw_calcs_dceip *bw_dceip, struct bw_calcs_vbios *bw_vbios, struct hw_asic_id asic_id)

    :param bw_dceip:
        *undescribed*
    :type bw_dceip: struct bw_calcs_dceip \*

    :param bw_vbios:
        *undescribed*
    :type bw_vbios: struct bw_calcs_vbios \*

    :param asic_id:
        *undescribed*
    :type asic_id: struct hw_asic_id

.. _`bw_calcs`:

bw_calcs
========

.. c:function:: bool bw_calcs(struct dc_context *ctx, const struct bw_calcs_dceip *dceip, const struct bw_calcs_vbios *vbios, const struct pipe_ctx *pipe, int pipe_count, struct dce_bw_output *calcs_output)

    true -  Display(s) configuration supported. In this case 'calcs_output' contains data for HW programming false - Display(s) configuration not supported (not enough bandwidth).

    :param ctx:
        *undescribed*
    :type ctx: struct dc_context \*

    :param dceip:
        *undescribed*
    :type dceip: const struct bw_calcs_dceip \*

    :param vbios:
        *undescribed*
    :type vbios: const struct bw_calcs_vbios \*

    :param pipe:
        *undescribed*
    :type pipe: const struct pipe_ctx \*

    :param pipe_count:
        *undescribed*
    :type pipe_count: int

    :param calcs_output:
        *undescribed*
    :type calcs_output: struct dce_bw_output \*

.. This file was automatic generated / don't edit.

