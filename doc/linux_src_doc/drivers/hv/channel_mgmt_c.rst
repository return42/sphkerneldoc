.. -*- coding: utf-8; mode: rst -*-

==============
channel_mgmt.c
==============


.. _`vmbus_prep_negotiate_resp`:

vmbus_prep_negotiate_resp
=========================

.. c:function:: bool vmbus_prep_negotiate_resp (struct icmsg_hdr *icmsghdrp, struct icmsg_negotiate *negop, u8 *buf, int fw_version, int srv_version)

    Create default response for Hyper-V Negotiate message

    :param struct icmsg_hdr \*icmsghdrp:
        Pointer to msg header structure

    :param struct icmsg_negotiate \*negop:

        *undescribed*

    :param u8 \*buf:
        Raw buffer channel data

    :param int fw_version:

        *undescribed*

    :param int srv_version:

        *undescribed*



.. _`vmbus_prep_negotiate_resp.description`:

Description
-----------

``icmsghdrp`` is of type :c:type:`struct icmsg_hdr <icmsg_hdr>`.
``negop`` is of type :c:type:`struct icmsg_negotiate <icmsg_negotiate>`.
Set up and fill in default negotiate response message.

The fw_version specifies the  framework version that
we can support and srv_version specifies the service
version we can support.

Mainly used by Hyper-V drivers.

