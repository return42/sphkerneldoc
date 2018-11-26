.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/bestcomm/gen_bd.c

.. _`bcom_psc_gen_bd_rx_init`:

bcom_psc_gen_bd_rx_init
=======================

.. c:function:: struct bcom_task *bcom_psc_gen_bd_rx_init(unsigned psc_num, int queue_len, phys_addr_t fifo, int maxbufsize)

    Allocate a receive bcom_task for a PSC port

    :param psc_num:
        Number of the PSC to allocate a task for
    :type psc_num: unsigned

    :param queue_len:
        number of buffer descriptors to allocate for the task
    :type queue_len: int

    :param fifo:
        physical address of FIFO register
    :type fifo: phys_addr_t

    :param maxbufsize:
        Maximum receive data size in bytes.
    :type maxbufsize: int

.. _`bcom_psc_gen_bd_rx_init.description`:

Description
-----------

Allocate a bestcomm task structure for receiving data from a PSC.

.. _`bcom_psc_gen_bd_tx_init`:

bcom_psc_gen_bd_tx_init
=======================

.. c:function:: struct bcom_task *bcom_psc_gen_bd_tx_init(unsigned psc_num, int queue_len, phys_addr_t fifo)

    Allocate a transmit bcom_task for a PSC port

    :param psc_num:
        Number of the PSC to allocate a task for
    :type psc_num: unsigned

    :param queue_len:
        number of buffer descriptors to allocate for the task
    :type queue_len: int

    :param fifo:
        physical address of FIFO register
    :type fifo: phys_addr_t

.. _`bcom_psc_gen_bd_tx_init.description`:

Description
-----------

Allocate a bestcomm task structure for transmitting data to a PSC.

.. This file was automatic generated / don't edit.

