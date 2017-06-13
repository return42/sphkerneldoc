.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/intel_scu_ipc.c

.. _`intel_scu_ipc_ioread8`:

intel_scu_ipc_ioread8
=====================

.. c:function:: int intel_scu_ipc_ioread8(u16 addr, u8 *data)

    read a word via the SCU

    :param u16 addr:
        register on SCU

    :param u8 \*data:
        return pointer for read byte

.. _`intel_scu_ipc_ioread8.description`:

Description
-----------

Read a single register. Returns 0 on success or an error code. All
locking between SCU accesses is handled for the caller.

This function may sleep.

.. _`intel_scu_ipc_ioread16`:

intel_scu_ipc_ioread16
======================

.. c:function:: int intel_scu_ipc_ioread16(u16 addr, u16 *data)

    read a word via the SCU

    :param u16 addr:
        register on SCU

    :param u16 \*data:
        return pointer for read word

.. _`intel_scu_ipc_ioread16.description`:

Description
-----------

Read a register pair. Returns 0 on success or an error code. All
locking between SCU accesses is handled for the caller.

This function may sleep.

.. _`intel_scu_ipc_ioread32`:

intel_scu_ipc_ioread32
======================

.. c:function:: int intel_scu_ipc_ioread32(u16 addr, u32 *data)

    read a dword via the SCU

    :param u16 addr:
        register on SCU

    :param u32 \*data:
        return pointer for read dword

.. _`intel_scu_ipc_ioread32.description`:

Description
-----------

Read four registers. Returns 0 on success or an error code. All
locking between SCU accesses is handled for the caller.

This function may sleep.

.. _`intel_scu_ipc_iowrite8`:

intel_scu_ipc_iowrite8
======================

.. c:function:: int intel_scu_ipc_iowrite8(u16 addr, u8 data)

    write a byte via the SCU

    :param u16 addr:
        register on SCU

    :param u8 data:
        byte to write

.. _`intel_scu_ipc_iowrite8.description`:

Description
-----------

Write a single register. Returns 0 on success or an error code. All
locking between SCU accesses is handled for the caller.

This function may sleep.

.. _`intel_scu_ipc_iowrite16`:

intel_scu_ipc_iowrite16
=======================

.. c:function:: int intel_scu_ipc_iowrite16(u16 addr, u16 data)

    write a word via the SCU

    :param u16 addr:
        register on SCU

    :param u16 data:
        word to write

.. _`intel_scu_ipc_iowrite16.description`:

Description
-----------

Write two registers. Returns 0 on success or an error code. All
locking between SCU accesses is handled for the caller.

This function may sleep.

.. _`intel_scu_ipc_iowrite32`:

intel_scu_ipc_iowrite32
=======================

.. c:function:: int intel_scu_ipc_iowrite32(u16 addr, u32 data)

    write a dword via the SCU

    :param u16 addr:
        register on SCU

    :param u32 data:
        dword to write

.. _`intel_scu_ipc_iowrite32.description`:

Description
-----------

Write four registers. Returns 0 on success or an error code. All
locking between SCU accesses is handled for the caller.

This function may sleep.

.. _`intel_scu_ipc_readv`:

intel_scu_ipc_readv
===================

.. c:function:: int intel_scu_ipc_readv(u16 *addr, u8 *data, int len)

    read a set of registers

    :param u16 \*addr:
        register list

    :param u8 \*data:
        bytes to return

    :param int len:
        length of array

.. _`intel_scu_ipc_readv.description`:

Description
-----------

Read registers. Returns 0 on success or an error code. All
locking between SCU accesses is handled for the caller.

The largest array length permitted by the hardware is 5 items.

This function may sleep.

.. _`intel_scu_ipc_writev`:

intel_scu_ipc_writev
====================

.. c:function:: int intel_scu_ipc_writev(u16 *addr, u8 *data, int len)

    write a set of registers

    :param u16 \*addr:
        register list

    :param u8 \*data:
        bytes to write

    :param int len:
        length of array

.. _`intel_scu_ipc_writev.description`:

Description
-----------

Write registers. Returns 0 on success or an error code. All
locking between SCU accesses is handled for the caller.

The largest array length permitted by the hardware is 5 items.

This function may sleep.

.. _`intel_scu_ipc_update_register`:

intel_scu_ipc_update_register
=============================

.. c:function:: int intel_scu_ipc_update_register(u16 addr, u8 bits, u8 mask)

    r/m/w a register

    :param u16 addr:
        register address

    :param u8 bits:
        bits to update

    :param u8 mask:
        mask of bits to update

.. _`intel_scu_ipc_update_register.description`:

Description
-----------

Read-modify-write power control unit register. The first data argument
must be register value and second is mask value
mask is a bitmap that indicates which bits to update.
0 = masked. Don't modify this bit, 1 = modify this bit.
returns 0 on success or an error code.

This function may sleep. Locking between SCU accesses is handled
for the caller.

.. _`intel_scu_ipc_simple_command`:

intel_scu_ipc_simple_command
============================

.. c:function:: int intel_scu_ipc_simple_command(int cmd, int sub)

    send a simple command

    :param int cmd:
        command

    :param int sub:
        sub type

.. _`intel_scu_ipc_simple_command.description`:

Description
-----------

Issue a simple command to the SCU. Do not use this interface if
you must then access data as any data values may be overwritten
by another SCU access by the time this function returns.

This function may sleep. Locking for SCU accesses is handled for
the caller.

.. _`intel_scu_ipc_command`:

intel_scu_ipc_command
=====================

.. c:function:: int intel_scu_ipc_command(int cmd, int sub, u32 *in, int inlen, u32 *out, int outlen)

    command with data

    :param int cmd:
        command

    :param int sub:
        sub type

    :param u32 \*in:
        input data

    :param int inlen:
        input length in dwords

    :param u32 \*out:
        output data

    :param int outlen:
        *undescribed*

.. _`intel_scu_ipc_command.description`:

Description
-----------

Issue a command to the SCU which involves data transfers. Do the
data copies under the lock but leave it for the caller to interpret

.. _`intel_scu_ipc_raw_command`:

intel_scu_ipc_raw_command
=========================

.. c:function:: int intel_scu_ipc_raw_command(int cmd, int sub, u8 *in, int inlen, u32 *out, int outlen, u32 dptr, u32 sptr)

    IPC command with data and pointers

    :param int cmd:
        IPC command code.

    :param int sub:
        IPC command sub type.

    :param u8 \*in:
        input data of this IPC command.

    :param int inlen:
        input data length in dwords.

    :param u32 \*out:
        output data of this IPC command.

    :param int outlen:
        output data length in dwords.

    :param u32 dptr:
        data writing to DPTR register.

    :param u32 sptr:
        data writing to SPTR register.

.. _`intel_scu_ipc_raw_command.description`:

Description
-----------

Send an IPC command to SCU with input/output data and source/dest pointers.

.. _`intel_scu_ipc_raw_command.return`:

Return
------

an IPC error code or 0 on success.

.. _`intel_scu_ipc_i2c_cntrl`:

intel_scu_ipc_i2c_cntrl
=======================

.. c:function:: int intel_scu_ipc_i2c_cntrl(u32 addr, u32 *data)

    I2C read/write operations

    :param u32 addr:
        I2C address + command bits

    :param u32 \*data:
        data to read/write

.. _`intel_scu_ipc_i2c_cntrl.description`:

Description
-----------

Perform an an I2C read/write operation via the SCU. All locking is
handled for the caller. This function may sleep.

Returns an error code or 0 on success.

This has to be in the IPC driver for the locking.

.. _`ipc_probe`:

ipc_probe
=========

.. c:function:: int ipc_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    probe an Intel SCU IPC

    :param struct pci_dev \*pdev:
        the PCI device matching

    :param const struct pci_device_id \*id:
        entry in the match table

.. _`ipc_probe.description`:

Description
-----------

Enable and install an intel SCU IPC. This appears in the PCI space
but uses some hard coded addresses as well.

.. This file was automatic generated / don't edit.

