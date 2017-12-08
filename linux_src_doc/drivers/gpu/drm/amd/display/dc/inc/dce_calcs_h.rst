.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/inc/dce_calcs.h

.. _`bw_calcs_init`:

bw_calcs_init
=============

.. c:function:: void bw_calcs_init(struct bw_calcs_dceip *bw_dceip, struct bw_calcs_vbios *bw_vbios, struct hw_asic_id asic_id)

    :param struct bw_calcs_dceip \*bw_dceip:
        *undescribed*

    :param struct bw_calcs_vbios \*bw_vbios:
        *undescribed*

    :param struct hw_asic_id asic_id:
        *undescribed*

.. _`bw_calcs`:

bw_calcs
========

.. c:function:: bool bw_calcs(struct dc_context *ctx, const struct bw_calcs_dceip *dceip, const struct bw_calcs_vbios *vbios, const struct pipe_ctx *pipe, int pipe_count, struct dce_bw_output *calcs_output)

    true -  Display(s) configuration supported. In this case 'calcs_output' contains data for HW programming false - Display(s) configuration not supported (not enough bandwidth).

    :param struct dc_context \*ctx:
        *undescribed*

    :param const struct bw_calcs_dceip \*dceip:
        *undescribed*

    :param const struct bw_calcs_vbios \*vbios:
        *undescribed*

    :param const struct pipe_ctx \*pipe:
        *undescribed*

    :param int pipe_count:
        *undescribed*

    :param struct dce_bw_output \*calcs_output:
        *undescribed*

.. This file was automatic generated / don't edit.

