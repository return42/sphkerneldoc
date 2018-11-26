.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/qlogic/qlge/qlge_main.c

.. _`ql_update_mac_hdr_len`:

ql_update_mac_hdr_len
=====================

.. c:function:: void ql_update_mac_hdr_len(struct ql_adapter *qdev, struct ib_mac_iocb_rsp *ib_mac_rsp, void *page, size_t *len)

    helper routine to update the mac header length based on vlan tags if present

    :param qdev:
        *undescribed*
    :type qdev: struct ql_adapter \*

    :param ib_mac_rsp:
        *undescribed*
    :type ib_mac_rsp: struct ib_mac_iocb_rsp \*

    :param page:
        *undescribed*
    :type page: void \*

    :param len:
        *undescribed*
    :type len: size_t \*

.. _`qlge_update_hw_vlan_features`:

qlge_update_hw_vlan_features
============================

.. c:function:: int qlge_update_hw_vlan_features(struct net_device *ndev, netdev_features_t features)

    helper routine to reinitialize the adapter based on the features to enable/disable hardware vlan accel

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

    :param features:
        *undescribed*
    :type features: netdev_features_t

.. This file was automatic generated / don't edit.

