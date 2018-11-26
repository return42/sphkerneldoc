.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/intel_punit_ipc.c

.. _`intel_punit_ipc_simple_command`:

intel_punit_ipc_simple_command
==============================

.. c:function:: int intel_punit_ipc_simple_command(int cmd, int para1, int para2)

    Simple IPC command

    :param cmd:
        IPC command code.
    :type cmd: int

    :param para1:
        First 8bit parameter, set 0 if not used.
    :type para1: int

    :param para2:
        Second 8bit parameter, set 0 if not used.
    :type para2: int

.. _`intel_punit_ipc_simple_command.description`:

Description
-----------

Send a IPC command to P-Unit when there is no data transaction

.. _`intel_punit_ipc_simple_command.return`:

Return
------

IPC error code or 0 on success.

.. _`intel_punit_ipc_command`:

intel_punit_ipc_command
=======================

.. c:function:: int intel_punit_ipc_command(u32 cmd, u32 para1, u32 para2, u32 *in, u32 *out)

    IPC command with data and pointers

    :param cmd:
        IPC command code.
    :type cmd: u32

    :param para1:
        First 8bit parameter, set 0 if not used.
    :type para1: u32

    :param para2:
        Second 8bit parameter, set 0 if not used.
    :type para2: u32

    :param in:
        Input data, 32bit for BIOS cmd, two 32bit for GTD and ISPD.
    :type in: u32 \*

    :param out:
        Output data.
    :type out: u32 \*

.. _`intel_punit_ipc_command.description`:

Description
-----------

Send a IPC command to P-Unit with data transaction

.. _`intel_punit_ipc_command.return`:

Return
------

IPC error code or 0 on success.

.. This file was automatic generated / don't edit.

