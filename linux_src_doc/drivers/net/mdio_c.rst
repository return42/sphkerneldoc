.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/mdio.c

.. _`mdio45_probe`:

mdio45_probe
============

.. c:function:: int mdio45_probe(struct mdio_if_info *mdio, int prtad)

    probe for an MDIO (clause 45) device

    :param mdio:
        MDIO interface
    :type mdio: struct mdio_if_info \*

    :param prtad:
        Expected PHY address
    :type prtad: int

.. _`mdio45_probe.description`:

Description
-----------

This sets \ ``prtad``\  and \ ``mmds``\  in the MDIO interface if successful.
Returns 0 on success, negative on error.

.. _`mdio_set_flag`:

mdio_set_flag
=============

.. c:function:: int mdio_set_flag(const struct mdio_if_info *mdio, int prtad, int devad, u16 addr, int mask, bool sense)

    set or clear flag in an MDIO register

    :param mdio:
        MDIO interface
    :type mdio: const struct mdio_if_info \*

    :param prtad:
        PHY address
    :type prtad: int

    :param devad:
        MMD address
    :type devad: int

    :param addr:
        Register address
    :type addr: u16

    :param mask:
        Mask for flag (single bit set)
    :type mask: int

    :param sense:
        New value of flag
    :type sense: bool

.. _`mdio_set_flag.this-debounces-changes`:

This debounces changes
----------------------

it does not write the register if the flag
already has the proper value.  Returns 0 on success, negative on error.

.. _`mdio45_links_ok`:

mdio45_links_ok
===============

.. c:function:: int mdio45_links_ok(const struct mdio_if_info *mdio, u32 mmd_mask)

    is link status up/OK

    :param mdio:
        MDIO interface
    :type mdio: const struct mdio_if_info \*

    :param mmd_mask:
        Mask for MMDs to check
    :type mmd_mask: u32

.. _`mdio45_links_ok.description`:

Description
-----------

Returns 1 if the PHY reports link status up/OK, 0 otherwise.
\ ``mmd_mask``\  is normally \ ``mdio->mmds``\ , but if loopback is enabled
the MMDs being bypassed should be excluded from the mask.

.. _`mdio45_nway_restart`:

mdio45_nway_restart
===================

.. c:function:: int mdio45_nway_restart(const struct mdio_if_info *mdio)

    restart auto-negotiation for this interface

    :param mdio:
        MDIO interface
    :type mdio: const struct mdio_if_info \*

.. _`mdio45_nway_restart.description`:

Description
-----------

Returns 0 on success, negative on error.

.. _`mdio45_ethtool_gset_npage`:

mdio45_ethtool_gset_npage
=========================

.. c:function:: void mdio45_ethtool_gset_npage(const struct mdio_if_info *mdio, struct ethtool_cmd *ecmd, u32 npage_adv, u32 npage_lpa)

    get settings for ETHTOOL_GSET

    :param mdio:
        MDIO interface
    :type mdio: const struct mdio_if_info \*

    :param ecmd:
        Ethtool request structure
    :type ecmd: struct ethtool_cmd \*

    :param npage_adv:
        Modes currently advertised on next pages
    :type npage_adv: u32

    :param npage_lpa:
        Modes advertised by link partner on next pages
    :type npage_lpa: u32

.. _`mdio45_ethtool_gset_npage.description`:

Description
-----------

The \ ``ecmd``\  parameter is expected to have been cleared before calling
\ :c:func:`mdio45_ethtool_gset_npage`\ .

Since the CSRs for auto-negotiation using next pages are not fully
standardised, this function does not attempt to decode them.  The
caller must pass them in.

.. _`mdio45_ethtool_ksettings_get_npage`:

mdio45_ethtool_ksettings_get_npage
==================================

.. c:function:: void mdio45_ethtool_ksettings_get_npage(const struct mdio_if_info *mdio, struct ethtool_link_ksettings *cmd, u32 npage_adv, u32 npage_lpa)

    get settings for ETHTOOL_GLINKSETTINGS

    :param mdio:
        MDIO interface
    :type mdio: const struct mdio_if_info \*

    :param cmd:
        Ethtool request structure
    :type cmd: struct ethtool_link_ksettings \*

    :param npage_adv:
        Modes currently advertised on next pages
    :type npage_adv: u32

    :param npage_lpa:
        Modes advertised by link partner on next pages
    :type npage_lpa: u32

.. _`mdio45_ethtool_ksettings_get_npage.description`:

Description
-----------

The \ ``cmd``\  parameter is expected to have been cleared before calling
\ :c:func:`mdio45_ethtool_ksettings_get_npage`\ .

Since the CSRs for auto-negotiation using next pages are not fully
standardised, this function does not attempt to decode them.  The
caller must pass them in.

.. _`mdio_mii_ioctl`:

mdio_mii_ioctl
==============

.. c:function:: int mdio_mii_ioctl(const struct mdio_if_info *mdio, struct mii_ioctl_data *mii_data, int cmd)

    MII ioctl interface for MDIO (clause 22 or 45) PHYs

    :param mdio:
        MDIO interface
    :type mdio: const struct mdio_if_info \*

    :param mii_data:
        MII ioctl data structure
    :type mii_data: struct mii_ioctl_data \*

    :param cmd:
        MII ioctl command
    :type cmd: int

.. _`mdio_mii_ioctl.description`:

Description
-----------

Returns 0 on success, negative on error.

.. This file was automatic generated / don't edit.

