.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/mediatek/mt7601u/phy.c

.. _`mt7601u_bbp_r47_get`:

mt7601u_bbp_r47_get
===================

.. c:function:: u8 mt7601u_bbp_r47_get(struct mt7601u_dev *dev, u8 reg, u8 flag)

    read value through BBP R47/R49 pair

    :param dev:
        pointer to adapter structure
    :type dev: struct mt7601u_dev \*

    :param reg:
        value of BBP R47 before the operation
    :type reg: u8

    :param flag:
        one of the BBP_R47_F\_\* flags
    :type flag: u8

.. _`mt7601u_bbp_r47_get.description`:

Description
-----------

Convenience helper for reading values through BBP R47/R49 pair.
Takes old value of BBP R47 as \ ``reg``\ , because callers usually have it
cached already.

.. _`mt7601u_bbp_r47_get.return`:

Return
------

value of BBP R49.

.. _`mt7601u_set_rx_path`:

mt7601u_set_rx_path
===================

.. c:function:: void mt7601u_set_rx_path(struct mt7601u_dev *dev, u8 path)

    set rx path in BBP

    :param dev:
        pointer to adapter structure
    :type dev: struct mt7601u_dev \*

    :param path:
        rx path to set values are 0-based
    :type path: u8

.. _`mt7601u_set_tx_dac`:

mt7601u_set_tx_dac
==================

.. c:function:: void mt7601u_set_tx_dac(struct mt7601u_dev *dev, u8 dac)

    set which tx DAC to use

    :param dev:
        pointer to adapter structure
    :type dev: struct mt7601u_dev \*

    :param dac:
        *undescribed*
    :type dac: u8

.. This file was automatic generated / don't edit.

