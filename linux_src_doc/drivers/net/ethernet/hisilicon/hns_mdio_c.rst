.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns_mdio.c

.. _`hns_mdio_write`:

hns_mdio_write
==============

.. c:function:: int hns_mdio_write(struct mii_bus *bus, int phy_id, int regnum, u16 data)

    access phy register

    :param bus:
        mdio bus
    :type bus: struct mii_bus \*

    :param phy_id:
        phy id
    :type phy_id: int

    :param regnum:
        register num
    :type regnum: int

    :param data:
        *undescribed*
    :type data: u16

.. _`hns_mdio_write.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`hns_mdio_read`:

hns_mdio_read
=============

.. c:function:: int hns_mdio_read(struct mii_bus *bus, int phy_id, int regnum)

    access phy register

    :param bus:
        mdio bus
    :type bus: struct mii_bus \*

    :param phy_id:
        phy id
    :type phy_id: int

    :param regnum:
        register num
    :type regnum: int

.. _`hns_mdio_read.description`:

Description
-----------

Return phy register value

.. _`hns_mdio_reset`:

hns_mdio_reset
==============

.. c:function:: int hns_mdio_reset(struct mii_bus *bus)

    reset mdio bus

    :param bus:
        mdio bus
    :type bus: struct mii_bus \*

.. _`hns_mdio_reset.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`hns_mdio_probe`:

hns_mdio_probe
==============

.. c:function:: int hns_mdio_probe(struct platform_device *pdev)

    probe mdio device

    :param pdev:
        mdio platform device
    :type pdev: struct platform_device \*

.. _`hns_mdio_probe.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`hns_mdio_remove`:

hns_mdio_remove
===============

.. c:function:: int hns_mdio_remove(struct platform_device *pdev)

    remove mdio device

    :param pdev:
        mdio platform device
    :type pdev: struct platform_device \*

.. _`hns_mdio_remove.description`:

Description
-----------

Return 0 on success, negative on failure

.. This file was automatic generated / don't edit.

