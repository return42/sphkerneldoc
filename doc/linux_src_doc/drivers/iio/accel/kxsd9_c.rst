.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/accel/kxsd9.c

.. _`kxsd9_state`:

struct kxsd9_state
==================

.. c:type:: struct kxsd9_state

    device related storage

.. _`kxsd9_state.definition`:

Definition
----------

.. code-block:: c

    struct kxsd9_state {
        struct mutex buf_lock;
        struct spi_device *us;
        u8 rx[KXSD9_STATE_RX_SIZE] ____cacheline_aligned;
        u8 tx[KXSD9_STATE_TX_SIZE];
    }

.. _`kxsd9_state.members`:

Members
-------

buf_lock
    protect the rx and tx buffers.

us
    spi device

rx
    single rx buffer storage

tx
    single tx buffer storage

.. This file was automatic generated / don't edit.

