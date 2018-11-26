.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/sun4i-dma.c

.. _`__execute_vchan_pending`:

\__execute_vchan_pending
========================

.. c:function:: int __execute_vchan_pending(struct sun4i_dma_dev *priv, struct sun4i_dma_vchan *vchan)

    :param priv:
        *undescribed*
    :type priv: struct sun4i_dma_dev \*

    :param vchan:
        *undescribed*
    :type vchan: struct sun4i_dma_vchan \*

.. _`__execute_vchan_pending.description`:

Description
-----------

When given a vchan, this function will try to acquire a suitable
pchan and, if successful, will configure it to fulfill a promise
from the next pending contract.

This function must be called with \ :c:type:`vchan->vc <vchan>`\ .lock held.

.. _`generate_ndma_promise`:

generate_ndma_promise
=====================

.. c:function:: struct sun4i_dma_promise *generate_ndma_promise(struct dma_chan *chan, dma_addr_t src, dma_addr_t dest, size_t len, struct dma_slave_config *sconfig, enum dma_transfer_direction direction)

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

    :param src:
        *undescribed*
    :type src: dma_addr_t

    :param dest:
        *undescribed*
    :type dest: dma_addr_t

    :param len:
        *undescribed*
    :type len: size_t

    :param sconfig:
        *undescribed*
    :type sconfig: struct dma_slave_config \*

    :param direction:
        *undescribed*
    :type direction: enum dma_transfer_direction

.. _`generate_ndma_promise.description`:

Description
-----------

A NDMA promise contains all the information required to program the
normal part of the DMA Engine and get data copied. A non-executed
promise will live in the demands list on a contract. Once it has been
completed, it will be moved to the completed demands list for later freeing.
All linked promises will be freed when the corresponding contract is freed

.. _`generate_ddma_promise`:

generate_ddma_promise
=====================

.. c:function:: struct sun4i_dma_promise *generate_ddma_promise(struct dma_chan *chan, dma_addr_t src, dma_addr_t dest, size_t len, struct dma_slave_config *sconfig)

    :param chan:
        *undescribed*
    :type chan: struct dma_chan \*

    :param src:
        *undescribed*
    :type src: dma_addr_t

    :param dest:
        *undescribed*
    :type dest: dma_addr_t

    :param len:
        *undescribed*
    :type len: size_t

    :param sconfig:
        *undescribed*
    :type sconfig: struct dma_slave_config \*

.. _`generate_ddma_promise.description`:

Description
-----------

A DDMA promise contains all the information required to program the
Dedicated part of the DMA Engine and get data copied. A non-executed
promise will live in the demands list on a contract. Once it has been
completed, it will be moved to the completed demands list for later freeing.
All linked promises will be freed when the corresponding contract is freed

.. _`generate_dma_contract`:

generate_dma_contract
=====================

.. c:function:: struct sun4i_dma_contract *generate_dma_contract( void)

    :param void:
        no arguments
    :type void: 

.. _`generate_dma_contract.description`:

Description
-----------

Contracts function as DMA descriptors. As our hardware does not support
linked lists, we need to implement SG via software. We use a contract
to hold all the pieces of the request and process them serially one
after another. Each piece is represented as a promise.

.. _`get_next_cyclic_promise`:

get_next_cyclic_promise
=======================

.. c:function:: struct sun4i_dma_promise *get_next_cyclic_promise(struct sun4i_dma_contract *contract)

    :param contract:
        *undescribed*
    :type contract: struct sun4i_dma_contract \*

.. _`get_next_cyclic_promise.description`:

Description
-----------

Cyclic contracts contain a series of promises which are executed on a
loop. This function returns the next promise from a cyclic contract,
so it can be programmed into the hardware.

.. _`sun4i_dma_free_contract`:

sun4i_dma_free_contract
=======================

.. c:function:: void sun4i_dma_free_contract(struct virt_dma_desc *vd)

    :param vd:
        *undescribed*
    :type vd: struct virt_dma_desc \*

.. This file was automatic generated / don't edit.

