.. -*- coding: utf-8; mode: rst -*-

.. _API-svc-reserve:

===========
svc_reserve
===========

*man svc_reserve(9)*

*4.6.0-rc5*

change the space reserved for the reply to a request.


Synopsis
========

.. c:function:: void svc_reserve( struct svc_rqst * rqstp, int space )

Arguments
=========

``rqstp``
    The request in question

``space``
    new max space to reserve


Description
===========

Each request reserves some space on the output queue of the transport to
make sure the reply fits. This function reduces that reserved space to
be the amount of space used already, plus ``space``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
