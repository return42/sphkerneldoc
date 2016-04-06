
.. _API-drm-mm-dump-table:

=================
drm_mm_dump_table
=================

*man drm_mm_dump_table(9)*

*4.6.0-rc1*

dump allocator state to a seq_file


Synopsis
========

.. c:function:: int drm_mm_dump_table( struct seq_file * m, struct drm_mm * mm )

Arguments
=========

``m``
    seq_file to dump to

``mm``
    drm_mm allocator to dump
