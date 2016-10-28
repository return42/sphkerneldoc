.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/sysdev/fsl_rmu.c

.. _`fsl_rio_tx_handler`:

fsl_rio_tx_handler
==================

.. c:function:: irqreturn_t fsl_rio_tx_handler(int irq, void *dev_instance)

    MPC85xx outbound message interrupt handler

    :param int irq:
        Linux interrupt number

    :param void \*dev_instance:
        Pointer to interrupt-specific data

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

    :param int irq:
        Linux interrupt number

    :param void \*dev_instance:
        Pointer to interrupt-specific data

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

    :param int irq:
        Linux interrupt number

    :param void \*dev_instance:
        Pointer to interrupt-specific data

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

    :param int irq:
        Linux interrupt number

    :param void \*dev_instance:
        Pointer to interrupt-specific data

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

    :param struct rio_mport \*mport:
        Master port implementing the port write unit

    :param int enable:
        1=enable; 0=disable port-write message handling

.. _`fsl_rio_port_write_init`:

fsl_rio_port_write_init
=======================

.. c:function:: int fsl_rio_port_write_init(struct fsl_rio_pw *pw)

    MPC85xx port write interface init

    :param struct fsl_rio_pw \*pw:
        *undescribed*

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

    :param struct rio_mport \*mport:
        RapidIO master port info

    :param int index:
        ID of RapidIO interface

    :param u16 destid:
        Destination ID of target device

    :param u16 data:
        16-bit info field of RapidIO doorbell message

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

    :param struct rio_mport \*mport:
        Master port with outbound message queue

    :param struct rio_dev \*rdev:
        Target of outbound message

    :param int mbox:
        Outbound mailbox

    :param void \*buffer:
        Message to add to outbound queue

    :param size_t len:
        Length of message

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

    :param struct rio_mport \*mport:
        Master port implementing the outbound message unit

    :param void \*dev_id:
        Device specific pointer to pass on event

    :param int mbox:
        Mailbox to open

    :param int entries:
        Number of entries in the outbound mailbox ring

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

    :param struct rio_mport \*mport:
        Master port implementing the outbound message unit

    :param int mbox:
        Mailbox to close

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

    :param struct rio_mport \*mport:
        Master port implementing the inbound message unit

    :param void \*dev_id:
        Device specific pointer to pass on event

    :param int mbox:
        Mailbox to open

    :param int entries:
        Number of entries in the inbound mailbox ring

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

    :param struct rio_mport \*mport:
        Master port implementing the inbound message unit

    :param int mbox:
        Mailbox to close

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

    :param struct rio_mport \*mport:
        Master port implementing the inbound message unit

    :param int mbox:
        Inbound mailbox number

    :param void \*buf:
        Buffer to add to inbound queue

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

    :param struct rio_mport \*mport:
        Master port implementing the inbound message unit

    :param int mbox:
        Inbound mailbox number

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

    :param struct fsl_rio_dbell \*dbell:
        *undescribed*

.. _`fsl_rio_doorbell_init.description`:

Description
-----------

Initializes doorbell unit hardware and inbound DMA buffer
ring. Called from \ :c:func:`fsl_rio_setup`\ . Returns \ ``0``\  on success
or \ ``-ENOMEM``\  on failure.

.. This file was automatic generated / don't edit.

