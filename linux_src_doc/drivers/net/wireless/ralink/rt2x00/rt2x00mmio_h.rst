.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ralink/rt2x00/rt2x00mmio.h

.. _`rt2x00mmio_regbusy_read`:

rt2x00mmio_regbusy_read
=======================

.. c:function:: int rt2x00mmio_regbusy_read(struct rt2x00_dev *rt2x00dev, const unsigned int offset, const struct rt2x00_field32 field, u32 *reg)

    Read from register with busy check

    :param rt2x00dev:
        Device pointer, see \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

    :param offset:
        Register offset
    :type offset: const unsigned int

    :param field:
        Field to check if register is busy
    :type field: const struct rt2x00_field32

    :param reg:
        Pointer to where register contents should be stored
    :type reg: u32 \*

.. _`rt2x00mmio_regbusy_read.description`:

Description
-----------

This function will read the given register, and checks if the
register is busy. If it is, it will sleep for a couple of
microseconds before reading the register again. If the register
is not read after a certain timeout, this function will return
FALSE.

.. _`queue_entry_priv_mmio`:

struct queue_entry_priv_mmio
============================

.. c:type:: struct queue_entry_priv_mmio

    Per entry PCI specific information

.. _`queue_entry_priv_mmio.definition`:

Definition
----------

.. code-block:: c

    struct queue_entry_priv_mmio {
        __le32 *desc;
        dma_addr_t desc_dma;
    }

.. _`queue_entry_priv_mmio.members`:

Members
-------

desc
    Pointer to device descriptor

desc_dma
    DMA pointer to \ :c:type:`struct desc <desc>`\ .

.. _`rt2x00mmio_rxdone`:

rt2x00mmio_rxdone
=================

.. c:function:: bool rt2x00mmio_rxdone(struct rt2x00_dev *rt2x00dev)

    Handle RX done events

    :param rt2x00dev:
        Device pointer, see \ :c:type:`struct rt2x00_dev <rt2x00_dev>`\ .
    :type rt2x00dev: struct rt2x00_dev \*

.. _`rt2x00mmio_rxdone.description`:

Description
-----------

Returns true if there are still rx frames pending and false if all
pending rx frames were processed.

.. _`rt2x00mmio_flush_queue`:

rt2x00mmio_flush_queue
======================

.. c:function:: void rt2x00mmio_flush_queue(struct data_queue *queue, bool drop)

    Flush data queue

    :param queue:
        Data queue to stop
    :type queue: struct data_queue \*

    :param drop:
        True to drop all pending frames.
    :type drop: bool

.. _`rt2x00mmio_flush_queue.description`:

Description
-----------

This will wait for a maximum of 100ms, waiting for the queues
to become empty.

.. This file was automatic generated / don't edit.

