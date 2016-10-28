.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap3-restart.c

.. _`omap3xxx_restart`:

omap3xxx_restart
================

.. c:function:: void omap3xxx_restart(enum reboot_mode mode, const char *cmd)

    trigger a software restart of the SoC

    :param enum reboot_mode mode:
        the "reboot mode", see arch/arm/kernel/{setup,process}.c

    :param const char \*cmd:
        passed from the userspace program rebooting the system (if provided)

.. _`omap3xxx_restart.description`:

Description
-----------

Resets the SoC.  For \ ``cmd``\ , see the 'reboot' syscall in
kernel/sys.c.  No return value.

.. This file was automatic generated / don't edit.

