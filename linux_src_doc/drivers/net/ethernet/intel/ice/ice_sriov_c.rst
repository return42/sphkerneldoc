.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_sriov.c

.. _`ice_aq_send_msg_to_vf`:

ice_aq_send_msg_to_vf
=====================

.. c:function:: enum ice_status ice_aq_send_msg_to_vf(struct ice_hw *hw, u16 vfid, u32 v_opcode, u32 v_retval, u8 *msg, u16 msglen, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vfid:
        VF ID to send msg
    :type vfid: u16

    :param v_opcode:
        opcodes for VF-PF communication
    :type v_opcode: u32

    :param v_retval:
        return error code
    :type v_retval: u32

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param msglen:
        msg length
    :type msglen: u16

    :param cd:
        pointer to command details
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_send_msg_to_vf.description`:

Description
-----------

Send message to VF driver (0x0802) using mailbox
queue and asynchronously sending message via
\ :c:func:`ice_sq_send_cmd`\  function

.. _`ice_conv_link_speed_to_virtchnl`:

ice_conv_link_speed_to_virtchnl
===============================

.. c:function:: u32 ice_conv_link_speed_to_virtchnl(bool adv_link_support, u16 link_speed)

    :param adv_link_support:
        determines the format of the returned link speed
    :type adv_link_support: bool

    :param link_speed:
        variable containing the link_speed to be converted
    :type link_speed: u16

.. _`ice_conv_link_speed_to_virtchnl.description`:

Description
-----------

Convert link speed supported by HW to link speed supported by virtchnl.
If adv_link_support is true, then return link speed in Mbps.  Else return
link speed as a VIRTCHNL_LINK_SPEED\_\* casted to a u32. Note that the caller
needs to cast back to an enum virtchnl_link_speed in the case where
adv_link_support is false, but when adv_link_support is true the caller can
expect the speed in Mbps.

.. This file was automatic generated / don't edit.

