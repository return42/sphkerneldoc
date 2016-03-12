.. -*- coding: utf-8; mode: rst -*-

=============
v4l2-subdev.c
=============



.. _xref_v4l2_subdev_notify_event:

v4l2_subdev_notify_event
========================

.. c:function:: void v4l2_subdev_notify_event (struct v4l2_subdev * sd, const struct v4l2_event * ev)

    Delivers event notification for subdevice

    :param struct v4l2_subdev * sd:
        The subdev for which to deliver the event

    :param const struct v4l2_event * ev:
        The event to deliver



Description
-----------

Will deliver the specified event to all userspace event listeners which are
subscribed to the v42l subdev event queue as well as to the bridge driver
using the notify callback. The notification type for the notify callback
will be V4L2_DEVICE_NOTIFY_EVENT.


