.. -*- coding: utf-8; mode: rst -*-

======
mdio.c
======


.. _`mdio45_probe`:

mdio45_probe
============

.. c:function:: int mdio45_probe (struct mdio_if_info *mdio, int prtad)

    probe for an MDIO (clause 45) device

    :param struct mdio_if_info \*mdio:
        MDIO interface

    :param int prtad:
        Expected PHY address



.. _`mdio45_probe.description`:

Description
-----------

This sets ``prtad`` and ``mmds`` in the MDIO interface if successful.
Returns 0 on success, negative on error.



.. _`mdio_set_flag`:

mdio_set_flag
=============

.. c:function:: int mdio_set_flag (const struct mdio_if_info *mdio, int prtad, int devad, u16 addr, int mask, bool sense)

    set or clear flag in an MDIO register

    :param const struct mdio_if_info \*mdio:
        MDIO interface

    :param int prtad:
        PHY address

    :param int devad:
        MMD address

    :param u16 addr:
        Register address

    :param int mask:
        Mask for flag (single bit set)

    :param bool sense:
        New value of flag



.. _`mdio_set_flag.this-debounces-changes`:

This debounces changes
----------------------

it does not write the register if the flag
already has the proper value.  Returns 0 on success, negative on error.



.. _`mdio45_links_ok`:

mdio45_links_ok
===============

.. c:function:: int mdio45_links_ok (const struct mdio_if_info *mdio, u32 mmd_mask)

    is link status up/OK

    :param const struct mdio_if_info \*mdio:
        MDIO interface

    :param u32 mmd_mask:
        Mask for MMDs to check



.. _`mdio45_links_ok.description`:

Description
-----------

Returns 1 if the PHY reports link status up/OK, 0 otherwise.
``mmd_mask`` is normally ``mdio``\ ->mmds, but if loopback is enabled
the MMDs being bypassed should be excluded from the mask.



.. _`mdio45_nway_restart`:

mdio45_nway_restart
===================

.. c:function:: int mdio45_nway_restart (const struct mdio_if_info *mdio)

    restart auto-negotiation for this interface

    :param const struct mdio_if_info \*mdio:
        MDIO interface



.. _`mdio45_nway_restart.description`:

Description
-----------

Returns 0 on success, negative on error.



.. _`mdio45_ethtool_gset_npage`:

mdio45_ethtool_gset_npage
=========================

.. c:function:: void mdio45_ethtool_gset_npage (const struct mdio_if_info *mdio, struct ethtool_cmd *ecmd, u32 npage_adv, u32 npage_lpa)

    get settings for ETHTOOL_GSET

    :param const struct mdio_if_info \*mdio:
        MDIO interface

    :param struct ethtool_cmd \*ecmd:
        Ethtool request structure

    :param u32 npage_adv:
        Modes currently advertised on next pages

    :param u32 npage_lpa:
        Modes advertised by link partner on next pages



.. _`mdio45_ethtool_gset_npage.description`:

Description
-----------

The ``ecmd`` parameter is expected to have been cleared before calling
:c:func:`mdio45_ethtool_gset_npage`.

Since the CSRs for auto-negotiation using next pages are not fully
standardised, this function does not attempt to decode them.  The
caller must pass them in.



.. _`mdio_mii_ioctl`:

mdio_mii_ioctl
==============

.. c:function:: int mdio_mii_ioctl (const struct mdio_if_info *mdio, struct mii_ioctl_data *mii_data, int cmd)

    MII ioctl interface for MDIO (clause 22 or 45) PHYs

    :param const struct mdio_if_info \*mdio:
        MDIO interface

    :param struct mii_ioctl_data \*mii_data:
        MII ioctl data structure

    :param int cmd:
        MII ioctl command



.. _`mdio_mii_ioctl.description`:

Description
-----------

Returns 0 on success, negative on error.

