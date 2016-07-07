.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/pvr2fb.c

.. _`pvr2fb_common_init`:

pvr2fb_common_init
==================

.. c:function:: int pvr2fb_common_init( void)

    :param  void:
        no arguments

.. _`pvr2fb_common_init.description`:

Description
-----------

Common init code for the PVR2 chips.

This mostly takes care of the common aspects of the fb setup and
registration. It's expected that the board-specific init code has
already setup pvr2_fix with something meaningful at this point.

Device info reporting is also done here, as well as picking a sane
default from the modedb. For board-specific modelines, simply define
a per-board modedb.

Also worth noting is that the cable and video output types are likely
always going to be VGA for the PCI-based PVR2 boards, but we leave this
in for flexibility anyways. Who knows, maybe someone has tv-out on a
PCI-based version of these things ;-)

.. This file was automatic generated / don't edit.

