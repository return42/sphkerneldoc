.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/kernel/sh_bios.c

.. _`sh_bios_vbr_reload`:

sh_bios_vbr_reload
==================

.. c:function:: void sh_bios_vbr_reload( void)

    Re-load the system VBR from the BIOS vector.

    :param void:
        no arguments
    :type void: 

.. _`sh_bios_vbr_reload.description`:

Description
-----------

This can be used by save/restore code to reinitialize the system VBR
from the fixed BIOS VBR. A no-op if no BIOS VBR is known.

.. This file was automatic generated / don't edit.

