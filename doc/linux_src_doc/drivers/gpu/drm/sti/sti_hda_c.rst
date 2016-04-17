.. -*- coding: utf-8; mode: rst -*-

=========
sti_hda.c
=========


.. _`hda_get_mode_idx`:

hda_get_mode_idx
================

.. c:function:: bool hda_get_mode_idx (struct drm_display_mode mode, int *idx)

    :param struct drm_display_mode mode:
        mode being searched

    :param int \*idx:
        index of the found mode



.. _`hda_get_mode_idx.description`:

Description
-----------

Return true if mode is found



.. _`hda_enable_hd_dacs`:

hda_enable_hd_dacs
==================

.. c:function:: void hda_enable_hd_dacs (struct sti_hda *hda, bool enable)

    :param struct sti_hda \*hda:
        pointer to HD analog structure

    :param bool enable:
        true if HD DACS need to be enabled, else false



.. _`sti_hda_configure_awg`:

sti_hda_configure_awg
=====================

.. c:function:: void sti_hda_configure_awg (struct sti_hda *hda, u32 *awg_instr, int nb)

    :param struct sti_hda \*hda:
        pointer to HD analog structure

    :param u32 \*awg_instr:
        pointer to AWG instructions table

    :param int nb:
        nb of AWG instructions

