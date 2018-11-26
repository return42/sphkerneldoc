.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_ethtool.c

.. _`ice_nvm_version_str`:

ice_nvm_version_str
===================

.. c:function:: char *ice_nvm_version_str(struct ice_hw *hw)

    format the NVM version strings

    :param hw:
        ptr to the hardware info
    :type hw: struct ice_hw \*

.. _`ice_phy_type_to_ethtool`:

ice_phy_type_to_ethtool
=======================

.. c:function:: void ice_phy_type_to_ethtool(struct net_device *netdev, struct ethtool_link_ksettings *ks)

    convert the phy_types to ethtool link modes

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ks:
        ethtool link ksettings struct to fill out
    :type ks: struct ethtool_link_ksettings \*

.. _`ice_get_settings_link_up`:

ice_get_settings_link_up
========================

.. c:function:: void ice_get_settings_link_up(struct ethtool_link_ksettings *ks, struct net_device *netdev)

    Get Link settings for when link is up

    :param ks:
        ethtool ksettings to fill in
    :type ks: struct ethtool_link_ksettings \*

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ice_get_settings_link_down`:

ice_get_settings_link_down
==========================

.. c:function:: void ice_get_settings_link_down(struct ethtool_link_ksettings *ks, struct net_device __always_unused *netdev)

    Get the Link settings when link is down

    :param ks:
        ethtool ksettings to fill in
    :type ks: struct ethtool_link_ksettings \*

    :param netdev:
        network interface device structure
    :type netdev: struct net_device __always_unused \*

.. _`ice_get_settings_link_down.description`:

Description
-----------

Reports link settings that can be determined when link is down

.. _`ice_get_link_ksettings`:

ice_get_link_ksettings
======================

.. c:function:: int ice_get_link_ksettings(struct net_device *netdev, struct ethtool_link_ksettings *ks)

    Get Link Speed and Duplex settings

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ks:
        ethtool ksettings
    :type ks: struct ethtool_link_ksettings \*

.. _`ice_get_link_ksettings.description`:

Description
-----------

Reports speed/duplex settings based on media_type

.. _`ice_ksettings_find_adv_link_speed`:

ice_ksettings_find_adv_link_speed
=================================

.. c:function:: u16 ice_ksettings_find_adv_link_speed(const struct ethtool_link_ksettings *ks)

    Find advertising link speed

    :param ks:
        ethtool ksettings
    :type ks: const struct ethtool_link_ksettings \*

.. _`ice_setup_autoneg`:

ice_setup_autoneg
=================

.. c:function:: int ice_setup_autoneg(struct ice_port_info *p, struct ethtool_link_ksettings *ks, struct ice_aqc_set_phy_cfg_data *config, u8 autoneg_enabled, u8 *autoneg_changed, struct net_device *netdev)

    :param p:
        port info
    :type p: struct ice_port_info \*

    :param ks:
        ethtool_link_ksettings
    :type ks: struct ethtool_link_ksettings \*

    :param config:
        configuration that will be sent down to FW
    :type config: struct ice_aqc_set_phy_cfg_data \*

    :param autoneg_enabled:
        autonegotiation is enabled or not
    :type autoneg_enabled: u8

    :param autoneg_changed:
        will there a change in autonegotiation
    :type autoneg_changed: u8 \*

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ice_setup_autoneg.description`:

Description
-----------

Setup PHY autonegotiation feature

.. _`ice_set_link_ksettings`:

ice_set_link_ksettings
======================

.. c:function:: int ice_set_link_ksettings(struct net_device *netdev, const struct ethtool_link_ksettings *ks)

    Set Speed and Duplex

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ks:
        ethtool ksettings
    :type ks: const struct ethtool_link_ksettings \*

.. _`ice_set_link_ksettings.description`:

Description
-----------

Set speed/duplex per media_types advertised/forced

.. _`ice_get_rxnfc`:

ice_get_rxnfc
=============

.. c:function:: int ice_get_rxnfc(struct net_device *netdev, struct ethtool_rxnfc *cmd, u32 __always_unused *rule_locs)

    command to get RX flow classification rules

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param cmd:
        ethtool rxnfc command
    :type cmd: struct ethtool_rxnfc \*

    :param rule_locs:
        buffer to rturn Rx flow classification rules
    :type rule_locs: u32 __always_unused \*

.. _`ice_get_rxnfc.description`:

Description
-----------

Returns Success if the command is supported.

.. _`ice_get_pauseparam`:

ice_get_pauseparam
==================

.. c:function:: void ice_get_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *pause)

    Get Flow Control status

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param pause:
        ethernet pause (flow control) parameters
    :type pause: struct ethtool_pauseparam \*

.. _`ice_set_pauseparam`:

ice_set_pauseparam
==================

.. c:function:: int ice_set_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *pause)

    Set Flow Control parameter

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param pause:
        return tx/rx flow control status
    :type pause: struct ethtool_pauseparam \*

.. _`ice_get_rxfh_key_size`:

ice_get_rxfh_key_size
=====================

.. c:function:: u32 ice_get_rxfh_key_size(struct net_device __always_unused *netdev)

    get the RSS hash key size

    :param netdev:
        network interface device structure
    :type netdev: struct net_device __always_unused \*

.. _`ice_get_rxfh_key_size.description`:

Description
-----------

Returns the table size.

.. _`ice_get_rxfh_indir_size`:

ice_get_rxfh_indir_size
=======================

.. c:function:: u32 ice_get_rxfh_indir_size(struct net_device *netdev)

    get the rx flow hash indirection table size

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ice_get_rxfh_indir_size.description`:

Description
-----------

Returns the table size.

.. _`ice_get_rxfh`:

ice_get_rxfh
============

.. c:function:: int ice_get_rxfh(struct net_device *netdev, u32 *indir, u8 *key, u8 *hfunc)

    get the rx flow hash indirection table

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param indir:
        indirection table
    :type indir: u32 \*

    :param key:
        hash key
    :type key: u8 \*

    :param hfunc:
        hash function
    :type hfunc: u8 \*

.. _`ice_get_rxfh.description`:

Description
-----------

Reads the indirection table directly from the hardware.

.. _`ice_set_rxfh`:

ice_set_rxfh
============

.. c:function:: int ice_set_rxfh(struct net_device *netdev, const u32 *indir, const u8 *key, const u8 hfunc)

    set the rx flow hash indirection table

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param indir:
        indirection table
    :type indir: const u32 \*

    :param key:
        hash key
    :type key: const u8 \*

    :param hfunc:
        hash function
    :type hfunc: const u8

.. _`ice_set_rxfh.description`:

Description
-----------

Returns -EINVAL if the table specifies an invalid queue id, otherwise
returns 0 after programming the table.

.. _`ice_set_ethtool_ops`:

ice_set_ethtool_ops
===================

.. c:function:: void ice_set_ethtool_ops(struct net_device *netdev)

    setup netdev ethtool ops

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ice_set_ethtool_ops.description`:

Description
-----------

setup netdev ethtool ops with ice specific ops

.. This file was automatic generated / don't edit.

