.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/originator.h

.. _`batadv_choose_orig`:

batadv_choose_orig
==================

.. c:function:: u32 batadv_choose_orig(const void *data, u32 size)

    Return the index of the orig entry in the hash table

    :param data:
        mac address of the originator node
    :type data: const void \*

    :param size:
        the size of the hash table
    :type size: u32

.. _`batadv_choose_orig.return`:

Return
------

the hash index where the object represented by \ ``data``\  should be
stored at.

.. This file was automatic generated / don't edit.

