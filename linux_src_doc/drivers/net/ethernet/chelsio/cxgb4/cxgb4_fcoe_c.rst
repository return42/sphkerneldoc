.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/cxgb4_fcoe.c

.. _`cxgb_fcoe_enable`:

cxgb_fcoe_enable
================

.. c:function:: int cxgb_fcoe_enable(struct net_device *netdev)

    enable FCoE offload features

    :param netdev:
        net device
    :type netdev: struct net_device \*

.. _`cxgb_fcoe_enable.description`:

Description
-----------

Returns 0 on success or -EINVAL on failure.

.. _`cxgb_fcoe_disable`:

cxgb_fcoe_disable
=================

.. c:function:: int cxgb_fcoe_disable(struct net_device *netdev)

    disable FCoE offload

    :param netdev:
        net device
    :type netdev: struct net_device \*

.. _`cxgb_fcoe_disable.description`:

Description
-----------

Returns 0 on success or -EINVAL on failure.

.. This file was automatic generated / don't edit.

