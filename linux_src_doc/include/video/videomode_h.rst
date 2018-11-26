.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/video/videomode.h

.. _`videomode_from_timing`:

videomode_from_timing
=====================

.. c:function:: void videomode_from_timing(const struct display_timing *dt, struct videomode *vm)

    convert display timing to videomode

    :param dt:
        display_timing structure
    :type dt: const struct display_timing \*

    :param vm:
        return value
    :type vm: struct videomode \*

.. _`videomode_from_timing.description`:

Description
-----------

This function converts a struct display_timing to a struct videomode.

.. _`videomode_from_timings`:

videomode_from_timings
======================

.. c:function:: int videomode_from_timings(const struct display_timings *disp, struct videomode *vm, unsigned int index)

    convert one display timings entry to videomode

    :param disp:
        structure with all possible timing entries
    :type disp: const struct display_timings \*

    :param vm:
        return value
    :type vm: struct videomode \*

    :param index:
        index into the list of display timings in devicetree
    :type index: unsigned int

.. _`videomode_from_timings.description`:

Description
-----------

This function converts one struct display_timing entry to a struct videomode.

.. This file was automatic generated / don't edit.

