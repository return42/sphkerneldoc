.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igbvf/mbx.c

.. _`e1000_poll_for_msg`:

e1000_poll_for_msg
==================

.. c:function:: s32 e1000_poll_for_msg(struct e1000_hw *hw)

    Wait for message notification

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_poll_for_msg.description`:

Description
-----------

returns SUCCESS if it successfully received a message notification

.. _`e1000_poll_for_ack`:

e1000_poll_for_ack
==================

.. c:function:: s32 e1000_poll_for_ack(struct e1000_hw *hw)

    Wait for message acknowledgment

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_poll_for_ack.description`:

Description
-----------

returns SUCCESS if it successfully received a message acknowledgment

.. _`e1000_read_posted_mbx`:

e1000_read_posted_mbx
=====================

.. c:function:: s32 e1000_read_posted_mbx(struct e1000_hw *hw, u32 *msg, u16 size)

    Wait for message notification and receive message

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 \*msg:
        The message buffer

    :param u16 size:
        Length of buffer

.. _`e1000_read_posted_mbx.description`:

Description
-----------

returns SUCCESS if it successfully received a message notification and
copied it into the receive buffer.

.. _`e1000_write_posted_mbx`:

e1000_write_posted_mbx
======================

.. c:function:: s32 e1000_write_posted_mbx(struct e1000_hw *hw, u32 *msg, u16 size)

    Write a message to the mailbox, wait for ack

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 \*msg:
        The message buffer

    :param u16 size:
        Length of buffer

.. _`e1000_write_posted_mbx.description`:

Description
-----------

returns SUCCESS if it successfully copied message into the buffer and
received an ack to that message within delay \* timeout period

.. _`e1000_read_v2p_mailbox`:

e1000_read_v2p_mailbox
======================

.. c:function:: u32 e1000_read_v2p_mailbox(struct e1000_hw *hw)

    read v2p mailbox

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_read_v2p_mailbox.description`:

Description
-----------

This function is used to read the v2p mailbox without losing the read to
clear status bits.

.. _`e1000_check_for_bit_vf`:

e1000_check_for_bit_vf
======================

.. c:function:: s32 e1000_check_for_bit_vf(struct e1000_hw *hw, u32 mask)

    Determine if a status bit was set

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 mask:
        bitmask for bits to be tested and cleared

.. _`e1000_check_for_bit_vf.description`:

Description
-----------

This function is used to check for the read to clear bits within
the V2P mailbox.

.. _`e1000_check_for_msg_vf`:

e1000_check_for_msg_vf
======================

.. c:function:: s32 e1000_check_for_msg_vf(struct e1000_hw *hw)

    checks to see if the PF has sent mail

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_check_for_msg_vf.description`:

Description
-----------

returns SUCCESS if the PF has set the Status bit or else ERR_MBX

.. _`e1000_check_for_ack_vf`:

e1000_check_for_ack_vf
======================

.. c:function:: s32 e1000_check_for_ack_vf(struct e1000_hw *hw)

    checks to see if the PF has ACK'd

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_check_for_ack_vf.description`:

Description
-----------

returns SUCCESS if the PF has set the ACK bit or else ERR_MBX

.. _`e1000_check_for_rst_vf`:

e1000_check_for_rst_vf
======================

.. c:function:: s32 e1000_check_for_rst_vf(struct e1000_hw *hw)

    checks to see if the PF has reset

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_check_for_rst_vf.description`:

Description
-----------

returns true if the PF has set the reset done bit or else false

.. _`e1000_obtain_mbx_lock_vf`:

e1000_obtain_mbx_lock_vf
========================

.. c:function:: s32 e1000_obtain_mbx_lock_vf(struct e1000_hw *hw)

    obtain mailbox lock

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_obtain_mbx_lock_vf.description`:

Description
-----------

return SUCCESS if we obtained the mailbox lock

.. _`e1000_write_mbx_vf`:

e1000_write_mbx_vf
==================

.. c:function:: s32 e1000_write_mbx_vf(struct e1000_hw *hw, u32 *msg, u16 size)

    Write a message to the mailbox

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 \*msg:
        The message buffer

    :param u16 size:
        Length of buffer

.. _`e1000_write_mbx_vf.description`:

Description
-----------

returns SUCCESS if it successfully copied message into the buffer

.. _`e1000_read_mbx_vf`:

e1000_read_mbx_vf
=================

.. c:function:: s32 e1000_read_mbx_vf(struct e1000_hw *hw, u32 *msg, u16 size)

    Reads a message from the inbox intended for VF

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 \*msg:
        The message buffer

    :param u16 size:
        Length of buffer

.. _`e1000_read_mbx_vf.description`:

Description
-----------

returns SUCCESS if it successfully read message from buffer

.. _`e1000_init_mbx_params_vf`:

e1000_init_mbx_params_vf
========================

.. c:function:: s32 e1000_init_mbx_params_vf(struct e1000_hw *hw)

    set initial values for VF mailbox

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_init_mbx_params_vf.description`:

Description
-----------

Initializes the hw->mbx struct to correct values for VF mailbox

.. This file was automatic generated / don't edit.

