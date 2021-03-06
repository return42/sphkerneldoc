.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/phy-core.c

.. _`phy_lookup_setting`:

phy_lookup_setting
==================

.. c:function:: const struct phy_setting *phy_lookup_setting(int speed, int duplex, const unsigned long *mask, size_t maxbit, bool exact)

    lookup a PHY setting

    :param speed:
        speed to match
    :type speed: int

    :param duplex:
        duplex to match
    :type duplex: int

    :param mask:
        allowed link modes
    :type mask: const unsigned long \*

    :param maxbit:
        bit size of link modes
    :type maxbit: size_t

    :param exact:
        an exact match is required
    :type exact: bool

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

.. _`phy_resolve_aneg_linkmode`:

phy_resolve_aneg_linkmode
=========================

.. c:function:: void phy_resolve_aneg_linkmode(struct phy_device *phydev)

    resolve the advertisements into phy settings

    :param phydev:
        The phy_device struct
    :type phydev: struct phy_device \*

.. _`phy_resolve_aneg_linkmode.description`:

Description
-----------

Resolve our and the link partner advertisements into their corresponding
speed and duplex. If full duplex was negotiated, extract the pause mode
from the link partner mask.

.. _`phy_read_mmd`:

phy_read_mmd
============

.. c:function:: int phy_read_mmd(struct phy_device *phydev, int devad, u32 regnum)

    Convenience function for reading a register from an MMD on a given PHY.

    :param phydev:
        The phy_device struct
    :type phydev: struct phy_device \*

    :param devad:
        The MMD to read from (0..31)
    :type devad: int

    :param regnum:
        The register on the MMD to read (0..65535)
    :type regnum: u32

.. _`phy_read_mmd.description`:

Description
-----------

Same rules as for \ :c:func:`phy_read`\ ;

.. _`phy_write_mmd`:

phy_write_mmd
=============

.. c:function:: int phy_write_mmd(struct phy_device *phydev, int devad, u32 regnum, u16 val)

    Convenience function for writing a register on an MMD on a given PHY.

    :param phydev:
        The phy_device struct
    :type phydev: struct phy_device \*

    :param devad:
        The MMD to read from
    :type devad: int

    :param regnum:
        The register on the MMD to read
    :type regnum: u32

    :param val:
        value to write to \ ``regnum``\ 
    :type val: u16

.. _`phy_write_mmd.description`:

Description
-----------

Same rules as for \ :c:func:`phy_write`\ ;

.. _`__phy_modify`:

\__phy_modify
=============

.. c:function:: int __phy_modify(struct phy_device *phydev, u32 regnum, u16 mask, u16 set)

    Convenience function for modifying a PHY register

    :param phydev:
        a pointer to a \ :c:type:`struct phy_device <phy_device>`\ 
    :type phydev: struct phy_device \*

    :param regnum:
        register number
    :type regnum: u32

    :param mask:
        bit mask of bits to clear
    :type mask: u16

    :param set:
        bit mask of bits to set
    :type set: u16

.. _`__phy_modify.description`:

Description
-----------

Unlocked helper function which allows a PHY register to be modified as
new register value = (old register value & ~mask) \| set

.. _`phy_modify`:

phy_modify
==========

.. c:function:: int phy_modify(struct phy_device *phydev, u32 regnum, u16 mask, u16 set)

    Convenience function for modifying a given PHY register

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

    :param regnum:
        register number to write
    :type regnum: u32

    :param mask:
        bit mask of bits to clear
    :type mask: u16

    :param set:
        new value of bits set in mask to write to \ ``regnum``\ 
    :type set: u16

.. _`phy_modify.note`:

NOTE
----

MUST NOT be called from interrupt context,
because the bus read/write functions may wait for an interrupt
to conclude the operation.

.. _`phy_save_page`:

phy_save_page
=============

.. c:function:: int phy_save_page(struct phy_device *phydev)

    take the bus lock and save the current page

    :param phydev:
        a pointer to a \ :c:type:`struct phy_device <phy_device>`\ 
    :type phydev: struct phy_device \*

.. _`phy_save_page.description`:

Description
-----------

Take the MDIO bus lock, and return the current page number. On error,
returns a negative errno. \ :c:func:`phy_restore_page`\  must always be called
after this, irrespective of success or failure of this call.

.. _`phy_select_page`:

phy_select_page
===============

.. c:function:: int phy_select_page(struct phy_device *phydev, int page)

    take the bus lock, save the current page, and set a page

    :param phydev:
        a pointer to a \ :c:type:`struct phy_device <phy_device>`\ 
    :type phydev: struct phy_device \*

    :param page:
        desired page
    :type page: int

.. _`phy_select_page.description`:

Description
-----------

Take the MDIO bus lock to protect against concurrent access, save the
current PHY page, and set the current page.  On error, returns a
negative errno, otherwise returns the previous page number.
\ :c:func:`phy_restore_page`\  must always be called after this, irrespective
of success or failure of this call.

.. _`phy_restore_page`:

phy_restore_page
================

.. c:function:: int phy_restore_page(struct phy_device *phydev, int oldpage, int ret)

    restore the page register and release the bus lock

    :param phydev:
        a pointer to a \ :c:type:`struct phy_device <phy_device>`\ 
    :type phydev: struct phy_device \*

    :param oldpage:
        the old page, return value from \ :c:func:`phy_save_page`\  or \ :c:func:`phy_select_page`\ 
    :type oldpage: int

    :param ret:
        operation's return code
    :type ret: int

.. _`phy_restore_page.description`:

Description
-----------

Release the MDIO bus lock, restoring \ ``oldpage``\  if it is a valid page.
This function propagates the earliest error code from the group of
operations.

.. _`phy_restore_page.return`:

Return
------

\ ``oldpage``\  if it was a negative value, otherwise
\ ``ret``\  if it was a negative errno value, otherwise
\ :c:func:`phy_write_page`\ 's negative value if it were in error, otherwise
\ ``ret``\ .

.. _`phy_read_paged`:

phy_read_paged
==============

.. c:function:: int phy_read_paged(struct phy_device *phydev, int page, u32 regnum)

    Convenience function for reading a paged register

    :param phydev:
        a pointer to a \ :c:type:`struct phy_device <phy_device>`\ 
    :type phydev: struct phy_device \*

    :param page:
        the page for the phy
    :type page: int

    :param regnum:
        register number
    :type regnum: u32

.. _`phy_read_paged.description`:

Description
-----------

Same rules as for \ :c:func:`phy_read`\ .

.. _`phy_write_paged`:

phy_write_paged
===============

.. c:function:: int phy_write_paged(struct phy_device *phydev, int page, u32 regnum, u16 val)

    Convenience function for writing a paged register

    :param phydev:
        a pointer to a \ :c:type:`struct phy_device <phy_device>`\ 
    :type phydev: struct phy_device \*

    :param page:
        the page for the phy
    :type page: int

    :param regnum:
        register number
    :type regnum: u32

    :param val:
        value to write
    :type val: u16

.. _`phy_write_paged.description`:

Description
-----------

Same rules as for \ :c:func:`phy_write`\ .

.. _`phy_modify_paged`:

phy_modify_paged
================

.. c:function:: int phy_modify_paged(struct phy_device *phydev, int page, u32 regnum, u16 mask, u16 set)

    Convenience function for modifying a paged register

    :param phydev:
        a pointer to a \ :c:type:`struct phy_device <phy_device>`\ 
    :type phydev: struct phy_device \*

    :param page:
        the page for the phy
    :type page: int

    :param regnum:
        register number
    :type regnum: u32

    :param mask:
        bit mask of bits to clear
    :type mask: u16

    :param set:
        bit mask of bits to set
    :type set: u16

.. _`phy_modify_paged.description`:

Description
-----------

Same rules as for \ :c:func:`phy_read`\  and \ :c:func:`phy_write`\ .

.. This file was automatic generated / don't edit.

