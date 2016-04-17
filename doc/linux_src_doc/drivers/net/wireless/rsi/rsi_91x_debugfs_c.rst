.. -*- coding: utf-8; mode: rst -*-

=================
rsi_91x_debugfs.c
=================


.. _`rsi_sdio_stats_read`:

rsi_sdio_stats_read
===================

.. c:function:: int rsi_sdio_stats_read (struct seq_file *seq, void *data)

    :param struct seq_file \*seq:

        *undescribed*

    :param void \*data:

        *undescribed*



.. _`rsi_sdio_stats_read.description`:

Description
-----------


Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.



.. _`rsi_sdio_stats_open`:

rsi_sdio_stats_open
===================

.. c:function:: int rsi_sdio_stats_open (struct inode *inode, struct file *file)

    This funtion calls single open function of seq_file to open file and read contents from it.

    :param struct inode \*inode:
        Pointer to the inode structure.

    :param struct file \*file:
        Pointer to the file structure.



.. _`rsi_sdio_stats_open.return`:

Return
------

Pointer to the opened file status: 0 on success, ENOMEM on failure.



.. _`rsi_version_read`:

rsi_version_read
================

.. c:function:: int rsi_version_read (struct seq_file *seq, void *data)

    This function gives driver and firmware version number.

    :param struct seq_file \*seq:
        Pointer to the sequence file structure.

    :param void \*data:
        Pointer to the data.



.. _`rsi_version_read.return`:

Return
------

0 on success, -1 on failure.



.. _`rsi_version_open`:

rsi_version_open
================

.. c:function:: int rsi_version_open (struct inode *inode, struct file *file)

    This funtion calls single open function of seq_file to open file and read contents from it.

    :param struct inode \*inode:
        Pointer to the inode structure.

    :param struct file \*file:
        Pointer to the file structure.



.. _`rsi_version_open.return`:

Return
------

Pointer to the opened file status: 0 on success, ENOMEM on failure.



.. _`rsi_stats_read`:

rsi_stats_read
==============

.. c:function:: int rsi_stats_read (struct seq_file *seq, void *data)

    This function return the status of the driver.

    :param struct seq_file \*seq:
        Pointer to the sequence file structure.

    :param void \*data:
        Pointer to the data.



.. _`rsi_stats_read.return`:

Return
------

0 on success, -1 on failure.



.. _`rsi_stats_open`:

rsi_stats_open
==============

.. c:function:: int rsi_stats_open (struct inode *inode, struct file *file)

    This funtion calls single open function of seq_file to open file and read contents from it.

    :param struct inode \*inode:
        Pointer to the inode structure.

    :param struct file \*file:
        Pointer to the file structure.



.. _`rsi_stats_open.return`:

Return
------

Pointer to the opened file status: 0 on success, ENOMEM on failure.



.. _`rsi_debug_zone_read`:

rsi_debug_zone_read
===================

.. c:function:: int rsi_debug_zone_read (struct seq_file *seq, void *data)

    This function display the currently enabled debug zones.

    :param struct seq_file \*seq:
        Pointer to the sequence file structure.

    :param void \*data:
        Pointer to the data.



.. _`rsi_debug_zone_read.return`:

Return
------

0 on success, -1 on failure.



.. _`rsi_debug_read`:

rsi_debug_read
==============

.. c:function:: int rsi_debug_read (struct inode *inode, struct file *file)

    This funtion calls single open function of seq_file to open file and read contents from it.

    :param struct inode \*inode:
        Pointer to the inode structure.

    :param struct file \*file:
        Pointer to the file structure.



.. _`rsi_debug_read.return`:

Return
------

Pointer to the opened file status: 0 on success, ENOMEM on failure.



.. _`rsi_debug_zone_write`:

rsi_debug_zone_write
====================

.. c:function:: ssize_t rsi_debug_zone_write (struct file *filp, const char __user *buff, size_t len, loff_t *data)

    This function writes into hal queues as per user requirement.

    :param struct file \*filp:
        Pointer to the file structure.

    :param const char __user \*buff:
        Pointer to the character buffer.

    :param size_t len:
        Length of the data to be written into buffer.

    :param loff_t \*data:
        Pointer to the data.



.. _`rsi_debug_zone_write.return`:

Return
------

len: Number of bytes read.



.. _`rsi_init_dbgfs`:

rsi_init_dbgfs
==============

.. c:function:: int rsi_init_dbgfs (struct rsi_hw *adapter)

    This function initializes the dbgfs entry.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.



.. _`rsi_init_dbgfs.return`:

Return
------

0 on success, -1 on failure.



.. _`rsi_remove_dbgfs`:

rsi_remove_dbgfs
================

.. c:function:: void rsi_remove_dbgfs (struct rsi_hw *adapter)

    Removes the previously created dbgfs file entries in the reverse order of creation.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.



.. _`rsi_remove_dbgfs.return`:

Return
------

None.

