.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/originator.h

.. _`batadv_choose_orig`:

batadv_choose_orig
==================

.. c:function:: u32 batadv_choose_orig(const void *data, u32 size)

    Return the index of the orig entry in the hash table

    :param const void \*data:
        mac address of the originator node

    :param u32 size:
        the size of the hash table

.. _`batadv_choose_orig.return`:

Return
------

the hash index where the object represented by \ ``data``\  should be
stored at.

.. This file was automatic generated / don't edit.

