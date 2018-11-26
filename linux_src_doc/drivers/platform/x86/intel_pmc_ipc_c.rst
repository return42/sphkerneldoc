.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/intel_pmc_ipc.c

.. _`intel_pmc_gcr_read`:

intel_pmc_gcr_read
==================

.. c:function:: int intel_pmc_gcr_read(u32 offset, u32 *data)

    Read a 32-bit PMC GCR register

    :param offset:
        offset of GCR register from GCR address base
    :type offset: u32

    :param data:
        data pointer for storing the register output
    :type data: u32 \*

.. _`intel_pmc_gcr_read.description`:

Description
-----------

Reads the 32-bit PMC GCR register at given offset.

.. _`intel_pmc_gcr_read.return`:

Return
------

negative value on error or 0 on success.

.. _`intel_pmc_gcr_read64`:

intel_pmc_gcr_read64
====================

.. c:function:: int intel_pmc_gcr_read64(u32 offset, u64 *data)

    Read a 64-bit PMC GCR register

    :param offset:
        offset of GCR register from GCR address base
    :type offset: u32

    :param data:
        data pointer for storing the register output
    :type data: u64 \*

.. _`intel_pmc_gcr_read64.description`:

Description
-----------

Reads the 64-bit PMC GCR register at given offset.

.. _`intel_pmc_gcr_read64.return`:

Return
------

negative value on error or 0 on success.

.. _`intel_pmc_gcr_write`:

intel_pmc_gcr_write
===================

.. c:function:: int intel_pmc_gcr_write(u32 offset, u32 data)

    Write PMC GCR register

    :param offset:
        offset of GCR register from GCR address base
    :type offset: u32

    :param data:
        register update value
    :type data: u32

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

    :param offset:
        offset of GCR register from GCR address base
    :type offset: u32

    :param mask:
        bit mask for update operation
    :type mask: u32

    :param val:
        update value
    :type val: u32

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

    :param cmd:
        IPC command code.
    :type cmd: int

    :param sub:
        IPC command sub type.
    :type sub: int

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

    :param cmd:
        IPC command code.
    :type cmd: u32

    :param sub:
        IPC command sub type.
    :type sub: u32

    :param in:
        input data of this IPC command.
    :type in: u8 \*

    :param inlen:
        input data length in bytes.
    :type inlen: u32

    :param out:
        output data of this IPC command.
    :type out: u32 \*

    :param outlen:
        output data length in dwords.
    :type outlen: u32

    :param dptr:
        data writing to DPTR register.
    :type dptr: u32

    :param sptr:
        data writing to SPTR register.
    :type sptr: u32

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

    :param cmd:
        IPC command code.
    :type cmd: u32

    :param sub:
        IPC command sub type.
    :type sub: u32

    :param in:
        input data of this IPC command.
    :type in: u8 \*

    :param inlen:
        input data length in bytes.
    :type inlen: u32

    :param out:
        output data of this IPC command.
    :type out: u32 \*

    :param outlen:
        output data length in dwords.
    :type outlen: u32

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

    :param data:
        Out param that contains current S0ix residency count.
    :type data: u64 \*

.. _`intel_pmc_s0ix_counter_read.return`:

Return
------

an error code or 0 on success.

.. This file was automatic generated / don't edit.

