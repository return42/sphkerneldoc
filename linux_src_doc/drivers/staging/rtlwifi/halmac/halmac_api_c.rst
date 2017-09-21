.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtlwifi/halmac/halmac_api.c

.. _`halmac_init_adapter`:

halmac_init_adapter
===================

.. c:function:: enum halmac_ret_status halmac_init_adapter(void *driver_adapter, struct halmac_platform_api *halmac_platform_api, enum halmac_interface halmac_interface, struct halmac_adapter **pp_halmac_adapter, struct halmac_api **pp_halmac_api)

    init halmac_adapter

    :param void \*driver_adapter:
        the adapter of caller

    :param struct halmac_platform_api \*halmac_platform_api:
        the platform APIs which is used in halmac APIs

    :param enum halmac_interface halmac_interface:
        bus interface

    :param struct halmac_adapter \*\*pp_halmac_adapter:
        the adapter of halmac

    :param struct halmac_api \*\*pp_halmac_api:
        the function pointer of APIs, caller shall call APIs by
        function pointer
        Author : KaiYuan Chang / Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_halt_api`:

halmac_halt_api
===============

.. c:function:: enum halmac_ret_status halmac_halt_api(struct halmac_adapter *halmac_adapter)

    stop halmac_api action

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac
        Author : Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_deinit_adapter`:

halmac_deinit_adapter
=====================

.. c:function:: enum halmac_ret_status halmac_deinit_adapter(struct halmac_adapter *halmac_adapter)

    deinit halmac adapter

    :param struct halmac_adapter \*halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang / Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. _`halmac_get_version`:

halmac_get_version
==================

.. c:function:: enum halmac_ret_status halmac_get_version(struct halmac_ver *version)

    get HALMAC version

    :param struct halmac_ver \*version:
        return version of major, prototype and minor information
        Author : KaiYuan Chang / Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document

.. This file was automatic generated / don't edit.

