.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/sta_info.c

.. _`sta_info_free`:

sta_info_free
=============

.. c:function:: void sta_info_free(struct ieee80211_local *local, struct sta_info *sta)

    free STA

    :param struct ieee80211_local \*local:
        pointer to the global information

    :param struct sta_info \*sta:
        STA info to free

.. _`sta_info_free.description`:

Description
-----------

This function must undo everything done by \ :c:func:`sta_info_alloc`\ 
that may happen before \ :c:func:`sta_info_insert`\ . It may only be
called when \ :c:func:`sta_info_insert`\  has not been attempted (and
if that fails, the station is freed anyway.)

.. This file was automatic generated / don't edit.

