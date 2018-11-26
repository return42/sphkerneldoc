.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtlwifi/halmac/halmac_api.c

.. _`halmac_init_adapter`:

halmac_init_adapter
===================

.. c:function:: enum halmac_ret_status halmac_init_adapter(void *driver_adapter, struct halmac_platform_api *halmac_platform_api, enum halmac_interface halmac_interface, struct halmac_adapter **pp_halmac_adapter, struct halmac_api **pp_halmac_api)

    init halmac_adapter

    :param driver_adapter:
        the adapter of caller
    :type driver_adapter: void \*

    :param halmac_platform_api:
        the platform APIs which is used in halmac APIs
    :type halmac_platform_api: struct halmac_platform_api \*

    :param halmac_interface:
        bus interface
    :type halmac_interface: enum halmac_interface

    :param pp_halmac_adapter:
        the adapter of halmac
    :type pp_halmac_adapter: struct halmac_adapter \*\*

    :param pp_halmac_api:
        the function pointer of APIs, caller shall call APIs by
        function pointer
        Author : KaiYuan Chang / Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type pp_halmac_api: struct halmac_api \*\*

.. _`halmac_halt_api`:

halmac_halt_api
===============

.. c:function:: enum halmac_ret_status halmac_halt_api(struct halmac_adapter *halmac_adapter)

    stop halmac_api action

    :param halmac_adapter:
        the adapter of halmac
        Author : Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_deinit_adapter`:

halmac_deinit_adapter
=====================

.. c:function:: enum halmac_ret_status halmac_deinit_adapter(struct halmac_adapter *halmac_adapter)

    deinit halmac adapter

    :param halmac_adapter:
        the adapter of halmac
        Author : KaiYuan Chang / Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type halmac_adapter: struct halmac_adapter \*

.. _`halmac_get_version`:

halmac_get_version
==================

.. c:function:: enum halmac_ret_status halmac_get_version(struct halmac_ver *version)

    get HALMAC version

    :param version:
        return version of major, prototype and minor information
        Author : KaiYuan Chang / Ivan Lin
        Return : enum halmac_ret_status
        More details of status code can be found in prototype document
    :type version: struct halmac_ver \*

.. This file was automatic generated / don't edit.

