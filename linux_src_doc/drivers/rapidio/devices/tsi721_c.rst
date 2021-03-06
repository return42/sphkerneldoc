.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rapidio/devices/tsi721.c

.. _`tsi721_lcread`:

tsi721_lcread
=============

.. c:function:: int tsi721_lcread(struct rio_mport *mport, int index, u32 offset, int len, u32 *data)

    read from local SREP config space

    :param mport:
        RapidIO master port info
    :type mport: struct rio_mport \*

    :param index:
        ID of RapdiIO interface
    :type index: int

    :param offset:
        Offset into configuration space
    :type offset: u32

    :param len:
        Length (in bytes) of the maintenance transaction
    :type len: int

    :param data:
        Value to be read into
    :type data: u32 \*

.. _`tsi721_lcread.description`:

Description
-----------

Generates a local SREP space read. Returns \ ``0``\  on
success or \ ``-EINVAL``\  on failure.

.. _`tsi721_lcwrite`:

tsi721_lcwrite
==============

.. c:function:: int tsi721_lcwrite(struct rio_mport *mport, int index, u32 offset, int len, u32 data)

    write into local SREP config space

    :param mport:
        RapidIO master port info
    :type mport: struct rio_mport \*

    :param index:
        ID of RapdiIO interface
    :type index: int

    :param offset:
        Offset into configuration space
    :type offset: u32

    :param len:
        Length (in bytes) of the maintenance transaction
    :type len: int

    :param data:
        Value to be written
    :type data: u32

.. _`tsi721_lcwrite.description`:

Description
-----------

Generates a local write into SREP configuration space. Returns \ ``0``\  on
success or \ ``-EINVAL``\  on failure.

.. _`tsi721_maint_dma`:

tsi721_maint_dma
================

.. c:function:: int tsi721_maint_dma(struct tsi721_device *priv, u32 sys_size, u16 destid, u8 hopcount, u32 offset, int len, u32 *data, int do_wr)

    Helper function to generate RapidIO maintenance transactions using designated Tsi721 DMA channel.

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

    :param sys_size:
        RapdiIO transport system size
    :type sys_size: u32

    :param destid:
        Destination ID of transaction
    :type destid: u16

    :param hopcount:
        Number of hops to target device
    :type hopcount: u8

    :param offset:
        Offset into configuration space
    :type offset: u32

    :param len:
        Length (in bytes) of the maintenance transaction
    :type len: int

    :param data:
        Location to be read from or write into
    :type data: u32 \*

    :param do_wr:
        Operation flag (1 == MAINT_WR)
    :type do_wr: int

.. _`tsi721_maint_dma.description`:

Description
-----------

Generates a RapidIO maintenance transaction (Read or Write).
Returns \ ``0``\  on success and \ ``-EINVAL``\  or \ ``-EFAULT``\  on failure.

.. _`tsi721_cread_dma`:

tsi721_cread_dma
================

.. c:function:: int tsi721_cread_dma(struct rio_mport *mport, int index, u16 destid, u8 hopcount, u32 offset, int len, u32 *data)

    Generate a RapidIO maintenance read transaction using Tsi721 BDMA engine.

    :param mport:
        RapidIO master port control structure
    :type mport: struct rio_mport \*

    :param index:
        ID of RapdiIO interface
    :type index: int

    :param destid:
        Destination ID of transaction
    :type destid: u16

    :param hopcount:
        Number of hops to target device
    :type hopcount: u8

    :param offset:
        Offset into configuration space
    :type offset: u32

    :param len:
        Length (in bytes) of the maintenance transaction
    :type len: int

    :param data:
        *undescribed*
    :type data: u32 \*

.. _`tsi721_cread_dma.description`:

Description
-----------

Generates a RapidIO maintenance read transaction.
Returns \ ``0``\  on success and \ ``-EINVAL``\  or \ ``-EFAULT``\  on failure.

.. _`tsi721_cwrite_dma`:

tsi721_cwrite_dma
=================

.. c:function:: int tsi721_cwrite_dma(struct rio_mport *mport, int index, u16 destid, u8 hopcount, u32 offset, int len, u32 data)

    Generate a RapidIO maintenance write transaction using Tsi721 BDMA engine

    :param mport:
        RapidIO master port control structure
    :type mport: struct rio_mport \*

    :param index:
        ID of RapdiIO interface
    :type index: int

    :param destid:
        Destination ID of transaction
    :type destid: u16

    :param hopcount:
        Number of hops to target device
    :type hopcount: u8

    :param offset:
        Offset into configuration space
    :type offset: u32

    :param len:
        Length (in bytes) of the maintenance transaction
    :type len: int

    :param data:
        *undescribed*
    :type data: u32

.. _`tsi721_cwrite_dma.description`:

Description
-----------

Generates a RapidIO maintenance write transaction.
Returns \ ``0``\  on success and \ ``-EINVAL``\  or \ ``-EFAULT``\  on failure.

.. _`tsi721_pw_handler`:

tsi721_pw_handler
=================

.. c:function:: int tsi721_pw_handler(struct tsi721_device *priv)

    Tsi721 inbound port-write interrupt handler

    :param priv:
        tsi721 device private structure
    :type priv: struct tsi721_device \*

.. _`tsi721_pw_handler.description`:

Description
-----------

Handles inbound port-write interrupts. Copies PW message from an internal
buffer into PW message FIFO and schedules deferred routine to process
queued messages.

.. _`tsi721_pw_enable`:

tsi721_pw_enable
================

.. c:function:: int tsi721_pw_enable(struct rio_mport *mport, int enable)

    enable/disable port-write interface init

    :param mport:
        Master port implementing the port write unit
    :type mport: struct rio_mport \*

    :param enable:
        1=enable; 0=disable port-write message handling
    :type enable: int

.. _`tsi721_dsend`:

tsi721_dsend
============

.. c:function:: int tsi721_dsend(struct rio_mport *mport, int index, u16 destid, u16 data)

    Send a RapidIO doorbell

    :param mport:
        RapidIO master port info
    :type mport: struct rio_mport \*

    :param index:
        ID of RapidIO interface
    :type index: int

    :param destid:
        Destination ID of target device
    :type destid: u16

    :param data:
        16-bit info field of RapidIO doorbell
    :type data: u16

.. _`tsi721_dsend.description`:

Description
-----------

Sends a RapidIO doorbell message. Always returns \ ``0``\ .

.. _`tsi721_dbell_handler`:

tsi721_dbell_handler
====================

.. c:function:: int tsi721_dbell_handler(struct tsi721_device *priv)

    Tsi721 doorbell interrupt handler

    :param priv:
        tsi721 device-specific data structure
    :type priv: struct tsi721_device \*

.. _`tsi721_dbell_handler.description`:

Description
-----------

Handles inbound doorbell interrupts. Copies doorbell entry from an internal
buffer into DB message FIFO and schedules deferred  routine to process
queued DBs.

.. _`tsi721_irqhandler`:

tsi721_irqhandler
=================

.. c:function:: irqreturn_t tsi721_irqhandler(int irq, void *ptr)

    Tsi721 interrupt handler

    :param irq:
        Linux interrupt number
    :type irq: int

    :param ptr:
        Pointer to interrupt-specific data (tsi721_device structure)
    :type ptr: void \*

.. _`tsi721_irqhandler.description`:

Description
-----------

Handles Tsi721 interrupts signaled using MSI and INTA. Checks reported
interrupt events and calls an event-specific handler(s).

.. _`tsi721_omsg_msix`:

tsi721_omsg_msix
================

.. c:function:: irqreturn_t tsi721_omsg_msix(int irq, void *ptr)

    MSI-X interrupt handler for outbound messaging

    :param irq:
        Linux interrupt number
    :type irq: int

    :param ptr:
        Pointer to interrupt-specific data (tsi721_device structure)
    :type ptr: void \*

.. _`tsi721_omsg_msix.description`:

Description
-----------

Handles outbound messaging interrupts signaled using MSI-X.

.. _`tsi721_imsg_msix`:

tsi721_imsg_msix
================

.. c:function:: irqreturn_t tsi721_imsg_msix(int irq, void *ptr)

    MSI-X interrupt handler for inbound messaging

    :param irq:
        Linux interrupt number
    :type irq: int

    :param ptr:
        Pointer to interrupt-specific data (tsi721_device structure)
    :type ptr: void \*

.. _`tsi721_imsg_msix.description`:

Description
-----------

Handles inbound messaging interrupts signaled using MSI-X.

.. _`tsi721_srio_msix`:

tsi721_srio_msix
================

.. c:function:: irqreturn_t tsi721_srio_msix(int irq, void *ptr)

    Tsi721 MSI-X SRIO MAC interrupt handler

    :param irq:
        Linux interrupt number
    :type irq: int

    :param ptr:
        Pointer to interrupt-specific data (tsi721_device structure)
    :type ptr: void \*

.. _`tsi721_srio_msix.description`:

Description
-----------

Handles Tsi721 interrupts from SRIO MAC.

.. _`tsi721_sr2pc_ch_msix`:

tsi721_sr2pc_ch_msix
====================

.. c:function:: irqreturn_t tsi721_sr2pc_ch_msix(int irq, void *ptr)

    Tsi721 MSI-X SR2PC Channel interrupt handler

    :param irq:
        Linux interrupt number
    :type irq: int

    :param ptr:
        Pointer to interrupt-specific data (tsi721_device structure)
    :type ptr: void \*

.. _`tsi721_sr2pc_ch_msix.description`:

Description
-----------

Handles Tsi721 interrupts from SR2PC Channel.

.. _`tsi721_sr2pc_ch_msix.note`:

NOTE
----

At this moment services only one SR2PC channel associated with inbound
doorbells.

.. _`tsi721_request_msix`:

tsi721_request_msix
===================

.. c:function:: int tsi721_request_msix(struct tsi721_device *priv)

    register interrupt service for MSI-X mode.

    :param priv:
        tsi721 device-specific data structure
    :type priv: struct tsi721_device \*

.. _`tsi721_request_msix.description`:

Description
-----------

Registers MSI-X interrupt service routines for interrupts that are active
immediately after mport initialization. Messaging interrupt service routines
should be registered during corresponding open requests.

.. _`tsi721_enable_msix`:

tsi721_enable_msix
==================

.. c:function:: int tsi721_enable_msix(struct tsi721_device *priv)

    Attempts to enable MSI-X support for Tsi721.

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

.. _`tsi721_enable_msix.description`:

Description
-----------

Configures MSI-X support for Tsi721. Supports only an exact number
of requested vectors.

.. _`tsi721_init_pc2sr_mapping`:

tsi721_init_pc2sr_mapping
=========================

.. c:function:: void tsi721_init_pc2sr_mapping(struct tsi721_device *priv)

    initializes outbound (PCIe->SRIO) translation regions.

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

.. _`tsi721_init_pc2sr_mapping.description`:

Description
-----------

Disables SREP translation regions.

.. _`tsi721_rio_map_inb_mem`:

tsi721_rio_map_inb_mem
======================

.. c:function:: int tsi721_rio_map_inb_mem(struct rio_mport *mport, dma_addr_t lstart, u64 rstart, u64 size, u32 flags)

    - Mapping inbound memory region.

    :param mport:
        RapidIO master port
    :type mport: struct rio_mport \*

    :param lstart:
        Local memory space start address.
    :type lstart: dma_addr_t

    :param rstart:
        RapidIO space start address.
    :type rstart: u64

    :param size:
        The mapping region size.
    :type size: u64

    :param flags:
        Flags for mapping. 0 for using default flags.
    :type flags: u32

.. _`tsi721_rio_map_inb_mem.return`:

Return
------

0 -- Success.

This function will create the inbound mapping
from rstart to lstart.

.. _`tsi721_rio_unmap_inb_mem`:

tsi721_rio_unmap_inb_mem
========================

.. c:function:: void tsi721_rio_unmap_inb_mem(struct rio_mport *mport, dma_addr_t lstart)

    - Unmapping inbound memory region.

    :param mport:
        RapidIO master port
    :type mport: struct rio_mport \*

    :param lstart:
        Local memory space start address.
    :type lstart: dma_addr_t

.. _`tsi721_init_sr2pc_mapping`:

tsi721_init_sr2pc_mapping
=========================

.. c:function:: void tsi721_init_sr2pc_mapping(struct tsi721_device *priv)

    initializes inbound (SRIO->PCIe) translation regions.

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

.. _`tsi721_init_sr2pc_mapping.description`:

Description
-----------

Disables inbound windows.

.. _`tsi721_port_write_init`:

tsi721_port_write_init
======================

.. c:function:: int tsi721_port_write_init(struct tsi721_device *priv)

    Inbound port write interface init

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

.. _`tsi721_port_write_init.description`:

Description
-----------

Initializes inbound port write handler.
Returns \ ``0``\  on success or \ ``-ENOMEM``\  on failure.

.. _`tsi721_bdma_maint_init`:

tsi721_bdma_maint_init
======================

.. c:function:: int tsi721_bdma_maint_init(struct tsi721_device *priv)

    Initialize maintenance request BDMA channel.

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

.. _`tsi721_bdma_maint_init.description`:

Description
-----------

Initialize BDMA channel allocated for RapidIO maintenance read/write
request generation
Returns \ ``0``\  on success or \ ``-ENOMEM``\  on failure.

.. _`tsi721_add_outb_message`:

tsi721_add_outb_message
=======================

.. c:function:: int tsi721_add_outb_message(struct rio_mport *mport, struct rio_dev *rdev, int mbox, void *buffer, size_t len)

    Add message to the Tsi721 outbound message queue

    :param mport:
        Master port with outbound message queue
    :type mport: struct rio_mport \*

    :param rdev:
        Target of outbound message
    :type rdev: struct rio_dev \*

    :param mbox:
        Outbound mailbox
    :type mbox: int

    :param buffer:
        Message to add to outbound queue
    :type buffer: void \*

    :param len:
        Length of message
    :type len: size_t

.. _`tsi721_omsg_handler`:

tsi721_omsg_handler
===================

.. c:function:: void tsi721_omsg_handler(struct tsi721_device *priv, int ch)

    Outbound Message Interrupt Handler

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

    :param ch:
        number of OB MSG channel to service
    :type ch: int

.. _`tsi721_omsg_handler.description`:

Description
-----------

Services channel interrupts from outbound messaging engine.

.. _`tsi721_open_outb_mbox`:

tsi721_open_outb_mbox
=====================

.. c:function:: int tsi721_open_outb_mbox(struct rio_mport *mport, void *dev_id, int mbox, int entries)

    Initialize Tsi721 outbound mailbox

    :param mport:
        Master port implementing Outbound Messaging Engine
    :type mport: struct rio_mport \*

    :param dev_id:
        Device specific pointer to pass on event
    :type dev_id: void \*

    :param mbox:
        Mailbox to open
    :type mbox: int

    :param entries:
        Number of entries in the outbound mailbox ring
    :type entries: int

.. _`tsi721_close_outb_mbox`:

tsi721_close_outb_mbox
======================

.. c:function:: void tsi721_close_outb_mbox(struct rio_mport *mport, int mbox)

    Close Tsi721 outbound mailbox

    :param mport:
        Master port implementing the outbound message unit
    :type mport: struct rio_mport \*

    :param mbox:
        Mailbox to close
    :type mbox: int

.. _`tsi721_imsg_handler`:

tsi721_imsg_handler
===================

.. c:function:: void tsi721_imsg_handler(struct tsi721_device *priv, int ch)

    Inbound Message Interrupt Handler

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

    :param ch:
        inbound message channel number to service
    :type ch: int

.. _`tsi721_imsg_handler.description`:

Description
-----------

Services channel interrupts from inbound messaging engine.

.. _`tsi721_open_inb_mbox`:

tsi721_open_inb_mbox
====================

.. c:function:: int tsi721_open_inb_mbox(struct rio_mport *mport, void *dev_id, int mbox, int entries)

    Initialize Tsi721 inbound mailbox

    :param mport:
        Master port implementing the Inbound Messaging Engine
    :type mport: struct rio_mport \*

    :param dev_id:
        Device specific pointer to pass on event
    :type dev_id: void \*

    :param mbox:
        Mailbox to open
    :type mbox: int

    :param entries:
        Number of entries in the inbound mailbox ring
    :type entries: int

.. _`tsi721_close_inb_mbox`:

tsi721_close_inb_mbox
=====================

.. c:function:: void tsi721_close_inb_mbox(struct rio_mport *mport, int mbox)

    Shut down Tsi721 inbound mailbox

    :param mport:
        Master port implementing the Inbound Messaging Engine
    :type mport: struct rio_mport \*

    :param mbox:
        Mailbox to close
    :type mbox: int

.. _`tsi721_add_inb_buffer`:

tsi721_add_inb_buffer
=====================

.. c:function:: int tsi721_add_inb_buffer(struct rio_mport *mport, int mbox, void *buf)

    Add buffer to the Tsi721 inbound message queue

    :param mport:
        Master port implementing the Inbound Messaging Engine
    :type mport: struct rio_mport \*

    :param mbox:
        Inbound mailbox number
    :type mbox: int

    :param buf:
        Buffer to add to inbound queue
    :type buf: void \*

.. _`tsi721_get_inb_message`:

tsi721_get_inb_message
======================

.. c:function:: void *tsi721_get_inb_message(struct rio_mport *mport, int mbox)

    Fetch inbound message from the Tsi721 MSG Queue

    :param mport:
        Master port implementing the Inbound Messaging Engine
    :type mport: struct rio_mport \*

    :param mbox:
        Inbound mailbox number
    :type mbox: int

.. _`tsi721_get_inb_message.description`:

Description
-----------

Returns pointer to the message on success or NULL on failure.

.. _`tsi721_messages_init`:

tsi721_messages_init
====================

.. c:function:: int tsi721_messages_init(struct tsi721_device *priv)

    Initialization of Messaging Engine

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

.. _`tsi721_messages_init.description`:

Description
-----------

Configures Tsi721 messaging engine.

.. _`tsi721_query_mport`:

tsi721_query_mport
==================

.. c:function:: int tsi721_query_mport(struct rio_mport *mport, struct rio_mport_attr *attr)

    Fetch inbound message from the Tsi721 MSG Queue

    :param mport:
        Master port implementing the Inbound Messaging Engine
    :type mport: struct rio_mport \*

    :param attr:
        *undescribed*
    :type attr: struct rio_mport_attr \*

.. _`tsi721_query_mport.description`:

Description
-----------

Returns pointer to the message on success or NULL on failure.

.. _`tsi721_disable_ints`:

tsi721_disable_ints
===================

.. c:function:: void tsi721_disable_ints(struct tsi721_device *priv)

    disables all device interrupts

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

.. _`tsi721_setup_mport`:

tsi721_setup_mport
==================

.. c:function:: int tsi721_setup_mport(struct tsi721_device *priv)

    Setup Tsi721 as RapidIO subsystem master port

    :param priv:
        pointer to tsi721 private data
    :type priv: struct tsi721_device \*

.. _`tsi721_setup_mport.description`:

Description
-----------

Configures Tsi721 as RapidIO master port.

.. This file was automatic generated / don't edit.

