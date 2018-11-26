.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/dm_helpers.h

.. _`dm_helpers_dp_read_dpcd`:

dm_helpers_dp_read_dpcd
=======================

.. c:function:: bool dm_helpers_dp_read_dpcd(struct dc_context *ctx, const struct dc_link *link, uint32_t address, uint8_t *data, uint32_t size)

    :param ctx:
        *undescribed*
    :type ctx: struct dc_context \*

    :param link:
        *undescribed*
    :type link: const struct dc_link \*

    :param address:
        *undescribed*
    :type address: uint32_t

    :param data:
        *undescribed*
    :type data: uint8_t \*

    :param size:
        *undescribed*
    :type size: uint32_t

.. _`dm_helpers_dp_write_dpcd`:

dm_helpers_dp_write_dpcd
========================

.. c:function:: bool dm_helpers_dp_write_dpcd(struct dc_context *ctx, const struct dc_link *link, uint32_t address, const uint8_t *data, uint32_t size)

    :param ctx:
        *undescribed*
    :type ctx: struct dc_context \*

    :param link:
        *undescribed*
    :type link: const struct dc_link \*

    :param address:
        *undescribed*
    :type address: uint32_t

    :param data:
        *undescribed*
    :type data: const uint8_t \*

    :param size:
        *undescribed*
    :type size: uint32_t

.. This file was automatic generated / don't edit.

