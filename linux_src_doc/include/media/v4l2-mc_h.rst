.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-mc.h

.. _`v4l2_mc_create_media_graph`:

v4l2_mc_create_media_graph
==========================

.. c:function:: int v4l2_mc_create_media_graph(struct media_device *mdev)

    create Media Controller links at the graph.

    :param mdev:
        pointer to the \ :c:type:`struct media_device <media_device>`\  struct.
    :type mdev: struct media_device \*

.. _`v4l2_mc_create_media_graph.description`:

Description
-----------

Add links between the entities commonly found on PC customer's hardware at
the V4L2 side: camera sensors, audio and video PLL-IF decoders, tuners,
analog TV decoder and I/O entities (video, VBI and Software Defined Radio).

.. note::

   Webcams are modelled on a very simple way: the sensor is
   connected directly to the I/O entity. All dirty details, like
   scaler and crop HW are hidden. While such mapping is enough for v4l2
   interface centric PC-consumer's hardware, V4L2 subdev centric camera
   hardware should not use this routine, as it will not build the right graph.

.. _`v4l_enable_media_source`:

v4l_enable_media_source
=======================

.. c:function:: int v4l_enable_media_source(struct video_device *vdev)

    Hold media source for exclusive use if free

    :param vdev:
        pointer to struct video_device
    :type vdev: struct video_device \*

.. _`v4l_enable_media_source.description`:

Description
-----------

This interface calls enable_source handler to determine if
media source is free for use. The enable_source handler is
responsible for checking is the media source is free and
start a pipeline between the media source and the media
entity associated with the video device. This interface
should be called from v4l2-core and dvb-core interfaces
that change the source configuration.

.. _`v4l_enable_media_source.return`:

Return
------

returns zero on success or a negative error code.

.. _`v4l_disable_media_source`:

v4l_disable_media_source
========================

.. c:function:: void v4l_disable_media_source(struct video_device *vdev)

    Release media source

    :param vdev:
        pointer to struct video_device
    :type vdev: struct video_device \*

.. _`v4l_disable_media_source.description`:

Description
-----------

This interface calls disable_source handler to release
the media source. The disable_source handler stops the
active media pipeline between the media source and the
media entity associated with the video device.

.. _`v4l_disable_media_source.return`:

Return
------

returns zero on success or a negative error code.

.. _`v4l2_pipeline_pm_use`:

v4l2_pipeline_pm_use
====================

.. c:function:: int v4l2_pipeline_pm_use(struct media_entity *entity, int use)

    Update the use count of an entity

    :param entity:
        The entity
    :type entity: struct media_entity \*

    :param use:
        Use (1) or stop using (0) the entity
    :type use: int

.. _`v4l2_pipeline_pm_use.description`:

Description
-----------

Update the use count of all entities in the pipeline and power entities on or
off accordingly.

This function is intended to be called in video node open (use ==
1) and release (use == 0). It uses struct media_entity.use_count to
track the power status. The use of this function should be paired
with \ :c:func:`v4l2_pipeline_link_notify`\ .

Return 0 on success or a negative error code on failure. Powering entities
off is assumed to never fail. No failure can occur when the use parameter is
set to 0.

.. _`v4l2_pipeline_link_notify`:

v4l2_pipeline_link_notify
=========================

.. c:function:: int v4l2_pipeline_link_notify(struct media_link *link, u32 flags, unsigned int notification)

    Link management notification callback

    :param link:
        The link
    :type link: struct media_link \*

    :param flags:
        New link flags that will be applied
    :type flags: u32

    :param notification:
        The link's state change notification type (MEDIA_DEV_NOTIFY_*)
    :type notification: unsigned int

.. _`v4l2_pipeline_link_notify.description`:

Description
-----------

React to link management on powered pipelines by updating the use count of
all entities in the source and sink sides of the link. Entities are powered
on or off accordingly. The use of this function should be paired
with \ :c:func:`v4l2_pipeline_pm_use`\ .

Return 0 on success or a negative error code on failure. Powering entities
off is assumed to never fail. This function will not fail for disconnection
events.

.. This file was automatic generated / don't edit.

