.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40evf/i40evf_ethtool.c

.. _`i40evf_get_settings`:

i40evf_get_settings
===================

.. c:function:: int i40evf_get_settings(struct net_device *netdev, struct ethtool_cmd *ecmd)

    Get Link Speed and Duplex settings

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_cmd \*ecmd:
        ethtool command

.. _`i40evf_get_settings.description`:

Description
-----------

Reports speed/duplex settings. Because this is a VF, we don't know what
kind of link we really have, so we fake it.

.. _`i40evf_get_sset_count`:

i40evf_get_sset_count
=====================

.. c:function:: int i40evf_get_sset_count(struct net_device *netdev, int sset)

    Get length of string set

    :param struct net_device \*netdev:
        network interface device structure

    :param int sset:
        id of string set

.. _`i40evf_get_sset_count.description`:

Description
-----------

Reports size of string table. This driver only supports
strings for statistics.

.. _`i40evf_get_ethtool_stats`:

i40evf_get_ethtool_stats
========================

.. c:function:: void i40evf_get_ethtool_stats(struct net_device *netdev, struct ethtool_stats *stats, u64 *data)

    report device statistics

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_stats \*stats:
        ethtool statistics structure

    :param u64 \*data:
        pointer to data buffer

.. _`i40evf_get_ethtool_stats.description`:

Description
-----------

All statistics are added to the data buffer as an array of u64.

.. _`i40evf_get_strings`:

i40evf_get_strings
==================

.. c:function:: void i40evf_get_strings(struct net_device *netdev, u32 sset, u8 *data)

    Get string set

    :param struct net_device \*netdev:
        network interface device structure

    :param u32 sset:
        id of string set

    :param u8 \*data:
        buffer for string data

.. _`i40evf_get_strings.description`:

Description
-----------

Builds stats string table.

.. _`i40evf_get_msglevel`:

i40evf_get_msglevel
===================

.. c:function:: u32 i40evf_get_msglevel(struct net_device *netdev)

    Get debug message level

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40evf_get_msglevel.description`:

Description
-----------

Returns current debug message level.

.. _`i40evf_set_msglevel`:

i40evf_set_msglevel
===================

.. c:function:: void i40evf_set_msglevel(struct net_device *netdev, u32 data)

    Set debug message level

    :param struct net_device \*netdev:
        network interface device structure

    :param u32 data:
        message level

.. _`i40evf_set_msglevel.description`:

Description
-----------

Set current debug message level. Higher values cause the driver to
be noisier.

.. _`i40evf_get_drvinfo`:

i40evf_get_drvinfo
==================

.. c:function:: void i40evf_get_drvinfo(struct net_device *netdev, struct ethtool_drvinfo *drvinfo)

    Get driver info

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_drvinfo \*drvinfo:
        ethool driver info structure

.. _`i40evf_get_drvinfo.description`:

Description
-----------

Returns information about the driver and device for display to the user.

.. _`i40evf_get_ringparam`:

i40evf_get_ringparam
====================

.. c:function:: void i40evf_get_ringparam(struct net_device *netdev, struct ethtool_ringparam *ring)

    Get ring parameters

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_ringparam \*ring:
        ethtool ringparam structure

.. _`i40evf_get_ringparam.description`:

Description
-----------

Returns current ring parameters. TX and RX rings are reported separately,
but the number of rings is not reported.

.. _`i40evf_set_ringparam`:

i40evf_set_ringparam
====================

.. c:function:: int i40evf_set_ringparam(struct net_device *netdev, struct ethtool_ringparam *ring)

    Set ring parameters

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_ringparam \*ring:
        ethtool ringparam structure

.. _`i40evf_set_ringparam.description`:

Description
-----------

Sets ring parameters. TX and RX rings are controlled separately, but the
number of rings is not specified, so all rings get the same settings.

.. _`i40evf_get_coalesce`:

i40evf_get_coalesce
===================

.. c:function:: int i40evf_get_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec)

    Get interrupt coalescing settings

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_coalesce \*ec:
        ethtool coalesce structure

.. _`i40evf_get_coalesce.description`:

Description
-----------

Returns current coalescing settings. This is referred to elsewhere in the
driver as Interrupt Throttle Rate, as this is how the hardware describes
this functionality.

.. _`i40evf_set_coalesce`:

i40evf_set_coalesce
===================

.. c:function:: int i40evf_set_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec)

    Set interrupt coalescing settings

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_coalesce \*ec:
        ethtool coalesce structure

.. _`i40evf_set_coalesce.description`:

Description
-----------

Change current coalescing settings.

.. _`i40evf_get_rxnfc`:

i40evf_get_rxnfc
================

.. c:function:: int i40evf_get_rxnfc(struct net_device *netdev, struct ethtool_rxnfc *cmd, u32 *rule_locs)

    command to get RX flow classification rules

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_rxnfc \*cmd:
        ethtool rxnfc command

    :param u32 \*rule_locs:
        *undescribed*

.. _`i40evf_get_rxnfc.description`:

Description
-----------

Returns Success if the command is supported.

.. _`i40evf_get_channels`:

i40evf_get_channels
===================

.. c:function:: void i40evf_get_channels(struct net_device *netdev, struct ethtool_channels *ch)

    get the number of channels supported by the device

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_channels \*ch:
        channel information structure

.. _`i40evf_get_channels.description`:

Description
-----------

For the purposes of our device, we only use combined channels, i.e. a tx/rx
queue pair. Report one extra channel to match our "other" MSI-X vector.

.. _`i40evf_get_rxfh_key_size`:

i40evf_get_rxfh_key_size
========================

.. c:function:: u32 i40evf_get_rxfh_key_size(struct net_device *netdev)

    get the RSS hash key size

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40evf_get_rxfh_key_size.description`:

Description
-----------

Returns the table size.

.. _`i40evf_get_rxfh_indir_size`:

i40evf_get_rxfh_indir_size
==========================

.. c:function:: u32 i40evf_get_rxfh_indir_size(struct net_device *netdev)

    get the rx flow hash indirection table size

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40evf_get_rxfh_indir_size.description`:

Description
-----------

Returns the table size.

.. _`i40evf_get_rxfh`:

i40evf_get_rxfh
===============

.. c:function:: int i40evf_get_rxfh(struct net_device *netdev, u32 *indir, u8 *key, u8 *hfunc)

    get the rx flow hash indirection table

    :param struct net_device \*netdev:
        network interface device structure

    :param u32 \*indir:
        indirection table

    :param u8 \*key:
        hash key

    :param u8 \*hfunc:
        *undescribed*

.. _`i40evf_get_rxfh.description`:

Description
-----------

Reads the indirection table directly from the hardware. Always returns 0.

.. _`i40evf_set_rxfh`:

i40evf_set_rxfh
===============

.. c:function:: int i40evf_set_rxfh(struct net_device *netdev, const u32 *indir, const u8 *key, const u8 hfunc)

    set the rx flow hash indirection table

    :param struct net_device \*netdev:
        network interface device structure

    :param const u32 \*indir:
        indirection table

    :param const u8 \*key:
        hash key

    :param const u8 hfunc:
        *undescribed*

.. _`i40evf_set_rxfh.description`:

Description
-----------

Returns -EINVAL if the table specifies an inavlid queue id, otherwise
returns 0 after programming the table.

.. _`i40evf_set_ethtool_ops`:

i40evf_set_ethtool_ops
======================

.. c:function:: void i40evf_set_ethtool_ops(struct net_device *netdev)

    Initialize ethtool ops struct

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40evf_set_ethtool_ops.description`:

Description
-----------

Sets ethtool ops struct in our netdev so that ethtool can call
our functions.

.. This file was automatic generated / don't edit.

