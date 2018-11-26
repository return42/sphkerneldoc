.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/soc/amlogic/meson-canvas.h

.. _`meson_canvas_get`:

meson_canvas_get
================

.. c:function:: struct meson_canvas *meson_canvas_get(struct device *dev)

    get a canvas provider instance

    :param dev:
        consumer device pointer
    :type dev: struct device \*

.. _`meson_canvas_alloc`:

meson_canvas_alloc
==================

.. c:function:: int meson_canvas_alloc(struct meson_canvas *canvas, u8 *canvas_index)

    take ownership of a canvas

    :param canvas:
        canvas provider instance retrieved from \ :c:func:`meson_canvas_get`\ 
    :type canvas: struct meson_canvas \*

    :param canvas_index:
        will be filled with the canvas ID
    :type canvas_index: u8 \*

.. _`meson_canvas_free`:

meson_canvas_free
=================

.. c:function:: int meson_canvas_free(struct meson_canvas *canvas, u8 canvas_index)

    remove ownership from a canvas

    :param canvas:
        canvas provider instance retrieved from \ :c:func:`meson_canvas_get`\ 
    :type canvas: struct meson_canvas \*

    :param canvas_index:
        canvas ID that was obtained via \ :c:func:`meson_canvas_alloc`\ 
    :type canvas_index: u8

.. _`meson_canvas_config`:

meson_canvas_config
===================

.. c:function:: int meson_canvas_config(struct meson_canvas *canvas, u8 canvas_index, u32 addr, u32 stride, u32 height, unsigned int wrap, unsigned int blkmode, unsigned int endian)

    configure a canvas

    :param canvas:
        canvas provider instance retrieved from \ :c:func:`meson_canvas_get`\ 
    :type canvas: struct meson_canvas \*

    :param canvas_index:
        canvas ID that was obtained via \ :c:func:`meson_canvas_alloc`\ 
    :type canvas_index: u8

    :param addr:
        physical address to the pixel buffer
    :type addr: u32

    :param stride:
        width of the buffer
    :type stride: u32

    :param height:
        height of the buffer
    :type height: u32

    :param wrap:
        undocumented
    :type wrap: unsigned int

    :param blkmode:
        block mode (linear, 32x32, 64x64)
    :type blkmode: unsigned int

    :param endian:
        byte swapping (swap16, swap32, swap64, swap128)
    :type endian: unsigned int

.. This file was automatic generated / don't edit.

