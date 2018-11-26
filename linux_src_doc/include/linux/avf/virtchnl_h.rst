.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/avf/virtchnl.h

.. _`virtchnl_vc_validate_vf_msg`:

virtchnl_vc_validate_vf_msg
===========================

.. c:function:: int virtchnl_vc_validate_vf_msg(struct virtchnl_version_info *ver, u32 v_opcode, u8 *msg, u16 msglen)

    :param ver:
        Virtchnl version info
    :type ver: struct virtchnl_version_info \*

    :param v_opcode:
        Opcode for the message
    :type v_opcode: u32

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param msglen:
        msg length
    :type msglen: u16

.. _`virtchnl_vc_validate_vf_msg.description`:

Description
-----------

validate msg format against struct for each opcode

.. This file was automatic generated / don't edit.

