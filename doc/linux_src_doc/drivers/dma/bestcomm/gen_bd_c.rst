.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/bestcomm/gen_bd.c

.. _`bcom_psc_gen_bd_rx_init`:

bcom_psc_gen_bd_rx_init
=======================

.. c:function:: struct bcom_task *bcom_psc_gen_bd_rx_init(unsigned psc_num, int queue_len, phys_addr_t fifo, int maxbufsize)

    Allocate a receive bcom_task for a PSC port

    :param unsigned psc_num:
        Number of the PSC to allocate a task for

    :param int queue_len:
        number of buffer descriptors to allocate for the task

    :param phys_addr_t fifo:
        physical address of FIFO register

    :param int maxbufsize:
        Maximum receive data size in bytes.

.. _`bcom_psc_gen_bd_rx_init.description`:

Description
-----------

Allocate a bestcomm task structure for receiving data from a PSC.

.. _`bcom_psc_gen_bd_tx_init`:

bcom_psc_gen_bd_tx_init
=======================

.. c:function:: struct bcom_task *bcom_psc_gen_bd_tx_init(unsigned psc_num, int queue_len, phys_addr_t fifo)

    Allocate a transmit bcom_task for a PSC port

    :param unsigned psc_num:
        Number of the PSC to allocate a task for

    :param int queue_len:
        number of buffer descriptors to allocate for the task

    :param phys_addr_t fifo:
        physical address of FIFO register

.. _`bcom_psc_gen_bd_tx_init.description`:

Description
-----------

Allocate a bestcomm task structure for transmitting data to a PSC.

.. This file was automatic generated / don't edit.

