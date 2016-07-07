.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_dcbnl.c

.. _`fm10k_dcbnl_ieee_getets`:

fm10k_dcbnl_ieee_getets
=======================

.. c:function:: int fm10k_dcbnl_ieee_getets(struct net_device *dev, struct ieee_ets *ets)

    get the ETS configuration for the device

    :param struct net_device \*dev:
        netdev interface for the device

    :param struct ieee_ets \*ets:
        ETS structure to push configuration to

.. _`fm10k_dcbnl_ieee_setets`:

fm10k_dcbnl_ieee_setets
=======================

.. c:function:: int fm10k_dcbnl_ieee_setets(struct net_device *dev, struct ieee_ets *ets)

    set the ETS configuration for the device

    :param struct net_device \*dev:
        netdev interface for the device

    :param struct ieee_ets \*ets:
        ETS structure to pull configuration from

.. _`fm10k_dcbnl_ieee_getpfc`:

fm10k_dcbnl_ieee_getpfc
=======================

.. c:function:: int fm10k_dcbnl_ieee_getpfc(struct net_device *dev, struct ieee_pfc *pfc)

    get the PFC configuration for the device

    :param struct net_device \*dev:
        netdev interface for the device

    :param struct ieee_pfc \*pfc:
        PFC structure to push configuration to

.. _`fm10k_dcbnl_ieee_setpfc`:

fm10k_dcbnl_ieee_setpfc
=======================

.. c:function:: int fm10k_dcbnl_ieee_setpfc(struct net_device *dev, struct ieee_pfc *pfc)

    set the PFC configuration for the device

    :param struct net_device \*dev:
        netdev interface for the device

    :param struct ieee_pfc \*pfc:
        PFC structure to pull configuration from

.. _`fm10k_dcbnl_getdcbx`:

fm10k_dcbnl_getdcbx
===================

.. c:function:: u8 fm10k_dcbnl_getdcbx(struct net_device __always_unused *dev)

    get the DCBX configuration for the device

    :param struct net_device __always_unused \*dev:
        netdev interface for the device

.. _`fm10k_dcbnl_getdcbx.description`:

Description
-----------

Returns that we support only IEEE DCB for this interface

.. _`fm10k_dcbnl_setdcbx`:

fm10k_dcbnl_setdcbx
===================

.. c:function:: u8 fm10k_dcbnl_setdcbx(struct net_device __always_unused *dev, u8 mode)

    get the DCBX configuration for the device

    :param struct net_device __always_unused \*dev:
        netdev interface for the device

    :param u8 mode:
        new mode for this device

.. _`fm10k_dcbnl_setdcbx.description`:

Description
-----------

Returns error on attempt to enable anything but IEEE DCB for this interface

.. _`fm10k_dcbnl_set_ops`:

fm10k_dcbnl_set_ops
===================

.. c:function:: void fm10k_dcbnl_set_ops(struct net_device *dev)

    Configures dcbnl ops pointer for netdev

    :param struct net_device \*dev:
        netdev interface for the device

.. _`fm10k_dcbnl_set_ops.description`:

Description
-----------

Enables PF for DCB by assigning DCBNL ops pointer.

.. This file was automatic generated / don't edit.

