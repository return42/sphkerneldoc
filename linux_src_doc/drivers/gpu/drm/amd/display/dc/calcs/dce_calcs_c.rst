.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/calcs/dce_calcs.c

.. _`is_display_configuration_supported`:

is_display_configuration_supported
==================================

.. c:function:: bool is_display_configuration_supported(const struct bw_calcs_vbios *vbios, const struct dce_bw_output *calcs_output)

    maximum voltage (max Performance Level).

    :param vbios:
        *undescribed*
    :type vbios: const struct bw_calcs_vbios \*

    :param calcs_output:
        *undescribed*
    :type calcs_output: const struct dce_bw_output \*

.. _`bw_calcs`:

bw_calcs
========

.. c:function:: bool bw_calcs(struct dc_context *ctx, const struct bw_calcs_dceip *dceip, const struct bw_calcs_vbios *vbios, const struct pipe_ctx pipe, int pipe_count, struct dce_bw_output *calcs_output)

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
    :type pipe: const struct pipe_ctx

    :param pipe_count:
        *undescribed*
    :type pipe_count: int

    :param calcs_output:
        *undescribed*
    :type calcs_output: struct dce_bw_output \*

.. This file was automatic generated / don't edit.

