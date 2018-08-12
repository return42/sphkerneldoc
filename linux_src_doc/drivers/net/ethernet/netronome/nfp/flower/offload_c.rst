.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/flower/offload.c

.. _`nfp_flower_add_offload`:

nfp_flower_add_offload
======================

.. c:function:: int nfp_flower_add_offload(struct nfp_app *app, struct net_device *netdev, struct tc_cls_flower_offload *flow, bool egress)

    Adds a new flow to hardware.

    :param struct nfp_app \*app:
        Pointer to the APP handle

    :param struct net_device \*netdev:
        netdev structure.

    :param struct tc_cls_flower_offload \*flow:
        TC flower classifier offload structure.

    :param bool egress:
        NFP netdev is the egress.

.. _`nfp_flower_add_offload.description`:

Description
-----------

Adds a new flow to the repeated hash structure and action payload.

.. _`nfp_flower_add_offload.return`:

Return
------

negative value on error, 0 if configured successfully.

.. _`nfp_flower_del_offload`:

nfp_flower_del_offload
======================

.. c:function:: int nfp_flower_del_offload(struct nfp_app *app, struct net_device *netdev, struct tc_cls_flower_offload *flow, bool egress)

    Removes a flow from hardware.

    :param struct nfp_app \*app:
        Pointer to the APP handle

    :param struct net_device \*netdev:
        netdev structure.

    :param struct tc_cls_flower_offload \*flow:
        TC flower classifier offload structure

    :param bool egress:
        Netdev is the egress dev.

.. _`nfp_flower_del_offload.description`:

Description
-----------

Removes a flow from the repeated hash structure and clears the
action payload.

.. _`nfp_flower_del_offload.return`:

Return
------

negative value on error, 0 if removed successfully.

.. _`nfp_flower_get_stats`:

nfp_flower_get_stats
====================

.. c:function:: int nfp_flower_get_stats(struct nfp_app *app, struct net_device *netdev, struct tc_cls_flower_offload *flow, bool egress)

    Populates flow stats obtained from hardware.

    :param struct nfp_app \*app:
        Pointer to the APP handle

    :param struct net_device \*netdev:
        Netdev structure.

    :param struct tc_cls_flower_offload \*flow:
        TC flower classifier offload structure

    :param bool egress:
        Netdev is the egress dev.

.. _`nfp_flower_get_stats.description`:

Description
-----------

Populates a flow statistics structure which which corresponds to a
specific flow.

.. _`nfp_flower_get_stats.return`:

Return
------

negative value on error, 0 if stats populated successfully.

.. This file was automatic generated / don't edit.

