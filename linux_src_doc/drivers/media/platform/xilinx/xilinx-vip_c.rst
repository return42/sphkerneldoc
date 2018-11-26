.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/xilinx/xilinx-vip.c

.. _`xvip_get_format_by_code`:

xvip_get_format_by_code
=======================

.. c:function:: const struct xvip_video_format *xvip_get_format_by_code(unsigned int code)

    Retrieve format information for a media bus code

    :param code:
        the format media bus code
    :type code: unsigned int

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

    :param fourcc:
        the format 4CC
    :type fourcc: u32

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

    :param node:
        the device tree node
    :type node: struct device_node \*

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

    :param format:
        V4L2 frame format on media bus
    :type format: struct v4l2_mbus_framefmt \*

    :param fmt:
        media bus format
    :type fmt: const struct v4l2_subdev_format \*

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

    :param xvip:
        Xilinx Video IP device
    :type xvip: struct xvip_device \*

    :param addr:
        address of register
    :type addr: u32

    :param mask:
        bitmask to be set or cleared
    :type mask: u32

    :param set:
        boolean flag indicating whether to set or clear
    :type set: bool

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

    :param xvip:
        Xilinx Video IP device
    :type xvip: struct xvip_device \*

    :param addr:
        address of register
    :type addr: u32

    :param clr:
        bitmask to be cleared
    :type clr: u32

    :param set:
        bitmask to be set
    :type set: u32

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

    :param subdev:
        V4L2 subdevice
    :type subdev: struct v4l2_subdev \*

    :param cfg:
        V4L2 subdev pad configuration
    :type cfg: struct v4l2_subdev_pad_config \*

    :param code:
        returning media bus code
    :type code: struct v4l2_subdev_mbus_code_enum \*

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

    :param subdev:
        V4L2 subdevice
    :type subdev: struct v4l2_subdev \*

    :param cfg:
        V4L2 subdev pad configuration
    :type cfg: struct v4l2_subdev_pad_config \*

    :param fse:
        returning media bus frame size
    :type fse: struct v4l2_subdev_frame_size_enum \*

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

