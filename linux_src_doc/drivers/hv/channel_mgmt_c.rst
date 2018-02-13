.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hv/channel_mgmt.c

.. _`vmbus_prep_negotiate_resp`:

vmbus_prep_negotiate_resp
=========================

.. c:function:: bool vmbus_prep_negotiate_resp(struct icmsg_hdr *icmsghdrp, u8 *buf, const int *fw_version, int fw_vercnt, const int *srv_version, int srv_vercnt, int *nego_fw_version, int *nego_srv_version)

    Create default response for Hyper-V Negotiate message

    :param struct icmsg_hdr \*icmsghdrp:
        Pointer to msg header structure

    :param u8 \*buf:
        Raw buffer channel data

    :param const int \*fw_version:
        *undescribed*

    :param int fw_vercnt:
        *undescribed*

    :param const int \*srv_version:
        *undescribed*

    :param int srv_vercnt:
        *undescribed*

    :param int \*nego_fw_version:
        *undescribed*

    :param int \*nego_srv_version:
        *undescribed*

.. _`vmbus_prep_negotiate_resp.description`:

Description
-----------

\ ``icmsghdrp``\  is of type \ :c:type:`struct icmsg_hdr <icmsg_hdr>`\ .
Set up and fill in default negotiate response message.

The fw_version and fw_vercnt specifies the framework version that
we can support.

The srv_version and srv_vercnt specifies the service
versions we can support.

Versions are given in decreasing order.

nego_fw_version and nego_srv_version store the selected protocol versions.

Mainly used by Hyper-V drivers.

.. This file was automatic generated / don't edit.

