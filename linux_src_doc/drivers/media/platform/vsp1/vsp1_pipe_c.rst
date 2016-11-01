.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_pipe.c

.. _`vsp1_get_format_info`:

vsp1_get_format_info
====================

.. c:function:: const struct vsp1_format_info *vsp1_get_format_info(struct vsp1_device *vsp1, u32 fourcc)

    Retrieve format information for a 4CC

    :param struct vsp1_device \*vsp1:
        the VSP1 device

    :param u32 fourcc:
        the format 4CC

.. _`vsp1_get_format_info.description`:

Description
-----------

Return a pointer to the format information structure corresponding to the
given V4L2 format 4CC, or NULL if no corresponding format can be found.

.. This file was automatic generated / don't edit.

