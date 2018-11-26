.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/sysdev/fsl_rmu.c

.. _`fsl_rio_tx_handler`:

fsl_rio_tx_handler
==================

.. c:function:: irqreturn_t fsl_rio_tx_handler(int irq, void *dev_instance)

    MPC85xx outbound message interrupt handler

    :param irq:
        Linux interrupt number
    :type irq: int

    :param dev_instance:
        Pointer to interrupt-specific data
    :type dev_instance: void \*

.. _`fsl_rio_tx_handler.description`:

Description
-----------

Handles outbound message interrupts. Executes a register outbound
mailbox event handler and acks the interrupt occurrence.

.. _`fsl_rio_rx_handler`:

fsl_rio_rx_handler
==================

.. c:function:: irqreturn_t fsl_rio_rx_handler(int irq, void *dev_instance)

    MPC85xx inbound message interrupt handler

    :param irq:
        Linux interrupt number
    :type irq: int

    :param dev_instance:
        Pointer to interrupt-specific data
    :type dev_instance: void \*

.. _`fsl_rio_rx_handler.description`:

Description
-----------

Handles inbound message interrupts. Executes a registered inbound
mailbox event handler and acks the interrupt occurrence.

.. _`fsl_rio_dbell_handler`:

fsl_rio_dbell_handler
=====================

.. c:function:: irqreturn_t fsl_rio_dbell_handler(int irq, void *dev_instance)

    MPC85xx doorbell interrupt handler

    :param irq:
        Linux interrupt number
    :type irq: int

    :param dev_instance:
        Pointer to interrupt-specific data
    :type dev_instance: void \*

.. _`fsl_rio_dbell_handler.description`:

Description
-----------

Handles doorbell interrupts. Parses a list of registered
doorbell event handlers and executes a matching event handler.

.. _`fsl_rio_port_write_handler`:

fsl_rio_port_write_handler
==========================

.. c:function:: irqreturn_t fsl_rio_port_write_handler(int irq, void *dev_instance)

    MPC85xx port write interrupt handler

    :param irq:
        Linux interrupt number
    :type irq: int

    :param dev_instance:
        Pointer to interrupt-specific data
    :type dev_instance: void \*

.. _`fsl_rio_port_write_handler.description`:

Description
-----------

Handles port write interrupts. Parses a list of registered
port write event handlers and executes a matching event handler.

.. _`fsl_rio_pw_enable`:

fsl_rio_pw_enable
=================

.. c:function:: int fsl_rio_pw_enable(struct rio_mport *mport, int enable)

    enable/disable port-write interface init

    :param mport:
        Master port implementing the port write unit
    :type mport: struct rio_mport \*

    :param enable:
        1=enable; 0=disable port-write message handling
    :type enable: int

.. _`fsl_rio_port_write_init`:

fsl_rio_port_write_init
=======================

.. c:function:: int fsl_rio_port_write_init(struct fsl_rio_pw *pw)

    MPC85xx port write interface init

    :param pw:
        *undescribed*
    :type pw: struct fsl_rio_pw \*

.. _`fsl_rio_port_write_init.description`:

Description
-----------

Initializes port write unit hardware and DMA buffer
ring. Called from \ :c:func:`fsl_rio_setup`\ . Returns \ ``0``\  on success
or \ ``-ENOMEM``\  on failure.

.. _`fsl_rio_doorbell_send`:

fsl_rio_doorbell_send
=====================

.. c:function:: int fsl_rio_doorbell_send(struct rio_mport *mport, int index, u16 destid, u16 data)

    Send a MPC85xx doorbell message

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
        16-bit info field of RapidIO doorbell message
    :type data: u16

.. _`fsl_rio_doorbell_send.description`:

Description
-----------

Sends a MPC85xx doorbell message. Returns \ ``0``\  on success or
\ ``-EINVAL``\  on failure.

.. _`fsl_add_outb_message`:

fsl_add_outb_message
====================

.. c:function:: int fsl_add_outb_message(struct rio_mport *mport, struct rio_dev *rdev, int mbox, void *buffer, size_t len)

    Add message to the MPC85xx outbound message queue

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

.. _`fsl_add_outb_message.description`:

Description
-----------

Adds the \ ``buffer``\  message to the MPC85xx outbound message queue. Returns
\ ``0``\  on success or \ ``-EINVAL``\  on failure.

.. _`fsl_open_outb_mbox`:

fsl_open_outb_mbox
==================

.. c:function:: int fsl_open_outb_mbox(struct rio_mport *mport, void *dev_id, int mbox, int entries)

    Initialize MPC85xx outbound mailbox

    :param mport:
        Master port implementing the outbound message unit
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

.. _`fsl_open_outb_mbox.description`:

Description
-----------

Initializes buffer ring, request the outbound message interrupt,
and enables the outbound message unit. Returns \ ``0``\  on success and
\ ``-EINVAL``\  or \ ``-ENOMEM``\  on failure.

.. _`fsl_close_outb_mbox`:

fsl_close_outb_mbox
===================

.. c:function:: void fsl_close_outb_mbox(struct rio_mport *mport, int mbox)

    Shut down MPC85xx outbound mailbox

    :param mport:
        Master port implementing the outbound message unit
    :type mport: struct rio_mport \*

    :param mbox:
        Mailbox to close
    :type mbox: int

.. _`fsl_close_outb_mbox.description`:

Description
-----------

Disables the outbound message unit, free all buffers, and
frees the outbound message interrupt.

.. _`fsl_open_inb_mbox`:

fsl_open_inb_mbox
=================

.. c:function:: int fsl_open_inb_mbox(struct rio_mport *mport, void *dev_id, int mbox, int entries)

    Initialize MPC85xx inbound mailbox

    :param mport:
        Master port implementing the inbound message unit
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

.. _`fsl_open_inb_mbox.description`:

Description
-----------

Initializes buffer ring, request the inbound message interrupt,
and enables the inbound message unit. Returns \ ``0``\  on success
and \ ``-EINVAL``\  or \ ``-ENOMEM``\  on failure.

.. _`fsl_close_inb_mbox`:

fsl_close_inb_mbox
==================

.. c:function:: void fsl_close_inb_mbox(struct rio_mport *mport, int mbox)

    Shut down MPC85xx inbound mailbox

    :param mport:
        Master port implementing the inbound message unit
    :type mport: struct rio_mport \*

    :param mbox:
        Mailbox to close
    :type mbox: int

.. _`fsl_close_inb_mbox.description`:

Description
-----------

Disables the inbound message unit, free all buffers, and
frees the inbound message interrupt.

.. _`fsl_add_inb_buffer`:

fsl_add_inb_buffer
==================

.. c:function:: int fsl_add_inb_buffer(struct rio_mport *mport, int mbox, void *buf)

    Add buffer to the MPC85xx inbound message queue

    :param mport:
        Master port implementing the inbound message unit
    :type mport: struct rio_mport \*

    :param mbox:
        Inbound mailbox number
    :type mbox: int

    :param buf:
        Buffer to add to inbound queue
    :type buf: void \*

.. _`fsl_add_inb_buffer.description`:

Description
-----------

Adds the \ ``buf``\  buffer to the MPC85xx inbound message queue. Returns
\ ``0``\  on success or \ ``-EINVAL``\  on failure.

.. _`fsl_get_inb_message`:

fsl_get_inb_message
===================

.. c:function:: void *fsl_get_inb_message(struct rio_mport *mport, int mbox)

    Fetch inbound message from the MPC85xx message unit

    :param mport:
        Master port implementing the inbound message unit
    :type mport: struct rio_mport \*

    :param mbox:
        Inbound mailbox number
    :type mbox: int

.. _`fsl_get_inb_message.description`:

Description
-----------

Gets the next available inbound message from the inbound message queue.
A pointer to the message is returned on success or NULL on failure.

.. _`fsl_rio_doorbell_init`:

fsl_rio_doorbell_init
=====================

.. c:function:: int fsl_rio_doorbell_init(struct fsl_rio_dbell *dbell)

    MPC85xx doorbell interface init

    :param dbell:
        *undescribed*
    :type dbell: struct fsl_rio_dbell \*

.. _`fsl_rio_doorbell_init.description`:

Description
-----------

Initializes doorbell unit hardware and inbound DMA buffer
ring. Called from \ :c:func:`fsl_rio_setup`\ . Returns \ ``0``\  on success
or \ ``-ENOMEM``\  on failure.

.. This file was automatic generated / don't edit.

