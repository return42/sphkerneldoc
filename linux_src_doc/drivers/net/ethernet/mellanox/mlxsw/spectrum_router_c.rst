.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/mellanox/mlxsw/spectrum_router.c

.. _`__mlxsw_sp_ipip_entry_update_tunnel`:

__mlxsw_sp_ipip_entry_update_tunnel
===================================

.. c:function:: int __mlxsw_sp_ipip_entry_update_tunnel(struct mlxsw_sp *mlxsw_sp, struct mlxsw_sp_ipip_entry *ipip_entry, bool recreate_loopback, bool keep_encap, bool update_nexthops, struct netlink_ext_ack *extack)

    :param struct mlxsw_sp \*mlxsw_sp:
        *undescribed*

    :param struct mlxsw_sp_ipip_entry \*ipip_entry:
        *undescribed*

    :param bool recreate_loopback:
        recreates the associated loopback RIF

    :param bool keep_encap:
        updates next hops that use the tunnel netdevice. This is only
        relevant when recreate_loopback is true.

    :param bool update_nexthops:
        updates next hops, keeping the current loopback RIF. This
        is only relevant when recreate_loopback is false.

    :param struct netlink_ext_ack \*extack:
        *undescribed*

.. This file was automatic generated / don't edit.

