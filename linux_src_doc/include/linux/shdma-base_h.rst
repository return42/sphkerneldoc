.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/shdma-base.h

.. _`shdma_ops`:

struct shdma_ops
================

.. c:type:: struct shdma_ops

    simple DMA driver operations

.. _`shdma_ops.definition`:

Definition
----------

.. code-block:: c

    struct shdma_ops {
        bool (*desc_completed)(struct shdma_chan *, struct shdma_desc *);
        void (*halt_channel)(struct shdma_chan *);
        bool (*channel_busy)(struct shdma_chan *);
        dma_addr_t (*slave_addr)(struct shdma_chan *);
        int (*desc_setup)(struct shdma_chan *, struct shdma_desc *,dma_addr_t, dma_addr_t, size_t *);
        int (*set_slave)(struct shdma_chan *, int, dma_addr_t, bool);
        void (*setup_xfer)(struct shdma_chan *, int);
        void (*start_xfer)(struct shdma_chan *, struct shdma_desc *);
        struct shdma_desc *(*embedded_desc)(void *, int);
        bool (*chan_irq)(struct shdma_chan *, int);
        size_t (*get_partial)(struct shdma_chan *, struct shdma_desc *);
    }

.. _`shdma_ops.members`:

Members
-------

desc_completed
    *undescribed*

halt_channel
    *undescribed*

channel_busy
    *undescribed*

slave_addr
    *undescribed*

desc_setup
    *undescribed*

set_slave
    *undescribed*

setup_xfer
    *undescribed*

start_xfer
    *undescribed*

embedded_desc
    *undescribed*

chan_irq
    *undescribed*

get_partial
    *undescribed*

.. _`shdma_ops.desc_completed`:

desc_completed
--------------

return true, if this is the descriptor, that just has
completed (atomic)

.. _`shdma_ops.halt_channel`:

halt_channel
------------

stop DMA channel operation (atomic)

.. _`shdma_ops.channel_busy`:

channel_busy
------------

return true, if the channel is busy (atomic)

.. _`shdma_ops.slave_addr`:

slave_addr
----------

return slave DMA address

.. _`shdma_ops.desc_setup`:

desc_setup
----------

set up the hardware specific descriptor portion (atomic)

.. _`shdma_ops.set_slave`:

set_slave
---------

bind channel to a slave

.. _`shdma_ops.setup_xfer`:

setup_xfer
----------

configure channel hardware for operation (atomic)

.. _`shdma_ops.start_xfer`:

start_xfer
----------

start the DMA transfer (atomic)

.. _`shdma_ops.embedded_desc`:

embedded_desc
-------------

return Nth struct shdma_desc pointer from the
descriptor array

.. _`shdma_ops.chan_irq`:

chan_irq
--------

process channel IRQ, return true if a transfer has
completed (atomic)

.. This file was automatic generated / don't edit.

