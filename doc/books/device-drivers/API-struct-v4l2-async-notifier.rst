.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-async-notifier:

==========================
struct v4l2_async_notifier
==========================

*man struct v4l2_async_notifier(9)*

*4.6.0-rc5*

v4l2_device notifier data


Synopsis
========

.. code-block:: c

    struct v4l2_async_notifier {
      unsigned int num_subdevs;
      struct v4l2_async_subdev ** subdevs;
      struct v4l2_device * v4l2_dev;
      struct list_head waiting;
      struct list_head done;
      struct list_head list;
      int (* bound) (struct v4l2_async_notifier *notifier,struct v4l2_subdev *subdev,struct v4l2_async_subdev *asd);
      int (* complete) (struct v4l2_async_notifier *notifier);
      void (* unbind) (struct v4l2_async_notifier *notifier,struct v4l2_subdev *subdev,struct v4l2_async_subdev *asd);
    };


Members
=======

num_subdevs
    number of subdevices

subdevs
    array of pointers to subdevice descriptors

v4l2_dev
    pointer to struct v4l2_device

waiting
    list of struct v4l2_async_subdev, waiting for their drivers

done
    list of struct v4l2_subdev, already probed

list
    member in a global list of notifiers

bound
    a subdevice driver has successfully probed one of subdevices

complete
    all subdevices have been probed successfully

unbind
    a subdevice is leaving


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
