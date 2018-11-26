.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sti/sti_hqvdp.c

.. _`sti_hqvdp_get_free_cmd`:

sti_hqvdp_get_free_cmd
======================

.. c:function:: int sti_hqvdp_get_free_cmd(struct sti_hqvdp *hqvdp)

    :param hqvdp:
        hqvdp structure
    :type hqvdp: struct sti_hqvdp \*

.. _`sti_hqvdp_get_free_cmd.description`:

Description
-----------

Look for a hqvdp_cmd that is not being used (or about to be used) by the FW.

.. _`sti_hqvdp_get_free_cmd.return`:

Return
------

the offset of the command to be used.
-1 in error cases

.. _`sti_hqvdp_get_curr_cmd`:

sti_hqvdp_get_curr_cmd
======================

.. c:function:: int sti_hqvdp_get_curr_cmd(struct sti_hqvdp *hqvdp)

    :param hqvdp:
        hqvdp structure
    :type hqvdp: struct sti_hqvdp \*

.. _`sti_hqvdp_get_curr_cmd.description`:

Description
-----------

Look for the hqvdp_cmd that is being used by the FW.

.. _`sti_hqvdp_get_curr_cmd.return`:

Return
------

the offset of the command to be used.
-1 in error cases

.. _`sti_hqvdp_get_next_cmd`:

sti_hqvdp_get_next_cmd
======================

.. c:function:: int sti_hqvdp_get_next_cmd(struct sti_hqvdp *hqvdp)

    :param hqvdp:
        hqvdp structure
    :type hqvdp: struct sti_hqvdp \*

.. _`sti_hqvdp_get_next_cmd.description`:

Description
-----------

Look for the next hqvdp_cmd that will be used by the FW.

.. _`sti_hqvdp_get_next_cmd.return`:

Return
------

the offset of the next command that will be used.
-1 in error cases

.. _`sti_hqvdp_update_hvsrc`:

sti_hqvdp_update_hvsrc
======================

.. c:function:: void sti_hqvdp_update_hvsrc(enum sti_hvsrc_orient orient, int scale, struct sti_hqvdp_hvsrc *hvsrc)

    :param orient:
        horizontal or vertical
    :type orient: enum sti_hvsrc_orient

    :param scale:
        scaling/zoom factor
    :type scale: int

    :param hvsrc:
        the structure containing the LUT coef
    :type hvsrc: struct sti_hqvdp_hvsrc \*

.. _`sti_hqvdp_update_hvsrc.description`:

Description
-----------

Update the Y and C Lut coef, as well as the shift param

.. _`sti_hqvdp_update_hvsrc.return`:

Return
------

None.

.. _`sti_hqvdp_check_hw_scaling`:

sti_hqvdp_check_hw_scaling
==========================

.. c:function:: bool sti_hqvdp_check_hw_scaling(struct sti_hqvdp *hqvdp, struct drm_display_mode *mode, int src_w, int src_h, int dst_w, int dst_h)

    :param hqvdp:
        hqvdp pointer
    :type hqvdp: struct sti_hqvdp \*

    :param mode:
        display mode with timing constraints
    :type mode: struct drm_display_mode \*

    :param src_w:
        source width
    :type src_w: int

    :param src_h:
        source height
    :type src_h: int

    :param dst_w:
        destination width
    :type dst_w: int

    :param dst_h:
        destination height
    :type dst_h: int

.. _`sti_hqvdp_check_hw_scaling.description`:

Description
-----------

Check if the HW is able to perform the scaling request
The firmware scaling limitation is "CEIL(1/Zy) <= FLOOR(LFW)" where:
Zy = OutputHeight / InputHeight
LFW = (Tx \* IPClock) / (MaxNbCycles \* Cp)
Tx : Total video mode horizontal resolution
IPClock : HQVDP IP clock (Mhz)

.. _`sti_hqvdp_check_hw_scaling.maxnbcycles`:

MaxNbCycles
-----------

max(InputWidth, OutputWidth)
Cp: Video mode pixel clock (Mhz)

.. _`sti_hqvdp_check_hw_scaling.return`:

Return
------

True if the HW can scale.

.. _`sti_hqvdp_disable`:

sti_hqvdp_disable
=================

.. c:function:: void sti_hqvdp_disable(struct sti_hqvdp *hqvdp)

    :param hqvdp:
        hqvdp pointer
    :type hqvdp: struct sti_hqvdp \*

.. _`sti_hqvdp_disable.description`:

Description
-----------

Disables the HQVDP plane

.. _`sti_hqvdp_vtg_cb`:

sti_hqvdp_vtg_cb
================

.. c:function:: int sti_hqvdp_vtg_cb(struct notifier_block *nb, unsigned long evt, void *data)

    :param nb:
        notifier block
    :type nb: struct notifier_block \*

    :param evt:
        event message
    :type evt: unsigned long

    :param data:
        private data
    :type data: void \*

.. _`sti_hqvdp_vtg_cb.description`:

Description
-----------

Handle VTG Vsync event, display pending bottom field

.. _`sti_hqvdp_vtg_cb.return`:

Return
------

0 on success.

.. _`sti_hqvdp_start_xp70`:

sti_hqvdp_start_xp70
====================

.. c:function:: void sti_hqvdp_start_xp70(struct sti_hqvdp *hqvdp)

    :param hqvdp:
        hqvdp pointer
    :type hqvdp: struct sti_hqvdp \*

.. _`sti_hqvdp_start_xp70.description`:

Description
-----------

Run the xP70 initialization sequence

.. This file was automatic generated / don't edit.

