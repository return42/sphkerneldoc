.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/vboxvideo/modesetting.c

.. _`hgsmi_process_display_info`:

hgsmi_process_display_info
==========================

.. c:function:: void hgsmi_process_display_info(struct gen_pool *ctx, u32 display, s32 origin_x, s32 origin_y, u32 start_offset, u32 pitch, u32 width, u32 height, u16 bpp, u16 flags)

    initialised first using \ ``a``\  VBoxHGSMISendViewInfo and if the mode is being set on the first display then it must be set first using registers. \ ``param``\   ctx           The context containing the heap to use \ ``param``\   display       The screen number \ ``param``\   origin_x      The horizontal displacement relative to the first scrn \ ``param``\   origin_y      The vertical displacement relative to the first screen \ ``param``\   start_offset  The offset of the visible area of the framebuffer relative to the framebuffer start \ ``param``\   pitch         The offset in bytes between the starts of two adjecent scan lines in video RAM \ ``param``\   width         The mode width \ ``param``\   height        The mode height \ ``param``\   bpp           The colour depth of the mode \ ``param``\   flags         Flags

    :param ctx:
        *undescribed*
    :type ctx: struct gen_pool \*

    :param display:
        *undescribed*
    :type display: u32

    :param origin_x:
        *undescribed*
    :type origin_x: s32

    :param origin_y:
        *undescribed*
    :type origin_y: s32

    :param start_offset:
        *undescribed*
    :type start_offset: u32

    :param pitch:
        *undescribed*
    :type pitch: u32

    :param width:
        *undescribed*
    :type width: u32

    :param height:
        *undescribed*
    :type height: u32

    :param bpp:
        *undescribed*
    :type bpp: u16

    :param flags:
        *undescribed*
    :type flags: u16

.. _`hgsmi_update_input_mapping`:

hgsmi_update_input_mapping
==========================

.. c:function:: int hgsmi_update_input_mapping(struct gen_pool *ctx, s32 origin_x, s32 origin_y, u32 width, u32 height)

    expressed.  This information remains valid until the next VBVA resize event for any screen, at which time it is reset to the bounding rectangle of all virtual screens. \ ``param``\   ctx       The context containing the heap to use. \ ``param``\   origin_x  Upper left X co-ordinate relative to the first screen. \ ``param``\   origin_y  Upper left Y co-ordinate relative to the first screen. \ ``param``\   width     Rectangle width. \ ``param``\   height    Rectangle height. \ ``returns``\  0 on success, -errno on failure

    :param ctx:
        *undescribed*
    :type ctx: struct gen_pool \*

    :param origin_x:
        *undescribed*
    :type origin_x: s32

    :param origin_y:
        *undescribed*
    :type origin_y: s32

    :param width:
        *undescribed*
    :type width: u32

    :param height:
        *undescribed*
    :type height: u32

.. _`hgsmi_get_mode_hints`:

hgsmi_get_mode_hints
====================

.. c:function:: int hgsmi_get_mode_hints(struct gen_pool *ctx, unsigned int screens, struct vbva_modehint *hints)

    \ ``param``\   ctx      The context containing the heap to use. \ ``param``\   screens  The number of screens to query hints for, starting at 0. \ ``param``\   hints    Array of vbva_modehint structures for receiving the hints. \ ``returns``\  0 on success, -errno on failure

    :param ctx:
        *undescribed*
    :type ctx: struct gen_pool \*

    :param screens:
        *undescribed*
    :type screens: unsigned int

    :param hints:
        *undescribed*
    :type hints: struct vbva_modehint \*

.. This file was automatic generated / don't edit.

