.. -*- coding: utf-8; mode: rst -*-

.. _API-call-usermodehelper:

===================
call_usermodehelper
===================

*man call_usermodehelper(9)*

*4.6.0-rc5*

prepare and start a usermode application


Synopsis
========

.. c:function:: int call_usermodehelper( char * path, char ** argv, char ** envp, int wait )

Arguments
=========

``path``
    path to usermode executable

``argv``
    arg vector for process

``envp``
    environment for process

``wait``
    wait for the application to finish and return status. when
    UMH_NO_WAIT don't wait at all, but you get no useful error back
    when the program couldn't be exec'ed. This makes it safe to call
    from interrupt context.


Description
===========

This function is the equivalent to use ``call_usermodehelper_setup`` and
``call_usermodehelper_exec``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
