.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/qlogic/qlcnic/qlcnic_83xx_vnic.c

.. _`qlcnic_83xx_init_mgmt_vnic`:

qlcnic_83xx_init_mgmt_vnic
==========================

.. c:function:: int qlcnic_83xx_init_mgmt_vnic(struct qlcnic_adapter *adapter)

    :param struct qlcnic_adapter \*adapter:
        adapter structure
        Management virtual NIC sets the operational mode of other vNIC's and
        configures embedded switch (ESWITCH).

.. _`qlcnic_83xx_init_mgmt_vnic.return`:

Return
------

Success(0) or error code.

.. _`qlcnic_83xx_config_vnic_opmode`:

qlcnic_83xx_config_vnic_opmode
==============================

.. c:function:: int qlcnic_83xx_config_vnic_opmode(struct qlcnic_adapter *adapter)

    :param struct qlcnic_adapter \*adapter:
        adapter structure
        Identify virtual NIC operational modes.

.. _`qlcnic_83xx_config_vnic_opmode.return`:

Return
------

Success(0) or error code.

.. This file was automatic generated / don't edit.

