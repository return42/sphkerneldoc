.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/spi/spi.h

.. _`spi_statistics`:

struct spi_statistics
=====================

.. c:type:: struct spi_statistics

    statistics for spi transfers

.. _`spi_statistics.definition`:

Definition
----------

.. code-block:: c

    struct spi_statistics {
        spinlock_t lock;
        unsigned long messages;
        unsigned long transfers;
        unsigned long errors;
        unsigned long timedout;
        unsigned long spi_sync;
        unsigned long spi_sync_immediate;
        unsigned long spi_async;
        unsigned long long bytes;
        unsigned long long bytes_rx;
        unsigned long long bytes_tx;
    #define SPI_STATISTICS_HISTO_SIZE 17
        unsigned long transfer_bytes_histo[SPI_STATISTICS_HISTO_SIZE];
        unsigned long transfers_split_maxsize;
    }

.. _`spi_statistics.members`:

Members
-------

lock
    lock protecting this structure

messages
    number of spi-messages handled

transfers
    number of spi_transfers handled

errors
    number of errors during spi_transfer

timedout
    number of timeouts during spi_transfer

spi_sync
    number of times spi_sync is used

spi_sync_immediate
    number of times spi_sync is executed immediately
    in calling context without queuing and scheduling

spi_async
    number of times spi_async is used

bytes
    number of bytes transferred to/from device

bytes_rx
    number of bytes received from device

bytes_tx
    number of bytes sent to device

transfer_bytes_histo
    transfer bytes histogramm

transfers_split_maxsize
    number of transfers that have been split because of
    maxsize limit

.. _`spi_device`:

struct spi_device
=================

.. c:type:: struct spi_device

    Controller side proxy for an SPI slave device

.. _`spi_device.definition`:

Definition
----------

.. code-block:: c

    struct spi_device {
        struct device dev;
        struct spi_controller *controller;
        struct spi_controller *master;
        u32 max_speed_hz;
        u8 chip_select;
        u8 bits_per_word;
        u16 mode;
    #define SPI_CPHA 0x01
    #define SPI_CPOL 0x02
    #define SPI_MODE_0 (0|0)
    #define SPI_MODE_1 (0|SPI_CPHA)
    #define SPI_MODE_2 (SPI_CPOL|0)
    #define SPI_MODE_3 (SPI_CPOL|SPI_CPHA)
    #define SPI_CS_HIGH 0x04
    #define SPI_LSB_FIRST 0x08
    #define SPI_3WIRE 0x10
    #define SPI_LOOP 0x20
    #define SPI_NO_CS 0x40
    #define SPI_READY 0x80
    #define SPI_TX_DUAL 0x100
    #define SPI_TX_QUAD 0x200
    #define SPI_RX_DUAL 0x400
    #define SPI_RX_QUAD 0x800
    #define SPI_CS_WORD 0x1000
        int irq;
        void *controller_state;
        void *controller_data;
        char modalias[SPI_NAME_SIZE];
        const char *driver_override;
        int cs_gpio;
        struct spi_statistics statistics;
    }

.. _`spi_device.members`:

Members
-------

dev
    Driver model representation of the device.

controller
    SPI controller used with the device.

master
    Copy of controller, for backwards compatibility.

max_speed_hz
    Maximum clock rate to be used with this chip
    (on this board); may be changed by the device's driver.
    The spi_transfer.speed_hz can override this for each transfer.

chip_select
    Chipselect, distinguishing chips handled by \ ``controller``\ .

bits_per_word
    Data transfers involve one or more words; word sizes
    like eight or 12 bits are common.  In-memory wordsizes are
    powers of two bytes (e.g. 20 bit samples use 32 bits).
    This may be changed by the device's driver, or left at the
    default (0) indicating protocol words are eight bit bytes.
    The spi_transfer.bits_per_word can override this for each transfer.

mode
    The spi mode defines how data is clocked out and in.
    This may be changed by the device's driver.
    The "active low" default for chipselect mode can be overridden
    (by specifying SPI_CS_HIGH) as can the "MSB first" default for
    each word in a transfer (by specifying SPI_LSB_FIRST).

irq
    Negative, or the number passed to \ :c:func:`request_irq`\  to receive
    interrupts from this device.

controller_state
    Controller's runtime state

controller_data
    Board-specific definitions for controller, such as
    FIFO initialization parameters; from board_info.controller_data

modalias
    Name of the driver to use with this device, or an alias
    for that name.  This appears in the sysfs "modalias" attribute
    for driver coldplugging, and in uevents used for hotplugging

driver_override
    *undescribed*

cs_gpio
    gpio number of the chipselect line (optional, -ENOENT when
    not using a GPIO line)

statistics
    statistics for the spi_device

.. _`spi_device.description`:

Description
-----------

A \ ``spi_device``\  is used to interchange data between an SPI slave
(usually a discrete chip) and CPU memory.

In \ ``dev``\ , the platform_data is used to hold information about this
device that's meaningful to the device's protocol driver, but not
to its controller.  One example might be an identifier for a chip
variant with slightly different functionality; another might be
information about how this particular board wires the chip's pins.

.. _`spi_driver`:

struct spi_driver
=================

.. c:type:: struct spi_driver

    Host side "protocol" driver

.. _`spi_driver.definition`:

Definition
----------

.. code-block:: c

    struct spi_driver {
        const struct spi_device_id *id_table;
        int (*probe)(struct spi_device *spi);
        int (*remove)(struct spi_device *spi);
        void (*shutdown)(struct spi_device *spi);
        struct device_driver driver;
    }

.. _`spi_driver.members`:

Members
-------

id_table
    List of SPI devices supported by this driver

probe
    Binds this driver to the spi device.  Drivers can verify
    that the device is actually present, and may need to configure
    characteristics (such as bits_per_word) which weren't needed for
    the initial configuration done during system setup.

remove
    Unbinds this driver from the spi device

shutdown
    Standard shutdown callback used during system state
    transitions such as powerdown/halt and kexec

driver
    SPI device drivers should initialize the name and owner
    field of this structure.

.. _`spi_driver.description`:

Description
-----------

This represents the kind of device driver that uses SPI messages to
interact with the hardware at the other end of a SPI link.  It's called
a "protocol" driver because it works through messages rather than talking
directly to SPI hardware (which is what the underlying SPI controller
driver does to pass those messages).  These protocols are defined in the
specification for the device(s) supported by the driver.

As a rule, those device protocols represent the lowest level interface
supported by a driver, and it will support upper level interfaces too.
Examples of such upper levels include frameworks like MTD, networking,
MMC, RTC, filesystem character device nodes, and hardware monitoring.

.. _`spi_unregister_driver`:

spi_unregister_driver
=====================

.. c:function:: void spi_unregister_driver(struct spi_driver *sdrv)

    reverse effect of spi_register_driver

    :param sdrv:
        the driver to unregister
    :type sdrv: struct spi_driver \*

.. _`spi_unregister_driver.context`:

Context
-------

can sleep

.. _`module_spi_driver`:

module_spi_driver
=================

.. c:function::  module_spi_driver( __spi_driver)

    Helper macro for registering a SPI driver

    :param __spi_driver:
        spi_driver struct
    :type __spi_driver: 

.. _`module_spi_driver.description`:

Description
-----------

Helper macro for SPI drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. _`spi_controller`:

struct spi_controller
=====================

.. c:type:: struct spi_controller

    interface to SPI master or slave controller

.. _`spi_controller.definition`:

Definition
----------

.. code-block:: c

    struct spi_controller {
        struct device dev;
        struct list_head list;
        s16 bus_num;
        u16 num_chipselect;
        u16 dma_alignment;
        u16 mode_bits;
        u32 bits_per_word_mask;
    #define SPI_BPW_MASK(bits) BIT((bits) - 1)
    #define SPI_BIT_MASK(bits) (((bits) == 32) ? ~0U : (BIT(bits) - 1))
    #define SPI_BPW_RANGE_MASK(min, max) (SPI_BIT_MASK(max) - SPI_BIT_MASK(min - 1))
        u32 min_speed_hz;
        u32 max_speed_hz;
        u16 flags;
    #define SPI_CONTROLLER_HALF_DUPLEX BIT(0)
    #define SPI_CONTROLLER_NO_RX BIT(1)
    #define SPI_CONTROLLER_NO_TX BIT(2)
    #define SPI_CONTROLLER_MUST_RX BIT(3)
    #define SPI_CONTROLLER_MUST_TX BIT(4)
    #define SPI_MASTER_GPIO_SS BIT(5)
        bool slave;
        size_t (*max_transfer_size)(struct spi_device *spi);
        size_t (*max_message_size)(struct spi_device *spi);
        struct mutex io_mutex;
        spinlock_t bus_lock_spinlock;
        struct mutex bus_lock_mutex;
        bool bus_lock_flag;
        int (*setup)(struct spi_device *spi);
        int (*transfer)(struct spi_device *spi, struct spi_message *mesg);
        void (*cleanup)(struct spi_device *spi);
        bool (*can_dma)(struct spi_controller *ctlr,struct spi_device *spi, struct spi_transfer *xfer);
        bool queued;
        struct kthread_worker kworker;
        struct task_struct *kworker_task;
        struct kthread_work pump_messages;
        spinlock_t queue_lock;
        struct list_head queue;
        struct spi_message *cur_msg;
        bool idling;
        bool busy;
        bool running;
        bool rt;
        bool auto_runtime_pm;
        bool cur_msg_prepared;
        bool cur_msg_mapped;
        struct completion xfer_completion;
        size_t max_dma_len;
        int (*prepare_transfer_hardware)(struct spi_controller *ctlr);
        int (*transfer_one_message)(struct spi_controller *ctlr, struct spi_message *mesg);
        int (*unprepare_transfer_hardware)(struct spi_controller *ctlr);
        int (*prepare_message)(struct spi_controller *ctlr, struct spi_message *message);
        int (*unprepare_message)(struct spi_controller *ctlr, struct spi_message *message);
        int (*slave_abort)(struct spi_controller *ctlr);
        void (*set_cs)(struct spi_device *spi, bool enable);
        int (*transfer_one)(struct spi_controller *ctlr, struct spi_device *spi, struct spi_transfer *transfer);
        void (*handle_err)(struct spi_controller *ctlr, struct spi_message *message);
        const struct spi_controller_mem_ops *mem_ops;
        int *cs_gpios;
        struct spi_statistics statistics;
        struct dma_chan *dma_tx;
        struct dma_chan *dma_rx;
        void *dummy_rx;
        void *dummy_tx;
        int (*fw_translate_cs)(struct spi_controller *ctlr, unsigned cs);
    }

.. _`spi_controller.members`:

Members
-------

dev
    device interface to this driver

list
    link with the global spi_controller list

bus_num
    board-specific (and often SOC-specific) identifier for a
    given SPI controller.

num_chipselect
    chipselects are used to distinguish individual
    SPI slaves, and are numbered from zero to num_chipselects.
    each slave has a chipselect signal, but it's common that not
    every chipselect is connected to a slave.

dma_alignment
    SPI controller constraint on DMA buffers alignment.

mode_bits
    flags understood by this controller driver

bits_per_word_mask
    A mask indicating which values of bits_per_word are
    supported by the driver. Bit n indicates that a bits_per_word n+1 is
    supported. If set, the SPI core will reject any transfer with an
    unsupported bits_per_word. If not set, this value is simply ignored,
    and it's up to the individual driver to perform any validation.

min_speed_hz
    Lowest supported transfer speed

max_speed_hz
    Highest supported transfer speed

flags
    other constraints relevant to this driver

slave
    indicates that this is an SPI slave controller

max_transfer_size
    function that returns the max transfer size for
    a \ :c:type:`struct spi_device <spi_device>`\ ; may be \ ``NULL``\ , so the default \ ``SIZE_MAX``\  will be used.

max_message_size
    function that returns the max message size for
    a \ :c:type:`struct spi_device <spi_device>`\ ; may be \ ``NULL``\ , so the default \ ``SIZE_MAX``\  will be used.

io_mutex
    mutex for physical bus access

bus_lock_spinlock
    spinlock for SPI bus locking

bus_lock_mutex
    mutex for exclusion of multiple callers

bus_lock_flag
    indicates that the SPI bus is locked for exclusive use

setup
    updates the device mode and clocking records used by a
    device's SPI controller; protocol code may call this.  This
    must fail if an unrecognized or unsupported mode is requested.
    It's always safe to call this unless transfers are pending on
    the device whose settings are being modified.

transfer
    adds a message to the controller's transfer queue.

cleanup
    frees controller-specific state

can_dma
    determine whether this controller supports DMA

queued
    whether this controller is providing an internal message queue

kworker
    thread struct for message pump

kworker_task
    pointer to task for message pump kworker thread

pump_messages
    work struct for scheduling work to the message pump

queue_lock
    spinlock to syncronise access to message queue

queue
    message queue

cur_msg
    the currently in-flight message

idling
    the device is entering idle state

busy
    message pump is busy

running
    message pump is running

rt
    whether this queue is set to run as a realtime task

auto_runtime_pm
    the core should ensure a runtime PM reference is held
    while the hardware is prepared, using the parent
    device for the spidev

cur_msg_prepared
    spi_prepare_message was called for the currently
    in-flight message

cur_msg_mapped
    message has been mapped for DMA

xfer_completion
    used by core \ :c:func:`transfer_one_message`\ 

max_dma_len
    Maximum length of a DMA transfer for the device.

prepare_transfer_hardware
    a message will soon arrive from the queue
    so the subsystem requests the driver to prepare the transfer hardware
    by issuing this call

transfer_one_message
    the subsystem calls the driver to transfer a single
    message while queuing transfers that arrive in the meantime. When the
    driver is finished with this message, it must call
    \ :c:func:`spi_finalize_current_message`\  so the subsystem can issue the next
    message

unprepare_transfer_hardware
    there are currently no more messages on the
    queue so the subsystem notifies the driver that it may relax the
    hardware by issuing this call

prepare_message
    set up the controller to transfer a single message,
    for example doing DMA mapping.  Called from threaded
    context.

unprepare_message
    undo any work done by \ :c:func:`prepare_message`\ .

slave_abort
    abort the ongoing transfer request on an SPI slave controller

set_cs
    set the logic level of the chip select line.  May be called
    from interrupt context.

transfer_one
    transfer a single spi_transfer.
    - return 0 if the transfer is finished,
    - return 1 if the transfer is still in progress. When
    the driver is finished with this transfer it must
    call \ :c:func:`spi_finalize_current_transfer`\  so the subsystem
    can issue the next transfer. Note: transfer_one and
    transfer_one_message are mutually exclusive; when both
    are set, the generic subsystem does not call your
    transfer_one callback.

handle_err
    the subsystem calls the driver to handle an error that occurs
    in the generic implementation of \ :c:func:`transfer_one_message`\ .

mem_ops
    optimized/dedicated operations for interactions with SPI memory.
    This field is optional and should only be implemented if the
    controller has native support for memory like operations.

cs_gpios
    Array of GPIOs to use as chip select lines; one per CS
    number. Any individual value may be -ENOENT for CS lines that
    are not GPIOs (driven by the SPI controller itself).

statistics
    statistics for the spi_controller

dma_tx
    DMA transmit channel

dma_rx
    DMA receive channel

dummy_rx
    dummy receive buffer for full-duplex devices

dummy_tx
    dummy transmit buffer for full-duplex devices

fw_translate_cs
    If the boot firmware uses different numbering scheme
    what Linux expects, this optional hook can be used to translate
    between the two.

.. _`spi_controller.description`:

Description
-----------

Each SPI controller can communicate with one or more \ ``spi_device``\ 
children.  These make a small bus, sharing MOSI, MISO and SCK signals
but not chip select signals.  Each device may be configured to use a
different clock rate, since those shared signals are ignored unless
the chip is selected.

The driver for an SPI controller manages access to those devices through
a queue of spi_message transactions, copying data between CPU memory and
an SPI slave device.  For each such message it queues, it calls the
message's completion function when the transaction completes.

.. _`spi_res`:

struct spi_res
==============

.. c:type:: struct spi_res

    spi resource management structure

.. _`spi_res.definition`:

Definition
----------

.. code-block:: c

    struct spi_res {
        struct list_head entry;
        spi_res_release_t release;
        unsigned long long data[];
    }

.. _`spi_res.members`:

Members
-------

entry
    list entry

release
    release code called prior to freeing this resource

data
    extra data allocated for the specific use-case

.. _`spi_res.description`:

Description
-----------

this is based on ideas from devres, but focused on life-cycle
management during spi_message processing

.. _`spi_transfer`:

struct spi_transfer
===================

.. c:type:: struct spi_transfer

    a read/write buffer pair

.. _`spi_transfer.definition`:

Definition
----------

.. code-block:: c

    struct spi_transfer {
        const void *tx_buf;
        void *rx_buf;
        unsigned len;
        dma_addr_t tx_dma;
        dma_addr_t rx_dma;
        struct sg_table tx_sg;
        struct sg_table rx_sg;
        unsigned cs_change:1;
        unsigned tx_nbits:3;
        unsigned rx_nbits:3;
    #define SPI_NBITS_SINGLE 0x01
    #define SPI_NBITS_DUAL 0x02
    #define SPI_NBITS_QUAD 0x04
        u8 bits_per_word;
        u16 delay_usecs;
        u32 speed_hz;
        u16 word_delay;
        struct list_head transfer_list;
    }

.. _`spi_transfer.members`:

Members
-------

tx_buf
    data to be written (dma-safe memory), or NULL

rx_buf
    data to be read (dma-safe memory), or NULL

len
    size of rx and tx buffers (in bytes)

tx_dma
    DMA address of tx_buf, if \ ``spi_message.is_dma_mapped``\ 

rx_dma
    DMA address of rx_buf, if \ ``spi_message.is_dma_mapped``\ 

tx_sg
    Scatterlist for transmit, currently not for client use

rx_sg
    Scatterlist for receive, currently not for client use

cs_change
    affects chipselect after this transfer completes

tx_nbits
    number of bits used for writing. If 0 the default
    (SPI_NBITS_SINGLE) is used.

rx_nbits
    number of bits used for reading. If 0 the default
    (SPI_NBITS_SINGLE) is used.

bits_per_word
    select a bits_per_word other than the device default
    for this transfer. If 0 the default (from \ ``spi_device``\ ) is used.

delay_usecs
    microseconds to delay after this transfer before
    (optionally) changing the chipselect status, then starting
    the next transfer or completing this \ ``spi_message``\ .

speed_hz
    Select a speed other than the device default for this
    transfer. If 0 the default (from \ ``spi_device``\ ) is used.

word_delay
    clock cycles to inter word delay after each word size
    (set by bits_per_word) transmission.

transfer_list
    transfers are sequenced through \ ``spi_message.transfers``\ 

.. _`spi_transfer.description`:

Description
-----------

SPI transfers always write the same number of bytes as they read.
Protocol drivers should always provide \ ``rx_buf``\  and/or \ ``tx_buf``\ .
In some cases, they may also want to provide DMA addresses for
the data being transferred; that may reduce overhead, when the
underlying driver uses dma.

If the transmit buffer is null, zeroes will be shifted out
while filling \ ``rx_buf``\ .  If the receive buffer is null, the data
shifted in will be discarded.  Only "len" bytes shift out (or in).
It's an error to try to shift out a partial word.  (For example, by
shifting out three bytes with word size of sixteen or twenty bits;
the former uses two bytes per word, the latter uses four bytes.)

In-memory data values are always in native CPU byte order, translated
from the wire byte order (big-endian except with SPI_LSB_FIRST).  So
for example when bits_per_word is sixteen, buffers are 2N bytes long
(@len = 2N) and hold N sixteen bit words in CPU byte order.

When the word size of the SPI transfer is not a power-of-two multiple
of eight bits, those in-memory words include extra bits.  In-memory
words are always seen by protocol drivers as right-justified, so the
undefined (rx) or unused (tx) bits are always the most significant bits.

All SPI transfers start with the relevant chipselect active.  Normally
it stays selected until after the last transfer in a message.  Drivers
can affect the chipselect signal using cs_change.

(i) If the transfer isn't the last one in the message, this flag is
used to make the chipselect briefly go inactive in the middle of the
message.  Toggling chipselect in this way may be needed to terminate
a chip command, letting a single spi_message perform all of group of
chip transactions together.

(ii) When the transfer is the last one in the message, the chip may
stay selected until the next transfer.  On multi-device SPI busses
with nothing blocking messages going to other devices, this is just
a performance hint; starting a message to another device deselects
this one.  But in other cases, this can be used to ensure correctness.
Some devices need protocol transactions to be built from a series of
spi_message submissions, where the content of one message is determined
by the results of previous messages and where the whole transaction
ends when the chipselect goes intactive.

When SPI can transfer in 1x,2x or 4x. It can get this transfer information
from device through \ ``tx_nbits``\  and \ ``rx_nbits``\ . In Bi-direction, these
two should both be set. User can set transfer mode with SPI_NBITS_SINGLE(1x)
SPI_NBITS_DUAL(2x) and SPI_NBITS_QUAD(4x) to support these three transfer.

The code that submits an spi_message (and its spi_transfers)
to the lower layers is responsible for managing its memory.
Zero-initialize every field you don't set up explicitly, to
insulate against future API updates.  After you submit a message
and its transfers, ignore them until its completion callback.

.. _`spi_message`:

struct spi_message
==================

.. c:type:: struct spi_message

    one multi-segment SPI transaction

.. _`spi_message.definition`:

Definition
----------

.. code-block:: c

    struct spi_message {
        struct list_head transfers;
        struct spi_device *spi;
        unsigned is_dma_mapped:1;
        void (*complete)(void *context);
        void *context;
        unsigned frame_length;
        unsigned actual_length;
        int status;
        struct list_head queue;
        void *state;
        struct list_head resources;
    }

.. _`spi_message.members`:

Members
-------

transfers
    list of transfer segments in this transaction

spi
    SPI device to which the transaction is queued

is_dma_mapped
    if true, the caller provided both dma and cpu virtual
    addresses for each transfer buffer

complete
    called to report transaction completions

context
    the argument to \ :c:func:`complete`\  when it's called

frame_length
    the total number of bytes in the message

actual_length
    the total number of bytes that were transferred in all
    successful segments

status
    zero for success, else negative errno

queue
    for use by whichever driver currently owns the message

state
    for use by whichever driver currently owns the message

resources
    for resource management when the spi message is processed

.. _`spi_message.description`:

Description
-----------

A \ ``spi_message``\  is used to execute an atomic sequence of data transfers,
each represented by a struct spi_transfer.  The sequence is "atomic"
in the sense that no other spi_message may use that SPI bus until that
sequence completes.  On some systems, many such sequences can execute as
as single programmed DMA transfer.  On all systems, these messages are
queued, and might complete after transactions to other devices.  Messages
sent to a given spi_device are always executed in FIFO order.

The code that submits an spi_message (and its spi_transfers)
to the lower layers is responsible for managing its memory.
Zero-initialize every field you don't set up explicitly, to
insulate against future API updates.  After you submit a message
and its transfers, ignore them until its completion callback.

.. _`spi_message_init_with_transfers`:

spi_message_init_with_transfers
===============================

.. c:function:: void spi_message_init_with_transfers(struct spi_message *m, struct spi_transfer *xfers, unsigned int num_xfers)

    Initialize spi_message and append transfers

    :param m:
        spi_message to be initialized
    :type m: struct spi_message \*

    :param xfers:
        An array of spi transfers
    :type xfers: struct spi_transfer \*

    :param num_xfers:
        Number of items in the xfer array
    :type num_xfers: unsigned int

.. _`spi_message_init_with_transfers.description`:

Description
-----------

This function initializes the given spi_message and adds each spi_transfer in
the given array to the message.

.. _`spi_replaced_transfers`:

struct spi_replaced_transfers
=============================

.. c:type:: struct spi_replaced_transfers

    structure describing the spi_transfer replacements that have occurred so that they can get reverted

.. _`spi_replaced_transfers.definition`:

Definition
----------

.. code-block:: c

    struct spi_replaced_transfers {
        spi_replaced_release_t release;
        void *extradata;
        struct list_head replaced_transfers;
        struct list_head *replaced_after;
        size_t inserted;
        struct spi_transfer inserted_transfers[];
    }

.. _`spi_replaced_transfers.members`:

Members
-------

release
    some extra release code to get executed prior to
    relasing this structure

extradata
    pointer to some extra data if requested or NULL

replaced_transfers
    transfers that have been replaced and which need
    to get restored

replaced_after
    the transfer after which the \ ``replaced_transfers``\ 
    are to get re-inserted

inserted
    number of transfers inserted

inserted_transfers
    array of spi_transfers of array-size \ ``inserted``\ ,
    that have been replacing replaced_transfers

.. _`spi_replaced_transfers.note`:

note
----

that \ ``extradata``\  will point to \ ``inserted_transfers``\ [@inserted]
if some extra allocation is requested, so alignment will be the same
as for spi_transfers

.. _`spi_sync_transfer`:

spi_sync_transfer
=================

.. c:function:: int spi_sync_transfer(struct spi_device *spi, struct spi_transfer *xfers, unsigned int num_xfers)

    synchronous SPI data transfer

    :param spi:
        device with which data will be exchanged
    :type spi: struct spi_device \*

    :param xfers:
        An array of spi_transfers
    :type xfers: struct spi_transfer \*

    :param num_xfers:
        Number of items in the xfer array
    :type num_xfers: unsigned int

.. _`spi_sync_transfer.context`:

Context
-------

can sleep

.. _`spi_sync_transfer.description`:

Description
-----------

Does a synchronous SPI data transfer of the given spi_transfer array.

For more specific semantics see \ :c:func:`spi_sync`\ .

.. _`spi_sync_transfer.return`:

Return
------

Return: zero on success, else a negative error code.

.. _`spi_write`:

spi_write
=========

.. c:function:: int spi_write(struct spi_device *spi, const void *buf, size_t len)

    SPI synchronous write

    :param spi:
        device to which data will be written
    :type spi: struct spi_device \*

    :param buf:
        data buffer
    :type buf: const void \*

    :param len:
        data buffer size
    :type len: size_t

.. _`spi_write.context`:

Context
-------

can sleep

.. _`spi_write.description`:

Description
-----------

This function writes the buffer \ ``buf``\ .
Callable only from contexts that can sleep.

.. _`spi_write.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_read`:

spi_read
========

.. c:function:: int spi_read(struct spi_device *spi, void *buf, size_t len)

    SPI synchronous read

    :param spi:
        device from which data will be read
    :type spi: struct spi_device \*

    :param buf:
        data buffer
    :type buf: void \*

    :param len:
        data buffer size
    :type len: size_t

.. _`spi_read.context`:

Context
-------

can sleep

.. _`spi_read.description`:

Description
-----------

This function reads the buffer \ ``buf``\ .
Callable only from contexts that can sleep.

.. _`spi_read.return`:

Return
------

zero on success, else a negative error code.

.. _`spi_w8r8`:

spi_w8r8
========

.. c:function:: ssize_t spi_w8r8(struct spi_device *spi, u8 cmd)

    SPI synchronous 8 bit write followed by 8 bit read

    :param spi:
        device with which data will be exchanged
    :type spi: struct spi_device \*

    :param cmd:
        command to be written before data is read back
    :type cmd: u8

.. _`spi_w8r8.context`:

Context
-------

can sleep

.. _`spi_w8r8.description`:

Description
-----------

Callable only from contexts that can sleep.

.. _`spi_w8r8.return`:

Return
------

the (unsigned) eight bit number returned by the
device, or else a negative error code.

.. _`spi_w8r16`:

spi_w8r16
=========

.. c:function:: ssize_t spi_w8r16(struct spi_device *spi, u8 cmd)

    SPI synchronous 8 bit write followed by 16 bit read

    :param spi:
        device with which data will be exchanged
    :type spi: struct spi_device \*

    :param cmd:
        command to be written before data is read back
    :type cmd: u8

.. _`spi_w8r16.context`:

Context
-------

can sleep

.. _`spi_w8r16.description`:

Description
-----------

The number is returned in wire-order, which is at least sometimes
big-endian.

Callable only from contexts that can sleep.

.. _`spi_w8r16.return`:

Return
------

the (unsigned) sixteen bit number returned by the
device, or else a negative error code.

.. _`spi_w8r16be`:

spi_w8r16be
===========

.. c:function:: ssize_t spi_w8r16be(struct spi_device *spi, u8 cmd)

    SPI synchronous 8 bit write followed by 16 bit big-endian read

    :param spi:
        device with which data will be exchanged
    :type spi: struct spi_device \*

    :param cmd:
        command to be written before data is read back
    :type cmd: u8

.. _`spi_w8r16be.context`:

Context
-------

can sleep

.. _`spi_w8r16be.description`:

Description
-----------

This function is similar to spi_w8r16, with the exception that it will
convert the read 16 bit data word from big-endian to native endianness.

Callable only from contexts that can sleep.

.. _`spi_w8r16be.return`:

Return
------

the (unsigned) sixteen bit number returned by the device in cpu
endianness, or else a negative error code.

.. _`spi_board_info`:

struct spi_board_info
=====================

.. c:type:: struct spi_board_info

    board-specific template for a SPI device

.. _`spi_board_info.definition`:

Definition
----------

.. code-block:: c

    struct spi_board_info {
        char modalias[SPI_NAME_SIZE];
        const void *platform_data;
        const struct property_entry *properties;
        void *controller_data;
        int irq;
        u32 max_speed_hz;
        u16 bus_num;
        u16 chip_select;
        u16 mode;
    }

.. _`spi_board_info.members`:

Members
-------

modalias
    Initializes spi_device.modalias; identifies the driver.

platform_data
    Initializes spi_device.platform_data; the particular
    data stored there is driver-specific.

properties
    Additional device properties for the device.

controller_data
    Initializes spi_device.controller_data; some
    controllers need hints about hardware setup, e.g. for DMA.

irq
    Initializes spi_device.irq; depends on how the board is wired.

max_speed_hz
    Initializes spi_device.max_speed_hz; based on limits
    from the chip datasheet and board-specific signal quality issues.

bus_num
    Identifies which spi_controller parents the spi_device; unused
    by \ :c:func:`spi_new_device`\ , and otherwise depends on board wiring.

chip_select
    Initializes spi_device.chip_select; depends on how
    the board is wired.

mode
    Initializes spi_device.mode; based on the chip datasheet, board
    wiring (some devices support both 3WIRE and standard modes), and
    possibly presence of an inverter in the chipselect path.

.. _`spi_board_info.description`:

Description
-----------

When adding new SPI devices to the device tree, these structures serve
as a partial device template.  They hold information which can't always
be determined by drivers.  Information that \ :c:func:`probe`\  can establish (such
as the default transfer wordsize) is not included here.

These structures are used in two places.  Their primary role is to
be stored in tables of board-specific device descriptors, which are
declared early in board initialization and then used (much later) to
populate a controller's device tree after the that controller's driver
initializes.  A secondary (and atypical) role is as a parameter to
\ :c:func:`spi_new_device`\  call, which happens after those controller drivers
are active in some dynamic board configuration models.

.. This file was automatic generated / don't edit.

