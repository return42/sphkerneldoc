.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ps3/ps3-vuart.c

.. _`ps3_vuart_port_priv`:

struct ps3_vuart_port_priv
==========================

.. c:type:: struct ps3_vuart_port_priv

    private vuart device data.

.. _`ps3_vuart_port_priv.definition`:

Definition
----------

.. code-block:: c

    struct ps3_vuart_port_priv {
        u64 interrupt_mask;
        struct tx_list;
        struct rx_list;
        struct ps3_vuart_stats stats;
    }

.. _`ps3_vuart_port_priv.members`:

Members
-------

interrupt_mask
    *undescribed*

tx_list
    *undescribed*

rx_list
    *undescribed*

stats
    *undescribed*

.. _`ports_bmp`:

struct ports_bmp
================

.. c:type:: struct ports_bmp

    bitmap indicating ports needing service.

.. _`ports_bmp.definition`:

Definition
----------

.. code-block:: c

    struct ports_bmp {
        u64 status;
        u64 unused;
    }

.. _`ports_bmp.members`:

Members
-------

status
    *undescribed*

unused
    *undescribed*

.. _`ports_bmp.description`:

Description
-----------

A 256 bit read only bitmap indicating ports needing service.  Do not write
to these bits.  Must not cross a page boundary.

.. _`ps3_vuart_set_interrupt_mask`:

ps3_vuart_set_interrupt_mask
============================

.. c:function:: int ps3_vuart_set_interrupt_mask(struct ps3_system_bus_device *dev, unsigned long mask)

    Enable/disable the port interrupt sources.

    :param struct ps3_system_bus_device \*dev:
        The struct ps3_system_bus_device instance.

    :param unsigned long mask:
        *undescribed*

.. _`ps3_vuart_raw_write`:

ps3_vuart_raw_write
===================

.. c:function:: int ps3_vuart_raw_write(struct ps3_system_bus_device *dev, const void *buf, unsigned int bytes, u64 *bytes_written)

    Low level write helper.

    :param struct ps3_system_bus_device \*dev:
        The struct ps3_system_bus_device instance.

    :param const void \*buf:
        *undescribed*

    :param unsigned int bytes:
        *undescribed*

    :param u64 \*bytes_written:
        *undescribed*

.. _`ps3_vuart_raw_write.description`:

Description
-----------

Do not call ps3_vuart_raw_write directly, use ps3_vuart_write.

.. _`ps3_vuart_raw_read`:

ps3_vuart_raw_read
==================

.. c:function:: int ps3_vuart_raw_read(struct ps3_system_bus_device *dev, void *buf, unsigned int bytes, u64 *bytes_read)

    Low level read helper.

    :param struct ps3_system_bus_device \*dev:
        The struct ps3_system_bus_device instance.

    :param void \*buf:
        *undescribed*

    :param unsigned int bytes:
        *undescribed*

    :param u64 \*bytes_read:
        *undescribed*

.. _`ps3_vuart_raw_read.description`:

Description
-----------

Do not call ps3_vuart_raw_read directly, use ps3_vuart_read.

.. _`ps3_vuart_clear_rx_bytes`:

ps3_vuart_clear_rx_bytes
========================

.. c:function:: void ps3_vuart_clear_rx_bytes(struct ps3_system_bus_device *dev, unsigned int bytes)

    Discard bytes received.

    :param struct ps3_system_bus_device \*dev:
        The struct ps3_system_bus_device instance.

    :param unsigned int bytes:
        Max byte count to discard, zero = all pending.

.. _`ps3_vuart_clear_rx_bytes.description`:

Description
-----------

Used to clear pending rx interrupt source.  Will not block.

.. _`list_buffer`:

struct list_buffer
==================

.. c:type:: struct list_buffer

    An element for a port device fifo buffer list.

.. _`list_buffer.definition`:

Definition
----------

.. code-block:: c

    struct list_buffer {
        struct list_head link;
        const unsigned char *head;
        const unsigned char *tail;
        unsigned long dbg_number;
        unsigned char data;
    }

.. _`list_buffer.members`:

Members
-------

link
    *undescribed*

head
    *undescribed*

tail
    *undescribed*

dbg_number
    *undescribed*

data
    *undescribed*

.. _`ps3_vuart_write`:

ps3_vuart_write
===============

.. c:function:: int ps3_vuart_write(struct ps3_system_bus_device *dev, const void *buf, unsigned int bytes)

    the entry point for writing data to a port

    :param struct ps3_system_bus_device \*dev:
        The struct ps3_system_bus_device instance.

    :param const void \*buf:
        *undescribed*

    :param unsigned int bytes:
        *undescribed*

.. _`ps3_vuart_write.description`:

Description
-----------

If the port is idle on entry as much of the incoming data is written to
the port as the port will accept.  Otherwise a list buffer is created
and any remaning incoming data is copied to that buffer.  The buffer is
then enqueued for transmision via the transmit interrupt.

.. _`ps3_vuart_queue_rx_bytes`:

ps3_vuart_queue_rx_bytes
========================

.. c:function:: int ps3_vuart_queue_rx_bytes(struct ps3_system_bus_device *dev, u64 *bytes_queued)

    Queue waiting bytes into the buffer list.

    :param struct ps3_system_bus_device \*dev:
        The struct ps3_system_bus_device instance.

    :param u64 \*bytes_queued:
        Number of bytes queued to the buffer list.

.. _`ps3_vuart_queue_rx_bytes.description`:

Description
-----------

Must be called with priv->rx_list.lock held.

.. _`ps3_vuart_read`:

ps3_vuart_read
==============

.. c:function:: int ps3_vuart_read(struct ps3_system_bus_device *dev, void *buf, unsigned int bytes)

    The entry point for reading data from a port.

    :param struct ps3_system_bus_device \*dev:
        *undescribed*

    :param void \*buf:
        *undescribed*

    :param unsigned int bytes:
        *undescribed*

.. _`ps3_vuart_read.description`:

Description
-----------

Queue data waiting at the port, and if enough bytes to satisfy the request
are held in the buffer list those bytes are dequeued and copied to the
caller's buffer.  Emptied list buffers are retiered.  If the request cannot
be statified by bytes held in the list buffers -EAGAIN is returned.

.. _`ps3_vuart_work`:

ps3_vuart_work
==============

.. c:function:: void ps3_vuart_work(struct work_struct *work)

    Asynchronous read handler.

    :param struct work_struct \*work:
        *undescribed*

.. _`ps3_vuart_handle_interrupt_tx`:

ps3_vuart_handle_interrupt_tx
=============================

.. c:function:: int ps3_vuart_handle_interrupt_tx(struct ps3_system_bus_device *dev)

    third stage transmit interrupt handler

    :param struct ps3_system_bus_device \*dev:
        *undescribed*

.. _`ps3_vuart_handle_interrupt_tx.description`:

Description
-----------

Services the transmit interrupt for the port.  Writes as much data from the
buffer list as the port will accept.  Retires any emptied list buffers and
adjusts the final list buffer state for a partial write.

.. _`ps3_vuart_handle_interrupt_rx`:

ps3_vuart_handle_interrupt_rx
=============================

.. c:function:: int ps3_vuart_handle_interrupt_rx(struct ps3_system_bus_device *dev)

    third stage receive interrupt handler

    :param struct ps3_system_bus_device \*dev:
        *undescribed*

.. _`ps3_vuart_handle_interrupt_rx.description`:

Description
-----------

Services the receive interrupt for the port.  Creates a list buffer and
copies all waiting port data to that buffer and enqueues the buffer in the
buffer list.  Buffer list data is dequeued via ps3_vuart_read.

.. _`ps3_vuart_handle_port_interrupt`:

ps3_vuart_handle_port_interrupt
===============================

.. c:function:: int ps3_vuart_handle_port_interrupt(struct ps3_system_bus_device *dev)

    second stage interrupt handler

    :param struct ps3_system_bus_device \*dev:
        *undescribed*

.. _`ps3_vuart_handle_port_interrupt.description`:

Description
-----------

Services any pending interrupt types for the port.  Passes control to the
third stage type specific interrupt handler.  Returns control to the first
stage handler after one iteration.

.. _`ps3_vuart_irq_handler`:

ps3_vuart_irq_handler
=====================

.. c:function:: irqreturn_t ps3_vuart_irq_handler(int irq, void *_private)

    first stage interrupt handler

    :param int irq:
        *undescribed*

    :param void \*_private:
        *undescribed*

.. _`ps3_vuart_irq_handler.description`:

Description
-----------

Loops finding any interrupting port and its associated instance data.
Passes control to the second stage port specific interrupt handler.  Loops
until all outstanding interrupts are serviced.

.. _`ps3_vuart_cleanup`:

ps3_vuart_cleanup
=================

.. c:function:: int ps3_vuart_cleanup(struct ps3_system_bus_device *dev)

    common cleanup helper.

    :param struct ps3_system_bus_device \*dev:
        The struct ps3_system_bus_device instance.

.. _`ps3_vuart_cleanup.description`:

Description
-----------

Cleans interrupts and HV resources.  Must be called with
vuart_bus_priv.probe_mutex held.  Used by ps3_vuart_remove and
ps3_vuart_shutdown.  After this call, polled reading will still work.

.. _`ps3_vuart_remove`:

ps3_vuart_remove
================

.. c:function:: int ps3_vuart_remove(struct ps3_system_bus_device *dev)

    Completely clean the device instance.

    :param struct ps3_system_bus_device \*dev:
        The struct ps3_system_bus_device instance.

.. _`ps3_vuart_remove.description`:

Description
-----------

Cleans all memory, interrupts and HV resources.  After this call the
device can no longer be used.

.. _`ps3_vuart_shutdown`:

ps3_vuart_shutdown
==================

.. c:function:: int ps3_vuart_shutdown(struct ps3_system_bus_device *dev)

    Cleans interrupts and HV resources.

    :param struct ps3_system_bus_device \*dev:
        The struct ps3_system_bus_device instance.

.. _`ps3_vuart_shutdown.description`:

Description
-----------

Cleans interrupts and HV resources.  After this call the
device can still be used in polling mode.  This behavior required
by sys-manager to be able to complete the device power operation
sequence.

.. _`ps3_vuart_port_driver_register`:

ps3_vuart_port_driver_register
==============================

.. c:function:: int ps3_vuart_port_driver_register(struct ps3_vuart_port_driver *drv)

    Add a vuart port device driver.

    :param struct ps3_vuart_port_driver \*drv:
        *undescribed*

.. _`ps3_vuart_port_driver_unregister`:

ps3_vuart_port_driver_unregister
================================

.. c:function:: void ps3_vuart_port_driver_unregister(struct ps3_vuart_port_driver *drv)

    Remove a vuart port device driver.

    :param struct ps3_vuart_port_driver \*drv:
        *undescribed*

.. This file was automatic generated / don't edit.

