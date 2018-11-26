.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_video.c

.. _`vsp1_video_calculate_partition`:

vsp1_video_calculate_partition
==============================

.. c:function:: void vsp1_video_calculate_partition(struct vsp1_pipeline *pipe, struct vsp1_partition *partition, unsigned int div_size, unsigned int index)

    Calculate the active partition output window

    :param pipe:
        the pipeline
    :type pipe: struct vsp1_pipeline \*

    :param partition:
        partition that will hold the calculated values
    :type partition: struct vsp1_partition \*

    :param div_size:
        pre-determined maximum partition division size
    :type div_size: unsigned int

    :param index:
        partition index
    :type index: unsigned int

.. This file was automatic generated / don't edit.

