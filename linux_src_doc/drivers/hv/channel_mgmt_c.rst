.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hv/channel_mgmt.c

.. _`vmbus_prep_negotiate_resp`:

vmbus_prep_negotiate_resp
=========================

.. c:function:: bool vmbus_prep_negotiate_resp(struct icmsg_hdr *icmsghdrp, u8 *buf, const int *fw_version, int fw_vercnt, const int *srv_version, int srv_vercnt, int *nego_fw_version, int *nego_srv_version)

    Create default response for Negotiate message

    :param icmsghdrp:
        Pointer to msg header structure
    :type icmsghdrp: struct icmsg_hdr \*

    :param buf:
        Raw buffer channel data
    :type buf: u8 \*

    :param fw_version:
        The framework versions we can support.
    :type fw_version: const int \*

    :param fw_vercnt:
        The size of \ ``fw_version``\ .
    :type fw_vercnt: int

    :param srv_version:
        The service versions we can support.
    :type srv_version: const int \*

    :param srv_vercnt:
        The size of \ ``srv_version``\ .
    :type srv_vercnt: int

    :param nego_fw_version:
        The selected framework version.
    :type nego_fw_version: int \*

    :param nego_srv_version:
        The selected service version.
    :type nego_srv_version: int \*

.. _`vmbus_prep_negotiate_resp.note`:

Note
----

Versions are given in decreasing order.

Set up and fill in default negotiate response message.
Mainly used by Hyper-V drivers.

.. This file was automatic generated / don't edit.

