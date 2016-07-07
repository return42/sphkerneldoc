.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_drm.c

.. _`vsp1_du_setup_lif`:

vsp1_du_setup_lif
=================

.. c:function:: int vsp1_du_setup_lif(struct device *dev, unsigned int width, unsigned int height)

    Setup the output part of the VSP pipeline

    :param struct device \*dev:
        the VSP device

    :param unsigned int width:
        output frame width in pixels

    :param unsigned int height:
        output frame height in pixels

.. _`vsp1_du_setup_lif.description`:

Description
-----------

Configure the output part of VSP DRM pipeline for the given frame \ ``width``\  and
\ ``height``\ . This sets up formats on the BRU source pad, the WPF0 sink and source
pads, and the LIF sink pad.

As the media bus code on the BRU source pad is conditioned by the
configuration of the BRU sink 0 pad, we also set up the formats on all BRU
sinks, even if the configuration will be overwritten later by
\ :c:func:`vsp1_du_setup_rpf`\ . This ensures that the BRU configuration is set to a well
defined state.

Return 0 on success or a negative error code on failure.

.. _`vsp1_du_atomic_begin`:

vsp1_du_atomic_begin
====================

.. c:function:: void vsp1_du_atomic_begin(struct device *dev)

    Prepare for an atomic update

    :param struct device \*dev:
        the VSP device

.. _`vsp1_du_atomic_update_ext`:

vsp1_du_atomic_update_ext
=========================

.. c:function:: int vsp1_du_atomic_update_ext(struct device *dev, unsigned int rpf_index, u32 pixelformat, unsigned int pitch, dma_addr_t mem[2], const struct v4l2_rect *src, const struct v4l2_rect *dst, unsigned int alpha, unsigned int zpos)

    Setup one RPF input of the VSP pipeline

    :param struct device \*dev:
        the VSP device

    :param unsigned int rpf_index:
        index of the RPF to setup (0-based)

    :param u32 pixelformat:
        V4L2 pixel format for the RPF memory input

    :param unsigned int pitch:
        number of bytes per line in the image stored in memory

    :param dma_addr_t mem:
        DMA addresses of the memory buffers (one per plane)

    :param const struct v4l2_rect \*src:
        the source crop rectangle for the RPF

    :param const struct v4l2_rect \*dst:
        the destination compose rectangle for the BRU input

    :param unsigned int alpha:
        global alpha value for the input

    :param unsigned int zpos:
        the Z-order position of the input

.. _`vsp1_du_atomic_update_ext.description`:

Description
-----------

Configure the VSP to perform composition of the image referenced by \ ``mem``\ 
through RPF \ ``rpf_index``\ , using the \ ``src``\  crop rectangle and the \ ``dst``\ 
composition rectangle. The Z-order is configurable with higher \ ``zpos``\  values
displayed on top.

Image format as stored in memory is expressed as a V4L2 \ ``pixelformat``\  value.
As a special case, setting the pixel format to 0 will disable the RPF. The
\ ``pitch``\ , \ ``mem``\ , \ ``src``\  and \ ``dst``\  parameters are ignored in that case. Calling the
function on a disabled RPF is allowed.

The memory pitch is configurable to allow for padding at end of lines, or
simple for images that extend beyond the crop rectangle boundaries. The
\ ``pitch``\  value is expressed in bytes and applies to all planes for multiplanar
formats.

The source memory buffer is referenced by the DMA address of its planes in
the \ ``mem``\  array. Up to two planes are supported. The second plane DMA address
is ignored for formats using a single plane.

This function isn't reentrant, the caller needs to serialize calls.

Return 0 on success or a negative error code on failure.

.. _`vsp1_du_atomic_flush`:

vsp1_du_atomic_flush
====================

.. c:function:: void vsp1_du_atomic_flush(struct device *dev)

    Commit an atomic update

    :param struct device \*dev:
        the VSP device

.. This file was automatic generated / don't edit.

