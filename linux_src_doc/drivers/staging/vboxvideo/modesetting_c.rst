.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/vboxvideo/modesetting.c

.. _`hgsmi_process_display_info`:

hgsmi_process_display_info
==========================

.. c:function:: void hgsmi_process_display_info(struct gen_pool *ctx, u32 display, s32 origin_x, s32 origin_y, u32 start_offset, u32 pitch, u32 width, u32 height, u16 bpp, u16 flags)

    initialised first using \ ``a``\  VBoxHGSMISendViewInfo and if the mode is being set on the first display then it must be set first using registers. \ ``param``\   ctx           The context containing the heap to use \ ``param``\   display       The screen number \ ``param``\   origin_x      The horizontal displacement relative to the first scrn \ ``param``\   origin_y      The vertical displacement relative to the first screen \ ``param``\   start_offset  The offset of the visible area of the framebuffer relative to the framebuffer start \ ``param``\   pitch         The offset in bytes between the starts of two adjecent scan lines in video RAM \ ``param``\   width         The mode width \ ``param``\   height        The mode height \ ``param``\   bpp           The colour depth of the mode \ ``param``\   flags         Flags

    :param struct gen_pool \*ctx:
        *undescribed*

    :param u32 display:
        *undescribed*

    :param s32 origin_x:
        *undescribed*

    :param s32 origin_y:
        *undescribed*

    :param u32 start_offset:
        *undescribed*

    :param u32 pitch:
        *undescribed*

    :param u32 width:
        *undescribed*

    :param u32 height:
        *undescribed*

    :param u16 bpp:
        *undescribed*

    :param u16 flags:
        *undescribed*

.. _`hgsmi_update_input_mapping`:

hgsmi_update_input_mapping
==========================

.. c:function:: int hgsmi_update_input_mapping(struct gen_pool *ctx, s32 origin_x, s32 origin_y, u32 width, u32 height)

    expressed.  This information remains valid until the next VBVA resize event for any screen, at which time it is reset to the bounding rectangle of all virtual screens. \ ``param``\   ctx       The context containing the heap to use. \ ``param``\   origin_x  Upper left X co-ordinate relative to the first screen. \ ``param``\   origin_y  Upper left Y co-ordinate relative to the first screen. \ ``param``\   width     Rectangle width. \ ``param``\   height    Rectangle height. \ ``returns``\  0 on success, -errno on failure

    :param struct gen_pool \*ctx:
        *undescribed*

    :param s32 origin_x:
        *undescribed*

    :param s32 origin_y:
        *undescribed*

    :param u32 width:
        *undescribed*

    :param u32 height:
        *undescribed*

.. _`hgsmi_get_mode_hints`:

hgsmi_get_mode_hints
====================

.. c:function:: int hgsmi_get_mode_hints(struct gen_pool *ctx, unsigned int screens, struct vbva_modehint *hints)

    @param  ctx      The context containing the heap to use. \ ``param``\   screens  The number of screens to query hints for, starting at 0. \ ``param``\   hints    Array of vbva_modehint structures for receiving the hints. \ ``returns``\  0 on success, -errno on failure

    :param struct gen_pool \*ctx:
        *undescribed*

    :param unsigned int screens:
        *undescribed*

    :param struct vbva_modehint \*hints:
        *undescribed*

.. This file was automatic generated / don't edit.

