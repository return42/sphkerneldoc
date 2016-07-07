.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/xilinx/xilinx-vip.c

.. _`xvip_get_format_by_code`:

xvip_get_format_by_code
=======================

.. c:function:: const struct xvip_video_format *xvip_get_format_by_code(unsigned int code)

    Retrieve format information for a media bus code

    :param unsigned int code:
        the format media bus code

.. _`xvip_get_format_by_code.return`:

Return
------

a pointer to the format information structure corresponding to the
given V4L2 media bus format \ ``code``\ , or ERR_PTR if no corresponding format can
be found.

.. _`xvip_get_format_by_fourcc`:

xvip_get_format_by_fourcc
=========================

.. c:function:: const struct xvip_video_format *xvip_get_format_by_fourcc(u32 fourcc)

    Retrieve format information for a 4CC

    :param u32 fourcc:
        the format 4CC

.. _`xvip_get_format_by_fourcc.return`:

Return
------

a pointer to the format information structure corresponding to the
given V4L2 format \ ``fourcc``\ , or ERR_PTR if no corresponding format can be
found.

.. _`xvip_of_get_format`:

xvip_of_get_format
==================

.. c:function:: const struct xvip_video_format *xvip_of_get_format(struct device_node *node)

    Parse a device tree node and return format information

    :param struct device_node \*node:
        the device tree node

.. _`xvip_of_get_format.description`:

Description
-----------

Read the xlnx,video-format, xlnx,video-width and xlnx,cfa-pattern properties
from the device tree \ ``node``\  passed as an argument and return the corresponding
format information.

.. _`xvip_of_get_format.return`:

Return
------

a pointer to the format information structure corresponding to the
format name and width, or ERR_PTR if no corresponding format can be found.

.. _`xvip_set_format_size`:

xvip_set_format_size
====================

.. c:function:: void xvip_set_format_size(struct v4l2_mbus_framefmt *format, const struct v4l2_subdev_format *fmt)

    Set the media bus frame format size

    :param struct v4l2_mbus_framefmt \*format:
        V4L2 frame format on media bus

    :param const struct v4l2_subdev_format \*fmt:
        media bus format

.. _`xvip_set_format_size.description`:

Description
-----------

Set the media bus frame format size. The width / height from the subdevice
format are set to the given media bus format. The new format size is stored
in \ ``format``\ . The width and height are clamped using default min / max values.

.. _`xvip_clr_or_set`:

xvip_clr_or_set
===============

.. c:function:: void xvip_clr_or_set(struct xvip_device *xvip, u32 addr, u32 mask, bool set)

    Clear or set the register with a bitmask

    :param struct xvip_device \*xvip:
        Xilinx Video IP device

    :param u32 addr:
        address of register

    :param u32 mask:
        bitmask to be set or cleared

    :param bool set:
        boolean flag indicating whether to set or clear

.. _`xvip_clr_or_set.description`:

Description
-----------

Clear or set the register at address \ ``addr``\  with a bitmask \ ``mask``\  depending on
the boolean flag \ ``set``\ . When the flag \ ``set``\  is true, the bitmask is set in
the register, otherwise the bitmask is cleared from the register
when the flag \ ``set``\  is false.

Fox eample, this function can be used to set a control with a boolean value
requested by users. If the caller knows whether to set or clear in the first
place, the caller should call \ :c:func:`xvip_clr`\  or \ :c:func:`xvip_set`\  directly instead of
using this function.

.. _`xvip_clr_and_set`:

xvip_clr_and_set
================

.. c:function:: void xvip_clr_and_set(struct xvip_device *xvip, u32 addr, u32 clr, u32 set)

    Clear and set the register with a bitmask

    :param struct xvip_device \*xvip:
        Xilinx Video IP device

    :param u32 addr:
        address of register

    :param u32 clr:
        bitmask to be cleared

    :param u32 set:
        bitmask to be set

.. _`xvip_clr_and_set.description`:

Description
-----------

Clear a bit(s) of mask \ ``clr``\  in the register at address \ ``addr``\ , then set
a bit(s) of mask \ ``set``\  in the register after.

.. _`xvip_enum_mbus_code`:

xvip_enum_mbus_code
===================

.. c:function:: int xvip_enum_mbus_code(struct v4l2_subdev *subdev, struct v4l2_subdev_pad_config *cfg, struct v4l2_subdev_mbus_code_enum *code)

    Enumerate the media format code

    :param struct v4l2_subdev \*subdev:
        V4L2 subdevice

    :param struct v4l2_subdev_pad_config \*cfg:
        V4L2 subdev pad configuration

    :param struct v4l2_subdev_mbus_code_enum \*code:
        returning media bus code

.. _`xvip_enum_mbus_code.description`:

Description
-----------

Enumerate the media bus code of the subdevice. Return the corresponding
pad format code. This function only works for subdevices with fixed format
on all pads. Subdevices with multiple format should have their own
function to enumerate mbus codes.

.. _`xvip_enum_mbus_code.return`:

Return
------

0 if the media bus code is found, or -EINVAL if the format index
is not valid.

.. _`xvip_enum_frame_size`:

xvip_enum_frame_size
====================

.. c:function:: int xvip_enum_frame_size(struct v4l2_subdev *subdev, struct v4l2_subdev_pad_config *cfg, struct v4l2_subdev_frame_size_enum *fse)

    Enumerate the media bus frame size

    :param struct v4l2_subdev \*subdev:
        V4L2 subdevice

    :param struct v4l2_subdev_pad_config \*cfg:
        V4L2 subdev pad configuration

    :param struct v4l2_subdev_frame_size_enum \*fse:
        returning media bus frame size

.. _`xvip_enum_frame_size.description`:

Description
-----------

This function is a drop-in implementation of the subdev enum_frame_size pad
operation. It assumes that the subdevice has one sink pad and one source
pad, and that the format on the source pad is always identical to the
format on the sink pad. Entities with different requirements need to
implement their own enum_frame_size handlers.

.. _`xvip_enum_frame_size.return`:

Return
------

0 if the media bus frame size is found, or -EINVAL
if the index or the code is not valid.

.. This file was automatic generated / don't edit.

