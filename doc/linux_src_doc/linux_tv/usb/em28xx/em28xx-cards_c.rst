.. -*- coding: utf-8; mode: rst -*-

==============
em28xx-cards.c
==============



.. _xref_em28xx_free_device:

em28xx_free_device
==================

.. c:function:: void em28xx_free_device (struct kref * ref)

    Free em28xx device

    :param struct kref * ref:
        struct kref for em28xx device



Description
-----------

This is called when all extensions and em28xx core unregisters a device


