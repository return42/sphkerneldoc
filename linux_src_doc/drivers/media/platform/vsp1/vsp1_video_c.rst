.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_video.c

.. _`vsp1_video_partition`:

vsp1_video_partition
====================

.. c:function:: struct v4l2_rect vsp1_video_partition(struct vsp1_pipeline *pipe, unsigned int div_size, unsigned int index)

    Calculate the active partition output window

    :param struct vsp1_pipeline \*pipe:
        *undescribed*

    :param unsigned int div_size:
        pre-determined maximum partition division size

    :param unsigned int index:
        partition index

.. _`vsp1_video_partition.description`:

Description
-----------

Returns a v4l2_rect describing the partition window.

.. This file was automatic generated / don't edit.

