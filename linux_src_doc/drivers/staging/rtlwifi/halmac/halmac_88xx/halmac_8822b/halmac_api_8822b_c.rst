.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtlwifi/halmac/halmac_88xx/halmac_8822b/halmac_api_8822b.c

.. _`halmac_mount_api_8822b`:

halmac_mount_api_8822b
======================

.. c:function:: enum halmac_ret_status halmac_mount_api_8822b(struct halmac_adapter *halmac_adapter)

    attach functions to function pointer \ ``halmac_adapter``\ 

    :param struct halmac_adapter \*halmac_adapter:
        *undescribed*

.. _`halmac_mount_api_8822b.description`:

Description
-----------

SD1 internal use

Author : KaiYuan Chang/Ivan Lin
Return : enum halmac_ret_status

.. _`halmac_init_trx_cfg_8822b`:

halmac_init_trx_cfg_8822b
=========================

.. c:function:: enum halmac_ret_status halmac_init_trx_cfg_8822b(struct halmac_adapter *halmac_adapter, enum halmac_trx_mode halmac_trx_mode)

    config trx dma register

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac

    :param enum halmac_trx_mode halmac_trx_mode:
        trx mode selection
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_init_protocol_cfg_8822b`:

halmac_init_protocol_cfg_8822b
==============================

.. c:function:: enum halmac_ret_status halmac_init_protocol_cfg_8822b(struct halmac_adapter *halmac_adapter)

    config protocol register

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_init_h2c_8822b`:

halmac_init_h2c_8822b
=====================

.. c:function:: enum halmac_ret_status halmac_init_h2c_8822b(struct halmac_adapter *halmac_adapter)

    config h2c packet buffer

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang/Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. This file was automatic generated / don't edit.

