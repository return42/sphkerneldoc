.. -*- coding: utf-8; mode: rst -*-

.. _filters:

===============
Frame filtering
===============

mac80211 requires to see many management frames for proper operation,
and users may want to see many more frames when in monitor mode.
However, for best CPU usage and power consumption, having as few frames
as possible percolate through the stack is desirable. Hence, the
hardware should filter as much as possible.

To achieve this, mac80211 uses filter flags (see below) to tell the
driver's ``configure_filter`` function which frames should be passed to
mac80211 and which should be filtered out.

Before ``configure_filter`` is invoked, the ``prepare_multicast``
callback is invoked with the parameters ``mc_count`` and ``mc_list`` for
the combined multicast address list of all virtual interfaces. It's use
is optional, and it returns a u64 that is passed to
``configure_filter``. Additionally, ``configure_filter`` has the
arguments ``changed_flags`` telling which flags were changed and
``total_flags`` with the new flag states.

If your device has no multicast address filters your driver will need to
check both the ``FIF_ALLMULTI`` flag and the ``mc_count`` parameter to
see whether multicast frames should be accepted or dropped.

All unsupported flags in ``total_flags`` must be cleared. Hardware does
not support a flag if it is incapable of _passing_ the frame to the
stack. Otherwise the driver must ignore the flag, but not clear it. You
must _only_ clear the flag (announce no support for the flag to
mac80211) if you are not able to pass the packet type to the stack (so
the hardware always filters it). So for example, you should clear
``FIF_CONTROL``, if your hardware always filters control frames. If your
hardware always passes control frames to the kernel and is incapable of
filtering them, you do _not_ clear the ``FIF_CONTROL`` flag. This rule
applies to all other FIF flags as well.


.. toctree::
    :maxdepth: 1

    API-enum-ieee80211-filter-flags




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
