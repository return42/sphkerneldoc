.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbevf/mbx.c

.. _`ixgbevf_poll_for_msg`:

ixgbevf_poll_for_msg
====================

.. c:function:: s32 ixgbevf_poll_for_msg(struct ixgbe_hw *hw)

    Wait for message notification

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbevf_poll_for_msg.description`:

Description
-----------

returns 0 if it successfully received a message notification

.. _`ixgbevf_poll_for_ack`:

ixgbevf_poll_for_ack
====================

.. c:function:: s32 ixgbevf_poll_for_ack(struct ixgbe_hw *hw)

    Wait for message acknowledgment

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbevf_poll_for_ack.description`:

Description
-----------

returns 0 if it successfully received a message acknowledgment

.. _`ixgbevf_read_posted_mbx`:

ixgbevf_read_posted_mbx
=======================

.. c:function:: s32 ixgbevf_read_posted_mbx(struct ixgbe_hw *hw, u32 *msg, u16 size)

    Wait for message notification and receive message

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

    :param u32 \*msg:
        The message buffer

    :param u16 size:
        Length of buffer

.. _`ixgbevf_read_posted_mbx.description`:

Description
-----------

returns 0 if it successfully received a message notification and
copied it into the receive buffer.

.. _`ixgbevf_write_posted_mbx`:

ixgbevf_write_posted_mbx
========================

.. c:function:: s32 ixgbevf_write_posted_mbx(struct ixgbe_hw *hw, u32 *msg, u16 size)

    Write a message to the mailbox, wait for ack

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

    :param u32 \*msg:
        The message buffer

    :param u16 size:
        Length of buffer

.. _`ixgbevf_write_posted_mbx.description`:

Description
-----------

returns 0 if it successfully copied message into the buffer and
received an ack to that message within delay \* timeout period

.. _`ixgbevf_read_v2p_mailbox`:

ixgbevf_read_v2p_mailbox
========================

.. c:function:: u32 ixgbevf_read_v2p_mailbox(struct ixgbe_hw *hw)

    read v2p mailbox

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbevf_read_v2p_mailbox.description`:

Description
-----------

This function is used to read the v2p mailbox without losing the read to
clear status bits.

.. _`ixgbevf_check_for_bit_vf`:

ixgbevf_check_for_bit_vf
========================

.. c:function:: s32 ixgbevf_check_for_bit_vf(struct ixgbe_hw *hw, u32 mask)

    Determine if a status bit was set

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

    :param u32 mask:
        bitmask for bits to be tested and cleared

.. _`ixgbevf_check_for_bit_vf.description`:

Description
-----------

This function is used to check for the read to clear bits within
the V2P mailbox.

.. _`ixgbevf_check_for_msg_vf`:

ixgbevf_check_for_msg_vf
========================

.. c:function:: s32 ixgbevf_check_for_msg_vf(struct ixgbe_hw *hw)

    checks to see if the PF has sent mail

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbevf_check_for_msg_vf.description`:

Description
-----------

returns 0 if the PF has set the Status bit or else ERR_MBX

.. _`ixgbevf_check_for_ack_vf`:

ixgbevf_check_for_ack_vf
========================

.. c:function:: s32 ixgbevf_check_for_ack_vf(struct ixgbe_hw *hw)

    checks to see if the PF has ACK'd

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbevf_check_for_ack_vf.description`:

Description
-----------

returns 0 if the PF has set the ACK bit or else ERR_MBX

.. _`ixgbevf_check_for_rst_vf`:

ixgbevf_check_for_rst_vf
========================

.. c:function:: s32 ixgbevf_check_for_rst_vf(struct ixgbe_hw *hw)

    checks to see if the PF has reset

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbevf_check_for_rst_vf.description`:

Description
-----------

returns true if the PF has set the reset done bit or else false

.. _`ixgbevf_obtain_mbx_lock_vf`:

ixgbevf_obtain_mbx_lock_vf
==========================

.. c:function:: s32 ixgbevf_obtain_mbx_lock_vf(struct ixgbe_hw *hw)

    obtain mailbox lock

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbevf_obtain_mbx_lock_vf.description`:

Description
-----------

return 0 if we obtained the mailbox lock

.. _`ixgbevf_write_mbx_vf`:

ixgbevf_write_mbx_vf
====================

.. c:function:: s32 ixgbevf_write_mbx_vf(struct ixgbe_hw *hw, u32 *msg, u16 size)

    Write a message to the mailbox

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

    :param u32 \*msg:
        The message buffer

    :param u16 size:
        Length of buffer

.. _`ixgbevf_write_mbx_vf.description`:

Description
-----------

returns 0 if it successfully copied message into the buffer

.. _`ixgbevf_read_mbx_vf`:

ixgbevf_read_mbx_vf
===================

.. c:function:: s32 ixgbevf_read_mbx_vf(struct ixgbe_hw *hw, u32 *msg, u16 size)

    Reads a message from the inbox intended for VF

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

    :param u32 \*msg:
        The message buffer

    :param u16 size:
        Length of buffer

.. _`ixgbevf_read_mbx_vf.description`:

Description
-----------

returns 0 if it successfully read message from buffer

.. _`ixgbevf_init_mbx_params_vf`:

ixgbevf_init_mbx_params_vf
==========================

.. c:function:: s32 ixgbevf_init_mbx_params_vf(struct ixgbe_hw *hw)

    set initial values for VF mailbox

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbevf_init_mbx_params_vf.description`:

Description
-----------

Initializes the hw->mbx struct to correct values for VF mailbox

.. This file was automatic generated / don't edit.

