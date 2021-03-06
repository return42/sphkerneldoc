.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi.c

.. _`__spi_register_driver`:

__spi_register_driver
=====================

.. c:function:: int __spi_register_driver(struct module *owner, struct spi_driver *sdrv)

    register a SPI driver

    :param owner:
        owner module of the driver to register
    :type owner: struct module \*

    :param sdrv:
        the driver to register
    :type sdrv: struct spi_driver \*

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

.. c:function:: struct spi_device *spi_alloc_device(struct spi_controller *ctlr)

    Allocate a new SPI device

    :param ctlr:
        Controller to which device is connected
    :type ctlr: struct spi_controller \*

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
spi_device structure to add it to the SPI controller.  If the caller
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

    :param spi:
        spi_device to register
    :type spi: struct spi_device \*

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

.. c:function:: struct spi_device *spi_new_device(struct spi_controller *ctlr, struct spi_board_info *chip)

    instantiate one new SPI device

    :param ctlr:
        Controller to which device is connected
    :type ctlr: struct spi_controller \*

    :param chip:
        Describes the SPI device
    :type chip: struct spi_board_info \*

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

    :param spi:
        spi_device to unregister
    :type spi: struct spi_device \*

.. _`spi_unregister_device.description`:

Description
-----------

Start making the passed SPI device vanish. Normally this would be handled
by \ :c:func:`spi_unregister_controller`\ .

.. _`spi_register_board_info`:

spi_register_board_info
=======================

.. c:function:: int spi_register_board_info(struct spi_board_info const *info, unsigned n)

    register SPI devices for a given board

    :param info:
        array of chip descriptors
    :type info: struct spi_board_info const \*

    :param n:
        how many descriptors are provided
    :type n: unsigned

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

.. c:function:: void spi_finalize_current_transfer(struct spi_controller *ctlr)

    report completion of a transfer

    :param ctlr:
        the controller reporting completion
    :type ctlr: struct spi_controller \*

.. _`spi_finalize_current_transfer.description`:

Description
-----------

Called by SPI drivers using the core \ :c:func:`transfer_one_message`\ 
implementation to notify it that the current interrupt driven
transfer has finished and the next one may be scheduled.

.. _`__spi_pump_messages`:

__spi_pump_messages
===================

.. c:function:: void __spi_pump_messages(struct spi_controller *ctlr, bool in_kthread)

    function which processes spi message queue

    :param ctlr:
        controller to process queue for
    :type ctlr: struct spi_controller \*

    :param in_kthread:
        true if we are in the context of the message pump thread
    :type in_kthread: bool

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

    :param work:
        pointer to kthread work struct contained in the controller struct
    :type work: struct kthread_work \*

.. _`spi_get_next_queued_message`:

spi_get_next_queued_message
===========================

.. c:function:: struct spi_message *spi_get_next_queued_message(struct spi_controller *ctlr)

    called by driver to check for queued messages

    :param ctlr:
        the controller to check for queued messages
    :type ctlr: struct spi_controller \*

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

.. c:function:: void spi_finalize_current_message(struct spi_controller *ctlr)

    the current message is complete

    :param ctlr:
        the controller to return the message to
    :type ctlr: struct spi_controller \*

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

    :param spi:
        spi device which is requesting transfer
    :type spi: struct spi_device \*

    :param msg:
        spi message which is to handled is queued to driver queue
    :type msg: struct spi_message \*

.. _`spi_queued_transfer.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_flush_queue`:

spi_flush_queue
===============

.. c:function:: void spi_flush_queue(struct spi_controller *ctlr)

    Send all pending messages in the queue from the callers' context

    :param ctlr:
        controller to process queue for
    :type ctlr: struct spi_controller \*

.. _`spi_flush_queue.description`:

Description
-----------

This should be used when one wants to ensure all pending messages have been
sent before doing something. Is used by the spi-mem code to make sure SPI
memory operations do not preempt regular SPI transfers that have been queued
before the spi-mem operation.

.. _`of_register_spi_devices`:

of_register_spi_devices
=======================

.. c:function:: void of_register_spi_devices(struct spi_controller *ctlr)

    Register child devices onto the SPI bus

    :param ctlr:
        Pointer to spi_controller device
    :type ctlr: struct spi_controller \*

.. _`of_register_spi_devices.description`:

Description
-----------

Registers an spi_device for each child node of controller node which
represents a valid SPI slave.

.. _`spi_slave_abort`:

spi_slave_abort
===============

.. c:function:: int spi_slave_abort(struct spi_device *spi)

    abort the ongoing transfer request on an SPI slave controller

    :param spi:
        device used for the current transfer
    :type spi: struct spi_device \*

.. _`__spi_alloc_controller`:

__spi_alloc_controller
======================

.. c:function:: struct spi_controller *__spi_alloc_controller(struct device *dev, unsigned int size, bool slave)

    allocate an SPI master or slave controller

    :param dev:
        the controller, possibly using the platform_bus
    :type dev: struct device \*

    :param size:
        how much zeroed driver-private data to allocate; the pointer to this
        memory is in the driver_data field of the returned device,
        accessible with \ :c:func:`spi_controller_get_devdata`\ .
    :type size: unsigned int

    :param slave:
        flag indicating whether to allocate an SPI master (false) or SPI
        slave (true) controller
    :type slave: bool

.. _`__spi_alloc_controller.context`:

Context
-------

can sleep

.. _`__spi_alloc_controller.description`:

Description
-----------

This call is used only by SPI controller drivers, which are the
only ones directly touching chip registers.  It's how they allocate
an spi_controller structure, prior to calling \ :c:func:`spi_register_controller`\ .

This must be called from context that can sleep.

The caller is responsible for assigning the bus number and initializing the
controller's methods before calling \ :c:func:`spi_register_controller`\ ; and (after
errors adding the device) calling \ :c:func:`spi_controller_put`\  to prevent a memory
leak.

.. _`__spi_alloc_controller.return`:

Return
------

the SPI controller structure on success, else NULL.

.. _`spi_register_controller`:

spi_register_controller
=======================

.. c:function:: int spi_register_controller(struct spi_controller *ctlr)

    register SPI master or slave controller

    :param ctlr:
        initialized master, originally from \ :c:func:`spi_alloc_master`\  or
        \ :c:func:`spi_alloc_slave`\ 
    :type ctlr: struct spi_controller \*

.. _`spi_register_controller.context`:

Context
-------

can sleep

.. _`spi_register_controller.description`:

Description
-----------

SPI controllers connect to their drivers using some non-SPI bus,
such as the platform bus.  The final stage of \ :c:func:`probe`\  in that code
includes calling \ :c:func:`spi_register_controller`\  to hook up to this SPI bus glue.

SPI controllers use board specific (often SOC specific) bus numbers,
and board-specific addressing for SPI devices combines those numbers
with chip select numbers.  Since SPI does not directly support dynamic
device identification, boards need configuration tables telling which
chip is at which address.

This must be called from context that can sleep.  It returns zero on
success, else a negative error code (dropping the controller's refcount).
After a successful return, the caller is responsible for calling
\ :c:func:`spi_unregister_controller`\ .

.. _`spi_register_controller.return`:

Return
------

zero on success, else a negative error code.

.. _`devm_spi_register_controller`:

devm_spi_register_controller
============================

.. c:function:: int devm_spi_register_controller(struct device *dev, struct spi_controller *ctlr)

    register managed SPI master or slave controller

    :param dev:
        device managing SPI controller
    :type dev: struct device \*

    :param ctlr:
        initialized controller, originally from \ :c:func:`spi_alloc_master`\  or
        \ :c:func:`spi_alloc_slave`\ 
    :type ctlr: struct spi_controller \*

.. _`devm_spi_register_controller.context`:

Context
-------

can sleep

.. _`devm_spi_register_controller.description`:

Description
-----------

Register a SPI device as with \ :c:func:`spi_register_controller`\  which will
automatically be unregistered and freed.

.. _`devm_spi_register_controller.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_unregister_controller`:

spi_unregister_controller
=========================

.. c:function:: void spi_unregister_controller(struct spi_controller *ctlr)

    unregister SPI master or slave controller

    :param ctlr:
        the controller being unregistered
    :type ctlr: struct spi_controller \*

.. _`spi_unregister_controller.context`:

Context
-------

can sleep

.. _`spi_unregister_controller.description`:

Description
-----------

This call is used only by SPI controller drivers, which are the
only ones directly touching chip registers.

This must be called from context that can sleep.

Note that this function also drops a reference to the controller.

.. _`spi_busnum_to_master`:

spi_busnum_to_master
====================

.. c:function:: struct spi_controller *spi_busnum_to_master(u16 bus_num)

    look up master associated with bus_num

    :param bus_num:
        the master's bus number
    :type bus_num: u16

.. _`spi_busnum_to_master.context`:

Context
-------

can sleep

.. _`spi_busnum_to_master.description`:

Description
-----------

This call may be used with devices that are registered after
arch init time.  It returns a refcounted pointer to the relevant
spi_controller (which the caller must release), or NULL if there is
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

    :param spi:
        the spi device for which we allocate memory
    :type spi: struct spi_device \*

    :param release:
        the release code to execute for this resource
    :type release: spi_res_release_t

    :param size:
        size to alloc and return
    :type size: size_t

    :param gfp:
        GFP allocation flags
    :type gfp: gfp_t

.. _`spi_res_alloc.return`:

Return
------

the pointer to the allocated data

This may get enhanced in the future to allocate from a memory pool
of the \ ``spi_device``\  or \ ``spi_controller``\  to avoid repeated allocations.

.. _`spi_res_free`:

spi_res_free
============

.. c:function:: void spi_res_free(void *res)

    free an spi resource

    :param res:
        pointer to the custom data of a resource
    :type res: void \*

.. _`spi_res_add`:

spi_res_add
===========

.. c:function:: void spi_res_add(struct spi_message *message, void *res)

    add a spi_res to the spi_message

    :param message:
        the spi message
    :type message: struct spi_message \*

    :param res:
        the spi_resource
    :type res: void \*

.. _`spi_res_release`:

spi_res_release
===============

.. c:function:: void spi_res_release(struct spi_controller *ctlr, struct spi_message *message)

    release all spi resources for this message

    :param ctlr:
        the \ ``spi_controller``\ 
    :type ctlr: struct spi_controller \*

    :param message:
        the \ ``spi_message``\ 
    :type message: struct spi_message \*

.. _`spi_replace_transfers`:

spi_replace_transfers
=====================

.. c:function:: struct spi_replaced_transfers *spi_replace_transfers(struct spi_message *msg, struct spi_transfer *xfer_first, size_t remove, size_t insert, spi_replaced_release_t release, size_t extradatasize, gfp_t gfp)

    replace transfers with several transfers and register change with spi_message.resources

    :param msg:
        the spi_message we work upon
    :type msg: struct spi_message \*

    :param xfer_first:
        the first spi_transfer we want to replace
    :type xfer_first: struct spi_transfer \*

    :param remove:
        number of transfers to remove
    :type remove: size_t

    :param insert:
        the number of transfers we want to insert instead
    :type insert: size_t

    :param release:
        extra release code necessary in some circumstances
    :type release: spi_replaced_release_t

    :param extradatasize:
        extra data to allocate (with alignment guarantees
        of struct \ ``spi_transfer``\ )
    :type extradatasize: size_t

    :param gfp:
        gfp flags
    :type gfp: gfp_t

.. _`spi_replace_transfers.return`:

Return
------

pointer to \ ``spi_replaced_transfers``\ ,
         PTR_ERR(...) in case of errors.

.. _`spi_split_transfers_maxsize`:

spi_split_transfers_maxsize
===========================

.. c:function:: int spi_split_transfers_maxsize(struct spi_controller *ctlr, struct spi_message *msg, size_t maxsize, gfp_t gfp)

    split spi transfers into multiple transfers when an individual transfer exceeds a certain size

    :param ctlr:
        the \ ``spi_controller``\  for this transfer
    :type ctlr: struct spi_controller \*

    :param msg:
        the \ ``spi_message``\  to transform
    :type msg: struct spi_message \*

    :param maxsize:
        the maximum when to apply this
    :type maxsize: size_t

    :param gfp:
        GFP allocation flags
    :type gfp: gfp_t

.. _`spi_split_transfers_maxsize.return`:

Return
------

status of transformation

.. _`spi_setup`:

spi_setup
=========

.. c:function:: int spi_setup(struct spi_device *spi)

    setup SPI mode and clock rate

    :param spi:
        the device whose settings are being modified
    :type spi: struct spi_device \*

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

    :param spi:
        device with which data will be exchanged
    :type spi: struct spi_device \*

    :param message:
        describes the data transfers, including completion callback
    :type message: struct spi_message \*

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

    :param spi:
        device with which data will be exchanged
    :type spi: struct spi_device \*

    :param message:
        describes the data transfers, including completion callback
    :type message: struct spi_message \*

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

    :param spi:
        device with which data will be exchanged
    :type spi: struct spi_device \*

    :param message:
        describes the data transfers
    :type message: struct spi_message \*

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

    :param spi:
        device with which data will be exchanged
    :type spi: struct spi_device \*

    :param message:
        describes the data transfers
    :type message: struct spi_message \*

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

.. c:function:: int spi_bus_lock(struct spi_controller *ctlr)

    obtain a lock for exclusive SPI bus usage

    :param ctlr:
        SPI bus master that should be locked for exclusive bus access
    :type ctlr: struct spi_controller \*

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

.. c:function:: int spi_bus_unlock(struct spi_controller *ctlr)

    release the lock for exclusive SPI bus usage

    :param ctlr:
        SPI bus master that was locked for exclusive bus access
    :type ctlr: struct spi_controller \*

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

    :param spi:
        device with which data will be exchanged
    :type spi: struct spi_device \*

    :param txbuf:
        data to be written (need not be dma-safe)
    :type txbuf: const void \*

    :param n_tx:
        size of txbuf, in bytes
    :type n_tx: unsigned

    :param rxbuf:
        buffer into which data will be read (need not be dma-safe)
    :type rxbuf: void \*

    :param n_rx:
        size of rxbuf, in bytes
    :type n_rx: unsigned

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

