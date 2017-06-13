.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ks7010/ks7010_sdio.h

.. _`ks_sdio_card`:

struct ks_sdio_card
===================

.. c:type:: struct ks_sdio_card

    SDIO device data.

.. _`ks_sdio_card.definition`:

Definition
----------

.. code-block:: c

    struct ks_sdio_card {
        struct sdio_func *func;
        struct ks_wlan_private *priv;
    }

.. _`ks_sdio_card.members`:

Members
-------

func
    Pointer to the SDIO function device.

priv
    Pointer to the \ :c:type:`struct net_device <net_device>`\  private data.

.. _`ks_sdio_card.description`:

Description
-----------

Structure is used as the \ :c:type:`struct sdio_func <sdio_func>`\  private data.

.. _`tx_device_buffer`:

struct tx_device_buffer
=======================

.. c:type:: struct tx_device_buffer

    Queue item for the tx queue.

.. _`tx_device_buffer.definition`:

Definition
----------

.. code-block:: c

    struct tx_device_buffer {
        unsigned char *sendp;
        unsigned int size;
        void (*complete_handler)(struct ks_wlan_private *priv, struct sk_buff *skb);
        struct sk_buff *skb;
    }

.. _`tx_device_buffer.members`:

Members
-------

sendp
    Pointer to the send request data.

size
    Size of \ ``sendp``\  data.

complete_handler
    Function called once data write to device is complete.

skb
    *undescribed*

.. _`tx_device`:

struct tx_device
================

.. c:type:: struct tx_device

    Tx buffer queue.

.. _`tx_device.definition`:

Definition
----------

.. code-block:: c

    struct tx_device {
        struct tx_device_buffer tx_dev_buff;
        unsigned int qhead;
        unsigned int qtail;
        spinlock_t tx_dev_lock;
    }

.. _`tx_device.members`:

Members
-------

tx_dev_buff
    *undescribed*

qhead
    Head of tx queue.

qtail
    Tail of tx queue.

tx_dev_lock
    Queue lock.

.. _`rx_device_buffer`:

struct rx_device_buffer
=======================

.. c:type:: struct rx_device_buffer

    Queue item for the rx queue.

.. _`rx_device_buffer.definition`:

Definition
----------

.. code-block:: c

    struct rx_device_buffer {
        unsigned char data;
        unsigned int size;
    }

.. _`rx_device_buffer.members`:

Members
-------

data
    rx data.

size
    Size of \ ``data``\ .

.. _`rx_device`:

struct rx_device
================

.. c:type:: struct rx_device

    Rx buffer queue.

.. _`rx_device.definition`:

Definition
----------

.. code-block:: c

    struct rx_device {
        struct rx_device_buffer rx_dev_buff;
        unsigned int qhead;
        unsigned int qtail;
        spinlock_t rx_dev_lock;
    }

.. _`rx_device.members`:

Members
-------

rx_dev_buff
    *undescribed*

qhead
    Head of rx queue.

qtail
    Tail of rx queue.

rx_dev_lock
    Queue lock.

.. This file was automatic generated / don't edit.

