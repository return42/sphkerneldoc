.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_dcb_nl.c

.. _`i40e_get_pfc_delay`:

i40e_get_pfc_delay
==================

.. c:function:: void i40e_get_pfc_delay(struct i40e_hw *hw, u16 *delay)

    retrieve PFC Link Delay

    :param struct i40e_hw \*hw:
        pointer to hardware struct

    :param u16 \*delay:
        holds the PFC Link delay value

.. _`i40e_get_pfc_delay.description`:

Description
-----------

Returns PFC Link Delay from the PRTDCB_GENC.PFCLDA

.. _`i40e_dcbnl_ieee_getets`:

i40e_dcbnl_ieee_getets
======================

.. c:function:: int i40e_dcbnl_ieee_getets(struct net_device *dev, struct ieee_ets *ets)

    retrieve local IEEE ETS configuration

    :param struct net_device \*dev:
        the corresponding netdev

    :param struct ieee_ets \*ets:
        structure to hold the ETS information

.. _`i40e_dcbnl_ieee_getets.description`:

Description
-----------

Returns local IEEE ETS configuration

.. _`i40e_dcbnl_ieee_getpfc`:

i40e_dcbnl_ieee_getpfc
======================

.. c:function:: int i40e_dcbnl_ieee_getpfc(struct net_device *dev, struct ieee_pfc *pfc)

    retrieve local IEEE PFC configuration

    :param struct net_device \*dev:
        the corresponding netdev

    :param struct ieee_pfc \*pfc:
        structure to hold the PFC information

.. _`i40e_dcbnl_ieee_getpfc.description`:

Description
-----------

Returns local IEEE PFC configuration

.. _`i40e_dcbnl_getdcbx`:

i40e_dcbnl_getdcbx
==================

.. c:function:: u8 i40e_dcbnl_getdcbx(struct net_device *dev)

    retrieve current DCBx capability

    :param struct net_device \*dev:
        the corresponding netdev

.. _`i40e_dcbnl_getdcbx.description`:

Description
-----------

Returns DCBx capability features

.. _`i40e_dcbnl_get_perm_hw_addr`:

i40e_dcbnl_get_perm_hw_addr
===========================

.. c:function:: void i40e_dcbnl_get_perm_hw_addr(struct net_device *dev, u8 *perm_addr)

    MAC address used by DCBx

    :param struct net_device \*dev:
        the corresponding netdev

    :param u8 \*perm_addr:
        buffer to store the MAC address

.. _`i40e_dcbnl_get_perm_hw_addr.description`:

Description
-----------

Returns the SAN MAC address used for LLDP exchange

.. _`i40e_dcbnl_set_all`:

i40e_dcbnl_set_all
==================

.. c:function:: void i40e_dcbnl_set_all(struct i40e_vsi *vsi)

    set all the apps and ieee data from DCBx config

    :param struct i40e_vsi \*vsi:
        the corresponding vsi

.. _`i40e_dcbnl_set_all.description`:

Description
-----------

Set up all the IEEE APPs in the DCBNL App Table and generate event for
other settings

.. _`i40e_dcbnl_vsi_del_app`:

i40e_dcbnl_vsi_del_app
======================

.. c:function:: int i40e_dcbnl_vsi_del_app(struct i40e_vsi *vsi, struct i40e_dcb_app_priority_table *app)

    Delete APP for given VSI

    :param struct i40e_vsi \*vsi:
        the corresponding vsi

    :param struct i40e_dcb_app_priority_table \*app:
        APP to delete

.. _`i40e_dcbnl_vsi_del_app.description`:

Description
-----------

Delete given APP from the DCBNL APP table for given
VSI

.. _`i40e_dcbnl_del_app`:

i40e_dcbnl_del_app
==================

.. c:function:: void i40e_dcbnl_del_app(struct i40e_pf *pf, struct i40e_dcb_app_priority_table *app)

    Delete APP on all VSIs

    :param struct i40e_pf \*pf:
        the corresponding PF

    :param struct i40e_dcb_app_priority_table \*app:
        APP to delete

.. _`i40e_dcbnl_del_app.description`:

Description
-----------

Delete given APP from all the VSIs for given PF

.. _`i40e_dcbnl_find_app`:

i40e_dcbnl_find_app
===================

.. c:function:: bool i40e_dcbnl_find_app(struct i40e_dcbx_config *cfg, struct i40e_dcb_app_priority_table *app)

    Search APP in given DCB config

    :param struct i40e_dcbx_config \*cfg:
        DCBX configuration data

    :param struct i40e_dcb_app_priority_table \*app:
        APP to search for

.. _`i40e_dcbnl_find_app.description`:

Description
-----------

Find given APP in the DCB configuration

.. _`i40e_dcbnl_flush_apps`:

i40e_dcbnl_flush_apps
=====================

.. c:function:: void i40e_dcbnl_flush_apps(struct i40e_pf *pf, struct i40e_dcbx_config *old_cfg, struct i40e_dcbx_config *new_cfg)

    Delete all removed APPs

    :param struct i40e_pf \*pf:
        the corresponding PF

    :param struct i40e_dcbx_config \*old_cfg:
        old DCBX configuration data

    :param struct i40e_dcbx_config \*new_cfg:
        new DCBX configuration data

.. _`i40e_dcbnl_flush_apps.description`:

Description
-----------

Find and delete all APPs that are not present in the passed
DCB configuration

.. _`i40e_dcbnl_setup`:

i40e_dcbnl_setup
================

.. c:function:: void i40e_dcbnl_setup(struct i40e_vsi *vsi)

    DCBNL setup

    :param struct i40e_vsi \*vsi:
        the corresponding vsi

.. _`i40e_dcbnl_setup.description`:

Description
-----------

Set up DCBNL ops and initial APP TLVs

.. This file was automatic generated / don't edit.

