.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/nvec/nvec.h

.. _`nvec_event_size`:

enum nvec_event_size
====================

.. c:type:: enum nvec_event_size

    The size of an event message

.. _`nvec_event_size.definition`:

Definition
----------

.. code-block:: c

    enum nvec_event_size {
        NVEC_2BYTES,
        NVEC_3BYTES,
        NVEC_VAR_SIZE
    };

.. _`nvec_event_size.constants`:

Constants
---------

NVEC_2BYTES
    The message has one command byte and one data byte

NVEC_3BYTES
    The message has one command byte and two data bytes

NVEC_VAR_SIZE
    The message has one command byte, one count byte, and has
    up to as many bytes as the number in the count byte. The
    maximum is 32

.. _`nvec_event_size.description`:

Description
-----------

Events can be fixed or variable sized. This is useless on other message
types, which are always variable sized.

.. _`nvec_msg_type`:

enum nvec_msg_type
==================

.. c:type:: enum nvec_msg_type

    The type of a message

.. _`nvec_msg_type.definition`:

Definition
----------

.. code-block:: c

    enum nvec_msg_type {
        NVEC_SYS,
        NVEC_BAT,
        NVEC_GPIO,
        NVEC_SLEEP,
        NVEC_KBD,
        NVEC_PS2,
        NVEC_CNTL,
        NVEC_OEM0,
        NVEC_KB_EVT,
        NVEC_PS2_EVT
    };

.. _`nvec_msg_type.constants`:

Constants
---------

NVEC_SYS
    A system request/response

NVEC_BAT
    A battery request/response

NVEC_GPIO
    *undescribed*

NVEC_SLEEP
    *undescribed*

NVEC_KBD
    A keyboard request/response

NVEC_PS2
    A mouse request/response

NVEC_CNTL
    A EC control request/response

NVEC_OEM0
    *undescribed*

NVEC_KB_EVT
    An event from the keyboard

NVEC_PS2_EVT
    An event from the mouse

.. _`nvec_msg_type.description`:

Description
-----------

Events can be fixed or variable sized. This is useless on other message
types, which are always variable sized.

.. _`nvec_msg`:

struct nvec_msg
===============

.. c:type:: struct nvec_msg

    A buffer for a single message

.. _`nvec_msg.definition`:

Definition
----------

.. code-block:: c

    struct nvec_msg {
        struct list_head node;
        unsigned char data[NVEC_MSG_SIZE];
        unsigned short size;
        unsigned short pos;
        atomic_t used;
    }

.. _`nvec_msg.members`:

Members
-------

node
    Messages are part of various lists in a \ :c:type:`struct nvec_chip <nvec_chip>`\ 

data
    The data of the message

size
    For TX messages, the number of bytes used in \ ``data``\ 

pos
    For RX messages, the current position to write to. For TX messages,
    the position to read from.

used
    Used for the message pool to mark a message as free/allocated.

.. _`nvec_msg.description`:

Description
-----------

This structure is used to hold outgoing and incoming messages. Outgoing
messages have a different format than incoming messages, and that is not
documented yet.

.. _`nvec_chip`:

struct nvec_chip
================

.. c:type:: struct nvec_chip

    A single connection to an NVIDIA Embedded controller

.. _`nvec_chip.definition`:

Definition
----------

.. code-block:: c

    struct nvec_chip {
        struct device *dev;
        struct gpio_desc *gpiod;
        int irq;
        u32 i2c_addr;
        void __iomem *base;
        struct clk *i2c_clk;
        struct reset_control *rst;
        struct atomic_notifier_head notifier_list;
        struct list_head rx_data, tx_data;
        struct notifier_block nvec_status_notifier;
        struct work_struct rx_work, tx_work;
        struct workqueue_struct *wq;
        struct nvec_msg msg_pool[NVEC_POOL_SIZE];
        struct nvec_msg *rx;
        struct nvec_msg *tx;
        struct nvec_msg tx_scratch;
        struct completion ec_transfer;
        spinlock_t tx_lock, rx_lock;
        struct mutex sync_write_mutex;
        struct completion sync_write;
        u16 sync_write_pending;
        struct nvec_msg *last_sync_msg;
        int state;
    }

.. _`nvec_chip.members`:

Members
-------

dev
    The device

gpiod
    *undescribed*

irq
    The IRQ of the I2C device

i2c_addr
    The address of the I2C slave

base
    The base of the memory mapped region of the I2C device

i2c_clk
    The clock of the I2C device

rst
    The reset of the I2C device

notifier_list
    Notifiers to be called on received messages, see
    \ :c:func:`nvec_register_notifier`\ 

rx_data
    Received messages that have to be processed

tx_data
    Messages waiting to be sent to the controller

nvec_status_notifier
    Internal notifier (see \ :c:func:`nvec_status_notifier`\ )

rx_work
    A work structure for the RX worker \ :c:func:`nvec_dispatch`\ 

tx_work
    A work structure for the TX worker \ :c:func:`nvec_request_master`\ 

wq
    The work queue in which \ ``rx_work``\  and \ ``tx_work``\  are executed

msg_pool
    A pool of messages for allocation

rx
    The message currently being retrieved or \ ``NULL``\ 

tx
    The message currently being transferred

tx_scratch
    Used for building pseudo messages

ec_transfer
    A completion that will be completed once a message has been
    received (see \ :c:func:`nvec_rx_completed`\ )

tx_lock
    Spinlock for modifications on \ ``tx_data``\ 

rx_lock
    Spinlock for modifications on \ ``rx_data``\ 

sync_write_mutex
    A mutex for \ :c:func:`nvec_write_sync`\ 

sync_write
    A completion to signal that a synchronous message is complete

sync_write_pending
    The first two bytes of the request (type and subtype)

last_sync_msg
    The last synchronous message.

state
    State of our finite state machine used in \ :c:func:`nvec_interrupt`\ 

.. This file was automatic generated / don't edit.

