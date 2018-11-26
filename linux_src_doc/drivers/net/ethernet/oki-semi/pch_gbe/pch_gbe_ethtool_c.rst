.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/oki-semi/pch_gbe/pch_gbe_ethtool.c

.. _`pch_gbe_get_link_ksettings`:

pch_gbe_get_link_ksettings
==========================

.. c:function:: int pch_gbe_get_link_ksettings(struct net_device *netdev, struct ethtool_link_ksettings *ecmd)

    Get device-specific settings

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param ecmd:
        Ethtool command
    :type ecmd: struct ethtool_link_ksettings \*

.. _`pch_gbe_get_link_ksettings.return`:

Return
------

0:                      Successful.

.. _`pch_gbe_get_link_ksettings.negative-value`:

Negative value
--------------

Failed.

.. _`pch_gbe_set_link_ksettings`:

pch_gbe_set_link_ksettings
==========================

.. c:function:: int pch_gbe_set_link_ksettings(struct net_device *netdev, const struct ethtool_link_ksettings *ecmd)

    Set device-specific settings

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param ecmd:
        Ethtool command
    :type ecmd: const struct ethtool_link_ksettings \*

.. _`pch_gbe_set_link_ksettings.return`:

Return
------

0:                      Successful.

.. _`pch_gbe_set_link_ksettings.negative-value`:

Negative value
--------------

Failed.

.. _`pch_gbe_get_regs_len`:

pch_gbe_get_regs_len
====================

.. c:function:: int pch_gbe_get_regs_len(struct net_device *netdev)

    Report the size of device registers

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

.. _`pch_gbe_get_regs_len.return`:

Return
------

the size of device registers.

.. _`pch_gbe_get_drvinfo`:

pch_gbe_get_drvinfo
===================

.. c:function:: void pch_gbe_get_drvinfo(struct net_device *netdev, struct ethtool_drvinfo *drvinfo)

    Report driver information

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param drvinfo:
        Driver information structure
    :type drvinfo: struct ethtool_drvinfo \*

.. _`pch_gbe_get_regs`:

pch_gbe_get_regs
================

.. c:function:: void pch_gbe_get_regs(struct net_device *netdev, struct ethtool_regs *regs, void *p)

    Get device registers

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param regs:
        Ethtool register structure
    :type regs: struct ethtool_regs \*

    :param p:
        Buffer pointer of read device register date
    :type p: void \*

.. _`pch_gbe_get_wol`:

pch_gbe_get_wol
===============

.. c:function:: void pch_gbe_get_wol(struct net_device *netdev, struct ethtool_wolinfo *wol)

    Report whether Wake-on-Lan is enabled

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param wol:
        Wake-on-Lan information
    :type wol: struct ethtool_wolinfo \*

.. _`pch_gbe_set_wol`:

pch_gbe_set_wol
===============

.. c:function:: int pch_gbe_set_wol(struct net_device *netdev, struct ethtool_wolinfo *wol)

    Turn Wake-on-Lan on or off

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param wol:
        Pointer of wake-on-Lan information straucture
    :type wol: struct ethtool_wolinfo \*

.. _`pch_gbe_set_wol.return`:

Return
------

0:                      Successful.

.. _`pch_gbe_set_wol.negative-value`:

Negative value
--------------

Failed.

.. _`pch_gbe_nway_reset`:

pch_gbe_nway_reset
==================

.. c:function:: int pch_gbe_nway_reset(struct net_device *netdev)

    Restart autonegotiation

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

.. _`pch_gbe_nway_reset.return`:

Return
------

0:                      Successful.

.. _`pch_gbe_nway_reset.negative-value`:

Negative value
--------------

Failed.

.. _`pch_gbe_get_ringparam`:

pch_gbe_get_ringparam
=====================

.. c:function:: void pch_gbe_get_ringparam(struct net_device *netdev, struct ethtool_ringparam *ring)

    Report ring sizes

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param ring:
        Ring param structure
    :type ring: struct ethtool_ringparam \*

.. _`pch_gbe_set_ringparam`:

pch_gbe_set_ringparam
=====================

.. c:function:: int pch_gbe_set_ringparam(struct net_device *netdev, struct ethtool_ringparam *ring)

    Set ring sizes

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param ring:
        Ring param structure
        Returns
        0:                      Successful.
    :type ring: struct ethtool_ringparam \*

.. _`pch_gbe_set_ringparam.negative-value`:

Negative value
--------------

Failed.

.. _`pch_gbe_get_pauseparam`:

pch_gbe_get_pauseparam
======================

.. c:function:: void pch_gbe_get_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *pause)

    Report pause parameters

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param pause:
        Pause parameters structure
    :type pause: struct ethtool_pauseparam \*

.. _`pch_gbe_set_pauseparam`:

pch_gbe_set_pauseparam
======================

.. c:function:: int pch_gbe_set_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *pause)

    Set pause parameters

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param pause:
        Pause parameters structure
    :type pause: struct ethtool_pauseparam \*

.. _`pch_gbe_set_pauseparam.return`:

Return
------

0:                      Successful.

.. _`pch_gbe_set_pauseparam.negative-value`:

Negative value
--------------

Failed.

.. _`pch_gbe_get_strings`:

pch_gbe_get_strings
===================

.. c:function:: void pch_gbe_get_strings(struct net_device *netdev, u32 stringset, u8 *data)

    Return a set of strings that describe the requested objects

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param stringset:
        Select the stringset. [ETH_SS_TEST] [ETH_SS_STATS]
    :type stringset: u32

    :param data:
        Pointer of read string data.
    :type data: u8 \*

.. _`pch_gbe_get_ethtool_stats`:

pch_gbe_get_ethtool_stats
=========================

.. c:function:: void pch_gbe_get_ethtool_stats(struct net_device *netdev, struct ethtool_stats *stats, u64 *data)

    Return statistics about the device

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param stats:
        Ethtool statue structure
    :type stats: struct ethtool_stats \*

    :param data:
        Pointer of read status area
    :type data: u64 \*

.. This file was automatic generated / don't edit.

