.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_ethtool.c

.. _`ice_nvm_version_str`:

ice_nvm_version_str
===================

.. c:function:: char *ice_nvm_version_str(struct ice_hw *hw)

    format the NVM version strings

    :param struct ice_hw \*hw:
        ptr to the hardware info

.. _`ice_get_rxnfc`:

ice_get_rxnfc
=============

.. c:function:: int ice_get_rxnfc(struct net_device *netdev, struct ethtool_rxnfc *cmd, u32 __always_unused *rule_locs)

    command to get RX flow classification rules

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_rxnfc \*cmd:
        ethtool rxnfc command

    :param u32 __always_unused \*rule_locs:
        buffer to rturn Rx flow classification rules

.. _`ice_get_rxnfc.description`:

Description
-----------

Returns Success if the command is supported.

.. _`ice_get_pauseparam`:

ice_get_pauseparam
==================

.. c:function:: void ice_get_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *pause)

    Get Flow Control status

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_pauseparam \*pause:
        ethernet pause (flow control) parameters

.. _`ice_set_pauseparam`:

ice_set_pauseparam
==================

.. c:function:: int ice_set_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *pause)

    Set Flow Control parameter

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_pauseparam \*pause:
        return tx/rx flow control status

.. _`ice_get_rxfh_key_size`:

ice_get_rxfh_key_size
=====================

.. c:function:: u32 ice_get_rxfh_key_size(struct net_device __always_unused *netdev)

    get the RSS hash key size

    :param struct net_device __always_unused \*netdev:
        network interface device structure

.. _`ice_get_rxfh_key_size.description`:

Description
-----------

Returns the table size.

.. _`ice_get_rxfh_indir_size`:

ice_get_rxfh_indir_size
=======================

.. c:function:: u32 ice_get_rxfh_indir_size(struct net_device *netdev)

    get the rx flow hash indirection table size

    :param struct net_device \*netdev:
        network interface device structure

.. _`ice_get_rxfh_indir_size.description`:

Description
-----------

Returns the table size.

.. _`ice_get_rxfh`:

ice_get_rxfh
============

.. c:function:: int ice_get_rxfh(struct net_device *netdev, u32 *indir, u8 *key, u8 *hfunc)

    get the rx flow hash indirection table

    :param struct net_device \*netdev:
        network interface device structure

    :param u32 \*indir:
        indirection table

    :param u8 \*key:
        hash key

    :param u8 \*hfunc:
        hash function

.. _`ice_get_rxfh.description`:

Description
-----------

Reads the indirection table directly from the hardware.

.. _`ice_set_rxfh`:

ice_set_rxfh
============

.. c:function:: int ice_set_rxfh(struct net_device *netdev, const u32 *indir, const u8 *key, const u8 hfunc)

    set the rx flow hash indirection table

    :param struct net_device \*netdev:
        network interface device structure

    :param const u32 \*indir:
        indirection table

    :param const u8 \*key:
        hash key

    :param const u8 hfunc:
        hash function

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

    :param struct net_device \*netdev:
        network interface device structure

.. _`ice_set_ethtool_ops.description`:

Description
-----------

setup netdev ethtool ops with ice specific ops

.. This file was automatic generated / don't edit.

