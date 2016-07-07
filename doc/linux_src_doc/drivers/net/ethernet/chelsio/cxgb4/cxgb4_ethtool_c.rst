.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/cxgb4_ethtool.c

.. _`set_rx_intr_params`:

set_rx_intr_params
==================

.. c:function:: int set_rx_intr_params(struct net_device *dev, unsigned int us, unsigned int cnt)

    set a net devices's RX interrupt holdoff paramete!

    :param struct net_device \*dev:
        the network device

    :param unsigned int us:
        the hold-off time in us, or 0 to disable timer

    :param unsigned int cnt:
        the hold-off packet count, or 0 to disable counter

.. _`set_rx_intr_params.description`:

Description
-----------

Set the RX interrupt hold-off parameters for a network device.

.. _`eeprom_ptov`:

eeprom_ptov
===========

.. c:function:: int eeprom_ptov(unsigned int phys_addr, unsigned int fn, unsigned int sz)

    translate a physical EEPROM address to virtual

    :param unsigned int phys_addr:
        the physical EEPROM address

    :param unsigned int fn:
        the PCI function number

    :param unsigned int sz:
        size of function-specific area

.. _`eeprom_ptov.description`:

Description
-----------

Translate a physical EEPROM address to virtual.  The first 1K is
accessed through virtual addresses starting at 31K, the rest is
accessed through virtual addresses starting at 0.

.. _`eeprom_ptov.the-mapping-is-as-follows`:

The mapping is as follows
-------------------------

[0..1K) -> [31K..32K)
[1K..1K+A) -> [31K-A..31K)
[1K+A..ES) -> [0..ES-A-1K)

where A = \ ``fn``\  \* \ ``sz``\ , and ES = EEPROM size.

.. This file was automatic generated / don't edit.

