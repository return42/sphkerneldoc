.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-del-mport-pw-handler:

========================
rio_del_mport_pw_handler
========================

*man rio_del_mport_pw_handler(9)*

*4.6.0-rc5*

remove port-write message handler from the list of mport specific pw
handlers


Synopsis
========

.. c:function:: int rio_del_mport_pw_handler( struct rio_mport * mport, void * context, int (*pwcback) struct rio_mport *mport, void *context, union rio_pw_msg *msg, int step )

Arguments
=========

``mport``
    RIO master port to bind the portwrite callback

``context``
    Registered handler specific context to pass on event

``pwcback``
    Registered callback function


Description
===========

Returns 0 if the request has been satisfied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
