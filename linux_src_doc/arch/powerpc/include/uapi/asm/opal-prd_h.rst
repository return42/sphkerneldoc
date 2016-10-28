.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/uapi/asm/opal-prd.h

.. _`opal_prd_kernel_version`:

OPAL_PRD_KERNEL_VERSION
=======================

.. c:function::  OPAL_PRD_KERNEL_VERSION()

    interface available for the /dev/opal-prd device. The actual PRD message layout and content is private to the firmware <--> userspace interface, so is not covered by this versioning.

.. _`opal_prd_kernel_version.description`:

Description
-----------

Future interface versions are backwards-compatible; if a later kernel
version is encountered, functionality provided in earlier versions
will work.

.. This file was automatic generated / don't edit.

