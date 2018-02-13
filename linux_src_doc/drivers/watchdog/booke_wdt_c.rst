.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/booke_wdt.c

.. _`__booke_wdt_disable`:

\__booke_wdt_disable
====================

.. c:function:: void __booke_wdt_disable(void *data)

    disable the watchdog on the given CPU

    :param void \*data:
        *undescribed*

.. _`__booke_wdt_disable.description`:

Description
-----------

This function is called on each CPU.  It disables the watchdog on that CPU.

TCR[WRC] cannot be changed once it has been set to non-zero, but we can
effectively disable the watchdog by setting its period to the maximum value.

.. This file was automatic generated / don't edit.

