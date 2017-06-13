.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/mips_ejtag_fdc.c

.. _`mips_ejtag_fdc_tty_port`:

struct mips_ejtag_fdc_tty_port
==============================

.. c:type:: struct mips_ejtag_fdc_tty_port

    Wrapper struct for FDC tty_port.

.. _`mips_ejtag_fdc_tty_port.definition`:

Definition
----------

.. code-block:: c

    struct mips_ejtag_fdc_tty_port {
        struct tty_port port;
        struct mips_ejtag_fdc_tty *driver;
        raw_spinlock_t rx_lock;
        void *rx_buf;
        spinlock_t xmit_lock;
        unsigned int xmit_cnt;
        unsigned int xmit_head;
        unsigned int xmit_tail;
        struct completion xmit_empty;
    }

.. _`mips_ejtag_fdc_tty_port.members`:

Members
-------

port
    TTY port data

driver
    TTY driver.

rx_lock
    Lock for rx_buf.
    This protects between the hard interrupt and user
    context. It's also held during read SWITCH operations.

rx_buf
    Read buffer.

xmit_lock
    Lock for xmit\_\*, and port.xmit_buf.
    This protects between user context and kernel thread.
    It is used from \ :c:func:`chars_in_buffer`\ /write_room() TTY
    callbacks which are used during wait operations, so a
    mutex is unsuitable.

xmit_cnt
    Size of xmit buffer contents.

xmit_head
    Head of xmit buffer where data is written.

xmit_tail
    Tail of xmit buffer where data is read.

xmit_empty
    Completion for xmit buffer being empty.

.. _`mips_ejtag_fdc_tty`:

struct mips_ejtag_fdc_tty
=========================

.. c:type:: struct mips_ejtag_fdc_tty

    Driver data for FDC as a whole.

.. _`mips_ejtag_fdc_tty.definition`:

Definition
----------

.. code-block:: c

    struct mips_ejtag_fdc_tty {
        struct device *dev;
        struct tty_driver *driver;
        unsigned int cpu;
        char fdc_name;
        char driver_name;
        struct mips_ejtag_fdc_tty_port ports;
        wait_queue_head_t waitqueue;
        raw_spinlock_t lock;
        struct task_struct *thread;
        void __iomem *reg;
        u8 tx_fifo;
        unsigned int xmit_size;
        atomic_t xmit_total;
        unsigned int xmit_next;
        bool xmit_full;
        int irq;
        bool removing;
        struct timer_list poll_timer;
    #ifdef CONFIG_MAGIC_SYSRQ
        bool sysrq_pressed;
    #endif
    }

.. _`mips_ejtag_fdc_tty.members`:

Members
-------

dev
    FDC device (for dev\_\*() logging).

driver
    TTY driver.

cpu
    CPU number for this FDC.

fdc_name
    FDC name (not for base of channel names).

driver_name
    Base of driver name.

ports
    Per-channel data.

waitqueue
    Wait queue for waiting for TX data, or for space in TX
    FIFO.

lock
    Lock to protect FDCFG (interrupt enable).

thread
    KThread for writing out data to FDC.

reg
    FDC registers.

tx_fifo
    TX FIFO size.

xmit_size
    Size of each port's xmit buffer.

xmit_total
    Total number of bytes (from all ports) to transmit.

xmit_next
    Next port number to transmit from (round robin).

xmit_full
    Indicates TX FIFO is full, we're waiting for space.

irq
    IRQ number (negative if no IRQ).

removing
    Indicates the device is being removed and \ ``poll_timer``\ 
    should not be restarted.

poll_timer
    Timer for polling for interrupt events when \ ``irq``\  < 0.

sysrq_pressed
    Whether the magic sysrq key combination has been
    detected. See \ :c:func:`mips_ejtag_fdc_handle`\ .

.. _`fdc_word`:

struct fdc_word
===============

.. c:type:: struct fdc_word

    FDC word encoding some number of bytes of data.

.. _`fdc_word.definition`:

Definition
----------

.. code-block:: c

    struct fdc_word {
        u32 word;
        unsigned int bytes;
    }

.. _`fdc_word.members`:

Members
-------

word
    Raw FDC word.

bytes
    Number of bytes encoded by \ ``word``\ .

.. _`mips_ejtag_fdc_console`:

struct mips_ejtag_fdc_console
=============================

.. c:type:: struct mips_ejtag_fdc_console

    Wrapper struct for FDC consoles.

.. _`mips_ejtag_fdc_console.definition`:

Definition
----------

.. code-block:: c

    struct mips_ejtag_fdc_console {
        struct console cons;
        struct tty_driver *tty_drv;
        raw_spinlock_t lock;
        bool initialised;
        void __iomem  *regs;
    }

.. _`mips_ejtag_fdc_console.members`:

Members
-------

cons
    Console object.

tty_drv
    TTY driver associated with this console.

lock
    Lock to protect concurrent access to other fields.
    This is raw because it may be used very early.

initialised
    Whether the console is initialised.

regs
    Registers base address for each CPU.

.. _`mips_ejtag_fdc_put_chan`:

mips_ejtag_fdc_put_chan
=======================

.. c:function:: unsigned int mips_ejtag_fdc_put_chan(struct mips_ejtag_fdc_tty *priv, unsigned int chan)

    Write out a block of channel data.

    :param struct mips_ejtag_fdc_tty \*priv:
        Pointer to driver private data.

    :param unsigned int chan:
        Channel number.

.. _`mips_ejtag_fdc_put_chan.description`:

Description
-----------

Write a single block of data out to the debug adapter. If the circular buffer
is wrapped then only the first block is written.

.. _`mips_ejtag_fdc_put_chan.return`:

Return
------

The number of bytes that were written.

.. _`mips_ejtag_fdc_put`:

mips_ejtag_fdc_put
==================

.. c:function:: int mips_ejtag_fdc_put(void *arg)

    Kernel thread to write out channel data to FDC.

    :param void \*arg:
        Driver pointer.

.. _`mips_ejtag_fdc_put.description`:

Description
-----------

This kernel thread runs while \ ``priv``\ ->xmit_total != 0, and round robins the
channels writing out blocks of buffered data to the FDC TX FIFO.

.. _`mips_ejtag_fdc_handle`:

mips_ejtag_fdc_handle
=====================

.. c:function:: void mips_ejtag_fdc_handle(struct mips_ejtag_fdc_tty *priv)

    Handle FDC events.

    :param struct mips_ejtag_fdc_tty \*priv:
        Pointer to driver private data.

.. _`mips_ejtag_fdc_handle.description`:

Description
-----------

Handle FDC events, such as new incoming data which needs draining out of the
RX FIFO and feeding into the appropriate TTY ports, and space becoming
available in the TX FIFO which would allow more data to be written out.

.. _`mips_ejtag_fdc_isr`:

mips_ejtag_fdc_isr
==================

.. c:function:: irqreturn_t mips_ejtag_fdc_isr(int irq, void *dev_id)

    Interrupt handler.

    :param int irq:
        IRQ number.

    :param void \*dev_id:
        Pointer to driver private data.

.. _`mips_ejtag_fdc_isr.description`:

Description
-----------

This is the interrupt handler, used when interrupts are enabled.

It simply triggers the common FDC handler code.

.. _`mips_ejtag_fdc_isr.return`:

Return
------

IRQ_HANDLED if an FDC interrupt was pending.
IRQ_NONE otherwise.

.. _`mips_ejtag_fdc_tty_timer`:

mips_ejtag_fdc_tty_timer
========================

.. c:function:: void mips_ejtag_fdc_tty_timer(unsigned long opaque)

    Poll FDC for incoming data.

    :param unsigned long opaque:
        Pointer to driver private data.

.. _`mips_ejtag_fdc_tty_timer.description`:

Description
-----------

This is the timer handler for when interrupts are disabled and polling the
FDC state is required.

It simply triggers the common FDC handler code and arranges for further
polling.

.. This file was automatic generated / don't edit.

