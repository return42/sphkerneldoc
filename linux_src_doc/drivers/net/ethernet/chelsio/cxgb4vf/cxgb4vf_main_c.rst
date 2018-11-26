.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4vf/cxgb4vf_main.c

.. _`set_rxq_intr_params`:

set_rxq_intr_params
===================

.. c:function:: int set_rxq_intr_params(struct adapter *adapter, struct sge_rspq *rspq, unsigned int us, unsigned int cnt)

    set a queue's interrupt holdoff parameters

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param rspq:
        the RX response queue
    :type rspq: struct sge_rspq \*

    :param us:
        the hold-off time in us, or 0 to disable timer
    :type us: unsigned int

    :param cnt:
        the hold-off packet count, or 0 to disable counter
    :type cnt: unsigned int

.. _`set_rxq_intr_params.description`:

Description
-----------

Sets an RX response queue's interrupt hold-off time and packet count.
At least one of the two needs to be enabled for the queue to generate
interrupts.

.. _`from_fw_port_mod_type`:

from_fw_port_mod_type
=====================

.. c:function:: int from_fw_port_mod_type(enum fw_port_type port_type, enum fw_port_module_type mod_type)

    translate Firmware Port/Module type to Ethtool

    :param port_type:
        Firmware Port Type
    :type port_type: enum fw_port_type

    :param mod_type:
        Firmware Module Type
    :type mod_type: enum fw_port_module_type

.. _`from_fw_port_mod_type.description`:

Description
-----------

Translate Firmware Port/Module type to Ethtool Port Type.

.. _`fw_caps_to_lmm`:

fw_caps_to_lmm
==============

.. c:function:: void fw_caps_to_lmm(enum fw_port_type port_type, unsigned int fw_caps, unsigned long *link_mode_mask)

    translate Firmware to ethtool Link Mode Mask

    :param port_type:
        Firmware Port Type
    :type port_type: enum fw_port_type

    :param fw_caps:
        Firmware Port Capabilities
    :type fw_caps: unsigned int

    :param link_mode_mask:
        ethtool Link Mode Mask
    :type link_mode_mask: unsigned long \*

.. _`fw_caps_to_lmm.description`:

Description
-----------

Translate a Firmware Port Capabilities specification to an ethtool
Link Mode Mask.

.. This file was automatic generated / don't edit.

