.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hnae.c

.. _`raw_notifier_head`:

RAW_NOTIFIER_HEAD
=================

.. c:function::  RAW_NOTIFIER_HEAD( ae_chain)

    define ae chain head

    :param  ae_chain:
        *undescribed*

.. _`hnae_ae_register`:

hnae_ae_register
================

.. c:function:: int hnae_ae_register(struct hnae_ae_dev *hdev, struct module *owner)

    register a AE engine to hnae framework

    :param struct hnae_ae_dev \*hdev:
        the hnae ae engine device

    :param struct module \*owner:
        the module who provides this dev

.. _`hnae_ae_register.note`:

NOTE
----

the duplicated name will not be checked

.. _`hnae_ae_unregister`:

hnae_ae_unregister
==================

.. c:function:: void hnae_ae_unregister(struct hnae_ae_dev *hdev)

    unregisters a HNAE AE engine

    :param struct hnae_ae_dev \*hdev:
        *undescribed*

.. This file was automatic generated / don't edit.

