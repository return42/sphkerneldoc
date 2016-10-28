.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/btt_devs.c

.. _`nd_btt_arena_is_valid`:

nd_btt_arena_is_valid
=====================

.. c:function:: bool nd_btt_arena_is_valid(struct nd_btt *nd_btt, struct btt_sb *super)

    check if the metadata layout is valid

    :param struct nd_btt \*nd_btt:
        device with BTT geometry and backing device info

    :param struct btt_sb \*super:
        pointer to the arena's info block being tested

.. _`nd_btt_arena_is_valid.description`:

Description
-----------

Check consistency of the btt info block with itself by validating
the checksum, and with the parent namespace by verifying the
parent_uuid contained in the info block with the one supplied in.

.. _`nd_btt_arena_is_valid.return`:

Return
------

false for an invalid info block, true for a valid one

.. This file was automatic generated / don't edit.

