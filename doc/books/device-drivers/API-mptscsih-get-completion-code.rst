.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-get-completion-code:

============================
mptscsih_get_completion_code
============================

*man mptscsih_get_completion_code(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
