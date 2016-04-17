.. -*- coding: utf-8; mode: rst -*-

============
shdma-base.h
============


.. _`shdma_ops`:

struct shdma_ops
================

.. c:type:: shdma_ops

    simple DMA driver operations


.. _`shdma_ops.definition`:

Definition
----------

.. code-block:: c

  struct shdma_ops {
  };


.. _`shdma_ops.members`:

Members
-------




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

