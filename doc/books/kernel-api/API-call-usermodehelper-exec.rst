
.. _API-call-usermodehelper-exec:

========================
call_usermodehelper_exec
========================

*man call_usermodehelper_exec(9)*

*4.6.0-rc1*

start a usermode application


Synopsis
========

.. c:function:: int call_usermodehelper_exec( struct subprocess_info * sub_info, int wait )

Arguments
=========

``sub_info``
    information about the subprocessa

``wait``
    wait for the application to finish and return status. when UMH_NO_WAIT don't wait at all, but you get no useful error back when the program couldn't be exec'ed. This makes it
    safe to call from interrupt context.


Description
===========

Runs a user-space application. The application is started asynchronously if wait is not set, and runs as a child of system workqueues. (ie. it runs with full root capabilities and
optimized affinity).
