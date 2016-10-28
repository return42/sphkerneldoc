.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/qlogic/qlge/qlge_main.c

.. _`ql_update_mac_hdr_len`:

ql_update_mac_hdr_len
=====================

.. c:function:: void ql_update_mac_hdr_len(struct ql_adapter *qdev, struct ib_mac_iocb_rsp *ib_mac_rsp, void *page, size_t *len)

    helper routine to update the mac header length based on vlan tags if present

    :param struct ql_adapter \*qdev:
        *undescribed*

    :param struct ib_mac_iocb_rsp \*ib_mac_rsp:
        *undescribed*

    :param void \*page:
        *undescribed*

    :param size_t \*len:
        *undescribed*

.. _`qlge_update_hw_vlan_features`:

qlge_update_hw_vlan_features
============================

.. c:function:: int qlge_update_hw_vlan_features(struct net_device *ndev, netdev_features_t features)

    helper routine to reinitialize the adapter based on the features to enable/disable hardware vlan accel

    :param struct net_device \*ndev:
        *undescribed*

    :param netdev_features_t features:
        *undescribed*

.. This file was automatic generated / don't edit.

