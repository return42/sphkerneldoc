
.. _API-call-usermodehelper:

===================
call_usermodehelper
===================

*man call_usermodehelper(9)*

*4.6.0-rc1*

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
    wait for the application to finish and return status. when UMH_NO_WAIT don't wait at all, but you get no useful error back when the program couldn't be exec'ed. This makes it
    safe to call from interrupt context.


Description
===========

This function is the equivalent to use ``call_usermodehelper_setup`` and ``call_usermodehelper_exec``.
