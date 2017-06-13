.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/openvswitch/flow_netlink.c

.. _`ovs_nla_get_match`:

ovs_nla_get_match
=================

.. c:function:: int ovs_nla_get_match(struct net *net, struct sw_flow_match *match, const struct nlattr *nla_key, const struct nlattr *nla_mask, bool log)

    parses Netlink attributes into a flow key and mask. In case the 'mask' is NULL, the flow is treated as exact match flow. Otherwise, it is treated as a wildcarded flow, except the mask does not include any don't care bit.

    :param struct net \*net:
        Used to determine per-namespace field support.

    :param struct sw_flow_match \*match:
        receives the extracted flow match information.

    :param const struct nlattr \*nla_key:
        *undescribed*

    :param const struct nlattr \*nla_mask:
        *undescribed*

    :param bool log:
        Boolean to allow kernel error logging.  Normally true, but when
        probing for feature compatibility this should be passed in as false to
        suppress unnecessary error logging.

.. _`ovs_nla_get_flow_metadata`:

ovs_nla_get_flow_metadata
=========================

.. c:function:: int ovs_nla_get_flow_metadata(struct net *net, const struct nlattr  *a, u64 attrs, struct sw_flow_key *key, bool log)

    parses Netlink attributes into a flow key.

    :param struct net \*net:
        Network namespace.

    :param const struct nlattr  \*a:
        Array of netlink attributes holding parsed \ ``OVS_KEY_ATTR``\ \_\* Netlink
        attributes.

    :param u64 attrs:
        Bit mask for the netlink attributes included in \ ``a``\ .

    :param struct sw_flow_key \*key:
        Receives extracted in_port, priority, tun_key, skb_mark and conntrack
        metadata.

    :param bool log:
        Boolean to allow kernel error logging.  Normally true, but when
        probing for feature compatibility this should be passed in as false to
        suppress unnecessary error logging.

.. _`ovs_nla_get_flow_metadata.description`:

Description
-----------

This parses a series of Netlink attributes that form a flow key, which must
take the same form accepted by \ :c:func:`flow_from_nlattrs`\ , but only enough of it to
get the metadata, that is, the parts of the flow key that cannot be
extracted from the packet itself.

This must be called before the packet key fields are filled in 'key'.

.. This file was automatic generated / don't edit.

