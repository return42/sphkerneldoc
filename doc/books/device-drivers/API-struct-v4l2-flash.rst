.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-flash:

=================
struct v4l2_flash
=================

*man struct v4l2_flash(9)*

*4.6.0-rc5*

Flash sub-device context


Synopsis
========

.. code-block:: c

    struct v4l2_flash {
      struct led_classdev_flash * fled_cdev;
      struct led_classdev_flash * iled_cdev;
      const struct v4l2_flash_ops * ops;
      struct v4l2_subdev sd;
      struct v4l2_ctrl_handler hdl;
      struct v4l2_ctrl ** ctrls;
    };


Members
=======

fled_cdev
    LED flash class device controlled by this sub-device

iled_cdev
    LED class device representing indicator LED associated with the LED
    flash class device

ops
    V4L2 specific flash ops

sd
    V4L2 sub-device

hdl
    flash controls handler

ctrls
    array of pointers to controls, whose values define the sub-device
    state


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
