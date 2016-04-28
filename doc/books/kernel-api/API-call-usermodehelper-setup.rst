.. -*- coding: utf-8; mode: rst -*-

.. _API-call-usermodehelper-setup:

=========================
call_usermodehelper_setup
=========================

*man call_usermodehelper_setup(9)*

*4.6.0-rc5*

prepare to call a usermode helper


Synopsis
========

.. c:function:: struct subprocess_info * call_usermodehelper_setup( char * path, char ** argv, char ** envp, gfp_t gfp_mask, int (*init) struct subprocess_info *info, struct cred *new, void (*cleanup) struct subprocess_info *info, void * data )

Arguments
=========

``path``
    path to usermode executable

``argv``
    arg vector for process

``envp``
    environment for process

``gfp_mask``
    gfp mask for memory allocation

``init``
    an init function

``cleanup``
    a cleanup function

``data``
    arbitrary context sensitive data


Description
===========

Returns either ``NULL`` on allocation failure, or a subprocess_info
structure. This should be passed to call_usermodehelper_exec to exec
the process and free the structure.

The init function is used to customize the helper process prior to exec.
A non-zero return code causes the process to error out, exit, and return
the failure to the calling process

The cleanup function is just before ethe subprocess_info is about to be
freed. This can be used for freeing the argv and envp. The Function must
be runnable in either a process context or the context in which
call_usermodehelper_exec is called.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
