.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/gateway_common.c

.. _`batadv_parse_throughput`:

batadv_parse_throughput
=======================

.. c:function:: bool batadv_parse_throughput(struct net_device *net_dev, char *buff, const char *description, u32 *throughput)

    parse supplied string buffer to extract throughput information

    :param net_dev:
        the soft interface net device
    :type net_dev: struct net_device \*

    :param buff:
        string buffer to parse
    :type buff: char \*

    :param description:
        text shown when throughput string cannot be parsed
    :type description: const char \*

    :param throughput:
        pointer holding the returned throughput information
    :type throughput: u32 \*

.. _`batadv_parse_throughput.return`:

Return
------

false on parse error and true otherwise.

.. _`batadv_parse_gw_bandwidth`:

batadv_parse_gw_bandwidth
=========================

.. c:function:: bool batadv_parse_gw_bandwidth(struct net_device *net_dev, char *buff, u32 *down, u32 *up)

    parse supplied string buffer to extract download and upload bandwidth information

    :param net_dev:
        the soft interface net device
    :type net_dev: struct net_device \*

    :param buff:
        string buffer to parse
    :type buff: char \*

    :param down:
        pointer holding the returned download bandwidth information
    :type down: u32 \*

    :param up:
        pointer holding the returned upload bandwidth information
    :type up: u32 \*

.. _`batadv_parse_gw_bandwidth.return`:

Return
------

false on parse error and true otherwise.

.. _`batadv_gw_tvlv_container_update`:

batadv_gw_tvlv_container_update
===============================

.. c:function:: void batadv_gw_tvlv_container_update(struct batadv_priv *bat_priv)

    update the gw tvlv container after gateway setting change

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_gw_bandwidth_set`:

batadv_gw_bandwidth_set
=======================

.. c:function:: ssize_t batadv_gw_bandwidth_set(struct net_device *net_dev, char *buff, size_t count)

    Parse and set download/upload gateway bandwidth from supplied string buffer

    :param net_dev:
        netdev struct of the soft interface
    :type net_dev: struct net_device \*

    :param buff:
        the buffer containing the user data
    :type buff: char \*

    :param count:
        number of bytes in the buffer
    :type count: size_t

.. _`batadv_gw_bandwidth_set.return`:

Return
------

'count' on success or a negative error code in case of failure

.. _`batadv_gw_tvlv_ogm_handler_v1`:

batadv_gw_tvlv_ogm_handler_v1
=============================

.. c:function:: void batadv_gw_tvlv_ogm_handler_v1(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 flags, void *tvlv_value, u16 tvlv_value_len)

    process incoming gateway tvlv container

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig:
        the orig_node of the ogm
    :type orig: struct batadv_orig_node \*

    :param flags:
        flags indicating the tvlv state (see batadv_tvlv_handler_flags)
    :type flags: u8

    :param tvlv_value:
        tvlv buffer containing the gateway data
    :type tvlv_value: void \*

    :param tvlv_value_len:
        tvlv buffer length
    :type tvlv_value_len: u16

.. _`batadv_gw_init`:

batadv_gw_init
==============

.. c:function:: void batadv_gw_init(struct batadv_priv *bat_priv)

    initialise the gateway handling internals

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_gw_free`:

batadv_gw_free
==============

.. c:function:: void batadv_gw_free(struct batadv_priv *bat_priv)

    free the gateway handling internals

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. This file was automatic generated / don't edit.

