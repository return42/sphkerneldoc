.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/intel_pmc_ipc.c

.. _`intel_pmc_gcr_read`:

intel_pmc_gcr_read
==================

.. c:function:: int intel_pmc_gcr_read(u32 offset, u32 *data)

    Read PMC GCR register

    :param u32 offset:
        offset of GCR register from GCR address base

    :param u32 \*data:
        data pointer for storing the register output

.. _`intel_pmc_gcr_read.description`:

Description
-----------

Reads the PMC GCR register of given offset.

.. _`intel_pmc_gcr_read.return`:

Return
------

negative value on error or 0 on success.

.. _`intel_pmc_gcr_write`:

intel_pmc_gcr_write
===================

.. c:function:: int intel_pmc_gcr_write(u32 offset, u32 data)

    Write PMC GCR register

    :param u32 offset:
        offset of GCR register from GCR address base

    :param u32 data:
        register update value

.. _`intel_pmc_gcr_write.description`:

Description
-----------

Writes the PMC GCR register of given offset with given
value.

.. _`intel_pmc_gcr_write.return`:

Return
------

negative value on error or 0 on success.

.. _`intel_pmc_gcr_update`:

intel_pmc_gcr_update
====================

.. c:function:: int intel_pmc_gcr_update(u32 offset, u32 mask, u32 val)

    Update PMC GCR register bits

    :param u32 offset:
        offset of GCR register from GCR address base

    :param u32 mask:
        bit mask for update operation

    :param u32 val:
        update value

.. _`intel_pmc_gcr_update.description`:

Description
-----------

Updates the bits of given GCR register as specified by
\ ``mask``\  and \ ``val``\ .

.. _`intel_pmc_gcr_update.return`:

Return
------

negative value on error or 0 on success.

.. _`intel_pmc_ipc_simple_command`:

intel_pmc_ipc_simple_command
============================

.. c:function:: int intel_pmc_ipc_simple_command(int cmd, int sub)

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

.. c:function:: int intel_pmc_ipc_raw_cmd(u32 cmd, u32 sub, u8 *in, u32 inlen, u32 *out, u32 outlen, u32 dptr, u32 sptr)

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

.. c:function:: int intel_pmc_ipc_command(u32 cmd, u32 sub, u8 *in, u32 inlen, u32 *out, u32 outlen)

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

.. _`intel_pmc_s0ix_counter_read`:

intel_pmc_s0ix_counter_read
===========================

.. c:function:: int intel_pmc_s0ix_counter_read(u64 *data)

    Read S0ix residency.

    :param u64 \*data:
        Out param that contains current S0ix residency count.

.. _`intel_pmc_s0ix_counter_read.return`:

Return
------

an error code or 0 on success.

.. This file was automatic generated / don't edit.

