.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/iavf/iavf_ethtool.c

.. _`iavf_stats`:

struct iavf_stats
=================

.. c:type:: struct iavf_stats

    definition for an ethtool statistic

.. _`iavf_stats.definition`:

Definition
----------

.. code-block:: c

    struct iavf_stats {
        char stat_string[ETH_GSTRING_LEN];
        int sizeof_stat;
        int stat_offset;
    }

.. _`iavf_stats.members`:

Members
-------

stat_string
    statistic name to display in ethtool -S output

sizeof_stat
    the \ :c:func:`sizeof`\  the stat, must be no greater than sizeof(u64)

stat_offset
    \ :c:func:`offsetof`\  the stat from a base pointer

.. _`iavf_stats.description`:

Description
-----------

This structure defines a statistic to be added to the ethtool stats buffer.
It defines a statistic as offset from a common base pointer. Stats should
be defined in constant arrays using the IAVF_STAT macro, with every element
of the array using the same \_type for calculating the sizeof_stat and
stat_offset.

The \ ``sizeof_stat``\  is expected to be sizeof(u8), sizeof(u16), sizeof(u32) or
sizeof(u64). Other sizes are not expected and will produce a WARN_ONCE from
the \ :c:func:`iavf_add_ethtool_stat`\  helper function.

The \ ``stat_string``\  is interpreted as a format string, allowing formatted
values to be inserted while looping over multiple structures for a given
statistics array. Thus, every statistic string in an array should have the
same type and number of format specifiers, to be formatted by variadic
arguments to the \ :c:func:`iavf_add_stat_string`\  helper function.

.. _`iavf_add_one_ethtool_stat`:

iavf_add_one_ethtool_stat
=========================

.. c:function:: void iavf_add_one_ethtool_stat(u64 *data, void *pointer, const struct iavf_stats *stat)

    copy the stat into the supplied buffer

    :param data:
        location to store the stat value
    :type data: u64 \*

    :param pointer:
        basis for where to copy from
    :type pointer: void \*

    :param stat:
        the stat definition
    :type stat: const struct iavf_stats \*

.. _`iavf_add_one_ethtool_stat.description`:

Description
-----------

Copies the stat data defined by the pointer and stat structure pair into
the memory supplied as data. Used to implement iavf_add_ethtool_stats and
iavf_add_queue_stats. If the pointer is null, data will be zero'd.

.. _`__iavf_add_ethtool_stats`:

\__iavf_add_ethtool_stats
=========================

.. c:function:: void __iavf_add_ethtool_stats(u64 **data, void *pointer, const struct iavf_stats stats, const unsigned int size)

    copy stats into the ethtool supplied buffer

    :param data:
        ethtool stats buffer
    :type data: u64 \*\*

    :param pointer:
        location to copy stats from
    :type pointer: void \*

    :param stats:
        array of stats to copy
    :type stats: const struct iavf_stats

    :param size:
        the size of the stats definition
    :type size: const unsigned int

.. _`__iavf_add_ethtool_stats.description`:

Description
-----------

Copy the stats defined by the stats array using the pointer as a base into
the data buffer supplied by ethtool. Updates the data pointer to point to
the next empty location for successive calls to \__iavf_add_ethtool_stats.
If pointer is null, set the data values to zero and update the pointer to
skip these stats.

.. _`iavf_add_ethtool_stats`:

iavf_add_ethtool_stats
======================

.. c:function::  iavf_add_ethtool_stats( data,  pointer,  stats)

    copy stats into ethtool supplied buffer

    :param data:
        ethtool stats buffer
    :type data: 

    :param pointer:
        location where stats are stored
    :type pointer: 

    :param stats:
        static const array of stat definitions
    :type stats: 

.. _`iavf_add_ethtool_stats.description`:

Description
-----------

Macro to ease the use of \__iavf_add_ethtool_stats by taking a static
constant stats array and passing the \ :c:func:`ARRAY_SIZE`\ . This avoids typos by
ensuring that we pass the size associated with the given stats array.

The parameter \ ``stats``\  is evaluated twice, so parameters with side effects
should be avoided.

.. _`iavf_add_queue_stats`:

iavf_add_queue_stats
====================

.. c:function:: void iavf_add_queue_stats(u64 **data, struct iavf_ring *ring)

    copy queue statistics into supplied buffer

    :param data:
        ethtool stats buffer
    :type data: u64 \*\*

    :param ring:
        the ring to copy
    :type ring: struct iavf_ring \*

.. _`iavf_add_queue_stats.description`:

Description
-----------

Queue statistics must be copied while protected by
u64_stats_fetch_begin_irq, so we can't directly use iavf_add_ethtool_stats.
Assumes that queue stats are defined in iavf_gstrings_queue_stats. If the
ring pointer is null, zero out the queue stat values and update the data
pointer. Otherwise safely copy the stats from the ring into the supplied
buffer and update the data pointer when finished.

This function expects to be called while under \ :c:func:`rcu_read_lock`\ .

.. _`__iavf_add_stat_strings`:

\__iavf_add_stat_strings
========================

.. c:function:: void __iavf_add_stat_strings(u8 **p, const struct iavf_stats stats, const unsigned int size,  ...)

    copy stat strings into ethtool buffer

    :param p:
        ethtool supplied buffer
    :type p: u8 \*\*

    :param stats:
        stat definitions array
    :type stats: const struct iavf_stats

    :param size:
        size of the stats array
    :type size: const unsigned int

    :param ellipsis ellipsis:
        variable arguments

.. _`__iavf_add_stat_strings.description`:

Description
-----------

Format and copy the strings described by stats into the buffer pointed at
by p.

.. _`iavf_add_stat_strings`:

iavf_add_stat_strings
=====================

.. c:function::  iavf_add_stat_strings( p,  stats,  ...)

    copy stat strings into ethtool buffer

    :param p:
        ethtool supplied buffer
    :type p: 

    :param stats:
        stat definitions array
    :type stats: 

    :param ellipsis ellipsis:
        variable arguments

.. _`iavf_add_stat_strings.description`:

Description
-----------

Format and copy the strings described by the const static stats value into
the buffer pointed at by p.

The parameter \ ``stats``\  is evaluated twice, so parameters with side effects
should be avoided. Additionally, stats must be an array such that
ARRAY_SIZE can be called on it.

.. _`iavf_get_link_ksettings`:

iavf_get_link_ksettings
=======================

.. c:function:: int iavf_get_link_ksettings(struct net_device *netdev, struct ethtool_link_ksettings *cmd)

    Get Link Speed and Duplex settings

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param cmd:
        ethtool command
    :type cmd: struct ethtool_link_ksettings \*

.. _`iavf_get_link_ksettings.description`:

Description
-----------

Reports speed/duplex settings. Because this is a VF, we don't know what
kind of link we really have, so we fake it.

.. _`iavf_get_sset_count`:

iavf_get_sset_count
===================

.. c:function:: int iavf_get_sset_count(struct net_device *netdev, int sset)

    Get length of string set

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param sset:
        id of string set
    :type sset: int

.. _`iavf_get_sset_count.description`:

Description
-----------

Reports size of various string tables.

.. _`iavf_get_ethtool_stats`:

iavf_get_ethtool_stats
======================

.. c:function:: void iavf_get_ethtool_stats(struct net_device *netdev, struct ethtool_stats *stats, u64 *data)

    report device statistics

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param stats:
        ethtool statistics structure
    :type stats: struct ethtool_stats \*

    :param data:
        pointer to data buffer
    :type data: u64 \*

.. _`iavf_get_ethtool_stats.description`:

Description
-----------

All statistics are added to the data buffer as an array of u64.

.. _`iavf_get_priv_flag_strings`:

iavf_get_priv_flag_strings
==========================

.. c:function:: void iavf_get_priv_flag_strings(struct net_device *netdev, u8 *data)

    Get private flag strings

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param data:
        buffer for string data
    :type data: u8 \*

.. _`iavf_get_priv_flag_strings.description`:

Description
-----------

Builds the private flags string table

.. _`iavf_get_stat_strings`:

iavf_get_stat_strings
=====================

.. c:function:: void iavf_get_stat_strings(struct net_device *netdev, u8 *data)

    Get stat strings

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param data:
        buffer for string data
    :type data: u8 \*

.. _`iavf_get_stat_strings.description`:

Description
-----------

Builds the statistics string table

.. _`iavf_get_strings`:

iavf_get_strings
================

.. c:function:: void iavf_get_strings(struct net_device *netdev, u32 sset, u8 *data)

    Get string set

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param sset:
        id of string set
    :type sset: u32

    :param data:
        buffer for string data
    :type data: u8 \*

.. _`iavf_get_strings.description`:

Description
-----------

Builds string tables for various string sets

.. _`iavf_get_priv_flags`:

iavf_get_priv_flags
===================

.. c:function:: u32 iavf_get_priv_flags(struct net_device *netdev)

    report device private flags

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`iavf_get_priv_flags.description`:

Description
-----------

The get string set count and the string set should be matched for each
flag returned.  Add new strings for each flag to the iavf_gstrings_priv_flags
array.

Returns a u32 bitmap of flags.

.. _`iavf_set_priv_flags`:

iavf_set_priv_flags
===================

.. c:function:: int iavf_set_priv_flags(struct net_device *netdev, u32 flags)

    set private flags

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param flags:
        bit flags to be set
    :type flags: u32

.. _`iavf_get_msglevel`:

iavf_get_msglevel
=================

.. c:function:: u32 iavf_get_msglevel(struct net_device *netdev)

    Get debug message level

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`iavf_get_msglevel.description`:

Description
-----------

Returns current debug message level.

.. _`iavf_set_msglevel`:

iavf_set_msglevel
=================

.. c:function:: void iavf_set_msglevel(struct net_device *netdev, u32 data)

    Set debug message level

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param data:
        message level
    :type data: u32

.. _`iavf_set_msglevel.description`:

Description
-----------

Set current debug message level. Higher values cause the driver to
be noisier.

.. _`iavf_get_drvinfo`:

iavf_get_drvinfo
================

.. c:function:: void iavf_get_drvinfo(struct net_device *netdev, struct ethtool_drvinfo *drvinfo)

    Get driver info

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param drvinfo:
        ethool driver info structure
    :type drvinfo: struct ethtool_drvinfo \*

.. _`iavf_get_drvinfo.description`:

Description
-----------

Returns information about the driver and device for display to the user.

.. _`iavf_get_ringparam`:

iavf_get_ringparam
==================

.. c:function:: void iavf_get_ringparam(struct net_device *netdev, struct ethtool_ringparam *ring)

    Get ring parameters

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ring:
        ethtool ringparam structure
    :type ring: struct ethtool_ringparam \*

.. _`iavf_get_ringparam.description`:

Description
-----------

Returns current ring parameters. TX and RX rings are reported separately,
but the number of rings is not reported.

.. _`iavf_set_ringparam`:

iavf_set_ringparam
==================

.. c:function:: int iavf_set_ringparam(struct net_device *netdev, struct ethtool_ringparam *ring)

    Set ring parameters

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ring:
        ethtool ringparam structure
    :type ring: struct ethtool_ringparam \*

.. _`iavf_set_ringparam.description`:

Description
-----------

Sets ring parameters. TX and RX rings are controlled separately, but the
number of rings is not specified, so all rings get the same settings.

.. _`__iavf_get_coalesce`:

\__iavf_get_coalesce
====================

.. c:function:: int __iavf_get_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec, int queue)

    get per-queue coalesce settings

    :param netdev:
        the netdev to check
    :type netdev: struct net_device \*

    :param ec:
        ethtool coalesce data structure
    :type ec: struct ethtool_coalesce \*

    :param queue:
        which queue to pick
    :type queue: int

.. _`__iavf_get_coalesce.description`:

Description
-----------

Gets the per-queue settings for coalescence. Specifically Rx and Tx usecs
are per queue. If queue is <0 then we default to queue 0 as the
representative value.

.. _`iavf_get_coalesce`:

iavf_get_coalesce
=================

.. c:function:: int iavf_get_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec)

    Get interrupt coalescing settings

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ec:
        ethtool coalesce structure
    :type ec: struct ethtool_coalesce \*

.. _`iavf_get_coalesce.description`:

Description
-----------

Returns current coalescing settings. This is referred to elsewhere in the
driver as Interrupt Throttle Rate, as this is how the hardware describes
this functionality. Note that if per-queue settings have been modified this
only represents the settings of queue 0.

.. _`iavf_get_per_queue_coalesce`:

iavf_get_per_queue_coalesce
===========================

.. c:function:: int iavf_get_per_queue_coalesce(struct net_device *netdev, u32 queue, struct ethtool_coalesce *ec)

    get coalesce values for specific queue

    :param netdev:
        netdev to read
    :type netdev: struct net_device \*

    :param queue:
        the queue to read
    :type queue: u32

    :param ec:
        coalesce settings from ethtool
    :type ec: struct ethtool_coalesce \*

.. _`iavf_get_per_queue_coalesce.description`:

Description
-----------

Read specific queue's coalesce settings.

.. _`iavf_set_itr_per_queue`:

iavf_set_itr_per_queue
======================

.. c:function:: void iavf_set_itr_per_queue(struct iavf_adapter *adapter, struct ethtool_coalesce *ec, int queue)

    set ITR values for specific queue

    :param adapter:
        the VF adapter struct to set values for
    :type adapter: struct iavf_adapter \*

    :param ec:
        coalesce settings from ethtool
    :type ec: struct ethtool_coalesce \*

    :param queue:
        the queue to modify
    :type queue: int

.. _`iavf_set_itr_per_queue.description`:

Description
-----------

Change the ITR settings for a specific queue.

.. _`__iavf_set_coalesce`:

\__iavf_set_coalesce
====================

.. c:function:: int __iavf_set_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec, int queue)

    set coalesce settings for particular queue

    :param netdev:
        the netdev to change
    :type netdev: struct net_device \*

    :param ec:
        ethtool coalesce settings
    :type ec: struct ethtool_coalesce \*

    :param queue:
        the queue to change
    :type queue: int

.. _`__iavf_set_coalesce.description`:

Description
-----------

Sets the coalesce settings for a particular queue.

.. _`iavf_set_coalesce`:

iavf_set_coalesce
=================

.. c:function:: int iavf_set_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec)

    Set interrupt coalescing settings

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ec:
        ethtool coalesce structure
    :type ec: struct ethtool_coalesce \*

.. _`iavf_set_coalesce.description`:

Description
-----------

Change current coalescing settings for every queue.

.. _`iavf_set_per_queue_coalesce`:

iavf_set_per_queue_coalesce
===========================

.. c:function:: int iavf_set_per_queue_coalesce(struct net_device *netdev, u32 queue, struct ethtool_coalesce *ec)

    set specific queue's coalesce settings

    :param netdev:
        the netdev to change
    :type netdev: struct net_device \*

    :param queue:
        the queue to modify
    :type queue: u32

    :param ec:
        ethtool's coalesce settings
    :type ec: struct ethtool_coalesce \*

.. _`iavf_set_per_queue_coalesce.description`:

Description
-----------

Modifies a specific queue's coalesce settings.

.. _`iavf_get_rxnfc`:

iavf_get_rxnfc
==============

.. c:function:: int iavf_get_rxnfc(struct net_device *netdev, struct ethtool_rxnfc *cmd, u32 *rule_locs)

    command to get RX flow classification rules

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param cmd:
        ethtool rxnfc command
    :type cmd: struct ethtool_rxnfc \*

    :param rule_locs:
        pointer to store rule locations
    :type rule_locs: u32 \*

.. _`iavf_get_rxnfc.description`:

Description
-----------

Returns Success if the command is supported.

.. _`iavf_get_channels`:

iavf_get_channels
=================

.. c:function:: void iavf_get_channels(struct net_device *netdev, struct ethtool_channels *ch)

    get the number of channels supported by the device

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ch:
        channel information structure
    :type ch: struct ethtool_channels \*

.. _`iavf_get_channels.description`:

Description
-----------

For the purposes of our device, we only use combined channels, i.e. a tx/rx
queue pair. Report one extra channel to match our "other" MSI-X vector.

.. _`iavf_set_channels`:

iavf_set_channels
=================

.. c:function:: int iavf_set_channels(struct net_device *netdev, struct ethtool_channels *ch)

    set the new channel count

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ch:
        channel information structure
    :type ch: struct ethtool_channels \*

.. _`iavf_set_channels.description`:

Description
-----------

Negotiate a new number of channels with the PF then do a reset.  During
reset we'll realloc queues and fix the RSS table.  Returns 0 on success,
negative on failure.

.. _`iavf_get_rxfh_key_size`:

iavf_get_rxfh_key_size
======================

.. c:function:: u32 iavf_get_rxfh_key_size(struct net_device *netdev)

    get the RSS hash key size

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`iavf_get_rxfh_key_size.description`:

Description
-----------

Returns the table size.

.. _`iavf_get_rxfh_indir_size`:

iavf_get_rxfh_indir_size
========================

.. c:function:: u32 iavf_get_rxfh_indir_size(struct net_device *netdev)

    get the rx flow hash indirection table size

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`iavf_get_rxfh_indir_size.description`:

Description
-----------

Returns the table size.

.. _`iavf_get_rxfh`:

iavf_get_rxfh
=============

.. c:function:: int iavf_get_rxfh(struct net_device *netdev, u32 *indir, u8 *key, u8 *hfunc)

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
        hash function in use
    :type hfunc: u8 \*

.. _`iavf_get_rxfh.description`:

Description
-----------

Reads the indirection table directly from the hardware. Always returns 0.

.. _`iavf_set_rxfh`:

iavf_set_rxfh
=============

.. c:function:: int iavf_set_rxfh(struct net_device *netdev, const u32 *indir, const u8 *key, const u8 hfunc)

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
        hash function to use
    :type hfunc: const u8

.. _`iavf_set_rxfh.description`:

Description
-----------

Returns -EINVAL if the table specifies an inavlid queue id, otherwise
returns 0 after programming the table.

.. _`iavf_set_ethtool_ops`:

iavf_set_ethtool_ops
====================

.. c:function:: void iavf_set_ethtool_ops(struct net_device *netdev)

    Initialize ethtool ops struct

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`iavf_set_ethtool_ops.description`:

Description
-----------

Sets ethtool ops struct in our netdev so that ethtool can call
our functions.

.. This file was automatic generated / don't edit.

