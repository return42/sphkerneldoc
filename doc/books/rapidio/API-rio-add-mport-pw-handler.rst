
.. _API-rio-add-mport-pw-handler:

========================
rio_add_mport_pw_handler
========================

*man rio_add_mport_pw_handler(9)*

*4.6.0-rc1*

add port-write message handler into the list of mport specific pw handlers


Synopsis
========

.. c:function:: int rio_add_mport_pw_handler( struct rio_mport * mport, void * context, int (*pwcback) struct rio_mport *mport, void *context, union rio_pw_msg *msg, int step )

Arguments
=========

``mport``
    RIO master port to bind the portwrite callback

``context``
    Handler specific context to pass on event

``pwcback``
    Callback to execute when portwrite is received


Description
===========

Returns 0 if the request has been satisfied.
