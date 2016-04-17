.. -*- coding: utf-8; mode: rst -*-

=============
fsl_ssi_dbg.c
=============


.. _`fsl_ssi_stats_show`:

fsl_ssi_stats_show
==================

.. c:function:: int fsl_ssi_stats_show (struct seq_file *s, void *unused)

    :param struct seq_file \*s:

        *undescribed*

    :param void \*unused:

        *undescribed*



.. _`fsl_ssi_stats_show.description`:

Description
-----------


Display the statistics for the current SSI device.  To avoid confusion,
we only show those counts that are enabled.

