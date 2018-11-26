.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igb/e1000_mbx.c

.. _`igb_read_mbx`:

igb_read_mbx
============

.. c:function:: s32 igb_read_mbx(struct e1000_hw *hw, u32 *msg, u16 size, u16 mbx_id, bool unlock)

    Reads a message from the mailbox

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param msg:
        The message buffer
    :type msg: u32 \*

    :param size:
        Length of buffer
    :type size: u16

    :param mbx_id:
        id of mailbox to read
    :type mbx_id: u16

    :param unlock:
        *undescribed*
    :type unlock: bool

.. _`igb_read_mbx.description`:

Description
-----------

returns SUCCESS if it successfully read message from buffer

.. _`igb_write_mbx`:

igb_write_mbx
=============

.. c:function:: s32 igb_write_mbx(struct e1000_hw *hw, u32 *msg, u16 size, u16 mbx_id)

    Write a message to the mailbox

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param msg:
        The message buffer
    :type msg: u32 \*

    :param size:
        Length of buffer
    :type size: u16

    :param mbx_id:
        id of mailbox to write
    :type mbx_id: u16

.. _`igb_write_mbx.description`:

Description
-----------

returns SUCCESS if it successfully copied message into the buffer

.. _`igb_check_for_msg`:

igb_check_for_msg
=================

.. c:function:: s32 igb_check_for_msg(struct e1000_hw *hw, u16 mbx_id)

    checks to see if someone sent us mail

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param mbx_id:
        id of mailbox to check
    :type mbx_id: u16

.. _`igb_check_for_msg.description`:

Description
-----------

returns SUCCESS if the Status bit was found or else ERR_MBX

.. _`igb_check_for_ack`:

igb_check_for_ack
=================

.. c:function:: s32 igb_check_for_ack(struct e1000_hw *hw, u16 mbx_id)

    checks to see if someone sent us ACK

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param mbx_id:
        id of mailbox to check
    :type mbx_id: u16

.. _`igb_check_for_ack.description`:

Description
-----------

returns SUCCESS if the Status bit was found or else ERR_MBX

.. _`igb_check_for_rst`:

igb_check_for_rst
=================

.. c:function:: s32 igb_check_for_rst(struct e1000_hw *hw, u16 mbx_id)

    checks to see if other side has reset

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param mbx_id:
        id of mailbox to check
    :type mbx_id: u16

.. _`igb_check_for_rst.description`:

Description
-----------

returns SUCCESS if the Status bit was found or else ERR_MBX

.. _`igb_unlock_mbx`:

igb_unlock_mbx
==============

.. c:function:: s32 igb_unlock_mbx(struct e1000_hw *hw, u16 mbx_id)

    unlock the mailbox

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param mbx_id:
        id of mailbox to check
    :type mbx_id: u16

.. _`igb_unlock_mbx.description`:

Description
-----------

returns SUCCESS if the mailbox was unlocked or else ERR_MBX

.. _`igb_poll_for_msg`:

igb_poll_for_msg
================

.. c:function:: s32 igb_poll_for_msg(struct e1000_hw *hw, u16 mbx_id)

    Wait for message notification

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param mbx_id:
        id of mailbox to write
    :type mbx_id: u16

.. _`igb_poll_for_msg.description`:

Description
-----------

returns SUCCESS if it successfully received a message notification

.. _`igb_poll_for_ack`:

igb_poll_for_ack
================

.. c:function:: s32 igb_poll_for_ack(struct e1000_hw *hw, u16 mbx_id)

    Wait for message acknowledgement

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param mbx_id:
        id of mailbox to write
    :type mbx_id: u16

.. _`igb_poll_for_ack.description`:

Description
-----------

returns SUCCESS if it successfully received a message acknowledgement

.. _`igb_read_posted_mbx`:

igb_read_posted_mbx
===================

.. c:function:: s32 igb_read_posted_mbx(struct e1000_hw *hw, u32 *msg, u16 size, u16 mbx_id)

    Wait for message notification and receive message

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param msg:
        The message buffer
    :type msg: u32 \*

    :param size:
        Length of buffer
    :type size: u16

    :param mbx_id:
        id of mailbox to write
    :type mbx_id: u16

.. _`igb_read_posted_mbx.description`:

Description
-----------

returns SUCCESS if it successfully received a message notification and
copied it into the receive buffer.

.. _`igb_write_posted_mbx`:

igb_write_posted_mbx
====================

.. c:function:: s32 igb_write_posted_mbx(struct e1000_hw *hw, u32 *msg, u16 size, u16 mbx_id)

    Write a message to the mailbox, wait for ack

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param msg:
        The message buffer
    :type msg: u32 \*

    :param size:
        Length of buffer
    :type size: u16

    :param mbx_id:
        id of mailbox to write
    :type mbx_id: u16

.. _`igb_write_posted_mbx.description`:

Description
-----------

returns SUCCESS if it successfully copied message into the buffer and
received an ack to that message within delay \* timeout period

.. _`igb_check_for_msg_pf`:

igb_check_for_msg_pf
====================

.. c:function:: s32 igb_check_for_msg_pf(struct e1000_hw *hw, u16 vf_number)

    checks to see if the VF has sent mail

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param vf_number:
        the VF index
    :type vf_number: u16

.. _`igb_check_for_msg_pf.description`:

Description
-----------

returns SUCCESS if the VF has set the Status bit or else ERR_MBX

.. _`igb_check_for_ack_pf`:

igb_check_for_ack_pf
====================

.. c:function:: s32 igb_check_for_ack_pf(struct e1000_hw *hw, u16 vf_number)

    checks to see if the VF has ACKed

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param vf_number:
        the VF index
    :type vf_number: u16

.. _`igb_check_for_ack_pf.description`:

Description
-----------

returns SUCCESS if the VF has set the Status bit or else ERR_MBX

.. _`igb_check_for_rst_pf`:

igb_check_for_rst_pf
====================

.. c:function:: s32 igb_check_for_rst_pf(struct e1000_hw *hw, u16 vf_number)

    checks to see if the VF has reset

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param vf_number:
        the VF index
    :type vf_number: u16

.. _`igb_check_for_rst_pf.description`:

Description
-----------

returns SUCCESS if the VF has set the Status bit or else ERR_MBX

.. _`igb_obtain_mbx_lock_pf`:

igb_obtain_mbx_lock_pf
======================

.. c:function:: s32 igb_obtain_mbx_lock_pf(struct e1000_hw *hw, u16 vf_number)

    obtain mailbox lock

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param vf_number:
        the VF index
    :type vf_number: u16

.. _`igb_obtain_mbx_lock_pf.description`:

Description
-----------

return SUCCESS if we obtained the mailbox lock

.. _`igb_release_mbx_lock_pf`:

igb_release_mbx_lock_pf
=======================

.. c:function:: s32 igb_release_mbx_lock_pf(struct e1000_hw *hw, u16 vf_number)

    release mailbox lock

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param vf_number:
        the VF index
    :type vf_number: u16

.. _`igb_release_mbx_lock_pf.description`:

Description
-----------

return SUCCESS if we released the mailbox lock

.. _`igb_write_mbx_pf`:

igb_write_mbx_pf
================

.. c:function:: s32 igb_write_mbx_pf(struct e1000_hw *hw, u32 *msg, u16 size, u16 vf_number)

    Places a message in the mailbox

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param msg:
        The message buffer
    :type msg: u32 \*

    :param size:
        Length of buffer
    :type size: u16

    :param vf_number:
        the VF index
    :type vf_number: u16

.. _`igb_write_mbx_pf.description`:

Description
-----------

returns SUCCESS if it successfully copied message into the buffer

.. _`igb_read_mbx_pf`:

igb_read_mbx_pf
===============

.. c:function:: s32 igb_read_mbx_pf(struct e1000_hw *hw, u32 *msg, u16 size, u16 vf_number, bool unlock)

    Read a message from the mailbox

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param msg:
        The message buffer
    :type msg: u32 \*

    :param size:
        Length of buffer
    :type size: u16

    :param vf_number:
        the VF index
    :type vf_number: u16

    :param unlock:
        unlock the mailbox when done?
    :type unlock: bool

.. _`igb_read_mbx_pf.description`:

Description
-----------

This function copies a message from the mailbox buffer to the caller's
memory buffer.  The presumption is that the caller knows that there was
a message due to a VF request so no polling for message is needed.

.. _`igb_init_mbx_params_pf`:

igb_init_mbx_params_pf
======================

.. c:function:: s32 igb_init_mbx_params_pf(struct e1000_hw *hw)

    set initial values for pf mailbox

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_init_mbx_params_pf.description`:

Description
-----------

Initializes the hw->mbx struct to correct values for pf mailbox

.. This file was automatic generated / don't edit.

