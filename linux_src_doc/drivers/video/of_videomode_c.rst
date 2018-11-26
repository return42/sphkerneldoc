.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/of_videomode.c

.. _`of_get_videomode`:

of_get_videomode
================

.. c:function:: int of_get_videomode(struct device_node *np, struct videomode *vm, int index)

    get the videomode #<index> from devicetree \ ``np``\  - devicenode with the display_timings \ ``vm``\  - set to return value \ ``index``\  - index into list of display_timings (Set this to OF_USE_NATIVE_MODE to use whatever mode is specified as native mode in the DT.)

    :param np:
        *undescribed*
    :type np: struct device_node \*

    :param vm:
        *undescribed*
    :type vm: struct videomode \*

    :param index:
        *undescribed*
    :type index: int

.. _`of_get_videomode.description`:

Description
-----------

Get a list of all display timings and put the one
specified by index into \*vm. This function should only be used, if
only one videomode is to be retrieved. A driver that needs to work
with multiple/all videomodes should work with
of_get_display_timings instead.

.. This file was automatic generated / don't edit.

