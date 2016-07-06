.. -*- coding: utf-8; mode: rst -*-

.. _filesystems:

******************
Filesystem support
******************

The NAND driver provides all necessary functions for a filesystem via
the MTD interface.

Filesystems must be aware of the NAND peculiarities and restrictions.
One major restrictions of NAND Flash is, that you cannot write as often
as you want to a page. The consecutive writes to a page, before erasing
it again, are restricted to 1-3 writes, depending on the manufacturers
specifications. This applies similar to the spare area.

Therefore NAND aware filesystems must either write in page size chunks
or hold a writebuffer to collect smaller writes until they sum up to
pagesize. Available NAND aware filesystems: JFFS2, YAFFS.

The spare area usage to store filesystem data is controlled by the spare
area placement functionality which is described in one of the earlier
chapters.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
