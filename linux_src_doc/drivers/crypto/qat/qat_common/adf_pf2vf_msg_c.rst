.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/qat/qat_common/adf_pf2vf_msg.c

.. _`adf_iov_putmsg`:

adf_iov_putmsg
==============

.. c:function:: int adf_iov_putmsg(struct adf_accel_dev *accel_dev, u32 msg, u8 vf_nr)

    send PF2VF message

    :param accel_dev:
        Pointer to acceleration device.
    :type accel_dev: struct adf_accel_dev \*

    :param msg:
        Message to send
    :type msg: u32

    :param vf_nr:
        VF number to which the message will be sent
    :type vf_nr: u8

.. _`adf_iov_putmsg.description`:

Description
-----------

Function sends a messge from the PF to a VF

.. _`adf_iov_putmsg.return`:

Return
------

0 on success, error code otherwise.

.. _`adf_enable_vf2pf_comms`:

adf_enable_vf2pf_comms
======================

.. c:function:: int adf_enable_vf2pf_comms(struct adf_accel_dev *accel_dev)

    Function enables communication from vf to pf

    :param accel_dev:
        Pointer to acceleration device virtual function.
    :type accel_dev: struct adf_accel_dev \*

.. _`adf_enable_vf2pf_comms.return`:

Return
------

0 on success, error code otherwise.

.. This file was automatic generated / don't edit.

