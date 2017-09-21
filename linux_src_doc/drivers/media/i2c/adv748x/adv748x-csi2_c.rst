.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/adv748x/adv748x-csi2.c

.. _`adv748x_csi2_register_link`:

adv748x_csi2_register_link
==========================

.. c:function:: int adv748x_csi2_register_link(struct adv748x_csi2 *tx, struct v4l2_device *v4l2_dev, struct v4l2_subdev *src, unsigned int src_pad)

    Register and link internal entities

    :param struct adv748x_csi2 \*tx:
        CSI2 private entity

    :param struct v4l2_device \*v4l2_dev:
        Video registration device

    :param struct v4l2_subdev \*src:
        Source subdevice to establish link

    :param unsigned int src_pad:
        Pad number of source to link to this \ ``tx``\ 

.. _`adv748x_csi2_register_link.description`:

Description
-----------

Ensure that the subdevice is registered against the v4l2_device, and link the
source pad to the sink pad of the CSI2 bus entity.

.. This file was automatic generated / don't edit.

