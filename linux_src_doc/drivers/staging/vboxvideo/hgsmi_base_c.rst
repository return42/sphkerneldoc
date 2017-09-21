.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/vboxvideo/hgsmi_base.c

.. _`hgsmi_report_flags_location`:

hgsmi_report_flags_location
===========================

.. c:function:: int hgsmi_report_flags_location(struct gen_pool *ctx, u32 location)

    @param    ctx          the context of the guest heap to use. \ ``param``\     location     the offset chosen for the flags within guest VRAM. \ ``returns``\  0 on success, -errno on failure

    :param struct gen_pool \*ctx:
        *undescribed*

    :param u32 location:
        *undescribed*

.. _`hgsmi_send_caps_info`:

hgsmi_send_caps_info
====================

.. c:function:: int hgsmi_send_caps_info(struct gen_pool *ctx, u32 caps)

    related guest capabilities via an HGSMI command. \ ``param``\     ctx                 the context of the guest heap to use. \ ``param``\     caps                the capabilities to report, see vbva_caps. \ ``returns``\  0 on success, -errno on failure

    :param struct gen_pool \*ctx:
        *undescribed*

    :param u32 caps:
        *undescribed*

.. _`hgsmi_query_conf`:

hgsmi_query_conf
================

.. c:function:: int hgsmi_query_conf(struct gen_pool *ctx, u32 index, u32 *value_ret)

    @param  ctx        the context containing the heap used \ ``param``\   index      the index of the parameter to query, \ ``see``\  vbva_conf32::index \ ``param``\   value_ret  where to store the value of the parameter on success \ ``returns``\  0 on success, -errno on failure

    :param struct gen_pool \*ctx:
        *undescribed*

    :param u32 index:
        *undescribed*

    :param u32 \*value_ret:
        *undescribed*

.. _`hgsmi_update_pointer_shape`:

hgsmi_update_pointer_shape
==========================

.. c:function:: int hgsmi_update_pointer_shape(struct gen_pool *ctx, u32 flags, u32 hot_x, u32 hot_y, u32 width, u32 height, u8 *pixels, u32 len)

    :param struct gen_pool \*ctx:
        *undescribed*

    :param u32 flags:
        *undescribed*

    :param u32 hot_x:
        *undescribed*

    :param u32 hot_y:
        *undescribed*

    :param u32 width:
        *undescribed*

    :param u32 height:
        *undescribed*

    :param u8 \*pixels:
        *undescribed*

    :param u32 len:
        *undescribed*

.. _`hgsmi_update_pointer_shape.description`:

Description
-----------

@param  ctx      the context containing the heap to be used

.. _`hgsmi_cursor_position`:

hgsmi_cursor_position
=====================

.. c:function:: int hgsmi_cursor_position(struct gen_pool *ctx, bool report_position, u32 x, u32 y, u32 *x_host, u32 *y_host)

    to re-position its own cursor (though this is currently unlikely).  The current host cursor position is returned. \ ``param``\   ctx              The context containing the heap used. \ ``param``\   report_position  Are we reporting a position? \ ``param``\   x                Guest cursor X position. \ ``param``\   y                Guest cursor Y position. \ ``param``\   x_host           Host cursor X position is stored here.  Optional. \ ``param``\   y_host           Host cursor Y position is stored here.  Optional. \ ``returns``\  0 on success, -errno on failure

    :param struct gen_pool \*ctx:
        *undescribed*

    :param bool report_position:
        *undescribed*

    :param u32 x:
        *undescribed*

    :param u32 y:
        *undescribed*

    :param u32 \*x_host:
        *undescribed*

    :param u32 \*y_host:
        *undescribed*

.. This file was automatic generated / don't edit.

