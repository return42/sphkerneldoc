.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/mdio-boardinfo.c

.. _`mdiobus_setup_mdiodev_from_board_info`:

mdiobus_setup_mdiodev_from_board_info
=====================================

.. c:function:: void mdiobus_setup_mdiodev_from_board_info(struct mii_bus *bus, int (*cb)(struct mii_bus *bus, struct mdio_board_info *bi))

    create and setup MDIO devices from pre-collected board specific MDIO information

    :param struct mii_bus \*bus:
        *undescribed*

    :param int (\*cb)(struct mii_bus \*bus, struct mdio_board_info \*bi):
        *undescribed*

.. _`mdiobus_setup_mdiodev_from_board_info.context`:

Context
-------

can sleep

.. _`mdiobus_register_board_info`:

mdiobus_register_board_info
===========================

.. c:function:: int mdiobus_register_board_info(const struct mdio_board_info *info, unsigned int n)

    register MDIO devices for a given board

    :param const struct mdio_board_info \*info:
        array of devices descriptors

    :param unsigned int n:
        number of descriptors provided

.. _`mdiobus_register_board_info.context`:

Context
-------

can sleep

.. _`mdiobus_register_board_info.description`:

Description
-----------

The board info passed can be marked with \__initdata but be pointers
such as platform_data etc. are copied as-is

.. This file was automatic generated / don't edit.

