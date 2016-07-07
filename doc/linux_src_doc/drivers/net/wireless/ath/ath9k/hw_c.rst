.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/hw.c

.. _`ath9k_hw_dfs_tested`:

ath9k_hw_dfs_tested
===================

.. c:function:: bool ath9k_hw_dfs_tested(struct ath_hw *ah)

    checks if DFS has been tested with used chipset

    :param struct ath_hw \*ah:
        the atheros hardware data structure

.. _`ath9k_hw_dfs_tested.description`:

Description
-----------

We enable DFS support upstream on chipsets which have passed a series
of tests. The testing requirements are going to be documented. Desired

.. _`ath9k_hw_dfs_tested.test-requirements-are-documented-at`:

test requirements are documented at
-----------------------------------


http://wireless.kernel.org/en/users/Drivers/ath9k/dfs

Once a new chipset gets properly tested an individual commit can be used
to document the testing for DFS for that chipset.

.. This file was automatic generated / don't edit.

