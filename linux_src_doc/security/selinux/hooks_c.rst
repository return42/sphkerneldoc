.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/hooks.c

.. _`selinux_secmark_enabled`:

selinux_secmark_enabled
=======================

.. c:function:: int selinux_secmark_enabled( void)

    Check to see if SECMARK is currently enabled

    :param  void:
        no arguments

.. _`selinux_secmark_enabled.description`:

Description
-----------

This function checks the SECMARK reference counter to see if any SECMARK
targets are currently configured, if the reference counter is greater than
zero SECMARK is considered to be enabled.  Returns true (1) if SECMARK is
enabled, false (0) if SECMARK is disabled.  If the always_check_network
policy capability is enabled, SECMARK is always considered enabled.

.. _`selinux_peerlbl_enabled`:

selinux_peerlbl_enabled
=======================

.. c:function:: int selinux_peerlbl_enabled( void)

    Check to see if peer labeling is currently enabled

    :param  void:
        no arguments

.. _`selinux_peerlbl_enabled.description`:

Description
-----------

This function checks if NetLabel or labeled IPSEC is enabled.  Returns true
(1) if any are enabled or false (0) if neither are enabled.  If the
always_check_network policy capability is enabled, peer labeling
is always considered enabled.

.. _`selinux_skb_peerlbl_sid`:

selinux_skb_peerlbl_sid
=======================

.. c:function:: int selinux_skb_peerlbl_sid(struct sk_buff *skb, u16 family, u32 *sid)

    Determine the peer label of a packet

    :param struct sk_buff \*skb:
        the packet

    :param u16 family:
        protocol family

    :param u32 \*sid:
        the packet's peer label SID

.. _`selinux_skb_peerlbl_sid.description`:

Description
-----------

Check the various different forms of network peer labeling and determine
the peer label/SID for the packet; most of the magic actually occurs in
the security server function \ :c:func:`security_net_peersid_cmp`\ .  The function
returns zero if the value in \ ``sid``\  is valid (although it may be SECSID_NULL)
or -EACCES if \ ``sid``\  is invalid due to inconsistencies with the different
peer labels.

.. _`selinux_conn_sid`:

selinux_conn_sid
================

.. c:function:: int selinux_conn_sid(u32 sk_sid, u32 skb_sid, u32 *conn_sid)

    Determine the child socket label for a connection

    :param u32 sk_sid:
        the parent socket's SID

    :param u32 skb_sid:
        the packet's SID

    :param u32 \*conn_sid:
        the resulting connection SID

.. _`selinux_conn_sid.description`:

Description
-----------

If \ ``skb_sid``\  is valid then the user:role:type information from \ ``sk_sid``\  is
combined with the MLS information from \ ``skb_sid``\  in order to create
\ ``conn_sid``\ .  If \ ``skb_sid``\  is not valid then then \ ``conn_sid``\  is simply a copy
of \ ``sk_sid``\ .  Returns zero on success, negative values on failure.

.. This file was automatic generated / don't edit.

