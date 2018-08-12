.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/apr.c

.. _`apr_send_pkt`:

apr_send_pkt
============

.. c:function:: int apr_send_pkt(struct apr_device *adev, struct apr_pkt *pkt)

    Send a apr message from apr device

    :param struct apr_device \*adev:
        Pointer to previously registered apr device.

    :param struct apr_pkt \*pkt:
        Pointer to apr packet to send

.. _`apr_send_pkt.return`:

Return
------

Will be an negative on packet size on success.

.. This file was automatic generated / don't edit.

