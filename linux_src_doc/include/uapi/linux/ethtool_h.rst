.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/ethtool.h

.. _`ethtool_cmd`:

struct ethtool_cmd
==================

.. c:type:: struct ethtool_cmd

    DEPRECATED, link control and status This structure is DEPRECATED, please use struct ethtool_link_settings.

.. _`ethtool_cmd.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_cmd {
        __u32 cmd;
        __u32 supported;
        __u32 advertising;
        __u16 speed;
        __u8 duplex;
        __u8 port;
        __u8 phy_address;
        __u8 transceiver;
        __u8 autoneg;
        __u8 mdio_support;
        __u32 maxtxpkt;
        __u32 maxrxpkt;
        __u16 speed_hi;
        __u8 eth_tp_mdix;
        __u8 eth_tp_mdix_ctrl;
        __u32 lp_advertising;
        __u32 reserved[2];
    }

.. _`ethtool_cmd.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GSET``\  or \ ``ETHTOOL_SSET``\ 

supported
    Bitmask of \ ``SUPPORTED``\ \_\* flags for the link modes,
    physical connectors and other link features for which the
    interface supports autonegotiation or auto-detection.
    Read-only.

advertising
    Bitmask of \ ``ADVERTISED``\ \_\* flags for the link modes,
    physical connectors and other link features that are
    advertised through autonegotiation or enabled for
    auto-detection.

speed
    Low bits of the speed, 1Mb units, 0 to INT_MAX or SPEED_UNKNOWN

duplex
    Duplex mode; one of \ ``DUPLEX``\ \_\*

port
    Physical connector type; one of \ ``PORT``\ \_\*

phy_address
    MDIO address of PHY (transceiver); 0 or 255 if not
    applicable.  For clause 45 PHYs this is the PRTAD.

transceiver
    Historically used to distinguish different possible
    PHY types, but not in a consistent way.  Deprecated.

autoneg
    Enable/disable autonegotiation and auto-detection;
    either \ ``AUTONEG_DISABLE``\  or \ ``AUTONEG_ENABLE``\ 

mdio_support
    Bitmask of \ ``ETH_MDIO_SUPPORTS``\ \_\* flags for the MDIO
    protocols supported by the interface; 0 if unknown.
    Read-only.

maxtxpkt
    Historically used to report TX IRQ coalescing; now
    obsoleted by \ :c:type:`struct ethtool_coalesce <ethtool_coalesce>`\ .  Read-only; deprecated.

maxrxpkt
    Historically used to report RX IRQ coalescing; now
    obsoleted by \ :c:type:`struct ethtool_coalesce <ethtool_coalesce>`\ .  Read-only; deprecated.

speed_hi
    High bits of the speed, 1Mb units, 0 to INT_MAX or SPEED_UNKNOWN

eth_tp_mdix
    Ethernet twisted-pair MDI(-X) status; one of
    \ ``ETH_TP_MDI``\ \_\*.  If the status is unknown or not applicable, the
    value will be \ ``ETH_TP_MDI_INVALID``\ .  Read-only.

eth_tp_mdix_ctrl
    Ethernet twisted pair MDI(-X) control; one of
    \ ``ETH_TP_MDI``\ \_\*.  If MDI(-X) control is not implemented, reads
    yield \ ``ETH_TP_MDI_INVALID``\  and writes may be ignored or rejected.
    When written successfully, the link should be renegotiated if
    necessary.

lp_advertising
    Bitmask of \ ``ADVERTISED``\ \_\* flags for the link modes
    and other link features that the link partner advertised
    through autonegotiation; 0 if unknown or not applicable.
    Read-only.

.. _`ethtool_cmd.description`:

Description
-----------

The link speed in Mbps is split between \ ``speed``\  and \ ``speed_hi``\ .  Use
the \ :c:func:`ethtool_cmd_speed`\  and \ :c:func:`ethtool_cmd_speed_set`\  functions to
access it.

If autonegotiation is disabled, the speed and \ ``duplex``\  represent the
fixed link mode and are writable if the driver supports multiple
link modes.  If it is enabled then they are read-only; if the link
is up they represent the negotiated link mode; if the link is down,
the speed is 0, \ ``SPEED_UNKNOWN``\  or the highest enabled speed and
\ ``duplex``\  is \ ``DUPLEX_UNKNOWN``\  or the best enabled duplex mode.

Some hardware interfaces may have multiple PHYs and/or physical
connectors fitted or do not allow the driver to detect which are
fitted.  For these interfaces \ ``port``\  and/or \ ``phy_address``\  may be
writable, possibly dependent on \ ``autoneg``\  being \ ``AUTONEG_DISABLE``\ .
Otherwise, attempts to write different values may be ignored or
rejected.

Users should assume that all fields not marked read-only are
writable and subject to validation by the driver.  They should use
\ ``ETHTOOL_GSET``\  to get the current values before making specific
changes and then applying them with \ ``ETHTOOL_SSET``\ .

Drivers that implement \ :c:func:`set_settings`\  should validate all fields
other than \ ``cmd``\  that are not described as read-only or deprecated,
and must ignore all fields described as read-only.

Deprecated fields should be ignored by both users and drivers.

.. _`ethtool_drvinfo`:

struct ethtool_drvinfo
======================

.. c:type:: struct ethtool_drvinfo

    general driver and device information

.. _`ethtool_drvinfo.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_drvinfo {
        __u32 cmd;
        char driver[32];
        char version[32];
        char fw_version[ETHTOOL_FWVERS_LEN];
        char bus_info[ETHTOOL_BUSINFO_LEN];
        char erom_version[ETHTOOL_EROMVERS_LEN];
        char reserved2[12];
        __u32 n_priv_flags;
        __u32 n_stats;
        __u32 testinfo_len;
        __u32 eedump_len;
        __u32 regdump_len;
    }

.. _`ethtool_drvinfo.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GDRVINFO``\ 

driver
    Driver short name.  This should normally match the name
    in its bus driver structure (e.g. pci_driver::name).  Must
    not be an empty string.

version
    Driver version string; may be an empty string

fw_version
    Firmware version string; may be an empty string

bus_info
    Device bus address.  This should match the \ :c:func:`dev_name`\ 
    string for the underlying bus device, if there is one.  May be
    an empty string.

erom_version
    Expansion ROM version string; may be an empty string

n_priv_flags
    Number of flags valid for \ ``ETHTOOL_GPFLAGS``\  and
    \ ``ETHTOOL_SPFLAGS``\  commands; also the number of strings in the
    \ ``ETH_SS_PRIV_FLAGS``\  set

n_stats
    Number of u64 statistics returned by the \ ``ETHTOOL_GSTATS``\ 
    command; also the number of strings in the \ ``ETH_SS_STATS``\  set

testinfo_len
    Number of results returned by the \ ``ETHTOOL_TEST``\ 
    command; also the number of strings in the \ ``ETH_SS_TEST``\  set

eedump_len
    Size of EEPROM accessible through the \ ``ETHTOOL_GEEPROM``\ 
    and \ ``ETHTOOL_SEEPROM``\  commands, in bytes

regdump_len
    Size of register dump returned by the \ ``ETHTOOL_GREGS``\ 
    command, in bytes

.. _`ethtool_drvinfo.description`:

Description
-----------

Users can use the \ ``ETHTOOL_GSSET_INFO``\  command to get the number of
strings in any string set (from Linux 2.6.34).

Drivers should set at most \ ``driver``\ , \ ``version``\ , \ ``fw_version``\  and
\ ``bus_info``\  in their \ :c:func:`get_drvinfo`\  implementation.  The ethtool
core fills in the other fields using other driver operations.

.. _`ethtool_wolinfo`:

struct ethtool_wolinfo
======================

.. c:type:: struct ethtool_wolinfo

    Wake-On-Lan configuration

.. _`ethtool_wolinfo.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_wolinfo {
        __u32 cmd;
        __u32 supported;
        __u32 wolopts;
        __u8 sopass[SOPASS_MAX];
    }

.. _`ethtool_wolinfo.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GWOL``\  or \ ``ETHTOOL_SWOL``\ 

supported
    Bitmask of \ ``WAKE``\ \_\* flags for supported Wake-On-Lan modes.
    Read-only.

wolopts
    Bitmask of \ ``WAKE``\ \_\* flags for enabled Wake-On-Lan modes.

sopass
    SecureOn(tm) password; meaningful only if \ ``WAKE_MAGICSECURE``\ 
    is set in \ ``wolopts``\ .

.. _`ethtool_regs`:

struct ethtool_regs
===================

.. c:type:: struct ethtool_regs

    hardware register dump

.. _`ethtool_regs.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_regs {
        __u32 cmd;
        __u32 version;
        __u32 len;
        __u8 data[0];
    }

.. _`ethtool_regs.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GREGS``\ 

version
    Dump format version.  This is driver-specific and may
    distinguish different chips/revisions.  Drivers must use new
    version numbers whenever the dump format changes in an
    incompatible way.

len
    On entry, the real length of \ ``data``\ .  On return, the number of
    bytes used.

data
    Buffer for the register dump

.. _`ethtool_regs.description`:

Description
-----------

Users should use \ ``ETHTOOL_GDRVINFO``\  to find the maximum length of
a register dump for the interface.  They must allocate the buffer
immediately following this structure.

.. _`ethtool_eeprom`:

struct ethtool_eeprom
=====================

.. c:type:: struct ethtool_eeprom

    EEPROM dump

.. _`ethtool_eeprom.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_eeprom {
        __u32 cmd;
        __u32 magic;
        __u32 offset;
        __u32 len;
        __u8 data[0];
    }

.. _`ethtool_eeprom.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GEEPROM``\ , \ ``ETHTOOL_GMODULEEEPROM``\  or
    \ ``ETHTOOL_SEEPROM``\ 

magic
    A 'magic cookie' value to guard against accidental changes.
    The value passed in to \ ``ETHTOOL_SEEPROM``\  must match the value
    returned by \ ``ETHTOOL_GEEPROM``\  for the same device.  This is
    unused when \ ``cmd``\  is \ ``ETHTOOL_GMODULEEEPROM``\ .

offset
    Offset within the EEPROM to begin reading/writing, in bytes

len
    On entry, number of bytes to read/write.  On successful
    return, number of bytes actually read/written.  In case of
    error, this may indicate at what point the error occurred.

data
    Buffer to read/write from

.. _`ethtool_eeprom.description`:

Description
-----------

Users may use \ ``ETHTOOL_GDRVINFO``\  or \ ``ETHTOOL_GMODULEINFO``\  to find
the length of an on-board or module EEPROM, respectively.  They
must allocate the buffer immediately following this structure.

.. _`ethtool_eee`:

struct ethtool_eee
==================

.. c:type:: struct ethtool_eee

    Energy Efficient Ethernet information

.. _`ethtool_eee.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_eee {
        __u32 cmd;
        __u32 supported;
        __u32 advertised;
        __u32 lp_advertised;
        __u32 eee_active;
        __u32 eee_enabled;
        __u32 tx_lpi_enabled;
        __u32 tx_lpi_timer;
        __u32 reserved[2];
    }

.. _`ethtool_eee.members`:

Members
-------

cmd
    ETHTOOL_{G,S}EEE

supported
    Mask of \ ``SUPPORTED``\ \_\* flags for the speed/duplex combinations
    for which there is EEE support.

advertised
    Mask of \ ``ADVERTISED``\ \_\* flags for the speed/duplex combinations
    advertised as eee capable.

lp_advertised
    Mask of \ ``ADVERTISED``\ \_\* flags for the speed/duplex
    combinations advertised by the link partner as eee capable.

eee_active
    Result of the eee auto negotiation.

eee_enabled
    EEE configured mode (enabled/disabled).

tx_lpi_enabled
    Whether the interface should assert its tx lpi, given
    that eee was negotiated.

tx_lpi_timer
    Time in microseconds the interface delays prior to asserting
    its tx lpi (after reaching 'idle' state). Effective only when eee
    was negotiated and tx_lpi_enabled was set.

.. _`ethtool_modinfo`:

struct ethtool_modinfo
======================

.. c:type:: struct ethtool_modinfo

    plugin module eeprom information

.. _`ethtool_modinfo.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_modinfo {
        __u32 cmd;
        __u32 type;
        __u32 eeprom_len;
        __u32 reserved[8];
    }

.. _`ethtool_modinfo.members`:

Members
-------

cmd
    %ETHTOOL_GMODULEINFO

type
    Standard the module information conforms to \ ``ETH_MODULE_SFF_xxxx``\ 

eeprom_len
    Length of the eeprom

.. _`ethtool_modinfo.description`:

Description
-----------

This structure is used to return the information to
properly size memory for a subsequent call to \ ``ETHTOOL_GMODULEEEPROM``\ .
The type code indicates the eeprom data format

.. _`ethtool_coalesce`:

struct ethtool_coalesce
=======================

.. c:type:: struct ethtool_coalesce

    coalescing parameters for IRQs and stats updates

.. _`ethtool_coalesce.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_coalesce {
        __u32 cmd;
        __u32 rx_coalesce_usecs;
        __u32 rx_max_coalesced_frames;
        __u32 rx_coalesce_usecs_irq;
        __u32 rx_max_coalesced_frames_irq;
        __u32 tx_coalesce_usecs;
        __u32 tx_max_coalesced_frames;
        __u32 tx_coalesce_usecs_irq;
        __u32 tx_max_coalesced_frames_irq;
        __u32 stats_block_coalesce_usecs;
        __u32 use_adaptive_rx_coalesce;
        __u32 use_adaptive_tx_coalesce;
        __u32 pkt_rate_low;
        __u32 rx_coalesce_usecs_low;
        __u32 rx_max_coalesced_frames_low;
        __u32 tx_coalesce_usecs_low;
        __u32 tx_max_coalesced_frames_low;
        __u32 pkt_rate_high;
        __u32 rx_coalesce_usecs_high;
        __u32 rx_max_coalesced_frames_high;
        __u32 tx_coalesce_usecs_high;
        __u32 tx_max_coalesced_frames_high;
        __u32 rate_sample_interval;
    }

.. _`ethtool_coalesce.members`:

Members
-------

cmd
    ETHTOOL_{G,S}COALESCE

rx_coalesce_usecs
    How many usecs to delay an RX interrupt after
    a packet arrives.

rx_max_coalesced_frames
    Maximum number of packets to receive
    before an RX interrupt.

rx_coalesce_usecs_irq
    Same as \ ``rx_coalesce_usecs``\ , except that
    this value applies while an IRQ is being serviced by the host.

rx_max_coalesced_frames_irq
    Same as \ ``rx_max_coalesced_frames``\ ,
    except that this value applies while an IRQ is being serviced
    by the host.

tx_coalesce_usecs
    How many usecs to delay a TX interrupt after
    a packet is sent.

tx_max_coalesced_frames
    Maximum number of packets to be sent
    before a TX interrupt.

tx_coalesce_usecs_irq
    Same as \ ``tx_coalesce_usecs``\ , except that
    this value applies while an IRQ is being serviced by the host.

tx_max_coalesced_frames_irq
    Same as \ ``tx_max_coalesced_frames``\ ,
    except that this value applies while an IRQ is being serviced
    by the host.

stats_block_coalesce_usecs
    How many usecs to delay in-memory
    statistics block updates.  Some drivers do not have an
    in-memory statistic block, and in such cases this value is
    ignored.  This value must not be zero.

use_adaptive_rx_coalesce
    Enable adaptive RX coalescing.

use_adaptive_tx_coalesce
    Enable adaptive TX coalescing.

pkt_rate_low
    Threshold for low packet rate (packets per second).

rx_coalesce_usecs_low
    How many usecs to delay an RX interrupt after
    a packet arrives, when the packet rate is below \ ``pkt_rate_low``\ .

rx_max_coalesced_frames_low
    Maximum number of packets to be received
    before an RX interrupt, when the packet rate is below \ ``pkt_rate_low``\ .

tx_coalesce_usecs_low
    How many usecs to delay a TX interrupt after
    a packet is sent, when the packet rate is below \ ``pkt_rate_low``\ .

tx_max_coalesced_frames_low
    Maximum nuumber of packets to be sent before
    a TX interrupt, when the packet rate is below \ ``pkt_rate_low``\ .

pkt_rate_high
    Threshold for high packet rate (packets per second).

rx_coalesce_usecs_high
    How many usecs to delay an RX interrupt after
    a packet arrives, when the packet rate is above \ ``pkt_rate_high``\ .

rx_max_coalesced_frames_high
    Maximum number of packets to be received
    before an RX interrupt, when the packet rate is above \ ``pkt_rate_high``\ .

tx_coalesce_usecs_high
    How many usecs to delay a TX interrupt after
    a packet is sent, when the packet rate is above \ ``pkt_rate_high``\ .

tx_max_coalesced_frames_high
    Maximum number of packets to be sent before
    a TX interrupt, when the packet rate is above \ ``pkt_rate_high``\ .

rate_sample_interval
    How often to do adaptive coalescing packet rate
    sampling, measured in seconds.  Must not be zero.

.. _`ethtool_coalesce.description`:

Description
-----------

Each pair of (usecs, max_frames) fields specifies that interrupts
should be coalesced until
(usecs > 0 && time_since_first_completion >= usecs) \|\|
(max_frames > 0 && completed_frames >= max_frames)

It is illegal to set both usecs and max_frames to zero as this
would cause interrupts to never be generated.  To disable
coalescing, set usecs = 0 and max_frames = 1.

Some implementations ignore the value of max_frames and use the
condition time_since_first_completion >= usecs

This is deprecated.  Drivers for hardware that does not support
counting completions should validate that max_frames == !rx_usecs.

Adaptive RX/TX coalescing is an algorithm implemented by some
drivers to improve latency under low packet rates and improve
throughput under high packet rates.  Some drivers only implement
one of RX or TX adaptive coalescing.  Anything not implemented by
the driver causes these values to be silently ignored.

When the packet rate is below \ ``pkt_rate_high``\  but above
\ ``pkt_rate_low``\  (both measured in packets per second) the
normal {rx,tx}_\* coalescing parameters are used.

.. _`ethtool_ringparam`:

struct ethtool_ringparam
========================

.. c:type:: struct ethtool_ringparam

    RX/TX ring parameters

.. _`ethtool_ringparam.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_ringparam {
        __u32 cmd;
        __u32 rx_max_pending;
        __u32 rx_mini_max_pending;
        __u32 rx_jumbo_max_pending;
        __u32 tx_max_pending;
        __u32 rx_pending;
        __u32 rx_mini_pending;
        __u32 rx_jumbo_pending;
        __u32 tx_pending;
    }

.. _`ethtool_ringparam.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GRINGPARAM``\  or \ ``ETHTOOL_SRINGPARAM``\ 

rx_max_pending
    Maximum supported number of pending entries per
    RX ring.  Read-only.

rx_mini_max_pending
    Maximum supported number of pending entries
    per RX mini ring.  Read-only.

rx_jumbo_max_pending
    Maximum supported number of pending entries
    per RX jumbo ring.  Read-only.

tx_max_pending
    Maximum supported number of pending entries per
    TX ring.  Read-only.

rx_pending
    Current maximum number of pending entries per RX ring

rx_mini_pending
    Current maximum number of pending entries per RX
    mini ring

rx_jumbo_pending
    Current maximum number of pending entries per RX
    jumbo ring

tx_pending
    Current maximum supported number of pending entries
    per TX ring

.. _`ethtool_ringparam.description`:

Description
-----------

If the interface does not have separate RX mini and/or jumbo rings,
\ ``rx_mini_max_pending``\  and/or \ ``rx_jumbo_max_pending``\  will be 0.

There may also be driver-dependent minimum values for the number
of entries per ring.

.. _`ethtool_channels`:

struct ethtool_channels
=======================

.. c:type:: struct ethtool_channels

    configuring number of network channel

.. _`ethtool_channels.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_channels {
        __u32 cmd;
        __u32 max_rx;
        __u32 max_tx;
        __u32 max_other;
        __u32 max_combined;
        __u32 rx_count;
        __u32 tx_count;
        __u32 other_count;
        __u32 combined_count;
    }

.. _`ethtool_channels.members`:

Members
-------

cmd
    ETHTOOL_{G,S}CHANNELS

max_rx
    Read only. Maximum number of receive channel the driver support.

max_tx
    Read only. Maximum number of transmit channel the driver support.

max_other
    Read only. Maximum number of other channel the driver support.

max_combined
    Read only. Maximum number of combined channel the driver
    support. Set of queues RX, TX or other.

rx_count
    Valid values are in the range 1 to the max_rx.

tx_count
    Valid values are in the range 1 to the max_tx.

other_count
    Valid values are in the range 1 to the max_other.

combined_count
    Valid values are in the range 1 to the max_combined.

.. _`ethtool_channels.description`:

Description
-----------

This can be used to configure RX, TX and other channels.

.. _`ethtool_pauseparam`:

struct ethtool_pauseparam
=========================

.. c:type:: struct ethtool_pauseparam

    Ethernet pause (flow control) parameters

.. _`ethtool_pauseparam.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_pauseparam {
        __u32 cmd;
        __u32 autoneg;
        __u32 rx_pause;
        __u32 tx_pause;
    }

.. _`ethtool_pauseparam.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GPAUSEPARAM``\  or \ ``ETHTOOL_SPAUSEPARAM``\ 

autoneg
    Flag to enable autonegotiation of pause frame use

rx_pause
    Flag to enable reception of pause frames

tx_pause
    Flag to enable transmission of pause frames

.. _`ethtool_pauseparam.description`:

Description
-----------

Drivers should reject a non-zero setting of \ ``autoneg``\  when
autoneogotiation is disabled (or not supported) for the link.

If the link is autonegotiated, drivers should use
\ :c:func:`mii_advertise_flowctrl`\  or similar code to set the advertised
pause frame capabilities based on the \ ``rx_pause``\  and \ ``tx_pause``\  flags,
even if \ ``autoneg``\  is zero.  They should also allow the advertised
pause frame capabilities to be controlled directly through the
advertising field of \ :c:type:`struct ethtool_cmd <ethtool_cmd>`\ .

If \ ``autoneg``\  is non-zero, the MAC is configured to send and/or
receive pause frames according to the result of autonegotiation.
Otherwise, it is configured directly based on the \ ``rx_pause``\  and
\ ``tx_pause``\  flags.

.. _`ethtool_stringset`:

enum ethtool_stringset
======================

.. c:type:: enum ethtool_stringset

    string set ID

.. _`ethtool_stringset.definition`:

Definition
----------

.. code-block:: c

    enum ethtool_stringset {
        ETH_SS_TEST,
        ETH_SS_STATS,
        ETH_SS_PRIV_FLAGS,
        ETH_SS_NTUPLE_FILTERS,
        ETH_SS_FEATURES,
        ETH_SS_RSS_HASH_FUNCS,
        ETH_SS_TUNABLES,
        ETH_SS_PHY_STATS
    };

.. _`ethtool_stringset.constants`:

Constants
---------

ETH_SS_TEST
    Self-test result names, for use with \ ``ETHTOOL_TEST``\ 

ETH_SS_STATS
    Statistic names, for use with \ ``ETHTOOL_GSTATS``\ 

ETH_SS_PRIV_FLAGS
    Driver private flag names, for use with
    \ ``ETHTOOL_GPFLAGS``\  and \ ``ETHTOOL_SPFLAGS``\ 

ETH_SS_NTUPLE_FILTERS
    Previously used with \ ``ETHTOOL_GRXNTUPLE``\ ;
    now deprecated

ETH_SS_FEATURES
    Device feature names

ETH_SS_RSS_HASH_FUNCS
    RSS hush function names

ETH_SS_TUNABLES
    *undescribed*

ETH_SS_PHY_STATS
    Statistic names, for use with \ ``ETHTOOL_GPHYSTATS``\ 

.. _`ethtool_gstrings`:

struct ethtool_gstrings
=======================

.. c:type:: struct ethtool_gstrings

    string set for data tagging

.. _`ethtool_gstrings.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_gstrings {
        __u32 cmd;
        __u32 string_set;
        __u32 len;
        __u8 data[0];
    }

.. _`ethtool_gstrings.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GSTRINGS``\ 

string_set
    String set ID; one of \ :c:type:`enum ethtool_stringset <ethtool_stringset>`\ 

len
    On return, the number of strings in the string set

data
    Buffer for strings.  Each string is null-padded to a size of
    \ ``ETH_GSTRING_LEN``\ .

.. _`ethtool_gstrings.description`:

Description
-----------

Users must use \ ``ETHTOOL_GSSET_INFO``\  to find the number of strings in
the string set.  They must allocate a buffer of the appropriate
size immediately following this structure.

.. _`ethtool_sset_info`:

struct ethtool_sset_info
========================

.. c:type:: struct ethtool_sset_info

    string set information

.. _`ethtool_sset_info.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_sset_info {
        __u32 cmd;
        __u32 reserved;
        __u64 sset_mask;
        __u32 data[0];
    }

.. _`ethtool_sset_info.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GSSET_INFO``\ 

reserved
    *undescribed*

sset_mask
    On entry, a bitmask of string sets to query, with bits
    numbered according to \ :c:type:`enum ethtool_stringset <ethtool_stringset>`\ .  On return, a
    bitmask of those string sets queried that are supported.

data
    Buffer for string set sizes.  On return, this contains the
    size of each string set that was queried and supported, in
    order of ID.

.. _`ethtool_sset_info.example`:

Example
-------

.. code-block:: c

    The user passes in @sset_mask = 0x7 (sets 0, 1, 2) and on
    return @sset_mask == 0x6 (sets 1, 2).  Then @data[0] contains the
    size of set 1 and @data[1] contains the size of set 2.

    Users must allocate a buffer of the appropriate size (4 * number of
    sets queried) immediately following this structure.


.. _`ethtool_test_flags`:

enum ethtool_test_flags
=======================

.. c:type:: enum ethtool_test_flags

    flags definition of ethtool_test

.. _`ethtool_test_flags.definition`:

Definition
----------

.. code-block:: c

    enum ethtool_test_flags {
        ETH_TEST_FL_OFFLINE,
        ETH_TEST_FL_FAILED,
        ETH_TEST_FL_EXTERNAL_LB,
        ETH_TEST_FL_EXTERNAL_LB_DONE
    };

.. _`ethtool_test_flags.constants`:

Constants
---------

ETH_TEST_FL_OFFLINE
    if set perform online and offline tests, otherwise
    only online tests.

ETH_TEST_FL_FAILED
    Driver set this flag if test fails.

ETH_TEST_FL_EXTERNAL_LB
    Application request to perform external loopback
    test.

ETH_TEST_FL_EXTERNAL_LB_DONE
    Driver performed the external loopback test

.. _`ethtool_test`:

struct ethtool_test
===================

.. c:type:: struct ethtool_test

    device self-test invocation

.. _`ethtool_test.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_test {
        __u32 cmd;
        __u32 flags;
        __u32 reserved;
        __u32 len;
        __u64 data[0];
    }

.. _`ethtool_test.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_TEST``\ 

flags
    A bitmask of flags from \ :c:type:`enum ethtool_test_flags <ethtool_test_flags>`\ .  Some
    flags may be set by the user on entry; others may be set by
    the driver on return.

reserved
    *undescribed*

len
    On return, the number of test results

data
    Array of test results

.. _`ethtool_test.description`:

Description
-----------

Users must use \ ``ETHTOOL_GSSET_INFO``\  or \ ``ETHTOOL_GDRVINFO``\  to find the
number of test results that will be returned.  They must allocate a
buffer of the appropriate size (8 \* number of results) immediately
following this structure.

.. _`ethtool_stats`:

struct ethtool_stats
====================

.. c:type:: struct ethtool_stats

    device-specific statistics

.. _`ethtool_stats.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_stats {
        __u32 cmd;
        __u32 n_stats;
        __u64 data[0];
    }

.. _`ethtool_stats.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GSTATS``\ 

n_stats
    On return, the number of statistics

data
    Array of statistics

.. _`ethtool_stats.description`:

Description
-----------

Users must use \ ``ETHTOOL_GSSET_INFO``\  or \ ``ETHTOOL_GDRVINFO``\  to find the
number of statistics that will be returned.  They must allocate a
buffer of the appropriate size (8 \* number of statistics)
immediately following this structure.

.. _`ethtool_perm_addr`:

struct ethtool_perm_addr
========================

.. c:type:: struct ethtool_perm_addr

    permanent hardware address

.. _`ethtool_perm_addr.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_perm_addr {
        __u32 cmd;
        __u32 size;
        __u8 data[0];
    }

.. _`ethtool_perm_addr.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GPERMADDR``\ 

size
    On entry, the size of the buffer.  On return, the size of the
    address.  The command fails if the buffer is too small.

data
    Buffer for the address

.. _`ethtool_perm_addr.description`:

Description
-----------

Users must allocate the buffer immediately following this structure.
A buffer size of \ ``MAX_ADDR_LEN``\  should be sufficient for any address
type.

.. _`ethtool_tcpip4_spec`:

struct ethtool_tcpip4_spec
==========================

.. c:type:: struct ethtool_tcpip4_spec

    flow specification for TCP/IPv4 etc.

.. _`ethtool_tcpip4_spec.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_tcpip4_spec {
        __be32 ip4src;
        __be32 ip4dst;
        __be16 psrc;
        __be16 pdst;
        __u8 tos;
    }

.. _`ethtool_tcpip4_spec.members`:

Members
-------

ip4src
    Source host

ip4dst
    Destination host

psrc
    Source port

pdst
    Destination port

tos
    Type-of-service

.. _`ethtool_tcpip4_spec.description`:

Description
-----------

This can be used to specify a TCP/IPv4, UDP/IPv4 or SCTP/IPv4 flow.

.. _`ethtool_ah_espip4_spec`:

struct ethtool_ah_espip4_spec
=============================

.. c:type:: struct ethtool_ah_espip4_spec

    flow specification for IPsec/IPv4

.. _`ethtool_ah_espip4_spec.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_ah_espip4_spec {
        __be32 ip4src;
        __be32 ip4dst;
        __be32 spi;
        __u8 tos;
    }

.. _`ethtool_ah_espip4_spec.members`:

Members
-------

ip4src
    Source host

ip4dst
    Destination host

spi
    Security parameters index

tos
    Type-of-service

.. _`ethtool_ah_espip4_spec.description`:

Description
-----------

This can be used to specify an IPsec transport or tunnel over IPv4.

.. _`ethtool_usrip4_spec`:

struct ethtool_usrip4_spec
==========================

.. c:type:: struct ethtool_usrip4_spec

    general flow specification for IPv4

.. _`ethtool_usrip4_spec.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_usrip4_spec {
        __be32 ip4src;
        __be32 ip4dst;
        __be32 l4_4_bytes;
        __u8 tos;
        __u8 ip_ver;
        __u8 proto;
    }

.. _`ethtool_usrip4_spec.members`:

Members
-------

ip4src
    Source host

ip4dst
    Destination host

l4_4_bytes
    First 4 bytes of transport (layer 4) header

tos
    Type-of-service

ip_ver
    Value must be \ ``ETH_RX_NFC_IP4``\ ; mask must be 0

proto
    Transport protocol number; mask must be 0

.. _`ethtool_tcpip6_spec`:

struct ethtool_tcpip6_spec
==========================

.. c:type:: struct ethtool_tcpip6_spec

    flow specification for TCP/IPv6 etc.

.. _`ethtool_tcpip6_spec.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_tcpip6_spec {
        __be32 ip6src[4];
        __be32 ip6dst[4];
        __be16 psrc;
        __be16 pdst;
        __u8 tclass;
    }

.. _`ethtool_tcpip6_spec.members`:

Members
-------

ip6src
    Source host

ip6dst
    Destination host

psrc
    Source port

pdst
    Destination port

tclass
    Traffic Class

.. _`ethtool_tcpip6_spec.description`:

Description
-----------

This can be used to specify a TCP/IPv6, UDP/IPv6 or SCTP/IPv6 flow.

.. _`ethtool_ah_espip6_spec`:

struct ethtool_ah_espip6_spec
=============================

.. c:type:: struct ethtool_ah_espip6_spec

    flow specification for IPsec/IPv6

.. _`ethtool_ah_espip6_spec.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_ah_espip6_spec {
        __be32 ip6src[4];
        __be32 ip6dst[4];
        __be32 spi;
        __u8 tclass;
    }

.. _`ethtool_ah_espip6_spec.members`:

Members
-------

ip6src
    Source host

ip6dst
    Destination host

spi
    Security parameters index

tclass
    Traffic Class

.. _`ethtool_ah_espip6_spec.description`:

Description
-----------

This can be used to specify an IPsec transport or tunnel over IPv6.

.. _`ethtool_usrip6_spec`:

struct ethtool_usrip6_spec
==========================

.. c:type:: struct ethtool_usrip6_spec

    general flow specification for IPv6

.. _`ethtool_usrip6_spec.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_usrip6_spec {
        __be32 ip6src[4];
        __be32 ip6dst[4];
        __be32 l4_4_bytes;
        __u8 tclass;
        __u8 l4_proto;
    }

.. _`ethtool_usrip6_spec.members`:

Members
-------

ip6src
    Source host

ip6dst
    Destination host

l4_4_bytes
    First 4 bytes of transport (layer 4) header

tclass
    Traffic Class

l4_proto
    Transport protocol number (nexthdr after any Extension Headers)

.. _`ethtool_flow_ext`:

struct ethtool_flow_ext
=======================

.. c:type:: struct ethtool_flow_ext

    additional RX flow fields

.. _`ethtool_flow_ext.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_flow_ext {
        __u8 padding[2];
        unsigned char h_dest[ETH_ALEN];
        __be16 vlan_etype;
        __be16 vlan_tci;
        __be32 data[2];
    }

.. _`ethtool_flow_ext.members`:

Members
-------

h_dest
    destination MAC address

vlan_etype
    VLAN EtherType

vlan_tci
    VLAN tag control information

data
    user defined data

.. _`ethtool_flow_ext.description`:

Description
-----------

Note, \ ``vlan_etype``\ , \ ``vlan_tci``\ , and \ ``data``\  are only valid if \ ``FLOW_EXT``\ 
is set in \ :c:type:`struct ethtool_rx_flow_spec <ethtool_rx_flow_spec>`\  \ ``flow_type``\ .
\ ``h_dest``\  is valid if \ ``FLOW_MAC_EXT``\  is set.

.. _`ethtool_rx_flow_spec`:

struct ethtool_rx_flow_spec
===========================

.. c:type:: struct ethtool_rx_flow_spec

    classification rule for RX flows

.. _`ethtool_rx_flow_spec.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_rx_flow_spec {
        __u32 flow_type;
        union ethtool_flow_union h_u;
        struct ethtool_flow_ext h_ext;
        union ethtool_flow_union m_u;
        struct ethtool_flow_ext m_ext;
        __u64 ring_cookie;
        __u32 location;
    }

.. _`ethtool_rx_flow_spec.members`:

Members
-------

flow_type
    Type of match to perform, e.g. \ ``TCP_V4_FLOW``\ 

h_u
    Flow fields to match (dependent on \ ``flow_type``\ )

h_ext
    Additional fields to match

m_u
    Masks for flow field bits to be matched

m_ext
    Masks for additional field bits to be matched
    Note, all additional fields must be ignored unless \ ``flow_type``\ 
    includes the \ ``FLOW_EXT``\  or \ ``FLOW_MAC_EXT``\  flag
    (see \ :c:type:`struct ethtool_flow_ext <ethtool_flow_ext>`\  description).

ring_cookie
    RX ring/queue index to deliver to, or \ ``RX_CLS_FLOW_DISC``\ 
    if packets should be discarded

location
    Location of rule in the table.  Locations must be
    numbered such that a flow matching multiple rules will be
    classified according to the first (lowest numbered) rule.

.. _`ethtool_rxnfc`:

struct ethtool_rxnfc
====================

.. c:type:: struct ethtool_rxnfc

    command to get or set RX flow classification rules

.. _`ethtool_rxnfc.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_rxnfc {
        __u32 cmd;
        __u32 flow_type;
        __u64 data;
        struct ethtool_rx_flow_spec fs;
        __u32 rule_cnt;
        __u32 rule_locs[0];
    }

.. _`ethtool_rxnfc.members`:

Members
-------

cmd
    Specific command number - \ ``ETHTOOL_GRXFH``\ , \ ``ETHTOOL_SRXFH``\ ,
    \ ``ETHTOOL_GRXRINGS``\ , \ ``ETHTOOL_GRXCLSRLCNT``\ , \ ``ETHTOOL_GRXCLSRULE``\ ,
    \ ``ETHTOOL_GRXCLSRLALL``\ , \ ``ETHTOOL_SRXCLSRLDEL``\  or \ ``ETHTOOL_SRXCLSRLINS``\ 

flow_type
    Type of flow to be affected, e.g. \ ``TCP_V4_FLOW``\ 

data
    Command-dependent value

fs
    Flow classification rule

rule_cnt
    Number of rules to be affected

rule_locs
    Array of used rule locations

.. _`ethtool_rxnfc.description`:

Description
-----------

For \ ``ETHTOOL_GRXFH``\  and \ ``ETHTOOL_SRXFH``\ , \ ``data``\  is a bitmask indicating
the fields included in the flow hash, e.g. \ ``RXH_IP_SRC``\ .  The following
structure fields must not be used.

For \ ``ETHTOOL_GRXRINGS``\ , \ ``data``\  is set to the number of RX rings/queues
on return.

For \ ``ETHTOOL_GRXCLSRLCNT``\ , \ ``rule_cnt``\  is set to the number of defined
rules on return.  If \ ``data``\  is non-zero on return then it is the
size of the rule table, plus the flag \ ``RX_CLS_LOC_SPECIAL``\  if the
driver supports any special location values.  If that flag is not
set in \ ``data``\  then special location values should not be used.

For \ ``ETHTOOL_GRXCLSRULE``\ , \ ``fs``\ .@location specifies the location of an
existing rule on entry and \ ``fs``\  contains the rule on return.

For \ ``ETHTOOL_GRXCLSRLALL``\ , \ ``rule_cnt``\  specifies the array size of the
user buffer for \ ``rule_locs``\  on entry.  On return, \ ``data``\  is the size
of the rule table, \ ``rule_cnt``\  is the number of defined rules, and
\ ``rule_locs``\  contains the locations of the defined rules.  Drivers
must use the second parameter to \ :c:func:`get_rxnfc`\  instead of \ ``rule_locs``\ .

For \ ``ETHTOOL_SRXCLSRLINS``\ , \ ``fs``\  specifies the rule to add or update.
\ ``fs``\ .@location either specifies the location to use or is a special
location value with \ ``RX_CLS_LOC_SPECIAL``\  flag set.  On return,
\ ``fs``\ .@location is the actual rule location.

For \ ``ETHTOOL_SRXCLSRLDEL``\ , \ ``fs``\ .@location specifies the location of an
existing rule on entry.

A driver supporting the special location values for
\ ``ETHTOOL_SRXCLSRLINS``\  may add the rule at any suitable unused
location, and may remove a rule at a later location (lower
priority) that matches exactly the same set of flows.  The special
values are \ ``RX_CLS_LOC_ANY``\ , selecting any location;
\ ``RX_CLS_LOC_FIRST``\ , selecting the first suitable location (maximum
priority); and \ ``RX_CLS_LOC_LAST``\ , selecting the last suitable
location (minimum priority).  Additional special values may be
defined in future and drivers must return -%EINVAL for any
unrecognised value.

.. _`ethtool_rxfh_indir`:

struct ethtool_rxfh_indir
=========================

.. c:type:: struct ethtool_rxfh_indir

    command to get or set RX flow hash indirection

.. _`ethtool_rxfh_indir.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_rxfh_indir {
        __u32 cmd;
        __u32 size;
        __u32 ring_index[0];
    }

.. _`ethtool_rxfh_indir.members`:

Members
-------

cmd
    Specific command number - \ ``ETHTOOL_GRXFHINDIR``\  or \ ``ETHTOOL_SRXFHINDIR``\ 

size
    On entry, the array size of the user buffer, which may be zero.
    On return from \ ``ETHTOOL_GRXFHINDIR``\ , the array size of the hardware
    indirection table.

ring_index
    RX ring/queue index for each hash value

.. _`ethtool_rxfh_indir.description`:

Description
-----------

For \ ``ETHTOOL_GRXFHINDIR``\ , a \ ``size``\  of zero means that only the size
should be returned.  For \ ``ETHTOOL_SRXFHINDIR``\ , a \ ``size``\  of zero means
the table should be reset to default values.  This last feature
is not supported by the original implementations.

.. _`ethtool_rxfh`:

struct ethtool_rxfh
===================

.. c:type:: struct ethtool_rxfh

    command to get/set RX flow hash indir or/and hash key.

.. _`ethtool_rxfh.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_rxfh {
        __u32 cmd;
        __u32 rss_context;
        __u32 indir_size;
        __u32 key_size;
        __u8 hfunc;
        __u8 rsvd8[3];
        __u32 rsvd32;
        __u32 rss_config[0];
    }

.. _`ethtool_rxfh.members`:

Members
-------

cmd
    Specific command number - \ ``ETHTOOL_GRSSH``\  or \ ``ETHTOOL_SRSSH``\ 

rss_context
    RSS context identifier.

indir_size
    On entry, the array size of the user buffer for the
    indirection table, which may be zero, or (for \ ``ETHTOOL_SRSSH``\ ),
    \ ``ETH_RXFH_INDIR_NO_CHANGE``\ .  On return from \ ``ETHTOOL_GRSSH``\ ,
    the array size of the hardware indirection table.

key_size
    On entry, the array size of the user buffer for the hash key,
    which may be zero.  On return from \ ``ETHTOOL_GRSSH``\ , the size of the
    hardware hash key.

hfunc
    Defines the current RSS hash function used by HW (or to be set to).
    Valid values are one of the \ ``ETH_RSS_HASH``\ \_\*.

rsvd32
    *undescribed*

rss_config
    RX ring/queue index for each hash value i.e., indirection table
    of \ ``indir_size``\  \__u32 elements, followed by hash key of \ ``key_size``\ 
    bytes.

.. _`ethtool_rxfh.description`:

Description
-----------

For \ ``ETHTOOL_GRSSH``\ , a \ ``indir_size``\  and key_size of zero means that only the
size should be returned.  For \ ``ETHTOOL_SRSSH``\ , an \ ``indir_size``\  of
\ ``ETH_RXFH_INDIR_NO_CHANGE``\  means that indir table setting is not requested
and a \ ``indir_size``\  of zero means the indir table should be reset to default
values. An hfunc of zero means that hash function setting is not requested.

.. _`ethtool_rx_ntuple_flow_spec`:

struct ethtool_rx_ntuple_flow_spec
==================================

.. c:type:: struct ethtool_rx_ntuple_flow_spec

    specification for RX flow filter

.. _`ethtool_rx_ntuple_flow_spec.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_rx_ntuple_flow_spec {
        __u32 flow_type;
        union h_u;
        union m_u;
        __u16 vlan_tag;
        __u16 vlan_tag_mask;
        __u64 data;
        __u64 data_mask;
        __s32 action;
    #define ETHTOOL_RXNTUPLE_ACTION_DROP (-1)
    #define ETHTOOL_RXNTUPLE_ACTION_CLEAR (-2)
    }

.. _`ethtool_rx_ntuple_flow_spec.members`:

Members
-------

flow_type
    Type of match to perform, e.g. \ ``TCP_V4_FLOW``\ 

h_u
    Flow field values to match (dependent on \ ``flow_type``\ )

m_u
    Masks for flow field value bits to be ignored

vlan_tag
    VLAN tag to match

vlan_tag_mask
    Mask for VLAN tag bits to be ignored

data
    Driver-dependent data to match

data_mask
    Mask for driver-dependent data bits to be ignored

action
    RX ring/queue index to deliver to (non-negative) or other action
    (negative, e.g. \ ``ETHTOOL_RXNTUPLE_ACTION_DROP``\ )

.. _`ethtool_rx_ntuple_flow_spec.description`:

Description
-----------

For flow types \ ``TCP_V4_FLOW``\ , \ ``UDP_V4_FLOW``\  and \ ``SCTP_V4_FLOW``\ , where
a field value and mask are both zero this is treated as if all mask
bits are set i.e. the field is ignored.

.. _`ethtool_rx_ntuple`:

struct ethtool_rx_ntuple
========================

.. c:type:: struct ethtool_rx_ntuple

    command to set or clear RX flow filter

.. _`ethtool_rx_ntuple.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_rx_ntuple {
        __u32 cmd;
        struct ethtool_rx_ntuple_flow_spec fs;
    }

.. _`ethtool_rx_ntuple.members`:

Members
-------

cmd
    Command number - \ ``ETHTOOL_SRXNTUPLE``\ 

fs
    Flow filter specification

.. _`ethtool_dump`:

struct ethtool_dump
===================

.. c:type:: struct ethtool_dump

    used for retrieving, setting device dump

.. _`ethtool_dump.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_dump {
        __u32 cmd;
        __u32 version;
        __u32 flag;
        __u32 len;
        __u8 data[0];
    }

.. _`ethtool_dump.members`:

Members
-------

cmd
    Command number - \ ``ETHTOOL_GET_DUMP_FLAG``\ , \ ``ETHTOOL_GET_DUMP_DATA``\ , or
    \ ``ETHTOOL_SET_DUMP``\ 

version
    FW version of the dump, filled in by driver

flag
    driver dependent flag for dump setting, filled in by driver during
    get and filled in by ethtool for set operation.
    flag must be initialized by macro ETH_FW_DUMP_DISABLE value when
    firmware dump is disabled.

len
    length of dump data, used as the length of the user buffer on entry to
    \ ``ETHTOOL_GET_DUMP_DATA``\  and this is returned as dump length by driver
    for \ ``ETHTOOL_GET_DUMP_FLAG``\  command

data
    data collected for get dump data operation

.. _`ethtool_get_features_block`:

struct ethtool_get_features_block
=================================

.. c:type:: struct ethtool_get_features_block

    block with state of 32 features

.. _`ethtool_get_features_block.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_get_features_block {
        __u32 available;
        __u32 requested;
        __u32 active;
        __u32 never_changed;
    }

.. _`ethtool_get_features_block.members`:

Members
-------

available
    mask of changeable features

requested
    mask of features requested to be enabled if possible

active
    mask of currently enabled features

never_changed
    mask of features not changeable for any device

.. _`ethtool_gfeatures`:

struct ethtool_gfeatures
========================

.. c:type:: struct ethtool_gfeatures

    command to get state of device's features

.. _`ethtool_gfeatures.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_gfeatures {
        __u32 cmd;
        __u32 size;
        struct ethtool_get_features_block features[0];
    }

.. _`ethtool_gfeatures.members`:

Members
-------

cmd
    command number = \ ``ETHTOOL_GFEATURES``\ 

size
    On entry, the number of elements in the features[] array;
    on return, the number of elements in features[] needed to hold
    all features

features
    state of features

.. _`ethtool_set_features_block`:

struct ethtool_set_features_block
=================================

.. c:type:: struct ethtool_set_features_block

    block with request for 32 features

.. _`ethtool_set_features_block.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_set_features_block {
        __u32 valid;
        __u32 requested;
    }

.. _`ethtool_set_features_block.members`:

Members
-------

valid
    mask of features to be changed

requested
    values of features to be changed

.. _`ethtool_sfeatures`:

struct ethtool_sfeatures
========================

.. c:type:: struct ethtool_sfeatures

    command to request change in device's features

.. _`ethtool_sfeatures.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_sfeatures {
        __u32 cmd;
        __u32 size;
        struct ethtool_set_features_block features[0];
    }

.. _`ethtool_sfeatures.members`:

Members
-------

cmd
    command number = \ ``ETHTOOL_SFEATURES``\ 

size
    array size of the features[] array

features
    feature change masks

.. _`ethtool_ts_info`:

struct ethtool_ts_info
======================

.. c:type:: struct ethtool_ts_info

    holds a device's timestamping and PHC association

.. _`ethtool_ts_info.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_ts_info {
        __u32 cmd;
        __u32 so_timestamping;
        __s32 phc_index;
        __u32 tx_types;
        __u32 tx_reserved[3];
        __u32 rx_filters;
        __u32 rx_reserved[3];
    }

.. _`ethtool_ts_info.members`:

Members
-------

cmd
    command number = \ ``ETHTOOL_GET_TS_INFO``\ 

so_timestamping
    bit mask of the sum of the supported SO_TIMESTAMPING flags

phc_index
    device index of the associated PHC, or -1 if there is none

tx_types
    bit mask of the supported hwtstamp_tx_types enumeration values

rx_filters
    bit mask of the supported hwtstamp_rx_filters enumeration values

.. _`ethtool_ts_info.description`:

Description
-----------

The bits in the 'tx_types' and 'rx_filters' fields correspond to
the 'hwtstamp_tx_types' and 'hwtstamp_rx_filters' enumeration values,
respectively.  For example, if the device supports HWTSTAMP_TX_ON,
then (1 << HWTSTAMP_TX_ON) in 'tx_types' will be set.

Drivers should only report the filters they actually support without
upscaling in the SIOCSHWTSTAMP ioctl. If the SIOCSHWSTAMP request for
HWTSTAMP_FILTER_V1_SYNC is supported by HWTSTAMP_FILTER_V1_EVENT, then the
driver should only report HWTSTAMP_FILTER_V1_EVENT in this op.

.. _`ethtool_per_queue_op`:

struct ethtool_per_queue_op
===========================

.. c:type:: struct ethtool_per_queue_op

    apply sub command to the queues in mask.

.. _`ethtool_per_queue_op.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_per_queue_op {
        __u32 cmd;
        __u32 sub_command;
        __u32 queue_mask[__KERNEL_DIV_ROUND_UP(MAX_NUM_QUEUE# 32)];
        char data[];
    }

.. _`ethtool_per_queue_op.members`:

Members
-------

cmd
    ETHTOOL_PERQUEUE

sub_command
    the sub command which apply to each queues

queue_mask
    Bitmap of the queues which sub command apply to

data
    A complete command structure following for each of the queues addressed

.. _`ethtool_link_settings`:

struct ethtool_link_settings
============================

.. c:type:: struct ethtool_link_settings

    link control and status

.. _`ethtool_link_settings.definition`:

Definition
----------

.. code-block:: c

    struct ethtool_link_settings {
        __u32 cmd;
        __u32 speed;
        __u8 duplex;
        __u8 port;
        __u8 phy_address;
        __u8 autoneg;
        __u8 mdio_support;
        __u8 eth_tp_mdix;
        __u8 eth_tp_mdix_ctrl;
        __s8 link_mode_masks_nwords;
        __u32 reserved[8];
        __u32 link_mode_masks[0];
    }

.. _`ethtool_link_settings.members`:

Members
-------

cmd
    Command number = \ ``ETHTOOL_GLINKSETTINGS``\  or \ ``ETHTOOL_SLINKSETTINGS``\ 

speed
    Link speed (Mbps)

duplex
    Duplex mode; one of \ ``DUPLEX``\ \_\*

port
    Physical connector type; one of \ ``PORT``\ \_\*

phy_address
    MDIO address of PHY (transceiver); 0 or 255 if not
    applicable.  For clause 45 PHYs this is the PRTAD.

autoneg
    Enable/disable autonegotiation and auto-detection;
    either \ ``AUTONEG_DISABLE``\  or \ ``AUTONEG_ENABLE``\ 

mdio_support
    Bitmask of \ ``ETH_MDIO_SUPPORTS``\ \_\* flags for the MDIO
    protocols supported by the interface; 0 if unknown.
    Read-only.

eth_tp_mdix
    Ethernet twisted-pair MDI(-X) status; one of
    \ ``ETH_TP_MDI``\ \_\*.  If the status is unknown or not applicable, the
    value will be \ ``ETH_TP_MDI_INVALID``\ .  Read-only.

eth_tp_mdix_ctrl
    Ethernet twisted pair MDI(-X) control; one of
    \ ``ETH_TP_MDI``\ \_\*.  If MDI(-X) control is not implemented, reads
    yield \ ``ETH_TP_MDI_INVALID``\  and writes may be ignored or rejected.
    When written successfully, the link should be renegotiated if
    necessary.

link_mode_masks_nwords
    Number of 32-bit words for each of the
    supported, advertising, lp_advertising link mode bitmaps. For
    \ ``ETHTOOL_GLINKSETTINGS``\ : on entry, number of words passed by user
    (>= 0); on return, if handshake in progress, negative if

.. _`ethtool_link_settings.description`:

Description
-----------

IMPORTANT, Backward compatibility notice: When implementing new
user-space tools, please first try \ ``ETHTOOL_GLINKSETTINGS``\ , and
if it succeeds use \ ``ETHTOOL_SLINKSETTINGS``\  to change link
settings; do not use \ ``ETHTOOL_SSET``\  if \ ``ETHTOOL_GLINKSETTINGS``\ 

If autonegotiation is disabled, the speed and \ ``duplex``\  represent the
fixed link mode and are writable if the driver supports multiple
link modes.  If it is enabled then they are read-only; if the link
is up they represent the negotiated link mode; if the link is down,
the speed is 0, \ ``SPEED_UNKNOWN``\  or the highest enabled speed and
\ ``duplex``\  is \ ``DUPLEX_UNKNOWN``\  or the best enabled duplex mode.

Some hardware interfaces may have multiple PHYs and/or physical
connectors fitted or do not allow the driver to detect which are
fitted.  For these interfaces \ ``port``\  and/or \ ``phy_address``\  may be
writable, possibly dependent on \ ``autoneg``\  being \ ``AUTONEG_DISABLE``\ .
Otherwise, attempts to write different values may be ignored or
rejected.

Deprecated \ ``ethtool_cmd``\  fields transceiver, maxtxpkt and maxrxpkt
are not available in \ ``ethtool_link_settings``\ . Until all drivers are
converted to ignore them or to the new \ ``ethtool_link_settings``\  API,
for both queries and changes, users should always try
\ ``ETHTOOL_GLINKSETTINGS``\  first, and if it fails with -ENOTSUPP stick
only to \ ``ETHTOOL_GSET``\  and \ ``ETHTOOL_SSET``\  consistently. If it
succeeds, then users should stick to \ ``ETHTOOL_GLINKSETTINGS``\  and
\ ``ETHTOOL_SLINKSETTINGS``\  (which would support drivers implementing
either \ ``ethtool_cmd``\  or \ ``ethtool_link_settings``\ ).

Users should assume that all fields not marked read-only are
writable and subject to validation by the driver.  They should use
\ ``ETHTOOL_GLINKSETTINGS``\  to get the current values before making specific
changes and then applying them with \ ``ETHTOOL_SLINKSETTINGS``\ .

Drivers that implement \ ``get_link_ksettings``\  and/or
\ ``set_link_ksettings``\  should ignore the \ ``cmd``\ 
and \ ``link_mode_masks_nwords``\  fields (any change to them overwritten
by kernel), and rely only on kernel's internal
\ ``__ETHTOOL_LINK_MODE_MASK_NBITS``\  and
\ ``ethtool_link_mode_mask_t``\ . Drivers that implement
\ ``set_link_ksettings``\ () should validate all fields other than \ ``cmd``\ 
and \ ``link_mode_masks_nwords``\  that are not described as read-only or
deprecated, and must ignore all fields described as read-only.

.. _`ethtool_link_settings.succeeded`:

succeeded
---------

stick to \ ``ETHTOOL_GLINKSETTINGS``\ /%SLINKSETTINGS in
that case.  Conversely, if \ ``ETHTOOL_GLINKSETTINGS``\  fails, use
\ ``ETHTOOL_GSET``\  to query and \ ``ETHTOOL_SSET``\  to change link
settings; do not use \ ``ETHTOOL_SLINKSETTINGS``\  if
\ ``ETHTOOL_GLINKSETTINGS``\  failed: stick to
\ ``ETHTOOL_GSET``\ /%ETHTOOL_SSET in that case.

.. _`ethtool_link_settings.request-size-unsupported-by-kernel`:

request size unsupported by kernel
----------------------------------

absolute value indicates
kernel expected size and all the other fields but cmd
are 0; otherwise (handshake completed), strictly positive
to indicate size used by kernel and cmd field stays
\ ``ETHTOOL_GLINKSETTINGS``\ , all other fields populated by driver. For
\ ``ETHTOOL_SLINKSETTINGS``\ : must be valid on entry, ie. a positive
value returned previously by \ ``ETHTOOL_GLINKSETTINGS``\ , otherwise
refused. For drivers: ignore this field (use kernel's
\__ETHTOOL_LINK_MODE_MASK_NBITS instead), any change to it will
be overwritten by kernel.

.. This file was automatic generated / don't edit.

