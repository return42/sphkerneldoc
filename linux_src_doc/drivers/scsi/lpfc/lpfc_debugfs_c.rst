.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_debugfs.c

.. _`lpfc_debugfs_disc_trc_data`:

lpfc_debugfs_disc_trc_data
==========================

.. c:function:: int lpfc_debugfs_disc_trc_data(struct lpfc_vport *vport, char *buf, int size)

    Dump discovery logging to a buffer

    :param struct lpfc_vport \*vport:
        The vport to gather the log info from.

    :param char \*buf:
        The buffer to dump log into.

    :param int size:
        The maximum amount of data to process.

.. _`lpfc_debugfs_disc_trc_data.description`:

Description
-----------

This routine gathers the lpfc discovery debugfs data from the \ ``vport``\  and
dumps it to \ ``buf``\  up to \ ``size``\  number of bytes. It will start at the next entry
in the log and process the log until the end of the buffer. Then it will
gather from the beginning of the log and process until the current entry.

.. _`lpfc_debugfs_disc_trc_data.notes`:

Notes
-----

Discovery logging will be disabled while while this routine dumps the log.

.. _`lpfc_debugfs_disc_trc_data.return-value`:

Return Value
------------

This routine returns the amount of bytes that were dumped into \ ``buf``\  and will
not exceed \ ``size``\ .

.. _`lpfc_debugfs_slow_ring_trc_data`:

lpfc_debugfs_slow_ring_trc_data
===============================

.. c:function:: int lpfc_debugfs_slow_ring_trc_data(struct lpfc_hba *phba, char *buf, int size)

    Dump slow ring logging to a buffer

    :param struct lpfc_hba \*phba:
        The HBA to gather the log info from.

    :param char \*buf:
        The buffer to dump log into.

    :param int size:
        The maximum amount of data to process.

.. _`lpfc_debugfs_slow_ring_trc_data.description`:

Description
-----------

This routine gathers the lpfc slow ring debugfs data from the \ ``phba``\  and
dumps it to \ ``buf``\  up to \ ``size``\  number of bytes. It will start at the next entry
in the log and process the log until the end of the buffer. Then it will
gather from the beginning of the log and process until the current entry.

.. _`lpfc_debugfs_slow_ring_trc_data.notes`:

Notes
-----

Slow ring logging will be disabled while while this routine dumps the log.

.. _`lpfc_debugfs_slow_ring_trc_data.return-value`:

Return Value
------------

This routine returns the amount of bytes that were dumped into \ ``buf``\  and will
not exceed \ ``size``\ .

.. _`lpfc_debugfs_hbqinfo_data`:

lpfc_debugfs_hbqinfo_data
=========================

.. c:function:: int lpfc_debugfs_hbqinfo_data(struct lpfc_hba *phba, char *buf, int size)

    Dump host buffer queue info to a buffer

    :param struct lpfc_hba \*phba:
        The HBA to gather host buffer info from.

    :param char \*buf:
        The buffer to dump log into.

    :param int size:
        The maximum amount of data to process.

.. _`lpfc_debugfs_hbqinfo_data.description`:

Description
-----------

This routine dumps the host buffer queue info from the \ ``phba``\  to \ ``buf``\  up to
\ ``size``\  number of bytes. A header that describes the current hbq state will be
dumped to \ ``buf``\  first and then info on each hbq entry will be dumped to \ ``buf``\ 
until \ ``size``\  bytes have been dumped or all the hbq info has been dumped.

.. _`lpfc_debugfs_hbqinfo_data.notes`:

Notes
-----

This routine will rotate through each configured HBQ each time called.

.. _`lpfc_debugfs_hbqinfo_data.return-value`:

Return Value
------------

This routine returns the amount of bytes that were dumped into \ ``buf``\  and will
not exceed \ ``size``\ .

.. _`lpfc_debugfs_dumphbaslim_data`:

lpfc_debugfs_dumpHBASlim_data
=============================

.. c:function:: int lpfc_debugfs_dumpHBASlim_data(struct lpfc_hba *phba, char *buf, int size)

    Dump HBA SLIM info to a buffer

    :param struct lpfc_hba \*phba:
        The HBA to gather SLIM info from.

    :param char \*buf:
        The buffer to dump log into.

    :param int size:
        The maximum amount of data to process.

.. _`lpfc_debugfs_dumphbaslim_data.description`:

Description
-----------

This routine dumps the current contents of HBA SLIM for the HBA associated
with \ ``phba``\  to \ ``buf``\  up to \ ``size``\  bytes of data. This is the raw HBA SLIM data.

.. _`lpfc_debugfs_dumphbaslim_data.notes`:

Notes
-----

This routine will only dump up to 1024 bytes of data each time called and
should be called multiple times to dump the entire HBA SLIM.

.. _`lpfc_debugfs_dumphbaslim_data.return-value`:

Return Value
------------

This routine returns the amount of bytes that were dumped into \ ``buf``\  and will
not exceed \ ``size``\ .

.. _`lpfc_debugfs_dumphostslim_data`:

lpfc_debugfs_dumpHostSlim_data
==============================

.. c:function:: int lpfc_debugfs_dumpHostSlim_data(struct lpfc_hba *phba, char *buf, int size)

    Dump host SLIM info to a buffer

    :param struct lpfc_hba \*phba:
        The HBA to gather Host SLIM info from.

    :param char \*buf:
        The buffer to dump log into.

    :param int size:
        The maximum amount of data to process.

.. _`lpfc_debugfs_dumphostslim_data.description`:

Description
-----------

This routine dumps the current contents of host SLIM for the host associated
with \ ``phba``\  to \ ``buf``\  up to \ ``size``\  bytes of data. The dump will contain the
Mailbox, PCB, Rings, and Registers that are located in host memory.

.. _`lpfc_debugfs_dumphostslim_data.return-value`:

Return Value
------------

This routine returns the amount of bytes that were dumped into \ ``buf``\  and will
not exceed \ ``size``\ .

.. _`lpfc_debugfs_nodelist_data`:

lpfc_debugfs_nodelist_data
==========================

.. c:function:: int lpfc_debugfs_nodelist_data(struct lpfc_vport *vport, char *buf, int size)

    Dump target node list to a buffer

    :param struct lpfc_vport \*vport:
        The vport to gather target node info from.

    :param char \*buf:
        The buffer to dump log into.

    :param int size:
        The maximum amount of data to process.

.. _`lpfc_debugfs_nodelist_data.description`:

Description
-----------

This routine dumps the current target node list associated with \ ``vport``\  to
\ ``buf``\  up to \ ``size``\  bytes of data. Each node entry in the dump will contain a
node state, DID, WWPN, WWNN, RPI, flags, type, and other useful fields.

.. _`lpfc_debugfs_nodelist_data.return-value`:

Return Value
------------

This routine returns the amount of bytes that were dumped into \ ``buf``\  and will
not exceed \ ``size``\ .

.. _`lpfc_debugfs_disc_trc`:

lpfc_debugfs_disc_trc
=====================

.. c:function:: void lpfc_debugfs_disc_trc(struct lpfc_vport *vport, int mask, char *fmt, uint32_t data1, uint32_t data2, uint32_t data3)

    Store discovery trace log

    :param struct lpfc_vport \*vport:
        The vport to associate this trace string with for retrieval.

    :param int mask:
        Log entry classification.

    :param char \*fmt:
        Format string to be displayed when dumping the log.

    :param uint32_t data1:
        1st data parameter to be applied to \ ``fmt``\ .

    :param uint32_t data2:
        2nd data parameter to be applied to \ ``fmt``\ .

    :param uint32_t data3:
        3rd data parameter to be applied to \ ``fmt``\ .

.. _`lpfc_debugfs_disc_trc.description`:

Description
-----------

This routine is used by the driver code to add a debugfs log entry to the
discovery trace buffer associated with \ ``vport``\ . Only entries with a \ ``mask``\  that
match the current debugfs discovery mask will be saved. Entries that do not
match will be thrown away. \ ``fmt``\ , \ ``data1``\ , \ ``data2``\ , and \ ``data3``\  are used like
printf when displaying the log.

.. _`lpfc_debugfs_slow_ring_trc`:

lpfc_debugfs_slow_ring_trc
==========================

.. c:function:: void lpfc_debugfs_slow_ring_trc(struct lpfc_hba *phba, char *fmt, uint32_t data1, uint32_t data2, uint32_t data3)

    Store slow ring trace log

    :param struct lpfc_hba \*phba:
        The phba to associate this trace string with for retrieval.

    :param char \*fmt:
        Format string to be displayed when dumping the log.

    :param uint32_t data1:
        1st data parameter to be applied to \ ``fmt``\ .

    :param uint32_t data2:
        2nd data parameter to be applied to \ ``fmt``\ .

    :param uint32_t data3:
        3rd data parameter to be applied to \ ``fmt``\ .

.. _`lpfc_debugfs_slow_ring_trc.description`:

Description
-----------

This routine is used by the driver code to add a debugfs log entry to the
discovery trace buffer associated with \ ``vport``\ . \ ``fmt``\ , \ ``data1``\ , \ ``data2``\ , and
\ ``data3``\  are used like printf when displaying the log.

.. _`lpfc_debugfs_disc_trc_open`:

lpfc_debugfs_disc_trc_open
==========================

.. c:function:: int lpfc_debugfs_disc_trc_open(struct inode *inode, struct file *file)

    Open the discovery trace log

    :param struct inode \*inode:
        The inode pointer that contains a vport pointer.

    :param struct file \*file:
        The file pointer to attach the log output.

.. _`lpfc_debugfs_disc_trc_open.description`:

Description
-----------

This routine is the entry point for the debugfs open file operation. It gets
the vport from the i_private field in \ ``inode``\ , allocates the necessary buffer
for the log, fills the buffer from the in-memory log for this vport, and then
returns a pointer to that log in the private_data field in \ ``file``\ .

.. _`lpfc_debugfs_disc_trc_open.return`:

Return
------

This function returns zero if successful. On error it will return a negative
error value.

.. _`lpfc_debugfs_slow_ring_trc_open`:

lpfc_debugfs_slow_ring_trc_open
===============================

.. c:function:: int lpfc_debugfs_slow_ring_trc_open(struct inode *inode, struct file *file)

    Open the Slow Ring trace log

    :param struct inode \*inode:
        The inode pointer that contains a vport pointer.

    :param struct file \*file:
        The file pointer to attach the log output.

.. _`lpfc_debugfs_slow_ring_trc_open.description`:

Description
-----------

This routine is the entry point for the debugfs open file operation. It gets
the vport from the i_private field in \ ``inode``\ , allocates the necessary buffer
for the log, fills the buffer from the in-memory log for this vport, and then
returns a pointer to that log in the private_data field in \ ``file``\ .

.. _`lpfc_debugfs_slow_ring_trc_open.return`:

Return
------

This function returns zero if successful. On error it will return a negative
error value.

.. _`lpfc_debugfs_hbqinfo_open`:

lpfc_debugfs_hbqinfo_open
=========================

.. c:function:: int lpfc_debugfs_hbqinfo_open(struct inode *inode, struct file *file)

    Open the hbqinfo debugfs buffer

    :param struct inode \*inode:
        The inode pointer that contains a vport pointer.

    :param struct file \*file:
        The file pointer to attach the log output.

.. _`lpfc_debugfs_hbqinfo_open.description`:

Description
-----------

This routine is the entry point for the debugfs open file operation. It gets
the vport from the i_private field in \ ``inode``\ , allocates the necessary buffer
for the log, fills the buffer from the in-memory log for this vport, and then
returns a pointer to that log in the private_data field in \ ``file``\ .

.. _`lpfc_debugfs_hbqinfo_open.return`:

Return
------

This function returns zero if successful. On error it will return a negative
error value.

.. _`lpfc_debugfs_dumphbaslim_open`:

lpfc_debugfs_dumpHBASlim_open
=============================

.. c:function:: int lpfc_debugfs_dumpHBASlim_open(struct inode *inode, struct file *file)

    Open the Dump HBA SLIM debugfs buffer

    :param struct inode \*inode:
        The inode pointer that contains a vport pointer.

    :param struct file \*file:
        The file pointer to attach the log output.

.. _`lpfc_debugfs_dumphbaslim_open.description`:

Description
-----------

This routine is the entry point for the debugfs open file operation. It gets
the vport from the i_private field in \ ``inode``\ , allocates the necessary buffer
for the log, fills the buffer from the in-memory log for this vport, and then
returns a pointer to that log in the private_data field in \ ``file``\ .

.. _`lpfc_debugfs_dumphbaslim_open.return`:

Return
------

This function returns zero if successful. On error it will return a negative
error value.

.. _`lpfc_debugfs_dumphostslim_open`:

lpfc_debugfs_dumpHostSlim_open
==============================

.. c:function:: int lpfc_debugfs_dumpHostSlim_open(struct inode *inode, struct file *file)

    Open the Dump Host SLIM debugfs buffer

    :param struct inode \*inode:
        The inode pointer that contains a vport pointer.

    :param struct file \*file:
        The file pointer to attach the log output.

.. _`lpfc_debugfs_dumphostslim_open.description`:

Description
-----------

This routine is the entry point for the debugfs open file operation. It gets
the vport from the i_private field in \ ``inode``\ , allocates the necessary buffer
for the log, fills the buffer from the in-memory log for this vport, and then
returns a pointer to that log in the private_data field in \ ``file``\ .

.. _`lpfc_debugfs_dumphostslim_open.return`:

Return
------

This function returns zero if successful. On error it will return a negative
error value.

.. _`lpfc_debugfs_nodelist_open`:

lpfc_debugfs_nodelist_open
==========================

.. c:function:: int lpfc_debugfs_nodelist_open(struct inode *inode, struct file *file)

    Open the nodelist debugfs file

    :param struct inode \*inode:
        The inode pointer that contains a vport pointer.

    :param struct file \*file:
        The file pointer to attach the log output.

.. _`lpfc_debugfs_nodelist_open.description`:

Description
-----------

This routine is the entry point for the debugfs open file operation. It gets
the vport from the i_private field in \ ``inode``\ , allocates the necessary buffer
for the log, fills the buffer from the in-memory log for this vport, and then
returns a pointer to that log in the private_data field in \ ``file``\ .

.. _`lpfc_debugfs_nodelist_open.return`:

Return
------

This function returns zero if successful. On error it will return a negative
error value.

.. _`lpfc_debugfs_lseek`:

lpfc_debugfs_lseek
==================

.. c:function:: loff_t lpfc_debugfs_lseek(struct file *file, loff_t off, int whence)

    Seek through a debugfs file

    :param struct file \*file:
        The file pointer to seek through.

    :param loff_t off:
        The offset to seek to or the amount to seek by.

    :param int whence:
        Indicates how to seek.

.. _`lpfc_debugfs_lseek.description`:

Description
-----------

This routine is the entry point for the debugfs lseek file operation. The
\ ``whence``\  parameter indicates whether \ ``off``\  is the offset to directly seek to,
or if it is a value to seek forward or reverse by. This function figures out
what the new offset of the debugfs file will be and assigns that value to the
f_pos field of \ ``file``\ .

.. _`lpfc_debugfs_lseek.return`:

Return
------

This function returns the new offset if successful and returns a negative
error if unable to process the seek.

.. _`lpfc_debugfs_read`:

lpfc_debugfs_read
=================

.. c:function:: ssize_t lpfc_debugfs_read(struct file *file, char __user *buf, size_t nbytes, loff_t *ppos)

    Read a debugfs file

    :param struct file \*file:
        The file pointer to read from.

    :param char __user \*buf:
        The buffer to copy the data to.

    :param size_t nbytes:
        The number of bytes to read.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_debugfs_read.description`:

Description
-----------

This routine reads data from from the buffer indicated in the private_data
field of \ ``file``\ . It will start reading at \ ``ppos``\  and copy up to \ ``nbytes``\  of
data to \ ``buf``\ .

.. _`lpfc_debugfs_read.return`:

Return
------

This function returns the amount of data that was read (this could be less
than \ ``nbytes``\  if the end of the file was reached) or a negative error value.

.. _`lpfc_debugfs_release`:

lpfc_debugfs_release
====================

.. c:function:: int lpfc_debugfs_release(struct inode *inode, struct file *file)

    Release the buffer used to store debugfs file data

    :param struct inode \*inode:
        The inode pointer that contains a vport pointer. (unused)

    :param struct file \*file:
        The file pointer that contains the buffer to release.

.. _`lpfc_debugfs_release.description`:

Description
-----------

This routine frees the buffer that was allocated when the debugfs file was
opened.

.. _`lpfc_debugfs_release.return`:

Return
------

This function returns zero.

.. _`lpfc_idiag_cmd_get`:

lpfc_idiag_cmd_get
==================

.. c:function:: int lpfc_idiag_cmd_get(const char __user *buf, size_t nbytes, struct lpfc_idiag_cmd *idiag_cmd)

    Get and parse idiag debugfs comands from user space

    :param const char __user \*buf:
        The pointer to the user space buffer.

    :param size_t nbytes:
        The number of bytes in the user space buffer.

    :param struct lpfc_idiag_cmd \*idiag_cmd:
        pointer to the idiag command struct.

.. _`lpfc_idiag_cmd_get.description`:

Description
-----------

This routine reads data from debugfs user space buffer and parses the
buffer for getting the idiag command and arguments. The while space in
between the set of data is used as the parsing separator.

This routine returns 0 when successful, it returns proper error code
back to the user space in error conditions.

.. _`lpfc_idiag_open`:

lpfc_idiag_open
===============

.. c:function:: int lpfc_idiag_open(struct inode *inode, struct file *file)

    idiag open debugfs

    :param struct inode \*inode:
        The inode pointer that contains a pointer to phba.

    :param struct file \*file:
        The file pointer to attach the file operation.

.. _`lpfc_idiag_open.description`:

Description
-----------

This routine is the entry point for the debugfs open file operation. It
gets the reference to phba from the i_private field in \ ``inode``\ , it then
allocates buffer for the file operation, performs the necessary PCI config
space read into the allocated buffer according to the idiag user command
setup, and then returns a pointer to buffer in the private_data field in
\ ``file``\ .

.. _`lpfc_idiag_open.return`:

Return
------

This function returns zero if successful. On error it will return an
negative error value.

.. _`lpfc_idiag_release`:

lpfc_idiag_release
==================

.. c:function:: int lpfc_idiag_release(struct inode *inode, struct file *file)

    Release idiag access file operation

    :param struct inode \*inode:
        The inode pointer that contains a vport pointer. (unused)

    :param struct file \*file:
        The file pointer that contains the buffer to release.

.. _`lpfc_idiag_release.description`:

Description
-----------

This routine is the generic release routine for the idiag access file
operation, it frees the buffer that was allocated when the debugfs file
was opened.

.. _`lpfc_idiag_release.return`:

Return
------

This function returns zero.

.. _`lpfc_idiag_cmd_release`:

lpfc_idiag_cmd_release
======================

.. c:function:: int lpfc_idiag_cmd_release(struct inode *inode, struct file *file)

    Release idiag cmd access file operation

    :param struct inode \*inode:
        The inode pointer that contains a vport pointer. (unused)

    :param struct file \*file:
        The file pointer that contains the buffer to release.

.. _`lpfc_idiag_cmd_release.description`:

Description
-----------

This routine frees the buffer that was allocated when the debugfs file
was opened. It also reset the fields in the idiag command struct in the
case of command for write operation.

.. _`lpfc_idiag_cmd_release.return`:

Return
------

This function returns zero.

.. _`lpfc_idiag_pcicfg_read`:

lpfc_idiag_pcicfg_read
======================

.. c:function:: ssize_t lpfc_idiag_pcicfg_read(struct file *file, char __user *buf, size_t nbytes, loff_t *ppos)

    idiag debugfs read pcicfg

    :param struct file \*file:
        The file pointer to read from.

    :param char __user \*buf:
        The buffer to copy the data to.

    :param size_t nbytes:
        The number of bytes to read.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_pcicfg_read.description`:

Description
-----------

This routine reads data from the \ ``phba``\  pci config space according to the
idiag command, and copies to user \ ``buf``\ . Depending on the PCI config space
read command setup, it does either a single register read of a byte
(8 bits), a word (16 bits), or a dword (32 bits) or browsing through all
registers from the 4K extended PCI config space.

.. _`lpfc_idiag_pcicfg_read.return`:

Return
------

This function returns the amount of data that was read (this could be less
than \ ``nbytes``\  if the end of the file was reached) or a negative error value.

.. _`lpfc_idiag_pcicfg_write`:

lpfc_idiag_pcicfg_write
=======================

.. c:function:: ssize_t lpfc_idiag_pcicfg_write(struct file *file, const char __user *buf, size_t nbytes, loff_t *ppos)

    Syntax check and set up idiag pcicfg commands

    :param struct file \*file:
        The file pointer to read from.

    :param const char __user \*buf:
        The buffer to copy the user data from.

    :param size_t nbytes:
        The number of bytes to get.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_pcicfg_write.description`:

Description
-----------

This routine get the debugfs idiag command struct from user space and
then perform the syntax check for PCI config space read or write command
accordingly. In the case of PCI config space read command, it sets up
the command in the idiag command struct for the debugfs read operation.
In the case of PCI config space write operation, it executes the write
operation into the PCI config space accordingly.

It returns the \ ``nbytges``\  passing in from debugfs user space when successful.
In case of error conditions, it returns proper error code back to the user
space.

.. _`lpfc_idiag_baracc_read`:

lpfc_idiag_baracc_read
======================

.. c:function:: ssize_t lpfc_idiag_baracc_read(struct file *file, char __user *buf, size_t nbytes, loff_t *ppos)

    idiag debugfs pci bar access read

    :param struct file \*file:
        The file pointer to read from.

    :param char __user \*buf:
        The buffer to copy the data to.

    :param size_t nbytes:
        The number of bytes to read.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_baracc_read.description`:

Description
-----------

This routine reads data from the \ ``phba``\  pci bar memory mapped space
according to the idiag command, and copies to user \ ``buf``\ .

.. _`lpfc_idiag_baracc_read.return`:

Return
------

This function returns the amount of data that was read (this could be less
than \ ``nbytes``\  if the end of the file was reached) or a negative error value.

.. _`lpfc_idiag_baracc_write`:

lpfc_idiag_baracc_write
=======================

.. c:function:: ssize_t lpfc_idiag_baracc_write(struct file *file, const char __user *buf, size_t nbytes, loff_t *ppos)

    Syntax check and set up idiag bar access commands

    :param struct file \*file:
        The file pointer to read from.

    :param const char __user \*buf:
        The buffer to copy the user data from.

    :param size_t nbytes:
        The number of bytes to get.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_baracc_write.description`:

Description
-----------

This routine get the debugfs idiag command struct from user space and
then perform the syntax check for PCI bar memory mapped space read or
write command accordingly. In the case of PCI bar memory mapped space
read command, it sets up the command in the idiag command struct for
the debugfs read operation. In the case of PCI bar memorpy mapped space
write operation, it executes the write operation into the PCI bar memory
mapped space accordingly.

It returns the \ ``nbytges``\  passing in from debugfs user space when successful.
In case of error conditions, it returns proper error code back to the user
space.

.. _`lpfc_idiag_queinfo_read`:

lpfc_idiag_queinfo_read
=======================

.. c:function:: ssize_t lpfc_idiag_queinfo_read(struct file *file, char __user *buf, size_t nbytes, loff_t *ppos)

    idiag debugfs read queue information

    :param struct file \*file:
        The file pointer to read from.

    :param char __user \*buf:
        The buffer to copy the data to.

    :param size_t nbytes:
        The number of bytes to read.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_queinfo_read.description`:

Description
-----------

This routine reads data from the \ ``phba``\  SLI4 PCI function queue information,
and copies to user \ ``buf``\ .

.. _`lpfc_idiag_queinfo_read.return`:

Return
------

This function returns the amount of data that was read (this could be less
than \ ``nbytes``\  if the end of the file was reached) or a negative error value.

.. _`lpfc_idiag_que_param_check`:

lpfc_idiag_que_param_check
==========================

.. c:function:: int lpfc_idiag_que_param_check(struct lpfc_queue *q, int index, int count)

    queue access command parameter sanity check

    :param struct lpfc_queue \*q:
        The pointer to queue structure.

    :param int index:
        The index into a queue entry.

    :param int count:
        The number of queue entries to access.

.. _`lpfc_idiag_que_param_check.description`:

Description
-----------

The routine performs sanity check on device queue access method commands.

.. _`lpfc_idiag_que_param_check.return`:

Return
------

This function returns -EINVAL when fails the sanity check, otherwise, it
returns 0.

.. _`lpfc_idiag_queacc_read_qe`:

lpfc_idiag_queacc_read_qe
=========================

.. c:function:: int lpfc_idiag_queacc_read_qe(char *pbuffer, int len, struct lpfc_queue *pque, uint32_t index)

    read a single entry from the given queue index

    :param char \*pbuffer:
        The pointer to buffer to copy the read data into.

    :param int len:
        *undescribed*

    :param struct lpfc_queue \*pque:
        The pointer to the queue to be read.

    :param uint32_t index:
        The index into the queue entry.

.. _`lpfc_idiag_queacc_read_qe.description`:

Description
-----------

This routine reads out a single entry from the given queue's index location
and copies it into the buffer provided.

.. _`lpfc_idiag_queacc_read_qe.return`:

Return
------

This function returns 0 when it fails, otherwise, it returns the length of
the data read into the buffer provided.

.. _`lpfc_idiag_queacc_read`:

lpfc_idiag_queacc_read
======================

.. c:function:: ssize_t lpfc_idiag_queacc_read(struct file *file, char __user *buf, size_t nbytes, loff_t *ppos)

    idiag debugfs read port queue

    :param struct file \*file:
        The file pointer to read from.

    :param char __user \*buf:
        The buffer to copy the data to.

    :param size_t nbytes:
        The number of bytes to read.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_queacc_read.description`:

Description
-----------

This routine reads data from the \ ``phba``\  device queue memory according to the
idiag command, and copies to user \ ``buf``\ . Depending on the queue dump read
command setup, it does either a single queue entry read or browing through
all entries of the queue.

.. _`lpfc_idiag_queacc_read.return`:

Return
------

This function returns the amount of data that was read (this could be less
than \ ``nbytes``\  if the end of the file was reached) or a negative error value.

.. _`lpfc_idiag_queacc_write`:

lpfc_idiag_queacc_write
=======================

.. c:function:: ssize_t lpfc_idiag_queacc_write(struct file *file, const char __user *buf, size_t nbytes, loff_t *ppos)

    Syntax check and set up idiag queacc commands

    :param struct file \*file:
        The file pointer to read from.

    :param const char __user \*buf:
        The buffer to copy the user data from.

    :param size_t nbytes:
        The number of bytes to get.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_queacc_write.description`:

Description
-----------

This routine get the debugfs idiag command struct from user space and then
perform the syntax check for port queue read (dump) or write (set) command
accordingly. In the case of port queue read command, it sets up the command
in the idiag command struct for the following debugfs read operation. In
the case of port queue write operation, it executes the write operation
into the port queue entry accordingly.

It returns the \ ``nbytges``\  passing in from debugfs user space when successful.
In case of error conditions, it returns proper error code back to the user
space.

.. _`lpfc_idiag_drbacc_read_reg`:

lpfc_idiag_drbacc_read_reg
==========================

.. c:function:: int lpfc_idiag_drbacc_read_reg(struct lpfc_hba *phba, char *pbuffer, int len, uint32_t drbregid)

    idiag debugfs read a doorbell register

    :param struct lpfc_hba \*phba:
        The pointer to hba structure.

    :param char \*pbuffer:
        The pointer to the buffer to copy the data to.

    :param int len:
        The lenght of bytes to copied.

    :param uint32_t drbregid:
        The id to doorbell registers.

.. _`lpfc_idiag_drbacc_read_reg.description`:

Description
-----------

This routine reads a doorbell register and copies its content to the
user buffer pointed to by \ ``pbuffer``\ .

.. _`lpfc_idiag_drbacc_read_reg.return`:

Return
------

This function returns the amount of data that was copied into \ ``pbuffer``\ .

.. _`lpfc_idiag_drbacc_read`:

lpfc_idiag_drbacc_read
======================

.. c:function:: ssize_t lpfc_idiag_drbacc_read(struct file *file, char __user *buf, size_t nbytes, loff_t *ppos)

    idiag debugfs read port doorbell

    :param struct file \*file:
        The file pointer to read from.

    :param char __user \*buf:
        The buffer to copy the data to.

    :param size_t nbytes:
        The number of bytes to read.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_drbacc_read.description`:

Description
-----------

This routine reads data from the \ ``phba``\  device doorbell register according
to the idiag command, and copies to user \ ``buf``\ . Depending on the doorbell
register read command setup, it does either a single doorbell register
read or dump all doorbell registers.

.. _`lpfc_idiag_drbacc_read.return`:

Return
------

This function returns the amount of data that was read (this could be less
than \ ``nbytes``\  if the end of the file was reached) or a negative error value.

.. _`lpfc_idiag_drbacc_write`:

lpfc_idiag_drbacc_write
=======================

.. c:function:: ssize_t lpfc_idiag_drbacc_write(struct file *file, const char __user *buf, size_t nbytes, loff_t *ppos)

    Syntax check and set up idiag drbacc commands

    :param struct file \*file:
        The file pointer to read from.

    :param const char __user \*buf:
        The buffer to copy the user data from.

    :param size_t nbytes:
        The number of bytes to get.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_drbacc_write.description`:

Description
-----------

This routine get the debugfs idiag command struct from user space and then
perform the syntax check for port doorbell register read (dump) or write
(set) command accordingly. In the case of port queue read command, it sets
up the command in the idiag command struct for the following debugfs read
operation. In the case of port doorbell register write operation, it
executes the write operation into the port doorbell register accordingly.

It returns the \ ``nbytges``\  passing in from debugfs user space when successful.
In case of error conditions, it returns proper error code back to the user
space.

.. _`lpfc_idiag_ctlacc_read_reg`:

lpfc_idiag_ctlacc_read_reg
==========================

.. c:function:: int lpfc_idiag_ctlacc_read_reg(struct lpfc_hba *phba, char *pbuffer, int len, uint32_t ctlregid)

    idiag debugfs read a control registers

    :param struct lpfc_hba \*phba:
        The pointer to hba structure.

    :param char \*pbuffer:
        The pointer to the buffer to copy the data to.

    :param int len:
        The lenght of bytes to copied.

    :param uint32_t ctlregid:
        *undescribed*

.. _`lpfc_idiag_ctlacc_read_reg.description`:

Description
-----------

This routine reads a control register and copies its content to the
user buffer pointed to by \ ``pbuffer``\ .

.. _`lpfc_idiag_ctlacc_read_reg.return`:

Return
------

This function returns the amount of data that was copied into \ ``pbuffer``\ .

.. _`lpfc_idiag_ctlacc_read`:

lpfc_idiag_ctlacc_read
======================

.. c:function:: ssize_t lpfc_idiag_ctlacc_read(struct file *file, char __user *buf, size_t nbytes, loff_t *ppos)

    idiag debugfs read port and device control register

    :param struct file \*file:
        The file pointer to read from.

    :param char __user \*buf:
        The buffer to copy the data to.

    :param size_t nbytes:
        The number of bytes to read.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_ctlacc_read.description`:

Description
-----------

This routine reads data from the \ ``phba``\  port and device registers according
to the idiag command, and copies to user \ ``buf``\ .

.. _`lpfc_idiag_ctlacc_read.return`:

Return
------

This function returns the amount of data that was read (this could be less
than \ ``nbytes``\  if the end of the file was reached) or a negative error value.

.. _`lpfc_idiag_ctlacc_write`:

lpfc_idiag_ctlacc_write
=======================

.. c:function:: ssize_t lpfc_idiag_ctlacc_write(struct file *file, const char __user *buf, size_t nbytes, loff_t *ppos)

    Syntax check and set up idiag ctlacc commands

    :param struct file \*file:
        The file pointer to read from.

    :param const char __user \*buf:
        The buffer to copy the user data from.

    :param size_t nbytes:
        The number of bytes to get.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_ctlacc_write.description`:

Description
-----------

This routine get the debugfs idiag command struct from user space and then
perform the syntax check for port and device control register read (dump)
or write (set) command accordingly.

It returns the \ ``nbytges``\  passing in from debugfs user space when successful.
In case of error conditions, it returns proper error code back to the user
space.

.. _`lpfc_idiag_mbxacc_get_setup`:

lpfc_idiag_mbxacc_get_setup
===========================

.. c:function:: int lpfc_idiag_mbxacc_get_setup(struct lpfc_hba *phba, char *pbuffer)

    idiag debugfs get mailbox access setup

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param char \*pbuffer:
        Pointer to data buffer.

.. _`lpfc_idiag_mbxacc_get_setup.description`:

Description
-----------

This routine gets the driver mailbox access debugfs setup information.

.. _`lpfc_idiag_mbxacc_get_setup.return`:

Return
------

This function returns the amount of data that was read (this could be less
than \ ``nbytes``\  if the end of the file was reached) or a negative error value.

.. _`lpfc_idiag_mbxacc_read`:

lpfc_idiag_mbxacc_read
======================

.. c:function:: ssize_t lpfc_idiag_mbxacc_read(struct file *file, char __user *buf, size_t nbytes, loff_t *ppos)

    idiag debugfs read on mailbox access

    :param struct file \*file:
        The file pointer to read from.

    :param char __user \*buf:
        The buffer to copy the data to.

    :param size_t nbytes:
        The number of bytes to read.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_mbxacc_read.description`:

Description
-----------

This routine reads data from the \ ``phba``\  driver mailbox access debugfs setup
information.

.. _`lpfc_idiag_mbxacc_read.return`:

Return
------

This function returns the amount of data that was read (this could be less
than \ ``nbytes``\  if the end of the file was reached) or a negative error value.

.. _`lpfc_idiag_mbxacc_write`:

lpfc_idiag_mbxacc_write
=======================

.. c:function:: ssize_t lpfc_idiag_mbxacc_write(struct file *file, const char __user *buf, size_t nbytes, loff_t *ppos)

    Syntax check and set up idiag mbxacc commands

    :param struct file \*file:
        The file pointer to read from.

    :param const char __user \*buf:
        The buffer to copy the user data from.

    :param size_t nbytes:
        The number of bytes to get.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_mbxacc_write.description`:

Description
-----------

This routine get the debugfs idiag command struct from user space and then
perform the syntax check for driver mailbox command (dump) and sets up the
necessary states in the idiag command struct accordingly.

It returns the \ ``nbytges``\  passing in from debugfs user space when successful.
In case of error conditions, it returns proper error code back to the user
space.

.. _`lpfc_idiag_extacc_avail_get`:

lpfc_idiag_extacc_avail_get
===========================

.. c:function:: int lpfc_idiag_extacc_avail_get(struct lpfc_hba *phba, char *pbuffer, int len)

    get the available extents information

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param char \*pbuffer:
        pointer to internal buffer.

    :param int len:
        length into the internal buffer data has been copied.

.. _`lpfc_idiag_extacc_avail_get.description`:

Description
-----------

This routine is to get the available extent information.

.. _`lpfc_idiag_extacc_avail_get.return`:

Return
------

overall lenth of the data read into the internal buffer.

.. _`lpfc_idiag_extacc_alloc_get`:

lpfc_idiag_extacc_alloc_get
===========================

.. c:function:: int lpfc_idiag_extacc_alloc_get(struct lpfc_hba *phba, char *pbuffer, int len)

    get the allocated extents information

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param char \*pbuffer:
        pointer to internal buffer.

    :param int len:
        length into the internal buffer data has been copied.

.. _`lpfc_idiag_extacc_alloc_get.description`:

Description
-----------

This routine is to get the allocated extent information.

.. _`lpfc_idiag_extacc_alloc_get.return`:

Return
------

overall lenth of the data read into the internal buffer.

.. _`lpfc_idiag_extacc_drivr_get`:

lpfc_idiag_extacc_drivr_get
===========================

.. c:function:: int lpfc_idiag_extacc_drivr_get(struct lpfc_hba *phba, char *pbuffer, int len)

    get driver extent information

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param char \*pbuffer:
        pointer to internal buffer.

    :param int len:
        length into the internal buffer data has been copied.

.. _`lpfc_idiag_extacc_drivr_get.description`:

Description
-----------

This routine is to get the driver extent information.

.. _`lpfc_idiag_extacc_drivr_get.return`:

Return
------

overall lenth of the data read into the internal buffer.

.. _`lpfc_idiag_extacc_write`:

lpfc_idiag_extacc_write
=======================

.. c:function:: ssize_t lpfc_idiag_extacc_write(struct file *file, const char __user *buf, size_t nbytes, loff_t *ppos)

    Syntax check and set up idiag extacc commands

    :param struct file \*file:
        The file pointer to read from.

    :param const char __user \*buf:
        The buffer to copy the user data from.

    :param size_t nbytes:
        The number of bytes to get.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_extacc_write.description`:

Description
-----------

This routine get the debugfs idiag command struct from user space and then
perform the syntax check for extent information access commands and sets
up the necessary states in the idiag command struct accordingly.

It returns the \ ``nbytges``\  passing in from debugfs user space when successful.
In case of error conditions, it returns proper error code back to the user
space.

.. _`lpfc_idiag_extacc_read`:

lpfc_idiag_extacc_read
======================

.. c:function:: ssize_t lpfc_idiag_extacc_read(struct file *file, char __user *buf, size_t nbytes, loff_t *ppos)

    idiag debugfs read access to extent information

    :param struct file \*file:
        The file pointer to read from.

    :param char __user \*buf:
        The buffer to copy the data to.

    :param size_t nbytes:
        The number of bytes to read.

    :param loff_t \*ppos:
        The position in the file to start reading from.

.. _`lpfc_idiag_extacc_read.description`:

Description
-----------

This routine reads data from the proper extent information according to
the idiag command, and copies to user \ ``buf``\ .

.. _`lpfc_idiag_extacc_read.return`:

Return
------

This function returns the amount of data that was read (this could be less
than \ ``nbytes``\  if the end of the file was reached) or a negative error value.

.. _`lpfc_debugfs_initialize`:

lpfc_debugfs_initialize
=======================

.. c:function:: void lpfc_debugfs_initialize(struct lpfc_vport *vport)

    Initialize debugfs for a vport

    :param struct lpfc_vport \*vport:
        The vport pointer to initialize.

.. _`lpfc_debugfs_initialize.description`:

Description
-----------

When Debugfs is configured this routine sets up the lpfc debugfs file system.
If not already created, this routine will create the lpfc directory, and
lpfcX directory (for this HBA), and vportX directory for this vport. It will
also create each file used to access lpfc specific debugfs information.

.. _`lpfc_debugfs_terminate`:

lpfc_debugfs_terminate
======================

.. c:function:: void lpfc_debugfs_terminate(struct lpfc_vport *vport)

    Tear down debugfs infrastructure for this vport

    :param struct lpfc_vport \*vport:
        The vport pointer to remove from debugfs.

.. _`lpfc_debugfs_terminate.description`:

Description
-----------

When Debugfs is configured this routine removes debugfs file system elements
that are specific to this vport. It also checks to see if there are any
users left for the debugfs directories associated with the HBA and driver. If
this is the last user of the HBA directory or driver directory then it will
remove those from the debugfs infrastructure as well.

.. _`lpfc_debug_dump_all_queues`:

lpfc_debug_dump_all_queues
==========================

.. c:function:: void lpfc_debug_dump_all_queues(struct lpfc_hba *phba)

    dump all the queues with a hba

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_debug_dump_all_queues.description`:

Description
-----------

This function dumps entries of all the queues asociated with the \ ``phba``\ .

.. This file was automatic generated / don't edit.

