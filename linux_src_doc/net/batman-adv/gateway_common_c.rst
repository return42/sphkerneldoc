.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/gateway_common.c

.. _`batadv_parse_throughput`:

batadv_parse_throughput
=======================

.. c:function:: bool batadv_parse_throughput(struct net_device *net_dev, char *buff, const char *description, u32 *throughput)

    parse supplied string buffer to extract throughput information

    :param struct net_device \*net_dev:
        the soft interface net device

    :param char \*buff:
        string buffer to parse

    :param const char \*description:
        text shown when throughput string cannot be parsed

    :param u32 \*throughput:
        pointer holding the returned throughput information

.. _`batadv_parse_throughput.return`:

Return
------

false on parse error and true otherwise.

.. _`batadv_parse_gw_bandwidth`:

batadv_parse_gw_bandwidth
=========================

.. c:function:: bool batadv_parse_gw_bandwidth(struct net_device *net_dev, char *buff, u32 *down, u32 *up)

    parse supplied string buffer to extract download and upload bandwidth information

    :param struct net_device \*net_dev:
        the soft interface net device

    :param char \*buff:
        string buffer to parse

    :param u32 \*down:
        pointer holding the returned download bandwidth information

    :param u32 \*up:
        pointer holding the returned upload bandwidth information

.. _`batadv_parse_gw_bandwidth.return`:

Return
------

false on parse error and true otherwise.

.. _`batadv_gw_tvlv_container_update`:

batadv_gw_tvlv_container_update
===============================

.. c:function:: void batadv_gw_tvlv_container_update(struct batadv_priv *bat_priv)

    update the gw tvlv container after gateway setting change

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_gw_tvlv_ogm_handler_v1`:

batadv_gw_tvlv_ogm_handler_v1
=============================

.. c:function:: void batadv_gw_tvlv_ogm_handler_v1(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 flags, void *tvlv_value, u16 tvlv_value_len)

    process incoming gateway tvlv container

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig:
        the orig_node of the ogm

    :param u8 flags:
        flags indicating the tvlv state (see batadv_tvlv_handler_flags)

    :param void \*tvlv_value:
        tvlv buffer containing the gateway data

    :param u16 tvlv_value_len:
        tvlv buffer length

.. _`batadv_gw_init`:

batadv_gw_init
==============

.. c:function:: void batadv_gw_init(struct batadv_priv *bat_priv)

    initialise the gateway handling internals

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_gw_free`:

batadv_gw_free
==============

.. c:function:: void batadv_gw_free(struct batadv_priv *bat_priv)

    free the gateway handling internals

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. This file was automatic generated / don't edit.

