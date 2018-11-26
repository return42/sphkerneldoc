.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/qcom/qdsp6/q6core.c

.. _`q6core_get_svc_api_info`:

q6core_get_svc_api_info
=======================

.. c:function:: int q6core_get_svc_api_info(int svc_id, struct q6core_svc_api_info *ainfo)

    Get version number of a service.

    :param svc_id:
        service id of the service.
    :type svc_id: int

    :param ainfo:
        Valid struct pointer to fill svc api information.
    :type ainfo: struct q6core_svc_api_info \*

.. _`q6core_get_svc_api_info.return`:

Return
------

zero on success and error code on failure or unsupported

.. _`q6core_is_adsp_ready`:

q6core_is_adsp_ready
====================

.. c:function:: bool q6core_is_adsp_ready( void)

    Get status of adsp

    :param void:
        no arguments
    :type void: 

.. _`q6core_is_adsp_ready.return`:

Return
------

Will be an true if adsp is ready and false if not.

.. This file was automatic generated / don't edit.

