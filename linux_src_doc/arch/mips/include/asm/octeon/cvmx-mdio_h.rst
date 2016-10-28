.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-mdio.h

.. _`cvmx_mdio_phy_reg_control`:

CVMX_MDIO_PHY_REG_CONTROL
=========================

.. c:function::  CVMX_MDIO_PHY_REG_CONTROL()

.. _`cvmx_mdio_phy_reg_status`:

CVMX_MDIO_PHY_REG_STATUS
========================

.. c:function::  CVMX_MDIO_PHY_REG_STATUS()

.. _`cvmx_mdio_phy_reg_id1`:

CVMX_MDIO_PHY_REG_ID1
=====================

.. c:function::  CVMX_MDIO_PHY_REG_ID1()

.. _`cvmx_mdio_phy_reg_id2`:

CVMX_MDIO_PHY_REG_ID2
=====================

.. c:function::  CVMX_MDIO_PHY_REG_ID2()

.. _`cvmx_mdio_phy_reg_autoneg_adver`:

CVMX_MDIO_PHY_REG_AUTONEG_ADVER
===============================

.. c:function::  CVMX_MDIO_PHY_REG_AUTONEG_ADVER()

.. _`cvmx_mdio_phy_reg_link_partner_ability`:

CVMX_MDIO_PHY_REG_LINK_PARTNER_ABILITY
======================================

.. c:function::  CVMX_MDIO_PHY_REG_LINK_PARTNER_ABILITY()

.. _`cvmx_mdio_phy_reg_autoneg_expansion`:

CVMX_MDIO_PHY_REG_AUTONEG_EXPANSION
===================================

.. c:function::  CVMX_MDIO_PHY_REG_AUTONEG_EXPANSION()

.. _`cvmx_mdio_phy_reg_control_1000`:

CVMX_MDIO_PHY_REG_CONTROL_1000
==============================

.. c:function::  CVMX_MDIO_PHY_REG_CONTROL_1000()

.. _`cvmx_mdio_phy_reg_status_1000`:

CVMX_MDIO_PHY_REG_STATUS_1000
=============================

.. c:function::  CVMX_MDIO_PHY_REG_STATUS_1000()

.. _`cvmx_mdio_phy_reg_extended_status`:

CVMX_MDIO_PHY_REG_EXTENDED_STATUS
=================================

.. c:function::  CVMX_MDIO_PHY_REG_EXTENDED_STATUS()

.. _`cvmx_mdio_phy_reg_mmd_control`:

CVMX_MDIO_PHY_REG_MMD_CONTROL
=============================

.. c:function::  CVMX_MDIO_PHY_REG_MMD_CONTROL()

.. _`cvmx_mdio_phy_reg_mmd_address_data`:

CVMX_MDIO_PHY_REG_MMD_ADDRESS_DATA
==================================

.. c:function::  CVMX_MDIO_PHY_REG_MMD_ADDRESS_DATA()

.. _`cvmx_mdio_read`:

cvmx_mdio_read
==============

.. c:function:: int cvmx_mdio_read(int bus_id, int phy_id, int location)

    registers controlling auto negotiation.

    :param int bus_id:
        MDIO bus number. Zero on most chips, but some chips (ex CN56XX)
        support multiple busses.

    :param int phy_id:
        The MII phy id

    :param int location:
        Register location to read

.. _`cvmx_mdio_read.description`:

Description
-----------

Returns Result from the read or -1 on failure

.. _`cvmx_mdio_write`:

cvmx_mdio_write
===============

.. c:function:: int cvmx_mdio_write(int bus_id, int phy_id, int location, int val)

    registers controlling auto negotiation.

    :param int bus_id:
        MDIO bus number. Zero on most chips, but some chips (ex CN56XX)
        support multiple busses.

    :param int phy_id:
        The MII phy id

    :param int location:
        Register location to write

    :param int val:
        Value to write

.. _`cvmx_mdio_write.description`:

Description
-----------

Returns -1 on error
0 on success

.. _`cvmx_mdio_45_read`:

cvmx_mdio_45_read
=================

.. c:function:: int cvmx_mdio_45_read(int bus_id, int phy_id, int device, int location)

    read PHY registers controlling auto negotiation.

    :param int bus_id:
        MDIO bus number. Zero on most chips, but some chips (ex CN56XX)
        support multiple busses.

    :param int phy_id:
        The MII phy id

    :param int device:
        MDIO Managable Device (MMD) id

    :param int location:
        Register location to read

.. _`cvmx_mdio_45_read.description`:

Description
-----------

Returns Result from the read or -1 on failure

.. _`cvmx_mdio_45_write`:

cvmx_mdio_45_write
==================

.. c:function:: int cvmx_mdio_45_write(int bus_id, int phy_id, int device, int location, int val)

    write PHY registers controlling auto negotiation.

    :param int bus_id:
        MDIO bus number. Zero on most chips, but some chips (ex CN56XX)
        support multiple busses.

    :param int phy_id:
        The MII phy id

    :param int device:
        MDIO Managable Device (MMD) id

    :param int location:
        Register location to write

    :param int val:
        Value to write

.. _`cvmx_mdio_45_write.description`:

Description
-----------

Returns -1 on error
0 on success

.. This file was automatic generated / don't edit.

