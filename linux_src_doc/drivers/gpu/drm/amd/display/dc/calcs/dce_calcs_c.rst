.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/calcs/dce_calcs.c

.. _`is_display_configuration_supported`:

is_display_configuration_supported
==================================

.. c:function:: bool is_display_configuration_supported(const struct bw_calcs_vbios *vbios, const struct dce_bw_output *calcs_output)

    maximum voltage (max Performance Level).

    :param const struct bw_calcs_vbios \*vbios:
        *undescribed*

    :param const struct dce_bw_output \*calcs_output:
        *undescribed*

.. _`bw_calcs`:

bw_calcs
========

.. c:function:: bool bw_calcs(struct dc_context *ctx, const struct bw_calcs_dceip *dceip, const struct bw_calcs_vbios *vbios, const struct pipe_ctx pipe, int pipe_count, struct dce_bw_output *calcs_output)

    true -  Display(s) configuration supported. In this case 'calcs_output' contains data for HW programming false - Display(s) configuration not supported (not enough bandwidth).

    :param struct dc_context \*ctx:
        *undescribed*

    :param const struct bw_calcs_dceip \*dceip:
        *undescribed*

    :param const struct bw_calcs_vbios \*vbios:
        *undescribed*

    :param const struct pipe_ctx pipe:
        *undescribed*

    :param int pipe_count:
        *undescribed*

    :param struct dce_bw_output \*calcs_output:
        *undescribed*

.. This file was automatic generated / don't edit.

