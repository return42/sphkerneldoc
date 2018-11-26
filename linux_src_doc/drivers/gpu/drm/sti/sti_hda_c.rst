.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sti/sti_hda.c

.. _`hda_get_mode_idx`:

hda_get_mode_idx
================

.. c:function:: bool hda_get_mode_idx(struct drm_display_mode mode, int *idx)

    :param mode:
        mode being searched
    :type mode: struct drm_display_mode

    :param idx:
        index of the found mode
    :type idx: int \*

.. _`hda_get_mode_idx.description`:

Description
-----------

Return true if mode is found

.. _`hda_enable_hd_dacs`:

hda_enable_hd_dacs
==================

.. c:function:: void hda_enable_hd_dacs(struct sti_hda *hda, bool enable)

    :param hda:
        pointer to HD analog structure
    :type hda: struct sti_hda \*

    :param enable:
        true if HD DACS need to be enabled, else false
    :type enable: bool

.. _`sti_hda_configure_awg`:

sti_hda_configure_awg
=====================

.. c:function:: void sti_hda_configure_awg(struct sti_hda *hda, u32 *awg_instr, int nb)

    :param hda:
        pointer to HD analog structure
    :type hda: struct sti_hda \*

    :param awg_instr:
        pointer to AWG instructions table
    :type awg_instr: u32 \*

    :param nb:
        nb of AWG instructions
    :type nb: int

.. This file was automatic generated / don't edit.

