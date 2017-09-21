.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/dma_port.c

.. _`tb_dma_port`:

struct tb_dma_port
==================

.. c:type:: struct tb_dma_port

    DMA control port

.. _`tb_dma_port.definition`:

Definition
----------

.. code-block:: c

    struct tb_dma_port {
        struct tb_switch *sw;
        u8 port;
        u32 base;
        u8 *buf;
    }

.. _`tb_dma_port.members`:

Members
-------

sw
    Switch the DMA port belongs to

port
    Switch port number where DMA capability is found

base
    Start offset of the mailbox registers

buf
    Temporary buffer to store a single block

.. _`dma_port_alloc`:

dma_port_alloc
==============

.. c:function:: struct tb_dma_port *dma_port_alloc(struct tb_switch *sw)

    Finds DMA control port from a switch pointed by route

    :param struct tb_switch \*sw:
        Switch from where find the DMA port

.. _`dma_port_alloc.description`:

Description
-----------

Function checks if the switch NHI port supports DMA configuration
based mailbox capability and if it does, allocates and initializes
DMA port structure. Returns \ ``NULL``\  if the capabity was not found.

The DMA control port is functional also when the switch is in safe
mode.

.. _`dma_port_free`:

dma_port_free
=============

.. c:function:: void dma_port_free(struct tb_dma_port *dma)

    Release DMA control port structure

    :param struct tb_dma_port \*dma:
        DMA control port

.. _`dma_port_flash_read`:

dma_port_flash_read
===================

.. c:function:: int dma_port_flash_read(struct tb_dma_port *dma, unsigned int address, void *buf, size_t size)

    Read from active flash region

    :param struct tb_dma_port \*dma:
        DMA control port

    :param unsigned int address:
        Address relative to the start of active region

    :param void \*buf:
        Buffer where the data is read

    :param size_t size:
        Size of the buffer

.. _`dma_port_flash_write`:

dma_port_flash_write
====================

.. c:function:: int dma_port_flash_write(struct tb_dma_port *dma, unsigned int address, const void *buf, size_t size)

    Write to non-active flash region

    :param struct tb_dma_port \*dma:
        DMA control port

    :param unsigned int address:
        Address relative to the start of non-active region

    :param const void \*buf:
        Data to write

    :param size_t size:
        Size of the buffer

.. _`dma_port_flash_write.description`:

Description
-----------

Writes block of data to the non-active flash region of the switch. If
the address is given as \ ``DMA_PORT_CSS_ADDRESS``\  the block is written
using CSS command.

.. _`dma_port_flash_update_auth`:

dma_port_flash_update_auth
==========================

.. c:function:: int dma_port_flash_update_auth(struct tb_dma_port *dma)

    Starts flash authenticate cycle

    :param struct tb_dma_port \*dma:
        DMA control port

.. _`dma_port_flash_update_auth.description`:

Description
-----------

Starts the flash update authentication cycle. If the image in the
non-active area was valid, the switch starts upgrade process where
active and non-active area get swapped in the end. Caller should call
\ :c:func:`dma_port_flash_update_auth_status`\  to get status of this command.
This is because if the switch in question is root switch the
thunderbolt host controller gets reset as well.

.. _`dma_port_flash_update_auth_status`:

dma_port_flash_update_auth_status
=================================

.. c:function:: int dma_port_flash_update_auth_status(struct tb_dma_port *dma, u32 *status)

    Reads status of update auth command

    :param struct tb_dma_port \*dma:
        DMA control port

    :param u32 \*status:
        Status code of the operation

.. _`dma_port_flash_update_auth_status.description`:

Description
-----------

The function checks if there is status available from the last update
auth command. Returns \ ``0``\  if there is no status and no further
action is required. If there is status, \ ``1``\  is returned instead and
\ ``status``\  holds the failure code.

Negative return means there was an error reading status from the
switch.

.. _`dma_port_power_cycle`:

dma_port_power_cycle
====================

.. c:function:: int dma_port_power_cycle(struct tb_dma_port *dma)

    Power cycles the switch

    :param struct tb_dma_port \*dma:
        DMA control port

.. _`dma_port_power_cycle.description`:

Description
-----------

Triggers power cycle to the switch.

.. This file was automatic generated / don't edit.

