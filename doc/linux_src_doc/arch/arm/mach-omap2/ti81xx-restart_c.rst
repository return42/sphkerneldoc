.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/ti81xx-restart.c

.. _`ti81xx_restart`:

ti81xx_restart
==============

.. c:function:: void ti81xx_restart(enum reboot_mode mode, const char *cmd)

    trigger a software restart of the SoC

    :param enum reboot_mode mode:
        the "reboot mode", see arch/arm/kernel/{setup,process}.c

    :param const char \*cmd:
        passed from the userspace program rebooting the system (if provided)

.. _`ti81xx_restart.description`:

Description
-----------

Resets the SoC.  For \ ``cmd``\ , see the 'reboot' syscall in
kernel/sys.c.  No return value.

.. _`ti81xx_restart.note`:

NOTE
----

Warm reset does not seem to work, may require resetting
clocks to bypass mode.

.. This file was automatic generated / don't edit.

