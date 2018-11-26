.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/dma.c

.. _`dma-and-interrupt-masking-functions`:

DMA and interrupt masking functions
===================================

Here we setup descriptor pointers (rxdp/txdp) start/stop dma engine and
handle queue setup for 5210 chipset (rest are handled on qcu.c).
Also we setup interrupt mask register (IMR) and read the various interrupt
status registers (ISR).

.. _`ath5k_hw_start_rx_dma`:

ath5k_hw_start_rx_dma
=====================

.. c:function:: void ath5k_hw_start_rx_dma(struct ath5k_hw *ah)

    Start DMA receive

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_stop_rx_dma`:

ath5k_hw_stop_rx_dma
====================

.. c:function:: int ath5k_hw_stop_rx_dma(struct ath5k_hw *ah)

    Stop DMA receive

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_get_rxdp`:

ath5k_hw_get_rxdp
=================

.. c:function:: u32 ath5k_hw_get_rxdp(struct ath5k_hw *ah)

    Get RX Descriptor's address

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_set_rxdp`:

ath5k_hw_set_rxdp
=================

.. c:function:: int ath5k_hw_set_rxdp(struct ath5k_hw *ah, u32 phys_addr)

    Set RX Descriptor's address

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param phys_addr:
        RX descriptor address
    :type phys_addr: u32

.. _`ath5k_hw_set_rxdp.description`:

Description
-----------

Returns -EIO if rx is active

.. _`ath5k_hw_start_tx_dma`:

ath5k_hw_start_tx_dma
=====================

.. c:function:: int ath5k_hw_start_tx_dma(struct ath5k_hw *ah, unsigned int queue)

    Start DMA transmit for a specific queue

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        The hw queue number
    :type queue: unsigned int

.. _`ath5k_hw_start_tx_dma.description`:

Description
-----------

Start DMA transmit for a specific queue and since 5210 doesn't have
QCU/DCU, set up queue parameters for 5210 here based on queue type (one
queue for normal data and one queue for beacons). For queue setup
on newer chips check out qcu.c. Returns -EINVAL if queue number is out
of range or if queue is already disabled.

.. _`ath5k_hw_start_tx_dma.note`:

NOTE
----

Must be called after setting up tx control descriptor for that
queue (see below).

.. _`ath5k_hw_stop_tx_dma`:

ath5k_hw_stop_tx_dma
====================

.. c:function:: int ath5k_hw_stop_tx_dma(struct ath5k_hw *ah, unsigned int queue)

    Stop DMA transmit on a specific queue

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        The hw queue number
    :type queue: unsigned int

.. _`ath5k_hw_stop_tx_dma.description`:

Description
-----------

Stop DMA transmit on a specific hw queue and drain queue so we don't
have any pending frames. Returns -EBUSY if we still have pending frames,
-EINVAL if queue number is out of range or inactive.

.. _`ath5k_hw_stop_beacon_queue`:

ath5k_hw_stop_beacon_queue
==========================

.. c:function:: int ath5k_hw_stop_beacon_queue(struct ath5k_hw *ah, unsigned int queue)

    Stop beacon queue

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        The queue number
    :type queue: unsigned int

.. _`ath5k_hw_stop_beacon_queue.description`:

Description
-----------

Returns -EIO if queue didn't stop

.. _`ath5k_hw_get_txdp`:

ath5k_hw_get_txdp
=================

.. c:function:: u32 ath5k_hw_get_txdp(struct ath5k_hw *ah, unsigned int queue)

    Get TX Descriptor's address for a specific queue

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        The hw queue number
    :type queue: unsigned int

.. _`ath5k_hw_get_txdp.description`:

Description
-----------

Get TX descriptor's address for a specific queue. For 5210 we ignore
the queue number and use tx queue type since we only have 2 queues.
We use TXDP0 for normal data queue and TXDP1 for beacon queue.
For newer chips with QCU/DCU we just read the corresponding TXDP register.

.. _`ath5k_hw_get_txdp.xxx`:

XXX
---

Is TXDP read and clear ?

.. _`ath5k_hw_set_txdp`:

ath5k_hw_set_txdp
=================

.. c:function:: int ath5k_hw_set_txdp(struct ath5k_hw *ah, unsigned int queue, u32 phys_addr)

    Set TX Descriptor's address for a specific queue

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param queue:
        The hw queue number
    :type queue: unsigned int

    :param phys_addr:
        The physical address
    :type phys_addr: u32

.. _`ath5k_hw_set_txdp.description`:

Description
-----------

Set TX descriptor's address for a specific queue. For 5210 we ignore
the queue number and we use tx queue type since we only have 2 queues
so as above we use TXDP0 for normal data queue and TXDP1 for beacon queue.
For newer chips with QCU/DCU we just set the corresponding TXDP register.
Returns -EINVAL if queue type is invalid for 5210 and -EIO if queue is still
active.

.. _`ath5k_hw_update_tx_triglevel`:

ath5k_hw_update_tx_triglevel
============================

.. c:function:: int ath5k_hw_update_tx_triglevel(struct ath5k_hw *ah, bool increase)

    Update tx trigger level

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param increase:
        Flag to force increase of trigger level
    :type increase: bool

.. _`ath5k_hw_update_tx_triglevel.description`:

Description
-----------

This function increases/decreases the tx trigger level for the tx fifo
buffer (aka FIFO threshold) that is used to indicate when PCU flushes
the buffer and transmits its data. Lowering this results sending small
frames more quickly but can lead to tx underruns, raising it a lot can
result other problems. Right now we start with the lowest possible
(64Bytes) and if we get tx underrun we increase it using the increase
flag. Returns -EIO if we have reached maximum/minimum.

.. _`ath5k_hw_update_tx_triglevel.xxx`:

XXX
---

Link this with tx DMA size ?

.. _`ath5k_hw_update_tx_triglevel.xxx2`:

XXX2
----

Use it to save interrupts ?

.. _`ath5k_hw_is_intr_pending`:

ath5k_hw_is_intr_pending
========================

.. c:function:: bool ath5k_hw_is_intr_pending(struct ath5k_hw *ah)

    Check if we have pending interrupts

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_is_intr_pending.description`:

Description
-----------

Check if we have pending interrupts to process. Returns 1 if we
have pending interrupts and 0 if we haven't.

.. _`ath5k_hw_get_isr`:

ath5k_hw_get_isr
================

.. c:function:: int ath5k_hw_get_isr(struct ath5k_hw *ah, enum ath5k_int *interrupt_mask)

    Get interrupt status

    :param ah:
        The \ ``struct``\  ath5k_hw
    :type ah: struct ath5k_hw \*

    :param interrupt_mask:
        Driver's interrupt mask used to filter out
        interrupts in sw.
    :type interrupt_mask: enum ath5k_int \*

.. _`ath5k_hw_get_isr.description`:

Description
-----------

This function is used inside our interrupt handler to determine the reason
for the interrupt by reading Primary Interrupt Status Register. Returns an
abstract interrupt status mask which is mostly ISR with some uncommon bits
being mapped on some standard non hw-specific positions
(check out \ :c:type:`struct ath5k_int <ath5k_int>`\ ).

.. _`ath5k_hw_get_isr.note`:

NOTE
----

We do write-to-clear, so the active PISR/SISR bits at the time this
function gets called are cleared on return.

.. _`ath5k_hw_set_imr`:

ath5k_hw_set_imr
================

.. c:function:: enum ath5k_int ath5k_hw_set_imr(struct ath5k_hw *ah, enum ath5k_int new_mask)

    Set interrupt mask

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param new_mask:
        The new interrupt mask to be set
    :type new_mask: enum ath5k_int

.. _`ath5k_hw_set_imr.description`:

Description
-----------

Set the interrupt mask in hw to save interrupts. We do that by mapping
ath5k_int bits to hw-specific bits to remove abstraction and writing
Interrupt Mask Register.

.. _`ath5k_hw_dma_init`:

ath5k_hw_dma_init
=================

.. c:function:: void ath5k_hw_dma_init(struct ath5k_hw *ah)

    Initialize DMA unit

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_dma_init.description`:

Description
-----------

Set DMA size and pre-enable interrupts
(driver handles tx/rx buffer setup and
dma start/stop)

.. _`ath5k_hw_dma_init.xxx`:

XXX
---

Save/restore RXDP/TXDP registers ?

.. _`ath5k_hw_dma_stop`:

ath5k_hw_dma_stop
=================

.. c:function:: int ath5k_hw_dma_stop(struct ath5k_hw *ah)

    stop DMA unit

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_dma_stop.description`:

Description
-----------

Stop tx/rx DMA and interrupts. Returns
-EBUSY if tx or rx dma failed to stop.

.. _`ath5k_hw_dma_stop.xxx`:

XXX
---

Sometimes DMA unit hangs and we have
stuck frames on tx queues, only a reset
can fix that.

.. This file was automatic generated / don't edit.

