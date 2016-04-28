.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-spi-master:

=================
struct spi_master
=================

*man struct spi_master(9)*

*4.6.0-rc5*

interface to SPI master controller


Synopsis
========

.. code-block:: c

    struct spi_master {
      struct device dev;
      struct list_head list;
      s16 bus_num;
      u16 num_chipselect;
      u16 dma_alignment;
      u16 mode_bits;
      u32 bits_per_word_mask;
    #define SPI_BPW_MASK(bits) BIT((bits) - 1)
    #define SPI_BIT_MASK(bits) (((bits) == 32) ? ~0U : (BIT(bits) - 1))
    #define SPI_BPW_RANGE_MASK(min# max) (SPI_BIT_MASK(max) - SPI_BIT_MASK(min - 1))
      u32 min_speed_hz;
      u32 max_speed_hz;
      u16 flags;
    #define SPI_MASTER_HALF_DUPLEX  BIT(0)
    #define SPI_MASTER_NO_RX    BIT(1)
    #define SPI_MASTER_NO_TX    BIT(2)
    #define SPI_MASTER_MUST_RX      BIT(3)
    #define SPI_MASTER_MUST_TX      BIT(4)
      size_t (* max_transfer_size) (struct spi_device *spi);
      spinlock_t bus_lock_spinlock;
      struct mutex bus_lock_mutex;
      bool bus_lock_flag;
      int (* setup) (struct spi_device *spi);
      int (* transfer) (struct spi_device *spi,struct spi_message *mesg);
      void (* cleanup) (struct spi_device *spi);
      bool (* can_dma) (struct spi_master *master,struct spi_device *spi,struct spi_transfer *xfer);
      bool queued;
      struct kthread_worker kworker;
      struct task_struct * kworker_task;
      struct kthread_work pump_messages;
      spinlock_t queue_lock;
      struct list_head queue;
      struct spi_message * cur_msg;
      bool idling;
      bool busy;
      bool running;
      bool rt;
      bool auto_runtime_pm;
      bool cur_msg_prepared;
      bool cur_msg_mapped;
      struct completion xfer_completion;
      size_t max_dma_len;
      int (* prepare_transfer_hardware) (struct spi_master *master);
      int (* transfer_one_message) (struct spi_master *master,struct spi_message *mesg);
      int (* unprepare_transfer_hardware) (struct spi_master *master);
      int (* prepare_message) (struct spi_master *master,struct spi_message *message);
      int (* unprepare_message) (struct spi_master *master,struct spi_message *message);
      int (* spi_flash_read) (struct  spi_device *spi,struct spi_flash_read_message *msg);
      void (* set_cs) (struct spi_device *spi, bool enable);
      int (* transfer_one) (struct spi_master *master, struct spi_device *spi,struct spi_transfer *transfer);
      void (* handle_err) (struct spi_master *master,struct spi_message *message);
      int * cs_gpios;
      struct spi_statistics statistics;
      struct dma_chan * dma_tx;
      struct dma_chan * dma_rx;
      void * dummy_rx;
      void * dummy_tx;
      int (* fw_translate_cs) (struct spi_master *master, unsigned cs);
    };


Members
=======

dev
    device interface to this driver

list
    link with the global spi_master list

bus_num
    board-specific (and often SOC-specific) identifier for a given SPI
    controller.

num_chipselect
    chipselects are used to distinguish individual SPI slaves, and are
    numbered from zero to num_chipselects. each slave has a chipselect
    signal, but it's common that not every chipselect is connected to a
    slave.

dma_alignment
    SPI controller constraint on DMA buffers alignment.

mode_bits
    flags understood by this controller driver

bits_per_word_mask
    A mask indicating which values of bits_per_word are supported by
    the driver. Bit n indicates that a bits_per_word n+1 is supported.
    If set, the SPI core will reject any transfer with an unsupported
    bits_per_word. If not set, this value is simply ignored, and it's
    up to the individual driver to perform any validation.

min_speed_hz
    Lowest supported transfer speed

max_speed_hz
    Highest supported transfer speed

flags
    other constraints relevant to this driver

max_transfer_size
    function that returns the max transfer size for a ``spi_device``;
    may be ``NULL``, so the default ``SIZE_MAX`` will be used.

bus_lock_spinlock
    spinlock for SPI bus locking

bus_lock_mutex
    mutex for SPI bus locking

bus_lock_flag
    indicates that the SPI bus is locked for exclusive use

setup
    updates the device mode and clocking records used by a device's SPI
    controller; protocol code may call this. This must fail if an
    unrecognized or unsupported mode is requested. It's always safe to
    call this unless transfers are pending on the device whose settings
    are being modified.

transfer
    adds a message to the controller's transfer queue.

cleanup
    frees controller-specific state

can_dma
    determine whether this master supports DMA

queued
    whether this master is providing an internal message queue

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
    the core should ensure a runtime PM reference is held while the
    hardware is prepared, using the parent device for the spidev

cur_msg_prepared
    spi_prepare_message was called for the currently in-flight message

cur_msg_mapped
    message has been mapped for DMA

xfer_completion
    used by core ``transfer_one_message``

max_dma_len
    Maximum length of a DMA transfer for the device.

prepare_transfer_hardware
    a message will soon arrive from the queue so the subsystem requests
    the driver to prepare the transfer hardware by issuing this call

transfer_one_message
    the subsystem calls the driver to transfer a single message while
    queuing transfers that arrive in the meantime. When the driver is
    finished with this message, it must call
    ``spi_finalize_current_message`` so the subsystem can issue the next
    message

unprepare_transfer_hardware
    there are currently no more messages on the queue so the subsystem
    notifies the driver that it may relax the hardware by issuing this
    call

prepare_message
    set up the controller to transfer a single message, for example
    doing DMA mapping. Called from threaded context.

unprepare_message
    undo any work done by ``prepare_message``.

spi_flash_read
    to support spi-controller hardwares that provide accelerated
    interface to read from flash devices.

set_cs
    set the logic level of the chip select line. May be called from
    interrupt context.

transfer_one
    transfer a single spi_transfer. - return 0 if the transfer is
    finished, - return 1 if the transfer is still in progress. When the
    driver is finished with this transfer it must call
    ``spi_finalize_current_transfer`` so the subsystem can issue the
    next transfer. Note: transfer_one and transfer_one_message are
    mutually exclusive; when both are set, the generic subsystem does
    not call your transfer_one callback.

handle_err
    the subsystem calls the driver to handle an error that occurs in the
    generic implementation of ``transfer_one_message``.

cs_gpios
    Array of GPIOs to use as chip select lines; one per CS number. Any
    individual value may be -ENOENT for CS lines that are not GPIOs
    (driven by the SPI controller itself).

statistics
    statistics for the spi_master

dma_tx
    DMA transmit channel

dma_rx
    DMA receive channel

dummy_rx
    dummy receive buffer for full-duplex devices

dummy_tx
    dummy transmit buffer for full-duplex devices

fw_translate_cs
    If the boot firmware uses different numbering scheme what Linux
    expects, this optional hook can be used to translate between the
    two.


Description
===========

Each SPI master controller can communicate with one or more
``spi_device`` children. These make a small bus, sharing MOSI, MISO and
SCK signals but not chip select signals. Each device may be configured
to use a different clock rate, since those shared signals are ignored
unless the chip is selected.

The driver for an SPI controller manages access to those devices through
a queue of spi_message transactions, copying data between CPU memory
and an SPI slave device. For each such message it queues, it calls the
message's completion function when the transaction completes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
