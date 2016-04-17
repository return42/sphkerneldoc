.. -*- coding: utf-8; mode: rst -*-

===========
sti_hqvdp.c
===========


.. _`sti_hqvdp_get_free_cmd`:

sti_hqvdp_get_free_cmd
======================

.. c:function:: int sti_hqvdp_get_free_cmd (struct sti_hqvdp *hqvdp)

    :param struct sti_hqvdp \*hqvdp:
        hqvdp structure



.. _`sti_hqvdp_get_free_cmd.description`:

Description
-----------

Look for a hqvdp_cmd that is not being used (or about to be used) by the FW.



.. _`sti_hqvdp_get_free_cmd.returns`:

RETURNS
-------

the offset of the command to be used.
-1 in error cases



.. _`sti_hqvdp_get_curr_cmd`:

sti_hqvdp_get_curr_cmd
======================

.. c:function:: int sti_hqvdp_get_curr_cmd (struct sti_hqvdp *hqvdp)

    :param struct sti_hqvdp \*hqvdp:
        hqvdp structure



.. _`sti_hqvdp_get_curr_cmd.description`:

Description
-----------

Look for the hqvdp_cmd that is being used by the FW.



.. _`sti_hqvdp_get_curr_cmd.returns`:

RETURNS
-------

the offset of the command to be used.
-1 in error cases



.. _`sti_hqvdp_get_next_cmd`:

sti_hqvdp_get_next_cmd
======================

.. c:function:: int sti_hqvdp_get_next_cmd (struct sti_hqvdp *hqvdp)

    :param struct sti_hqvdp \*hqvdp:
        hqvdp structure



.. _`sti_hqvdp_get_next_cmd.description`:

Description
-----------

Look for the next hqvdp_cmd that will be used by the FW.



.. _`sti_hqvdp_get_next_cmd.returns`:

RETURNS
-------

the offset of the next command that will be used.
-1 in error cases



.. _`sti_hqvdp_update_hvsrc`:

sti_hqvdp_update_hvsrc
======================

.. c:function:: void sti_hqvdp_update_hvsrc (enum sti_hvsrc_orient orient, int scale, struct sti_hqvdp_hvsrc *hvsrc)

    :param enum sti_hvsrc_orient orient:
        horizontal or vertical

    :param int scale:
        scaling/zoom factor

    :param struct sti_hqvdp_hvsrc \*hvsrc:
        the structure containing the LUT coef



.. _`sti_hqvdp_update_hvsrc.description`:

Description
-----------

Update the Y and C Lut coef, as well as the shift param



.. _`sti_hqvdp_update_hvsrc.returns`:

RETURNS
-------

None.



.. _`sti_hqvdp_check_hw_scaling`:

sti_hqvdp_check_hw_scaling
==========================

.. c:function:: bool sti_hqvdp_check_hw_scaling (struct sti_hqvdp *hqvdp, struct drm_display_mode *mode, int src_w, int src_h, int dst_w, int dst_h)

    :param struct sti_hqvdp \*hqvdp:
        hqvdp pointer

    :param struct drm_display_mode \*mode:
        display mode with timing constraints

    :param int src_w:
        source width

    :param int src_h:
        source height

    :param int dst_w:
        destination width

    :param int dst_h:
        destination height



.. _`sti_hqvdp_check_hw_scaling.description`:

Description
-----------

Check if the HW is able to perform the scaling request
The firmware scaling limitation is "CEIL(1/Zy) <= FLOOR(LFW)" where::

  Zy = OutputHeight / InputHeight
  LFW = (Tx * IPClock) / (MaxNbCycles * Cp)



.. _`sti_hqvdp_check_hw_scaling.tx`:

Tx 
---

Total video mode horizontal resolution



.. _`sti_hqvdp_check_hw_scaling.ipclock`:

IPClock 
--------

HQVDP IP clock (Mhz)



.. _`sti_hqvdp_check_hw_scaling.maxnbcycles`:

MaxNbCycles
-----------

max(InputWidth, OutputWidth)



.. _`sti_hqvdp_check_hw_scaling.cp`:

Cp
--

Video mode pixel clock (Mhz)



.. _`sti_hqvdp_check_hw_scaling.returns`:

RETURNS
-------

True if the HW can scale.



.. _`sti_hqvdp_disable`:

sti_hqvdp_disable
=================

.. c:function:: void sti_hqvdp_disable (struct sti_hqvdp *hqvdp)

    :param struct sti_hqvdp \*hqvdp:
        hqvdp pointer



.. _`sti_hqvdp_disable.description`:

Description
-----------

Disables the HQVDP plane



.. _`sti_hqvdp_vtg_cb`:

sti_hqvdp_vtg_cb
================

.. c:function:: int sti_hqvdp_vtg_cb (struct notifier_block *nb, unsigned long evt, void *data)

    :param struct notifier_block \*nb:
        notifier block

    :param unsigned long evt:
        event message

    :param void \*data:
        private data



.. _`sti_hqvdp_vtg_cb.description`:

Description
-----------

Handle VTG Vsync event, display pending bottom field



.. _`sti_hqvdp_vtg_cb.returns`:

RETURNS
-------

0 on success.



.. _`sti_hqvdp_start_xp70`:

sti_hqvdp_start_xp70
====================

.. c:function:: void sti_hqvdp_start_xp70 (struct sti_hqvdp *hqvdp)

    :param struct sti_hqvdp \*hqvdp:
        hqvdp pointer



.. _`sti_hqvdp_start_xp70.description`:

Description
-----------

Run the xP70 initialization sequence

