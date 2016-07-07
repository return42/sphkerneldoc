.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/sdio_io.c

.. _`sdio_claim_host`:

sdio_claim_host
===============

.. c:function:: void sdio_claim_host(struct sdio_func *func)

    exclusively claim a bus for a certain SDIO function

    :param struct sdio_func \*func:
        SDIO function that will be accessed

.. _`sdio_claim_host.description`:

Description
-----------

Claim a bus for a set of operations. The SDIO function given
is used to figure out which bus is relevant.

.. _`sdio_release_host`:

sdio_release_host
=================

.. c:function:: void sdio_release_host(struct sdio_func *func)

    release a bus for a certain SDIO function

    :param struct sdio_func \*func:
        SDIO function that was accessed

.. _`sdio_release_host.description`:

Description
-----------

Release a bus, allowing others to claim the bus for their
operations.

.. _`sdio_enable_func`:

sdio_enable_func
================

.. c:function:: int sdio_enable_func(struct sdio_func *func)

    enables a SDIO function for usage

    :param struct sdio_func \*func:
        SDIO function to enable

.. _`sdio_enable_func.description`:

Description
-----------

Powers up and activates a SDIO function so that register
access is possible.

.. _`sdio_disable_func`:

sdio_disable_func
=================

.. c:function:: int sdio_disable_func(struct sdio_func *func)

    disable a SDIO function

    :param struct sdio_func \*func:
        SDIO function to disable

.. _`sdio_disable_func.description`:

Description
-----------

Powers down and deactivates a SDIO function. Register access
to this function will fail until the function is reenabled.

.. _`sdio_set_block_size`:

sdio_set_block_size
===================

.. c:function:: int sdio_set_block_size(struct sdio_func *func, unsigned blksz)

    set the block size of an SDIO function

    :param struct sdio_func \*func:
        SDIO function to change

    :param unsigned blksz:
        new block size or 0 to use the default.

.. _`sdio_set_block_size.description`:

Description
-----------

The default block size is the largest supported by both the function
and the host, with a maximum of 512 to ensure that arbitrarily sized
data transfer use the optimal (least) number of commands.

A driver may call this to override the default block size set by the
core. This can be used to set a block size greater than the maximum
that reported by the card; it is the driver's responsibility to ensure
it uses a value that the card supports.

Returns 0 on success, -EINVAL if the host does not support the
requested block size, or -EIO (etc.) if one of the resultant FBR block
size register writes failed.

.. _`sdio_align_size`:

sdio_align_size
===============

.. c:function:: unsigned int sdio_align_size(struct sdio_func *func, unsigned int sz)

    pads a transfer size to a more optimal value

    :param struct sdio_func \*func:
        SDIO function

    :param unsigned int sz:
        original transfer size

.. _`sdio_align_size.description`:

Description
-----------

Pads the original data size with a number of extra bytes in
order to avoid controller bugs and/or performance hits
(e.g. some controllers revert to PIO for certain sizes).

If possible, it will also adjust the size so that it can be
handled in just a single request.

Returns the improved size, which might be unmodified.

.. _`sdio_readb`:

sdio_readb
==========

.. c:function:: u8 sdio_readb(struct sdio_func *func, unsigned int addr, int *err_ret)

    read a single byte from a SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param unsigned int addr:
        address to read

    :param int \*err_ret:
        optional status value from transfer

.. _`sdio_readb.description`:

Description
-----------

Reads a single byte from the address space of a given SDIO
function. If there is a problem reading the address, 0xff
is returned and \ ``err_ret``\  will contain the error code.

.. _`sdio_writeb`:

sdio_writeb
===========

.. c:function:: void sdio_writeb(struct sdio_func *func, u8 b, unsigned int addr, int *err_ret)

    write a single byte to a SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param u8 b:
        byte to write

    :param unsigned int addr:
        address to write to

    :param int \*err_ret:
        optional status value from transfer

.. _`sdio_writeb.description`:

Description
-----------

Writes a single byte to the address space of a given SDIO
function. \ ``err_ret``\  will contain the status of the actual
transfer.

.. _`sdio_writeb_readb`:

sdio_writeb_readb
=================

.. c:function:: u8 sdio_writeb_readb(struct sdio_func *func, u8 write_byte, unsigned int addr, int *err_ret)

    write and read a byte from SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param u8 write_byte:
        byte to write

    :param unsigned int addr:
        address to write to

    :param int \*err_ret:
        optional status value from transfer

.. _`sdio_writeb_readb.description`:

Description
-----------

Performs a RAW (Read after Write) operation as defined by SDIO spec -
single byte is written to address space of a given SDIO function and
response is read back from the same address, both using single request.
If there is a problem with the operation, 0xff is returned and
\ ``err_ret``\  will contain the error code.

.. _`sdio_memcpy_fromio`:

sdio_memcpy_fromio
==================

.. c:function:: int sdio_memcpy_fromio(struct sdio_func *func, void *dst, unsigned int addr, int count)

    read a chunk of memory from a SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param void \*dst:
        buffer to store the data

    :param unsigned int addr:
        address to begin reading from

    :param int count:
        number of bytes to read

.. _`sdio_memcpy_fromio.description`:

Description
-----------

Reads from the address space of a given SDIO function. Return
value indicates if the transfer succeeded or not.

.. _`sdio_memcpy_toio`:

sdio_memcpy_toio
================

.. c:function:: int sdio_memcpy_toio(struct sdio_func *func, unsigned int addr, void *src, int count)

    write a chunk of memory to a SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param unsigned int addr:
        address to start writing to

    :param void \*src:
        buffer that contains the data to write

    :param int count:
        number of bytes to write

.. _`sdio_memcpy_toio.description`:

Description
-----------

Writes to the address space of a given SDIO function. Return
value indicates if the transfer succeeded or not.

.. _`sdio_readsb`:

sdio_readsb
===========

.. c:function:: int sdio_readsb(struct sdio_func *func, void *dst, unsigned int addr, int count)

    read from a FIFO on a SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param void \*dst:
        buffer to store the data

    :param unsigned int addr:
        address of (single byte) FIFO

    :param int count:
        number of bytes to read

.. _`sdio_readsb.description`:

Description
-----------

Reads from the specified FIFO of a given SDIO function. Return
value indicates if the transfer succeeded or not.

.. _`sdio_writesb`:

sdio_writesb
============

.. c:function:: int sdio_writesb(struct sdio_func *func, unsigned int addr, void *src, int count)

    write to a FIFO of a SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param unsigned int addr:
        address of (single byte) FIFO

    :param void \*src:
        buffer that contains the data to write

    :param int count:
        number of bytes to write

.. _`sdio_writesb.description`:

Description
-----------

Writes to the specified FIFO of a given SDIO function. Return
value indicates if the transfer succeeded or not.

.. _`sdio_readw`:

sdio_readw
==========

.. c:function:: u16 sdio_readw(struct sdio_func *func, unsigned int addr, int *err_ret)

    read a 16 bit integer from a SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param unsigned int addr:
        address to read

    :param int \*err_ret:
        optional status value from transfer

.. _`sdio_readw.description`:

Description
-----------

Reads a 16 bit integer from the address space of a given SDIO
function. If there is a problem reading the address, 0xffff
is returned and \ ``err_ret``\  will contain the error code.

.. _`sdio_writew`:

sdio_writew
===========

.. c:function:: void sdio_writew(struct sdio_func *func, u16 b, unsigned int addr, int *err_ret)

    write a 16 bit integer to a SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param u16 b:
        integer to write

    :param unsigned int addr:
        address to write to

    :param int \*err_ret:
        optional status value from transfer

.. _`sdio_writew.description`:

Description
-----------

Writes a 16 bit integer to the address space of a given SDIO
function. \ ``err_ret``\  will contain the status of the actual
transfer.

.. _`sdio_readl`:

sdio_readl
==========

.. c:function:: u32 sdio_readl(struct sdio_func *func, unsigned int addr, int *err_ret)

    read a 32 bit integer from a SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param unsigned int addr:
        address to read

    :param int \*err_ret:
        optional status value from transfer

.. _`sdio_readl.description`:

Description
-----------

Reads a 32 bit integer from the address space of a given SDIO
function. If there is a problem reading the address,
0xffffffff is returned and \ ``err_ret``\  will contain the error
code.

.. _`sdio_writel`:

sdio_writel
===========

.. c:function:: void sdio_writel(struct sdio_func *func, u32 b, unsigned int addr, int *err_ret)

    write a 32 bit integer to a SDIO function

    :param struct sdio_func \*func:
        SDIO function to access

    :param u32 b:
        integer to write

    :param unsigned int addr:
        address to write to

    :param int \*err_ret:
        optional status value from transfer

.. _`sdio_writel.description`:

Description
-----------

Writes a 32 bit integer to the address space of a given SDIO
function. \ ``err_ret``\  will contain the status of the actual
transfer.

.. _`sdio_f0_readb`:

sdio_f0_readb
=============

.. c:function:: unsigned char sdio_f0_readb(struct sdio_func *func, unsigned int addr, int *err_ret)

    read a single byte from SDIO function 0

    :param struct sdio_func \*func:
        an SDIO function of the card

    :param unsigned int addr:
        address to read

    :param int \*err_ret:
        optional status value from transfer

.. _`sdio_f0_readb.description`:

Description
-----------

Reads a single byte from the address space of SDIO function 0.
If there is a problem reading the address, 0xff is returned
and \ ``err_ret``\  will contain the error code.

.. _`sdio_f0_writeb`:

sdio_f0_writeb
==============

.. c:function:: void sdio_f0_writeb(struct sdio_func *func, unsigned char b, unsigned int addr, int *err_ret)

    write a single byte to SDIO function 0

    :param struct sdio_func \*func:
        an SDIO function of the card

    :param unsigned char b:
        byte to write

    :param unsigned int addr:
        address to write to

    :param int \*err_ret:
        optional status value from transfer

.. _`sdio_f0_writeb.description`:

Description
-----------

Writes a single byte to the address space of SDIO function 0.
\ ``err_ret``\  will contain the status of the actual transfer.

Only writes to the vendor specific CCCR registers (0xF0 -
0xFF) are permiited; \ ``err_ret``\  will be set to -EINVAL for \*
writes outside this range.

.. _`sdio_get_host_pm_caps`:

sdio_get_host_pm_caps
=====================

.. c:function:: mmc_pm_flag_t sdio_get_host_pm_caps(struct sdio_func *func)

    get host power management capabilities

    :param struct sdio_func \*func:
        SDIO function attached to host

.. _`sdio_get_host_pm_caps.description`:

Description
-----------

Returns a capability bitmask corresponding to power management
features supported by the host controller that the card function
might rely upon during a system suspend.  The host doesn't need
to be claimed, nor the function active, for this information to be
obtained.

.. _`sdio_set_host_pm_flags`:

sdio_set_host_pm_flags
======================

.. c:function:: int sdio_set_host_pm_flags(struct sdio_func *func, mmc_pm_flag_t flags)

    set wanted host power management capabilities

    :param struct sdio_func \*func:
        SDIO function attached to host

    :param mmc_pm_flag_t flags:
        *undescribed*

.. _`sdio_set_host_pm_flags.description`:

Description
-----------

Set a capability bitmask corresponding to wanted host controller
power management features for the upcoming suspend state.
This must be called, if needed, each time the suspend method of
the function driver is called, and must contain only bits that
were returned by \ :c:func:`sdio_get_host_pm_caps`\ .
The host doesn't need to be claimed, nor the function active,
for this information to be set.

.. This file was automatic generated / don't edit.

