.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_adminq.c

.. _`i40e_adminq_init_regs`:

i40e_adminq_init_regs
=====================

.. c:function:: void i40e_adminq_init_regs(struct i40e_hw *hw)

    Initialize AdminQ registers

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_adminq_init_regs.description`:

Description
-----------

This assumes the alloc_asq and alloc_arq functions have already been called

.. _`i40e_alloc_adminq_asq_ring`:

i40e_alloc_adminq_asq_ring
==========================

.. c:function:: i40e_status i40e_alloc_adminq_asq_ring(struct i40e_hw *hw)

    Allocate Admin Queue send rings

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_alloc_adminq_arq_ring`:

i40e_alloc_adminq_arq_ring
==========================

.. c:function:: i40e_status i40e_alloc_adminq_arq_ring(struct i40e_hw *hw)

    Allocate Admin Queue receive rings

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_free_adminq_asq`:

i40e_free_adminq_asq
====================

.. c:function:: void i40e_free_adminq_asq(struct i40e_hw *hw)

    Free Admin Queue send rings

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_free_adminq_asq.description`:

Description
-----------

This assumes the posted send buffers have already been cleaned
and de-allocated

.. _`i40e_free_adminq_arq`:

i40e_free_adminq_arq
====================

.. c:function:: void i40e_free_adminq_arq(struct i40e_hw *hw)

    Free Admin Queue receive rings

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_free_adminq_arq.description`:

Description
-----------

This assumes the posted receive buffers have already been cleaned
and de-allocated

.. _`i40e_alloc_arq_bufs`:

i40e_alloc_arq_bufs
===================

.. c:function:: i40e_status i40e_alloc_arq_bufs(struct i40e_hw *hw)

    Allocate pre-posted buffers for the receive queue

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_alloc_asq_bufs`:

i40e_alloc_asq_bufs
===================

.. c:function:: i40e_status i40e_alloc_asq_bufs(struct i40e_hw *hw)

    Allocate empty buffer structs for the send queue

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_free_arq_bufs`:

i40e_free_arq_bufs
==================

.. c:function:: void i40e_free_arq_bufs(struct i40e_hw *hw)

    Free receive queue buffer info elements

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_free_asq_bufs`:

i40e_free_asq_bufs
==================

.. c:function:: void i40e_free_asq_bufs(struct i40e_hw *hw)

    Free send queue buffer info elements

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_config_asq_regs`:

i40e_config_asq_regs
====================

.. c:function:: i40e_status i40e_config_asq_regs(struct i40e_hw *hw)

    configure ASQ registers

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_config_asq_regs.description`:

Description
-----------

Configure base address and length registers for the transmit queue

.. _`i40e_config_arq_regs`:

i40e_config_arq_regs
====================

.. c:function:: i40e_status i40e_config_arq_regs(struct i40e_hw *hw)

    ARQ register configuration

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_config_arq_regs.description`:

Description
-----------

Configure base address and length registers for the receive (event queue)

.. _`i40e_init_asq`:

i40e_init_asq
=============

.. c:function:: i40e_status i40e_init_asq(struct i40e_hw *hw)

    main initialization routine for ASQ

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_init_asq.description`:

Description
-----------

This is the main initialization routine for the Admin Send Queue
Prior to calling this function, drivers \*MUST\* set the following fields
in the hw->aq structure:
- hw->aq.num_asq_entries
- hw->aq.arq_buf_size

Do \*NOT\* hold the lock when calling this as the memory allocation routines
called are not going to be atomic context safe

.. _`i40e_init_arq`:

i40e_init_arq
=============

.. c:function:: i40e_status i40e_init_arq(struct i40e_hw *hw)

    initialize ARQ

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_init_arq.description`:

Description
-----------

The main initialization routine for the Admin Receive (Event) Queue.
Prior to calling this function, drivers \*MUST\* set the following fields
in the hw->aq structure:
- hw->aq.num_asq_entries
- hw->aq.arq_buf_size

Do \*NOT\* hold the lock when calling this as the memory allocation routines
called are not going to be atomic context safe

.. _`i40e_shutdown_asq`:

i40e_shutdown_asq
=================

.. c:function:: i40e_status i40e_shutdown_asq(struct i40e_hw *hw)

    shutdown the ASQ

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_shutdown_asq.description`:

Description
-----------

The main shutdown routine for the Admin Send Queue

.. _`i40e_shutdown_arq`:

i40e_shutdown_arq
=================

.. c:function:: i40e_status i40e_shutdown_arq(struct i40e_hw *hw)

    shutdown ARQ

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_shutdown_arq.description`:

Description
-----------

The main shutdown routine for the Admin Receive Queue

.. _`i40e_init_adminq`:

i40e_init_adminq
================

.. c:function:: i40e_status i40e_init_adminq(struct i40e_hw *hw)

    main initialization routine for Admin Queue

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_init_adminq.description`:

Description
-----------

Prior to calling this function, drivers \*MUST\* set the following fields
in the hw->aq structure:
- hw->aq.num_asq_entries
- hw->aq.num_arq_entries
- hw->aq.arq_buf_size
- hw->aq.asq_buf_size

.. _`i40e_shutdown_adminq`:

i40e_shutdown_adminq
====================

.. c:function:: i40e_status i40e_shutdown_adminq(struct i40e_hw *hw)

    shutdown routine for the Admin Queue

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_clean_asq`:

i40e_clean_asq
==============

.. c:function:: u16 i40e_clean_asq(struct i40e_hw *hw)

    cleans Admin send queue

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_clean_asq.description`:

Description
-----------

returns the number of free desc

.. _`i40e_asq_done`:

i40e_asq_done
=============

.. c:function:: bool i40e_asq_done(struct i40e_hw *hw)

    check if FW has processed the Admin Send Queue

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

.. _`i40e_asq_done.description`:

Description
-----------

Returns true if the firmware has processed all descriptors on the
admin send queue. Returns false if there are still requests pending.

.. _`i40e_asq_send_command`:

i40e_asq_send_command
=====================

.. c:function:: i40e_status i40e_asq_send_command(struct i40e_hw *hw, struct i40e_aq_desc *desc, void *buff, u16 buff_size, struct i40e_asq_cmd_details *cmd_details)

    send command to Admin Queue

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param desc:
        prefilled descriptor describing the command (non DMA mem)
    :type desc: struct i40e_aq_desc \*

    :param buff:
        buffer to use for indirect commands
    :type buff: void \*

    :param buff_size:
        size of buffer for indirect commands
    :type buff_size: u16

    :param cmd_details:
        pointer to command details structure
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_asq_send_command.description`:

Description
-----------

This is the main send command driver routine for the Admin Queue send
queue.  It runs the queue, cleans the queue, etc

.. _`i40e_fill_default_direct_cmd_desc`:

i40e_fill_default_direct_cmd_desc
=================================

.. c:function:: void i40e_fill_default_direct_cmd_desc(struct i40e_aq_desc *desc, u16 opcode)

    AQ descriptor helper function

    :param desc:
        pointer to the temp descriptor (non DMA mem)
    :type desc: struct i40e_aq_desc \*

    :param opcode:
        the opcode can be used to decide which flags to turn off or on
    :type opcode: u16

.. _`i40e_fill_default_direct_cmd_desc.description`:

Description
-----------

Fill the desc with default values

.. _`i40e_clean_arq_element`:

i40e_clean_arq_element
======================

.. c:function:: i40e_status i40e_clean_arq_element(struct i40e_hw *hw, struct i40e_arq_event_info *e, u16 *pending)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param e:
        event info from the receive descriptor, includes any buffers
    :type e: struct i40e_arq_event_info \*

    :param pending:
        number of events that could be left to process
    :type pending: u16 \*

.. _`i40e_clean_arq_element.description`:

Description
-----------

This function cleans one Admin Receive Queue element and returns
the contents through e.  It can also return how many events are
left to process through 'pending'

.. This file was automatic generated / don't edit.

