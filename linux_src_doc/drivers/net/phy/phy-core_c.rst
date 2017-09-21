.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/phy-core.c

.. _`phy_lookup_setting`:

phy_lookup_setting
==================

.. c:function:: const struct phy_setting *phy_lookup_setting(int speed, int duplex, const unsigned long *mask, size_t maxbit, bool exact)

    lookup a PHY setting

    :param int speed:
        speed to match

    :param int duplex:
        duplex to match

    :param const unsigned long \*mask:
        allowed link modes

    :param size_t maxbit:
        bit size of link modes

    :param bool exact:
        an exact match is required

.. _`phy_lookup_setting.description`:

Description
-----------

Search the settings array for a setting that matches the speed and
duplex, and which is supported.

If \ ``exact``\  is unset, either an exact match or \ ``NULL``\  for no match will
be returned.

If \ ``exact``\  is set, an exact match, the fastest supported setting at
or below the specified speed, the slowest supported setting, or if
they all fail, \ ``NULL``\  will be returned.

.. _`phy_read_mmd`:

phy_read_mmd
============

.. c:function:: int phy_read_mmd(struct phy_device *phydev, int devad, u32 regnum)

    Convenience function for reading a register from an MMD on a given PHY.

    :param struct phy_device \*phydev:
        The phy_device struct

    :param int devad:
        The MMD to read from (0..31)

    :param u32 regnum:
        The register on the MMD to read (0..65535)

.. _`phy_read_mmd.description`:

Description
-----------

Same rules as for \ :c:func:`phy_read`\ ;

.. _`phy_write_mmd`:

phy_write_mmd
=============

.. c:function:: int phy_write_mmd(struct phy_device *phydev, int devad, u32 regnum, u16 val)

    Convenience function for writing a register on an MMD on a given PHY.

    :param struct phy_device \*phydev:
        The phy_device struct

    :param int devad:
        The MMD to read from

    :param u32 regnum:
        The register on the MMD to read

    :param u16 val:
        value to write to \ ``regnum``\ 

.. _`phy_write_mmd.description`:

Description
-----------

Same rules as for \ :c:func:`phy_write`\ ;

.. This file was automatic generated / don't edit.

