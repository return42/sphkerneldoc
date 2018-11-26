.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/v4l2-dev.c

.. _`get_index`:

get_index
=========

.. c:function:: int get_index(struct video_device *vdev)

    assign stream index number based on v4l2_dev

    :param vdev:
        video_device to assign index number to, vdev->v4l2_dev should be assigned
    :type vdev: struct video_device \*

.. _`get_index.description`:

Description
-----------

Note that when this is called the new device has not yet been registered
in the video_device array, but it was able to obtain a minor number.

This means that we can always obtain a free stream index number since
the worst case scenario is that there are VIDEO_NUM_DEVICES - 1 slots in
use of the video_device array.

Returns a free index number.

.. _`video_unregister_device`:

video_unregister_device
=======================

.. c:function:: void video_unregister_device(struct video_device *vdev)

    unregister a video4linux device

    :param vdev:
        the device to unregister
    :type vdev: struct video_device \*

.. _`video_unregister_device.description`:

Description
-----------

This unregisters the passed device. Future open calls will
be met with errors.

.. This file was automatic generated / don't edit.

