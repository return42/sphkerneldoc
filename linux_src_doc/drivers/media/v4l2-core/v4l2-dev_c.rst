.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/v4l2-dev.c

.. _`get_index`:

get_index
=========

.. c:function:: int get_index(struct video_device *vdev)

    assign stream index number based on v4l2_dev

    :param struct video_device \*vdev:
        video_device to assign index number to, vdev->v4l2_dev should be assigned

.. _`get_index.description`:

Description
-----------

Note that when this is called the new device has not yet been registered
in the video_device array, but it was able to obtain a minor number.

This means that we can always obtain a free stream index number since
the worst case scenario is that there are VIDEO_NUM_DEVICES - 1 slots in
use of the video_device array.

Returns a free index number.

.. _`__video_register_device`:

__video_register_device
=======================

.. c:function:: int __video_register_device(struct video_device *vdev, int type, int nr, int warn_if_nr_in_use, struct module *owner)

    register video4linux devices

    :param struct video_device \*vdev:
        video device structure we want to register

    :param int type:
        type of device to register

    :param int nr:
        which device node number (0 == /dev/video0, 1 == /dev/video1, ...
        -1 == first free)

    :param int warn_if_nr_in_use:
        warn if the desired device node number
        was already in use and another number was chosen instead.

    :param struct module \*owner:
        module that owns the video device node

.. _`__video_register_device.description`:

Description
-----------

The registration code assigns minor numbers and device node numbers
based on the requested type and registers the new device node with
the kernel.

This function assumes that struct video_device was zeroed when it
was allocated and does not contain any stale date.

An error is returned if no free minor or device node number could be
found, or if the registration of the device node failed.

Zero is returned on success.

Valid types are

\ ``VFL_TYPE_GRABBER``\  - A frame grabber

\ ``VFL_TYPE_VBI``\  - Vertical blank data (undecoded)

\ ``VFL_TYPE_RADIO``\  - A radio card

\ ``VFL_TYPE_SUBDEV``\  - A subdevice

\ ``VFL_TYPE_SDR``\  - Software Defined Radio

.. _`video_unregister_device`:

video_unregister_device
=======================

.. c:function:: void video_unregister_device(struct video_device *vdev)

    unregister a video4linux device

    :param struct video_device \*vdev:
        the device to unregister

.. _`video_unregister_device.description`:

Description
-----------

This unregisters the passed device. Future open calls will
be met with errors.

.. This file was automatic generated / don't edit.

