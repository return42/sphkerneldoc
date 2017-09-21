.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/avf/virtchnl.h

.. _`virtchnl_vc_validate_vf_msg`:

virtchnl_vc_validate_vf_msg
===========================

.. c:function:: int virtchnl_vc_validate_vf_msg(struct virtchnl_version_info *ver, u32 v_opcode, u8 *msg, u16 msglen)

    :param struct virtchnl_version_info \*ver:
        Virtchnl version info

    :param u32 v_opcode:
        Opcode for the message

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`virtchnl_vc_validate_vf_msg.description`:

Description
-----------

validate msg format against struct for each opcode

.. This file was automatic generated / don't edit.

