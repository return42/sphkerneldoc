.. -*- coding: utf-8; mode: rst -*-

==============
of_videomode.c
==============


.. _`of_get_videomode`:

of_get_videomode
================

.. c:function:: int of_get_videomode (struct device_node *np, struct videomode *vm, int index)

    get the videomode #<index> from devicetree @np - devicenode with the display_timings @vm - set to return value @index - index into list of display_timings (Set this to OF_USE_NATIVE_MODE to use whatever mode is specified as native mode in the DT.)

    :param struct device_node \*np:

        *undescribed*

    :param struct videomode \*vm:

        *undescribed*

    :param int index:

        *undescribed*



.. _`of_get_videomode.description`:

DESCRIPTION
-----------

Get a list of all display timings and put the one
specified by index into \*vm. This function should only be used, if
only one videomode is to be retrieved. A driver that needs to work
with multiple/all videomodes should work with
of_get_display_timings instead.

