.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/am33xx-restart.c

.. _`am33xx_restart`:

am33xx_restart
==============

.. c:function:: void am33xx_restart(enum reboot_mode mode, const char *cmd)

    trigger a software restart of the SoC

    :param mode:
        the "reboot mode", see arch/arm/kernel/{setup,process}.c
    :type mode: enum reboot_mode

    :param cmd:
        passed from the userspace program rebooting the system (if provided)
    :type cmd: const char \*

.. _`am33xx_restart.description`:

Description
-----------

Resets the SoC.  For \ ``cmd``\ , see the 'reboot' syscall in
kernel/sys.c.  No return value.

.. This file was automatic generated / don't edit.

