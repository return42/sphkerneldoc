.. -*- coding: utf-8; mode: rst -*-

===============
intel_pmc_ipc.c
===============


.. _`intel_pmc_ipc_simple_command`:

intel_pmc_ipc_simple_command
============================

.. c:function:: int intel_pmc_ipc_simple_command (int cmd, int sub)

    Simple IPC command

    :param int cmd:
        IPC command code.

    :param int sub:
        IPC command sub type.



.. _`intel_pmc_ipc_simple_command.description`:

Description
-----------

Send a simple IPC command to PMC when don't need to specify
input/output data and source/dest pointers.



.. _`intel_pmc_ipc_simple_command.return`:

Return
------

an IPC error code or 0 on success.



.. _`intel_pmc_ipc_raw_cmd`:

intel_pmc_ipc_raw_cmd
=====================

.. c:function:: int intel_pmc_ipc_raw_cmd (u32 cmd, u32 sub, u8 *in, u32 inlen, u32 *out, u32 outlen, u32 dptr, u32 sptr)

    IPC command with data and pointers

    :param u32 cmd:
        IPC command code.

    :param u32 sub:
        IPC command sub type.

    :param u8 \*in:
        input data of this IPC command.

    :param u32 inlen:
        input data length in bytes.

    :param u32 \*out:
        output data of this IPC command.

    :param u32 outlen:
        output data length in dwords.

    :param u32 dptr:
        data writing to DPTR register.

    :param u32 sptr:
        data writing to SPTR register.



.. _`intel_pmc_ipc_raw_cmd.description`:

Description
-----------

Send an IPC command to PMC with input/output data and source/dest pointers.



.. _`intel_pmc_ipc_raw_cmd.return`:

Return
------

an IPC error code or 0 on success.



.. _`intel_pmc_ipc_command`:

intel_pmc_ipc_command
=====================

.. c:function:: int intel_pmc_ipc_command (u32 cmd, u32 sub, u8 *in, u32 inlen, u32 *out, u32 outlen)

    IPC command with input/output data

    :param u32 cmd:
        IPC command code.

    :param u32 sub:
        IPC command sub type.

    :param u8 \*in:
        input data of this IPC command.

    :param u32 inlen:
        input data length in bytes.

    :param u32 \*out:
        output data of this IPC command.

    :param u32 outlen:
        output data length in dwords.



.. _`intel_pmc_ipc_command.description`:

Description
-----------

Send an IPC command to PMC with input/output data.



.. _`intel_pmc_ipc_command.return`:

Return
------

an IPC error code or 0 on success.

