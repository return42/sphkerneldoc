.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_validate.c

.. _`size_is_lt`:

size_is_lt
==========

.. c:function:: bool size_is_lt(uint32_t width, uint32_t height, int cpp)

    Returns whether a miplevel of the given size will use the lineartile (LT) tiling layout rather than the normal T tiling layout.

    :param uint32_t width:
        Width in pixels of the miplevel

    :param uint32_t height:
        Height in pixels of the miplevel

    :param int cpp:
        Bytes per pixel of the pixel format

.. This file was automatic generated / don't edit.

