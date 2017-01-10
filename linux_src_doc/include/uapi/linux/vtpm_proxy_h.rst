.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/vtpm_proxy.h

.. _`vtpm_proxy_flags`:

enum vtpm_proxy_flags
=====================

.. c:type:: enum vtpm_proxy_flags

    flags for the proxy TPM

.. _`vtpm_proxy_flags.definition`:

Definition
----------

.. code-block:: c

    enum vtpm_proxy_flags {
        VTPM_PROXY_FLAG_TPM2
    };

.. _`vtpm_proxy_flags.constants`:

Constants
---------

VTPM_PROXY_FLAG_TPM2
    the proxy TPM uses TPM 2.0 protocol

.. _`vtpm_proxy_new_dev`:

struct vtpm_proxy_new_dev
=========================

.. c:type:: struct vtpm_proxy_new_dev

    parameter structure for the \ ``VTPM_PROXY_IOC_NEW_DEV``\  ioctl

.. _`vtpm_proxy_new_dev.definition`:

Definition
----------

.. code-block:: c

    struct vtpm_proxy_new_dev {
        __u32 flags;
        __u32 tpm_num;
        __u32 fd;
        __u32 major;
        __u32 minor;
    }

.. _`vtpm_proxy_new_dev.members`:

Members
-------

flags
    flags for the proxy TPM

tpm_num
    index of the TPM device

fd
    the file descriptor used by the proxy TPM

major
    the major number of the TPM device

minor
    the minor number of the TPM device

.. This file was automatic generated / don't edit.

