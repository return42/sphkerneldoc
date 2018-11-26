.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_drm.c

.. _`vsp1_du_setup_lif`:

vsp1_du_setup_lif
=================

.. c:function:: int vsp1_du_setup_lif(struct device *dev, unsigned int pipe_index, const struct vsp1_du_lif_config *cfg)

    Setup the output part of the VSP pipeline

    :param dev:
        the VSP device
    :type dev: struct device \*

    :param pipe_index:
        the DRM pipeline index
    :type pipe_index: unsigned int

    :param cfg:
        the LIF configuration
    :type cfg: const struct vsp1_du_lif_config \*

.. _`vsp1_du_setup_lif.description`:

Description
-----------

Configure the output part of VSP DRM pipeline for the given frame \ ``cfg.width``\ 
and \ ``cfg.height``\ . This sets up formats on the BRx source pad, the WPF sink and
source pads, and the LIF sink pad.

The \ ``pipe_index``\  argument selects which DRM pipeline to setup. The number of
available pipelines depend on the VSP instance.

As the media bus code on the blend unit source pad is conditioned by the
configuration of its sink 0 pad, we also set up the formats on all blend unit
sinks, even if the configuration will be overwritten later by
\ :c:func:`vsp1_du_setup_rpf`\ . This ensures that the blend unit configuration is set to
a well defined state.

Return 0 on success or a negative error code on failure.

.. _`vsp1_du_atomic_begin`:

vsp1_du_atomic_begin
====================

.. c:function:: void vsp1_du_atomic_begin(struct device *dev, unsigned int pipe_index)

    Prepare for an atomic update

    :param dev:
        the VSP device
    :type dev: struct device \*

    :param pipe_index:
        the DRM pipeline index
    :type pipe_index: unsigned int

.. _`vsp1_du_atomic_update`:

vsp1_du_atomic_update
=====================

.. c:function:: int vsp1_du_atomic_update(struct device *dev, unsigned int pipe_index, unsigned int rpf_index, const struct vsp1_du_atomic_config *cfg)

    Setup one RPF input of the VSP pipeline

    :param dev:
        the VSP device
    :type dev: struct device \*

    :param pipe_index:
        the DRM pipeline index
    :type pipe_index: unsigned int

    :param rpf_index:
        index of the RPF to setup (0-based)
    :type rpf_index: unsigned int

    :param cfg:
        the RPF configuration
    :type cfg: const struct vsp1_du_atomic_config \*

.. _`vsp1_du_atomic_update.description`:

Description
-----------

Configure the VSP to perform image composition through RPF \ ``rpf_index``\  as
described by the \ ``cfg``\  configuration. The image to compose is referenced by
\ ``cfg.mem``\  and composed using the \ ``cfg.src``\  crop rectangle and the \ ``cfg.dst``\ 
composition rectangle. The Z-order is configurable with higher \ ``zpos``\  values
displayed on top.

If the \ ``cfg``\  configuration is NULL, the RPF will be disabled. Calling the
function on a disabled RPF is allowed.

Image format as stored in memory is expressed as a V4L2 \ ``cfg.pixelformat``\ 
value. The memory pitch is configurable to allow for padding at end of lines,
or simply for images that extend beyond the crop rectangle boundaries. The
\ ``cfg.pitch``\  value is expressed in bytes and applies to all planes for
multiplanar formats.

The source memory buffer is referenced by the DMA address of its planes in
the \ ``cfg.mem``\  array. Up to two planes are supported. The second plane DMA
address is ignored for formats using a single plane.

This function isn't reentrant, the caller needs to serialize calls.

Return 0 on success or a negative error code on failure.

.. _`vsp1_du_atomic_flush`:

vsp1_du_atomic_flush
====================

.. c:function:: void vsp1_du_atomic_flush(struct device *dev, unsigned int pipe_index, const struct vsp1_du_atomic_pipe_config *cfg)

    Commit an atomic update

    :param dev:
        the VSP device
    :type dev: struct device \*

    :param pipe_index:
        the DRM pipeline index
    :type pipe_index: unsigned int

    :param cfg:
        atomic pipe configuration
    :type cfg: const struct vsp1_du_atomic_pipe_config \*

.. This file was automatic generated / don't edit.

