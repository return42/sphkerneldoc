.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/cxgb4_ethtool.c

.. _`from_fw_port_mod_type`:

from_fw_port_mod_type
=====================

.. c:function:: int from_fw_port_mod_type(enum fw_port_type port_type, enum fw_port_module_type mod_type)

    translate Firmware Port/Module type to Ethtool

    :param enum fw_port_type port_type:
        Firmware Port Type

    :param enum fw_port_module_type mod_type:
        Firmware Module Type

.. _`from_fw_port_mod_type.description`:

Description
-----------

Translate Firmware Port/Module type to Ethtool Port Type.

.. _`speed_to_fw_caps`:

speed_to_fw_caps
================

.. c:function:: unsigned int speed_to_fw_caps(int speed)

    translate Port Speed to Firmware Port Capabilities

    :param int speed:
        speed in Kb/s

.. _`speed_to_fw_caps.description`:

Description
-----------

Translates a specific Port Speed into a Firmware Port Capabilities
value.

.. _`fw_caps_to_lmm`:

fw_caps_to_lmm
==============

.. c:function:: void fw_caps_to_lmm(enum fw_port_type port_type, unsigned int fw_caps, unsigned long *link_mode_mask)

    translate Firmware to ethtool Link Mode Mask

    :param enum fw_port_type port_type:
        Firmware Port Type

    :param unsigned int fw_caps:
        Firmware Port Capabilities

    :param unsigned long \*link_mode_mask:
        ethtool Link Mode Mask

.. _`fw_caps_to_lmm.description`:

Description
-----------

Translate a Firmware Port Capabilities specification to an ethtool
Link Mode Mask.

.. _`lmm_to_fw_caps`:

lmm_to_fw_caps
==============

.. c:function:: unsigned int lmm_to_fw_caps(const unsigned long *link_mode_mask)

    translate ethtool Link Mode Mask to Firmware capabilities

    :param const unsigned long \*link_mode_mask:
        *undescribed*

.. _`lmm_to_fw_caps.description`:

Description
-----------

Translate ethtool Link Mode Mask into a Firmware Port capabilities
value.

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

.. This file was automatic generated / don't edit.

