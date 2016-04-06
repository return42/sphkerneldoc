
.. _API-mptscsih-get-completion-code:

============================
mptscsih_get_completion_code
============================

*man mptscsih_get_completion_code(9)*

*4.6.0-rc1*

get completion code from MPT request


Synopsis
========

.. c:function:: int mptscsih_get_completion_code( MPT_ADAPTER * ioc, MPT_FRAME_HDR * req, MPT_FRAME_HDR * reply )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``req``
    Pointer to original MPT request frame

``reply``
    Pointer to MPT reply frame (NULL if TurboReply)
