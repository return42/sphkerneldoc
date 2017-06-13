.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi.c

.. _`__spi_register_driver`:

__spi_register_driver
=====================

.. c:function:: int __spi_register_driver(struct module *owner, struct spi_driver *sdrv)

    register a SPI driver

    :param struct module \*owner:
        owner module of the driver to register

    :param struct spi_driver \*sdrv:
        the driver to register

.. _`__spi_register_driver.context`:

Context
-------

can sleep

.. _`__spi_register_driver.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_alloc_device`:

spi_alloc_device
================

.. c:function:: struct spi_device *spi_alloc_device(struct spi_master *master)

    Allocate a new SPI device

    :param struct spi_master \*master:
        Controller to which device is connected

.. _`spi_alloc_device.context`:

Context
-------

can sleep

.. _`spi_alloc_device.description`:

Description
-----------

Allows a driver to allocate and initialize a spi_device without
registering it immediately.  This allows a driver to directly
fill the spi_device with device parameters before calling
\ :c:func:`spi_add_device`\  on it.

Caller is responsible to call \ :c:func:`spi_add_device`\  on the returned
spi_device structure to add it to the SPI master.  If the caller
needs to discard the spi_device without adding it, then it should
call \ :c:func:`spi_dev_put`\  on it.

.. _`spi_alloc_device.return`:

Return
------

a pointer to the new device, or NULL.

.. _`spi_add_device`:

spi_add_device
==============

.. c:function:: int spi_add_device(struct spi_device *spi)

    Add spi_device allocated with spi_alloc_device

    :param struct spi_device \*spi:
        spi_device to register

.. _`spi_add_device.description`:

Description
-----------

Companion function to spi_alloc_device.  Devices allocated with
spi_alloc_device can be added onto the spi bus with this function.

.. _`spi_add_device.return`:

Return
------

0 on success; negative errno on failure

.. _`spi_new_device`:

spi_new_device
==============

.. c:function:: struct spi_device *spi_new_device(struct spi_master *master, struct spi_board_info *chip)

    instantiate one new SPI device

    :param struct spi_master \*master:
        Controller to which device is connected

    :param struct spi_board_info \*chip:
        Describes the SPI device

.. _`spi_new_device.context`:

Context
-------

can sleep

.. _`spi_new_device.description`:

Description
-----------

On typical mainboards, this is purely internal; and it's not needed
after board init creates the hard-wired devices.  Some development
platforms may not be able to use spi_register_board_info though, and
this is exported so that for example a USB or parport based adapter
driver could add devices (which it would learn about out-of-band).

.. _`spi_new_device.return`:

Return
------

the new device, or NULL.

.. _`spi_unregister_device`:

spi_unregister_device
=====================

.. c:function:: void spi_unregister_device(struct spi_device *spi)

    unregister a single SPI device

    :param struct spi_device \*spi:
        spi_device to unregister

.. _`spi_unregister_device.description`:

Description
-----------

Start making the passed SPI device vanish. Normally this would be handled
by \ :c:func:`spi_unregister_master`\ .

.. _`spi_register_board_info`:

spi_register_board_info
=======================

.. c:function:: int spi_register_board_info(struct spi_board_info const *info, unsigned n)

    register SPI devices for a given board

    :param struct spi_board_info const \*info:
        array of chip descriptors

    :param unsigned n:
        how many descriptors are provided

.. _`spi_register_board_info.context`:

Context
-------

can sleep

.. _`spi_register_board_info.description`:

Description
-----------

Board-specific early init code calls this (probably during arch_initcall)
with segments of the SPI device table.  Any device nodes are created later,
after the relevant parent SPI controller (bus_num) is defined.  We keep
this table of devices forever, so that reloading a controller driver will
not make Linux forget about these hard-wired devices.

Other code can also call this, e.g. a particular add-on board might provide
SPI devices through its expansion connector, so code initializing that board
would naturally declare its SPI devices.

The board info passed can safely be __initdata ... but be careful of
any embedded pointers (platform_data, etc), they're copied as-is.
Device properties are deep-copied though.

.. _`spi_register_board_info.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_finalize_current_transfer`:

spi_finalize_current_transfer
=============================

.. c:function:: void spi_finalize_current_transfer(struct spi_master *master)

    report completion of a transfer

    :param struct spi_master \*master:
        the master reporting completion

.. _`spi_finalize_current_transfer.description`:

Description
-----------

Called by SPI drivers using the core \ :c:func:`transfer_one_message`\ 
implementation to notify it that the current interrupt driven
transfer has finished and the next one may be scheduled.

.. _`__spi_pump_messages`:

__spi_pump_messages
===================

.. c:function:: void __spi_pump_messages(struct spi_master *master, bool in_kthread)

    function which processes spi message queue

    :param struct spi_master \*master:
        master to process queue for

    :param bool in_kthread:
        true if we are in the context of the message pump thread

.. _`__spi_pump_messages.description`:

Description
-----------

This function checks if there is any spi message in the queue that
needs processing and if so call out to the driver to initialize hardware
and transfer each message.

Note that it is called both from the kthread itself and also from
inside \ :c:func:`spi_sync`\ ; the queue extraction handling at the top of the
function should deal with this safely.

.. _`spi_pump_messages`:

spi_pump_messages
=================

.. c:function:: void spi_pump_messages(struct kthread_work *work)

    kthread work function which processes spi message queue

    :param struct kthread_work \*work:
        pointer to kthread work struct contained in the master struct

.. _`spi_get_next_queued_message`:

spi_get_next_queued_message
===========================

.. c:function:: struct spi_message *spi_get_next_queued_message(struct spi_master *master)

    called by driver to check for queued messages

    :param struct spi_master \*master:
        the master to check for queued messages

.. _`spi_get_next_queued_message.description`:

Description
-----------

If there are more messages in the queue, the next message is returned from
this call.

.. _`spi_get_next_queued_message.return`:

Return
------

the next message in the queue, else NULL if the queue is empty.

.. _`spi_finalize_current_message`:

spi_finalize_current_message
============================

.. c:function:: void spi_finalize_current_message(struct spi_master *master)

    the current message is complete

    :param struct spi_master \*master:
        the master to return the message to

.. _`spi_finalize_current_message.description`:

Description
-----------

Called by the driver to notify the core that the message in the front of the
queue is complete and can be removed from the queue.

.. _`spi_queued_transfer`:

spi_queued_transfer
===================

.. c:function:: int spi_queued_transfer(struct spi_device *spi, struct spi_message *msg)

    transfer function for queued transfers

    :param struct spi_device \*spi:
        spi device which is requesting transfer

    :param struct spi_message \*msg:
        spi message which is to handled is queued to driver queue

.. _`spi_queued_transfer.return`:

Return
------

zero on success, else a negative error code.

.. _`of_register_spi_devices`:

of_register_spi_devices
=======================

.. c:function:: void of_register_spi_devices(struct spi_master *master)

    Register child devices onto the SPI bus

    :param struct spi_master \*master:
        Pointer to spi_master device

.. _`of_register_spi_devices.description`:

Description
-----------

Registers an spi_device for each child node of master node which has a 'reg'
property.

.. _`spi_alloc_master`:

spi_alloc_master
================

.. c:function:: struct spi_master *spi_alloc_master(struct device *dev, unsigned size)

    allocate SPI master controller

    :param struct device \*dev:
        the controller, possibly using the platform_bus

    :param unsigned size:
        how much zeroed driver-private data to allocate; the pointer to this
        memory is in the driver_data field of the returned device,
        accessible with \ :c:func:`spi_master_get_devdata`\ .

.. _`spi_alloc_master.context`:

Context
-------

can sleep

.. _`spi_alloc_master.description`:

Description
-----------

This call is used only by SPI master controller drivers, which are the
only ones directly touching chip registers.  It's how they allocate
an spi_master structure, prior to calling \ :c:func:`spi_register_master`\ .

This must be called from context that can sleep.

The caller is responsible for assigning the bus number and initializing
the master's methods before calling \ :c:func:`spi_register_master`\ ; and (after errors
adding the device) calling \ :c:func:`spi_master_put`\  to prevent a memory leak.

.. _`spi_alloc_master.return`:

Return
------

the SPI master structure on success, else NULL.

.. _`spi_register_master`:

spi_register_master
===================

.. c:function:: int spi_register_master(struct spi_master *master)

    register SPI master controller

    :param struct spi_master \*master:
        initialized master, originally from \ :c:func:`spi_alloc_master`\ 

.. _`spi_register_master.context`:

Context
-------

can sleep

.. _`spi_register_master.description`:

Description
-----------

SPI master controllers connect to their drivers using some non-SPI bus,
such as the platform bus.  The final stage of \ :c:func:`probe`\  in that code
includes calling \ :c:func:`spi_register_master`\  to hook up to this SPI bus glue.

SPI controllers use board specific (often SOC specific) bus numbers,
and board-specific addressing for SPI devices combines those numbers
with chip select numbers.  Since SPI does not directly support dynamic
device identification, boards need configuration tables telling which
chip is at which address.

This must be called from context that can sleep.  It returns zero on
success, else a negative error code (dropping the master's refcount).
After a successful return, the caller is responsible for calling
\ :c:func:`spi_unregister_master`\ .

.. _`spi_register_master.return`:

Return
------

zero on success, else a negative error code.

.. _`devm_spi_register_master`:

devm_spi_register_master
========================

.. c:function:: int devm_spi_register_master(struct device *dev, struct spi_master *master)

    register managed SPI master controller

    :param struct device \*dev:
        device managing SPI master

    :param struct spi_master \*master:
        initialized master, originally from \ :c:func:`spi_alloc_master`\ 

.. _`devm_spi_register_master.context`:

Context
-------

can sleep

.. _`devm_spi_register_master.description`:

Description
-----------

Register a SPI device as with \ :c:func:`spi_register_master`\  which will
automatically be unregister

.. _`devm_spi_register_master.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_unregister_master`:

spi_unregister_master
=====================

.. c:function:: void spi_unregister_master(struct spi_master *master)

    unregister SPI master controller

    :param struct spi_master \*master:
        the master being unregistered

.. _`spi_unregister_master.context`:

Context
-------

can sleep

.. _`spi_unregister_master.description`:

Description
-----------

This call is used only by SPI master controller drivers, which are the
only ones directly touching chip registers.

This must be called from context that can sleep.

.. _`spi_busnum_to_master`:

spi_busnum_to_master
====================

.. c:function:: struct spi_master *spi_busnum_to_master(u16 bus_num)

    look up master associated with bus_num

    :param u16 bus_num:
        the master's bus number

.. _`spi_busnum_to_master.context`:

Context
-------

can sleep

.. _`spi_busnum_to_master.description`:

Description
-----------

This call may be used with devices that are registered after
arch init time.  It returns a refcounted pointer to the relevant
spi_master (which the caller must release), or NULL if there is
no such master registered.

.. _`spi_busnum_to_master.return`:

Return
------

the SPI master structure on success, else NULL.

.. _`spi_res_alloc`:

spi_res_alloc
=============

.. c:function:: void *spi_res_alloc(struct spi_device *spi, spi_res_release_t release, size_t size, gfp_t gfp)

    allocate a spi resource that is life-cycle managed during the processing of a spi_message while using spi_transfer_one

    :param struct spi_device \*spi:
        the spi device for which we allocate memory

    :param spi_res_release_t release:
        the release code to execute for this resource

    :param size_t size:
        size to alloc and return

    :param gfp_t gfp:
        GFP allocation flags

.. _`spi_res_alloc.return`:

Return
------

the pointer to the allocated data

This may get enhanced in the future to allocate from a memory pool
of the \ ``spi_device``\  or \ ``spi_master``\  to avoid repeated allocations.

.. _`spi_res_free`:

spi_res_free
============

.. c:function:: void spi_res_free(void *res)

    free an spi resource

    :param void \*res:
        pointer to the custom data of a resource

.. _`spi_res_add`:

spi_res_add
===========

.. c:function:: void spi_res_add(struct spi_message *message, void *res)

    add a spi_res to the spi_message

    :param struct spi_message \*message:
        the spi message

    :param void \*res:
        the spi_resource

.. _`spi_res_release`:

spi_res_release
===============

.. c:function:: void spi_res_release(struct spi_master *master, struct spi_message *message)

    release all spi resources for this message

    :param struct spi_master \*master:
        the \ ``spi_master``\ 

    :param struct spi_message \*message:
        the \ ``spi_message``\ 

.. _`spi_replace_transfers`:

spi_replace_transfers
=====================

.. c:function:: struct spi_replaced_transfers *spi_replace_transfers(struct spi_message *msg, struct spi_transfer *xfer_first, size_t remove, size_t insert, spi_replaced_release_t release, size_t extradatasize, gfp_t gfp)

    replace transfers with several transfers and register change with spi_message.resources

    :param struct spi_message \*msg:
        the spi_message we work upon

    :param struct spi_transfer \*xfer_first:
        the first spi_transfer we want to replace

    :param size_t remove:
        number of transfers to remove

    :param size_t insert:
        the number of transfers we want to insert instead

    :param spi_replaced_release_t release:
        extra release code necessary in some circumstances

    :param size_t extradatasize:
        extra data to allocate (with alignment guarantees
        of struct \ ``spi_transfer``\ )

    :param gfp_t gfp:
        gfp flags

.. _`spi_replace_transfers.return`:

Return
------

pointer to \ ``spi_replaced_transfers``\ ,
         PTR_ERR(...) in case of errors.

.. _`spi_split_transfers_maxsize`:

spi_split_transfers_maxsize
===========================

.. c:function:: int spi_split_transfers_maxsize(struct spi_master *master, struct spi_message *msg, size_t maxsize, gfp_t gfp)

    split spi transfers into multiple transfers when an individual transfer exceeds a certain size

    :param struct spi_master \*master:
        the \ ``spi_master``\  for this transfer

    :param struct spi_message \*msg:
        the \ ``spi_message``\  to transform

    :param size_t maxsize:
        the maximum when to apply this

    :param gfp_t gfp:
        GFP allocation flags

.. _`spi_split_transfers_maxsize.return`:

Return
------

status of transformation

.. _`spi_setup`:

spi_setup
=========

.. c:function:: int spi_setup(struct spi_device *spi)

    setup SPI mode and clock rate

    :param struct spi_device \*spi:
        the device whose settings are being modified

.. _`spi_setup.context`:

Context
-------

can sleep, and no requests are queued to the device

.. _`spi_setup.description`:

Description
-----------

SPI protocol drivers may need to update the transfer mode if the
device doesn't work with its default.  They may likewise need
to update clock rates or word sizes from initial values.  This function
changes those settings, and must be called from a context that can sleep.
Except for SPI_CS_HIGH, which takes effect immediately, the changes take
effect the next time the device is selected and data is transferred to
or from it.  When this function returns, the spi device is deselected.

Note that this call will fail if the protocol driver specifies an option
that the underlying controller or its driver does not support.  For
example, not all hardware supports wire transfers using nine bit words,
LSB-first wire encoding, or active-high chipselects.

.. _`spi_setup.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_async`:

spi_async
=========

.. c:function:: int spi_async(struct spi_device *spi, struct spi_message *message)

    asynchronous SPI transfer

    :param struct spi_device \*spi:
        device with which data will be exchanged

    :param struct spi_message \*message:
        describes the data transfers, including completion callback

.. _`spi_async.context`:

Context
-------

any (irqs may be blocked, etc)

.. _`spi_async.description`:

Description
-----------

This call may be used in_irq and other contexts which can't sleep,
as well as from task contexts which can sleep.

The completion callback is invoked in a context which can't sleep.
Before that invocation, the value of message->status is undefined.
When the callback is issued, message->status holds either zero (to
indicate complete success) or a negative error code.  After that
callback returns, the driver which issued the transfer request may
deallocate the associated memory; it's no longer in use by any SPI
core or controller driver code.

Note that although all messages to a spi_device are handled in
FIFO order, messages may go to different devices in other orders.
Some device might be higher priority, or have various "hard" access
time requirements, for example.

On detection of any fault during the transfer, processing of
the entire message is aborted, and the device is deselected.
Until returning from the associated message completion callback,
no other spi_message queued to that device will be processed.
(This rule applies equally to all the synchronous transfer calls,
which are wrappers around this core asynchronous primitive.)

.. _`spi_async.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_async_locked`:

spi_async_locked
================

.. c:function:: int spi_async_locked(struct spi_device *spi, struct spi_message *message)

    version of spi_async with exclusive bus usage

    :param struct spi_device \*spi:
        device with which data will be exchanged

    :param struct spi_message \*message:
        describes the data transfers, including completion callback

.. _`spi_async_locked.context`:

Context
-------

any (irqs may be blocked, etc)

.. _`spi_async_locked.description`:

Description
-----------

This call may be used in_irq and other contexts which can't sleep,
as well as from task contexts which can sleep.

The completion callback is invoked in a context which can't sleep.
Before that invocation, the value of message->status is undefined.
When the callback is issued, message->status holds either zero (to
indicate complete success) or a negative error code.  After that
callback returns, the driver which issued the transfer request may
deallocate the associated memory; it's no longer in use by any SPI
core or controller driver code.

Note that although all messages to a spi_device are handled in
FIFO order, messages may go to different devices in other orders.
Some device might be higher priority, or have various "hard" access
time requirements, for example.

On detection of any fault during the transfer, processing of
the entire message is aborted, and the device is deselected.
Until returning from the associated message completion callback,
no other spi_message queued to that device will be processed.
(This rule applies equally to all the synchronous transfer calls,
which are wrappers around this core asynchronous primitive.)

.. _`spi_async_locked.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_sync`:

spi_sync
========

.. c:function:: int spi_sync(struct spi_device *spi, struct spi_message *message)

    blocking/synchronous SPI data transfers

    :param struct spi_device \*spi:
        device with which data will be exchanged

    :param struct spi_message \*message:
        describes the data transfers

.. _`spi_sync.context`:

Context
-------

can sleep

.. _`spi_sync.description`:

Description
-----------

This call may only be used from a context that may sleep.  The sleep
is non-interruptible, and has no timeout.  Low-overhead controller
drivers may DMA directly into and out of the message buffers.

Note that the SPI device's chip select is active during the message,
and then is normally disabled between messages.  Drivers for some
frequently-used devices may want to minimize costs of selecting a chip,
by leaving it selected in anticipation that the next message will go
to the same chip.  (That may increase power usage.)

Also, the caller is guaranteeing that the memory associated with the
message will not be freed before this call returns.

.. _`spi_sync.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_sync_locked`:

spi_sync_locked
===============

.. c:function:: int spi_sync_locked(struct spi_device *spi, struct spi_message *message)

    version of spi_sync with exclusive bus usage

    :param struct spi_device \*spi:
        device with which data will be exchanged

    :param struct spi_message \*message:
        describes the data transfers

.. _`spi_sync_locked.context`:

Context
-------

can sleep

.. _`spi_sync_locked.description`:

Description
-----------

This call may only be used from a context that may sleep.  The sleep
is non-interruptible, and has no timeout.  Low-overhead controller
drivers may DMA directly into and out of the message buffers.

This call should be used by drivers that require exclusive access to the
SPI bus. It has to be preceded by a spi_bus_lock call. The SPI bus must
be released by a spi_bus_unlock call when the exclusive access is over.

.. _`spi_sync_locked.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_bus_lock`:

spi_bus_lock
============

.. c:function:: int spi_bus_lock(struct spi_master *master)

    obtain a lock for exclusive SPI bus usage

    :param struct spi_master \*master:
        SPI bus master that should be locked for exclusive bus access

.. _`spi_bus_lock.context`:

Context
-------

can sleep

.. _`spi_bus_lock.description`:

Description
-----------

This call may only be used from a context that may sleep.  The sleep
is non-interruptible, and has no timeout.

This call should be used by drivers that require exclusive access to the
SPI bus. The SPI bus must be released by a spi_bus_unlock call when the
exclusive access is over. Data transfer must be done by spi_sync_locked
and spi_async_locked calls when the SPI bus lock is held.

.. _`spi_bus_lock.return`:

Return
------

always zero.

.. _`spi_bus_unlock`:

spi_bus_unlock
==============

.. c:function:: int spi_bus_unlock(struct spi_master *master)

    release the lock for exclusive SPI bus usage

    :param struct spi_master \*master:
        SPI bus master that was locked for exclusive bus access

.. _`spi_bus_unlock.context`:

Context
-------

can sleep

.. _`spi_bus_unlock.description`:

Description
-----------

This call may only be used from a context that may sleep.  The sleep
is non-interruptible, and has no timeout.

This call releases an SPI bus lock previously obtained by an spi_bus_lock
call.

.. _`spi_bus_unlock.return`:

Return
------

always zero.

.. _`spi_write_then_read`:

spi_write_then_read
===================

.. c:function:: int spi_write_then_read(struct spi_device *spi, const void *txbuf, unsigned n_tx, void *rxbuf, unsigned n_rx)

    SPI synchronous write followed by read

    :param struct spi_device \*spi:
        device with which data will be exchanged

    :param const void \*txbuf:
        data to be written (need not be dma-safe)

    :param unsigned n_tx:
        size of txbuf, in bytes

    :param void \*rxbuf:
        buffer into which data will be read (need not be dma-safe)

    :param unsigned n_rx:
        size of rxbuf, in bytes

.. _`spi_write_then_read.context`:

Context
-------

can sleep

.. _`spi_write_then_read.description`:

Description
-----------

This performs a half duplex MicroWire style transaction with the
device, sending txbuf and then reading rxbuf.  The return value
is zero for success, else a negative errno status code.
This call may only be used from a context that may sleep.

Parameters to this routine are always copied using a small buffer;
portable code should never use this for more than 32 bytes.
Performance-sensitive or bulk transfer code should instead use
spi_{async,sync}() calls with dma-safe buffers.

.. _`spi_write_then_read.return`:

Return
------

zero on success, else a negative error code.

.. This file was automatic generated / don't edit.

